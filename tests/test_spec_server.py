from __future__ import annotations

import importlib
import json
from pathlib import Path
import sys
import types
import pytest

from fastapi.testclient import TestClient

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Stub pycrate deps only when the real dependency is unavailable.
if importlib.util.find_spec("pycrate_asn1c") is None:
    stub_asnproc = types.ModuleType("pycrate_asn1c.asnproc")
    stub_asnproc.GLOBAL = {}
    stub_asnproc.JSONDepGraphGenerator = object
    stub_asnproc.PycrateGenerator = object
    stub_asnproc.compile_text = lambda *args, **kwargs: None
    stub_asnproc.generate_modules = lambda *args, **kwargs: None
    sys.modules.setdefault("pycrate_asn1c", types.ModuleType("pycrate_asn1c"))
    sys.modules["pycrate_asn1c"].asnproc = stub_asnproc
    sys.modules["pycrate_asn1c.asnproc"] = stub_asnproc

if importlib.util.find_spec("pycrate_asn1rt") is None:
    stub_dictobj = types.ModuleType("pycrate_asn1rt.dictobj")
    stub_dictobj.ASN1Dict = dict
    stub_setobj = types.ModuleType("pycrate_asn1rt.setobj")
    stub_setobj.ASN1Set = set
    sys.modules.setdefault("pycrate_asn1rt", types.ModuleType("pycrate_asn1rt"))
    sys.modules["pycrate_asn1rt"].dictobj = stub_dictobj
    sys.modules["pycrate_asn1rt"].setobj = stub_setobj
    sys.modules["pycrate_asn1rt.dictobj"] = stub_dictobj
    sys.modules["pycrate_asn1rt.setobj"] = stub_setobj

from asntools.spec_server import app

spec_mcp_available = importlib.util.find_spec("fastmcp") is not None
if spec_mcp_available:
    from asntools.spec_mcp_server import build_spec_fastmcp_server


def _write_fixture(tmp_path: Path) -> tuple[str, Path]:
    docs_dir = tmp_path / "docs"
    docs_dir.mkdir()

    html_path = docs_dir / "38300-j00.html"
    toc_path = docs_dir / "38300-j00_toc.json"

    html_path.write_text(
        "\n".join(
            [
                "<html><body>",
                '<h2 id="1-1">1.1 Intro</h2>',
                "<p>Intro text.</p>",
                '<h3 id="1-1-1-table-sec">1.1.1 Table Section</h3>',
                "<p>Table 7.2.1-1: Mapping of commands</p>",
                '<table id="t7211">',
                "<tr><th>Cmd</th><th>Delta</th></tr>",
                "<tr><td>00</td><td>-1</td></tr>",
                "<tr><td>01</td><td>+1</td></tr>",
                "</table>",
                '<h2 id="1-2">1.2 Next</h2>',
                "<p>Next text.</p>",
                "</body></html>",
            ]
        ),
        encoding="utf-8",
    )

    toc_json = {
        "metadata": {"document": "38300-j00"},
        "table_of_contents": [
            {"clause_id": "1.1", "clause_title": "Intro", "level": 2, "id": "1-1", "children": []},
            {
                "clause_id": "1.1.1",
                "clause_title": "Table Section",
                "level": 3,
                "id": "1-1-1-table-sec",
                "children": [],
            },
            {"clause_id": "1.2", "clause_title": "Next", "level": 2, "id": "1-2", "children": []},
        ],
    }
    toc_path.write_text(json.dumps(toc_json, indent=2), encoding="utf-8")
    return "38300-j00", docs_dir


def test_toc_endpoint_filters_depth_and_section(tmp_path: Path) -> None:
    spec_id, docs_dir = _write_fixture(tmp_path)
    client = TestClient(app)

    resp = client.get(f"/specs/{spec_id}/toc", params={"docs_dir": str(docs_dir), "depth": 1})
    assert resp.status_code == 200
    toc = resp.json()["toc"]
    assert all(item["depth"] == 0 for item in toc)
    assert len(toc) >= 1

    resp2 = client.get(f"/specs/{spec_id}/toc", params={"docs_dir": str(docs_dir), "section_id": "1.1"})
    assert resp2.status_code == 200
    toc2 = resp2.json()["toc"]
    assert any(item["clause_id"] == "1.1.1" for item in toc2)
    assert all(item["id"].startswith("1-1") for item in toc2)


def test_section_search_by_heading(tmp_path: Path) -> None:
    spec_id, docs_dir = _write_fixture(tmp_path)
    client = TestClient(app)

    resp = client.get(
        f"/specs/{spec_id}/sections/by-heading",
        params={"docs_dir": str(docs_dir), "heading_text": "Table Section", "chunk_size": 50},
    )
    assert resp.status_code == 200
    payload = resp.json()
    assert payload["html_id"] == "1-1-1-table-sec"
    assert payload["markdown"]["chunk_count"] >= 1

    resp2 = client.get(
        f"/specs/{spec_id}/sections/by-heading",
        params={"docs_dir": str(docs_dir), "heading_text": "Nonexistent Heading"},
    )
    assert resp2.status_code == 404
    detail = resp2.json()["detail"]
    assert "suggestions" in detail
    assert isinstance(detail["suggestions"], list)


def test_section_endpoint_returns_chunked_markdown(tmp_path: Path) -> None:
    spec_id, docs_dir = _write_fixture(tmp_path)
    client = TestClient(app)

    resp = client.get(
        f"/specs/{spec_id}/sections/1-1-1-table-sec",
        params={"docs_dir": str(docs_dir), "chunk_size": 20},
    )
    assert resp.status_code == 200
    payload = resp.json()

    md_info = payload["markdown"]
    assert md_info["bytes"] == len(md_info["md"].encode("utf-8"))
    assert md_info["chunk_count"] >= 1
    assert len(md_info["chunks"]) == md_info["chunk_count"]
    assert "Table 7.2.1-1" in md_info["md"]
    # Table should be converted to markdown pipes.
    assert "| Cmd | Delta |" in md_info["md"]


def test_table_endpoint_finds_caption(tmp_path: Path) -> None:
    spec_id, docs_dir = _write_fixture(tmp_path)
    client = TestClient(app)

    resp = client.get(f"/specs/{spec_id}/tables/7.2.1-1", params={"docs_dir": str(docs_dir)})
    assert resp.status_code == 200
    payload = resp.json()
    assert payload["caption"].startswith("Table 7.2.1-1")
    assert "| Cmd | Delta |" in payload["markdown"]["md"]
    assert payload["markdown"]["bytes"] == len(payload["markdown"]["md"].encode("utf-8"))


def test_grep_regex(tmp_path: Path) -> None:
    spec_id, docs_dir = _write_fixture(tmp_path)
    client = TestClient(app)

    # Regex spanning words, case-insensitive.
    resp = client.get(
        f"/specs/{spec_id}/grep",
        params={"docs_dir": str(docs_dir), "pattern": r"table\s+7\.2\.1-1", "regex": True},
    )
    assert resp.status_code == 200, resp.text
    payload = resp.json()
    assert payload["status"] == "ok"
    assert payload["match_count"] >= 1
    assert any("Table 7.2.1-1" in chunk for chunk in payload["chunks"])


@pytest.mark.skipif(not spec_mcp_available, reason="fastmcp not installed")
def test_spec_fastmcp_builds():
    server = build_spec_fastmcp_server()
    # Basic sanity: ensure tool mapping contains the spec endpoints.
    assert "spec_sections_get" in server.tool_names
    assert "spec_grep_get" in server.tool_names
