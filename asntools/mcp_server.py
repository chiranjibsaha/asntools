"""FastMCP server exposing the asntools FastAPI endpoints as native MCP tools."""
from __future__ import annotations

import argparse
from typing import Sequence

from fastmcp import FastMCP
from fastmcp.server.openapi.routing import MCPType, RouteMap

from . import __version__
from .server import app as fastapi_app

INSTRUCTIONS = """MCP interface for NR-RRC ASN.1 tooling. Call `asntools_compile` to rebuild
pycrate artifacts, `asntools_show` to fetch an IE JSON definition, `asntools_tree`
for ancestry trees/markdown, `asntools_grep` to search ASN.1 text, and the describe
tools for field narratives. Use the `asntools_help` resource (GET /help) for
up-to-date payload examples."""

OPERATION_NAME_MAP = {
    "compile_endpoint_compile_post": "asntools_compile",
    "describe_endpoint_ies__ie_name__get": "asntools_show",
    "search_endpoint_ies_search_get": "asntools_search",
    "tree_endpoint_trees_post": "asntools_tree",
    "field_description_endpoint_fields__field_name__get": "asntools_describe_field",
    "ie_field_description_endpoint_field_descriptions_ies__ie_name__get": "asntools_describe_ie",
    "asntools_grep": "asntools_grep",
    "help_endpoint_help_get": "asntools_help",
}

ROUTE_MAPS: Sequence[RouteMap] = (
    RouteMap(
        methods=["GET"],
        pattern=r"^/health$",
        mcp_type=MCPType.EXCLUDE,
    ),
    RouteMap(
        methods=["GET"],
        pattern=r"^/field-descriptions/fields/.*$",
        mcp_type=MCPType.EXCLUDE,
    ),
    RouteMap(
        methods=["GET"],
        pattern=r"^/help$",
        mcp_type=MCPType.RESOURCE,
    ),
)


def build_fastmcp_server() -> FastMCP:
    """Create a FastMCP server backed by the FastAPI app."""

    return FastMCP.from_fastapi(
        fastapi_app,
        name="asntools",
        version=__version__,
        instructions=INSTRUCTIONS,
        route_maps=list(ROUTE_MAPS),
        mcp_names=OPERATION_NAME_MAP,
        tags={"asntools"},
    )


def main(argv: Sequence[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        prog="asntools-fastmcp",
        description="Expose NR-RRC ASN.1 tooling over the FastMCP protocol.",
    )
    parser.add_argument(
        "--host",
        default="127.0.0.1",
        help="Interface to bind when using HTTP transports (ignored for stdio).",
    )
    parser.add_argument(
        "--port",
        default=8765,
        type=int,
        help="Port for HTTP/SSE transports.",
    )
    parser.add_argument(
        "--path",
        default="/mcp",
        help="HTTP path for streamable-http/SSE transports (default: /mcp).",
    )
    parser.add_argument(
        "--transport",
        choices=["stdio", "http", "streamable-http", "sse"],
        default="streamable-http",
        help="FastMCP transport to use (streamable-http works with Codex MCP).",
    )
    args = parser.parse_args(argv)

    server = build_fastmcp_server()
    if args.transport == "stdio":
        server.run(transport="stdio")
    else:
        server.run(
            transport=args.transport,
            host=args.host,
            port=args.port,
            path=args.path,
        )


__all__ = ["build_fastmcp_server", "main"]
