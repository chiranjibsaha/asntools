# Spec Doc Tools (`asntools-spec-toc`, `asntools-spec-extract`)

These tools work with spec HTML documents stored under the directory configured in `spec_config.json`
(`specs_dir`, defaults to `./doc`) and their TOC JSON files (same basename, suffixed with `_toc.json`).

## Setup

Install the project so the entrypoints are available:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Files Expected

For a document basename like `38300-j00`:

- HTML: `docs/38300-j00.html`
- TOC JSON: `docs/38300-j00_toc.json`

You can pass either the basename or a path to the HTML/TOC file as `DOC`.

## Inspect TOC

Print the table of contents:

```bash
asntools-spec-toc 38300-j00
```

Filter by prefix (clause or id prefix):

```bash
asntools-spec-toc 38300-j00 --prefix 4.7
asntools-spec-toc 38300-j00 --prefix 4-7
```

Search by substring:

```bash
asntools-spec-toc 38300-j00 --search architecture
```

Emit JSON instead of text:

```bash
asntools-spec-toc 38300-j00 --format json
```

Use a non-default docs directory:

```bash
asntools-spec-toc 38300-j00 --docs-dir /path/to/docs
```

If `--docs-dir` is not provided, the directory comes from `spec_config.json` in the project root.

## Extract a Section

By default this extracts the section, converts HTML→Markdown, saves it to an auto-named file, and prints the output path:

```bash
asntools-spec-extract 38300-j00 4-7-2
```

Section selectors accepted:

- Clause id: `4.7.2`
- Exact heading id: `4-7-2-protocol-stacks`
- Heading id prefix: `4-7-2` (resolves to the best matching heading id)

### Output Control

Write to an explicit file path:

```bash
asntools-spec-extract 38300-j00 4-7-2 --output artifacts/my_section.md
```

Choose the directory for auto-named markdown output:

```bash
asntools-spec-extract 38300-j00 4-7-2 --out-dir artifacts/sections
```

Return HTML or plain text instead of Markdown:

```bash
asntools-spec-extract 38300-j00 4-7-2 --format html
asntools-spec-extract 38300-j00 4-7-2 --format text
```

Exclude the heading tag itself (extract only the content following it):

```bash
asntools-spec-extract 38300-j00 4-7-2 --no-include-heading
```

## Spec Extraction API

Run the dedicated FastAPI server on a different port from the main asntools API:

```bash
asntools-spec-api  # defaults to 0.0.0.0:8010
```

- Sections: `GET /specs/{spec_id}/sections/{section_id}`  
  Returns markdown plus chunk metadata (`bytes`, `chunk_count`, `chunks[*].md_snippet`). Use `chunk_size` to tune the maximum characters per chunk.  
  Optional `docs_dir` overrides the configured specs directory.
- Sections by heading: `GET /specs/{spec_id}/sections/by-heading?heading_text=...`  
  Matches heading text case-insensitively; returns the section markdown with chunk metadata. If no match, responds 404 with `suggestions` of close headings. `include_heading` and `chunk_size` are supported.
- Grep: `GET /specs/{spec_id}/grep?pattern=...`  
  Case-insensitive substring search across the spec HTML. Set `regex=true` to treat the pattern as a regex (compiled with `re.IGNORECASE`; invalid regex → HTTP 400). Returns structured matches with `match_count`, per-match `line`, `char_offset`, `message_length`, `message`, and `chunks` (one per match). Optional `docs_dir` overrides the specs directory.
- TOC: `GET /specs/{spec_id}/toc`  
  Returns the table of contents as JSON. Optional `depth` limits tree depth (1 = top level only). Optional `section_id` filters by clause/html id prefix (e.g. `2.2.1` or `2-2-1`). `docs_dir` can override the configured specs directory.
- Tables: `GET /specs/{spec_id}/tables/{table_id}`  
  Finds the table by caption prefix (e.g. “Table 7.2.1-1”) or table id attribute, returns markdown plus caption and chunk metadata.

## FastMCP server (specs)

`asntools-spec-mcp` wraps the spec API in FastMCP so MCP clients can call the endpoints as tools without hand-written configs.

1. Start the server (default transport: streamable-http):
   ```bash
   asntools-spec-mcp --host 0.0.0.0 --port 8810 --path /spec-mcp
   ```
   - Use `--transport stdio` for local pipes, or keep the default for HTTP/SSE.
2. Discover tools with a FastMCP client:
   ```bash
   fastmcp client connect streamable-http http://SERVER:8810/spec-mcp list-tools
   fastmcp client connect streamable-http http://SERVER:8810/spec-mcp read-resource spec_help
   ```
3. Available MCP tools (operation ids):  
   - `spec_sections_get` → GET `/specs/{spec_id}/sections/{section_id}`  
   - `spec_sections_by_heading_get` → GET `/specs/{spec_id}/sections/by-heading`  
   - `spec_tables_get` → GET `/specs/{spec_id}/tables/{table_id}`  
   - `spec_toc_get` → GET `/specs/{spec_id}/toc`  
   - `spec_grep_get` → GET `/specs/{spec_id}/grep`  
   (`spec_health_get` is excluded; `/help` is exposed as the `spec_help` MCP resource.)

The `spec_help` resource mirrors `/help` metadata so agents can pull live request/response shapes. Tools support the same parameters documented above (including `docs_dir` overrides and `regex` for grep).
