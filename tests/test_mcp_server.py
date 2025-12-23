"""Tests for the FastMCP wrapper server."""
from __future__ import annotations

import anyio

from asntools.mcp_server import build_fastmcp_server


async def _collect_names(scope: str) -> set[str]:
    server = build_fastmcp_server()
    if scope == "tools":
        entries = await server.get_tools()
    else:
        entries = await server.get_resources()
    return set(entries.keys())


def test_fastmcp_tools_exposed():
    tool_names = anyio.run(_collect_names, "tools")
    assert "asntools_tree" in tool_names
    assert "asntools_describe_field" in tool_names


def test_fastmcp_help_resource():
    resource_names = anyio.run(_collect_names, "resources")
    assert any("help" in name for name in resource_names)
