# asntools API Reference

This document summarizes the FastAPI surface exported by `asntools.server`. Use
it when integrating remote MCP agents or other clients that need RRC IE
introspection over HTTP.

## Running the server

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e .[dev]
asntools --compile --input-dir /path/to/asnfiles
uvicorn asntools.server:app --host 0.0.0.0 --port 8000
```

The OpenAPI document is served at `/openapi.json`. All examples below assume the
server is reachable at `http://SERVER:8000`.

## Endpoint summary

| Route | Method | CLI equivalent | Notes |
| --- | --- | --- | --- |
| `/health` | GET | `n/a` | Simple readiness probe. |
| `/compile` | POST | `asntools --compile` | Accepts custom file lists or discovery directories. |
| `/ies/{ie}` | GET | `asntools --show <ie>` | Returns JSON structure for one IE. |
| `/ies/search?pattern=` | GET | `asntools --show`, tab completion | Simple substring search across IE names. |
| `/trees` | POST | `asntools --tree` | Builds ancestry paths, ASCII trees, Mermaid, and Markdown (with pretty-file support). |
| `/grep` | GET | `asntools --grep <pattern>` | Searches ASN.1 text; returns structured match JSON. |
| `/fields/{field}` | GET | `asntools --describe-field` | Looks up narrative field descriptions. |
| `/field-descriptions/ies/{ie}` | GET | `asntools --describe-ie` | Dumps IE-level field description tables. |
| `/help` | GET | `n/a` | Returns metadata for every endpoint/tool. |

### Tool cheat sheet

| Tool | Method/Path | Request | Response |
| --- | --- | --- | --- |
| `asntools_compile` | `POST /compile` | JSON body with `asn1_files`, `description_files`, `discover_dirs`, `subdirs` (all optional lists). | `{"status":"ok","merged_asn1": str,"module": str,"field_descriptions": str\|null}` on success; 400/404 with `detail` on error. |
| `asntools_show` | `GET /ies/{ie_name}` | Path param `ie_name`; query params `compile` (bool) and `asn1_path` (str) optional. | `{"status":"ok","ie_name": str,"data": {...}}` or 404 with error message. |
| `asntools_search` | `GET /ies/search` | Query `pattern`, optional `compile`/`asn1_path`. | `{"status":"ok","pattern": str,"matches": [str], "count": int}`. |
| `asntools_tree` | `POST /trees` | JSON body mirroring CLI `--tree` flags (`leaf_ie_name`, `roots`, toggles such as `include_markdown`, `pretty_file`, etc.). | `{"status":"ok","query": str,"paths": {...}, "tree": str?, "mermaid": str?, "tree_json": {...}?, "markdown": str?, "pretty_file_path": str?}` or `status` of `ambiguous_versions`/`not_found`. |
| `asntools_grep` | `GET /grep` | Query `pattern` (required), optional `asn1_path`, `regex` (bool, default false). | `{"status":"ok","query": str,"asn1_path": str,"match_count": int,"matches":[...],"chunks":[...]}`
or `{"status":"not_found",...}` when no hits. |
| `asntools_describe_field` | `GET /fields/{field_name}` | Path param `field_name`. | `{"status":"ok","query": str,"matches":[...],"variants":[...],"source": str}` or 404 with `detail.suggestions`. |
| `asntools_describe_ie` | `GET /field-descriptions/ies/{ie_name}` | Path param `ie_name`. | `{"status":"ok","query": str,"ie_name": str,"fields": {...},"variants":[...],"source": str}` or 404 with suggestions. |
| `asntools_help` | `GET /help` | none | `{"status":"ok","tools": [...]}` list describing every tool (see below). |

## `/compile`

```json
POST /compile
{
  "asn1_files": ["/abs/path/NR-RRC-Definitions.asn"],
  "description_files": ["/abs/path/field_descriptions.json"],
  "discover_dirs": ["/home/user/asninputs"],
  "subdirs": ["rrc"]
}
```

Returns paths to the merged ASN.1 file, generated pycrate module, and merged
field descriptions. Any relative path is resolved on the server.

## `/ies/{ie_name}`

Returns the same JSON payload printed by the CLI `--show` flag. Optional query
parameters:

- `compile` (bool, default `true`): automatically run `asntools --compile` if
  the pycrate outputs are missing.
- `asn1_path`: override the ASN.1 input path when auto-compiling.

## `/trees`

JSON body matches `TreeRequest`:

```json
{
  "leaf_ie_name": "ULInformationTransfer",
  "roots": ["RRCResume"],
  "tree_depth": 2,
  "include_tree": true,
  "include_mermaid": false,
  "include_tree_json": true,
  "include_markdown": true,
  "wrap_markdown": true,
  "pretty_file": true,
  "markdown_path": "artifacts/ULInformationTransfer_tree.md",
  "allow_version_aggregation": false
}
```

- `tree_depth` maps to the CLI `--tree-depth` flag and limits ancestor hops.
- `include_markdown` adds a Markdown block containing the ASCII tree.
- `wrap_markdown` controls whether the Markdown is fenced (default `true`).
- `pretty_file` mirrors `--tree-pretty`: the response includes the resolved
  markdown path and the server writes the Markdown file locally. When omitted,
  no file is written.
- `markdown_path` mirrors `--tree-markdown-output`; defaults to the CLI’s
  `artifacts/<ie>_tree.md` when `pretty_file` is `true`.

Responses contain `paths`, `tree`, `tree_json`, and optional `markdown`/
`mermaid` strings depending on the toggles provided.

## `/grep`

```http
GET /grep?pattern=RACHConfig&asn1_path=asn1/NR-RRC-Definitions.asn
```

- `pattern` (required): substring match is case-insensitive.
- `asn1_path` (optional): override the ASN.1 file to search; defaults to the merged `asn1/NR-RRC-Definitions.asn`.

Responses:

- On hits: `{"status":"ok","query": str,"asn1_path": str,"match_count": int,"matches":[{index,line,char_offset,message_length,message}], "chunks":[str,...]}`
- On miss: `{"status":"not_found","match_count":0,"matches":[],"chunks":[],"asn1_path": "..."}`

`chunks` aligns one-to-one with `matches` (currently the full lines containing each match).

## `/fields/{field_name}`

Returns all description entries that mention the field along with related
version variants. HTTP 404 responses include a `suggestions` list when the field
was not found.

## `/field-descriptions/ies/{ie_name}`

Returns the entire field-description table for one IE, matching the CLI
`--describe-ie` output.

## `/help`

Returns `{"status":"ok","tools":[...]}` where each entry documents the method,
path, expected request fields, and response shape for a tool. Agents can call
this endpoint at runtime to discover or refresh tool syntax.

## FastMCP server (recommended)

`asntools-fastmcp` wraps the FastAPI app with FastMCP so MCP clients can rely on
the standard `list_tools`/`list_resources` flows (no manual JSON config).

1. Start the MCP server on the machine that hosts your ASN.1 inputs:
   ```bash
   python -m venv .venv && source .venv/bin/activate
   pip install -e .[dev]
   asntools --compile --input-dir /path/to/asnfiles
   asntools-fastmcp --host 0.0.0.0 --port 8765 --path /mcp
   ```
   The command exposes a streamable-HTTP MCP endpoint at
   `http://SERVER:8765/mcp`. Every REST endpoint becomes an MCP tool with the
   friendly names from the cheat sheet, and `/help` is published as the
   `asntools_help` resource.
2. From any MCP-aware client (e.g., `fastmcp`’s CLI), verify connectivity:
   ```bash
   fastmcp client connect streamable-http http://SERVER:8765/mcp list-tools
   fastmcp client connect streamable-http http://SERVER:8765/mcp read-resource asntools_help
   ```
   You should see the auto-generated tool metadata plus the descriptive help
   resource.
3. Configure your Codex MCP agent (or any other MCP host) to point at the
   streamable-HTTP endpoint. Example `~/.config/codex/mcp_servers.json` entry:
   ```json
   {
     "name": "asntools",
     "type": "fastmcp",
     "transport": "streamable-http",
     "endpoint": "http://SERVER:8765/mcp"
   }
   ```
   Adjust keys to whatever your client expects (host/port/path are the only
   required pieces).
4. Restart the agent and run the standard MCP discovery commands (e.g.,
   `codex mcp list-tools asntools`). Call the `asntools_help` resource once to
   fetch the live payload descriptions, then invoke other tools as needed.
5. Harden the deployment when exposing it outside a trusted LAN: wrap the MCP
   endpoint behind TLS, add reverse-proxy auth, or tunnel the connection over
   SSH/VPN.

> **Fallback REST integration:** if you cannot run FastMCP in your environment,
> all REST endpoints remain available. Use the cheat sheet above plus your MCP
> client’s custom REST tooling to recreate the manual configuration.
