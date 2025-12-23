"""Tests for the FastAPI server."""
from __future__ import annotations

import json
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from asntools import server
from asntools import rebuild
from asntools.introspect import IESelection


@pytest.fixture()
def client():
    return TestClient(server.app)


def test_health_endpoint(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


def test_compile_endpoint_success(monkeypatch, tmp_path, client):
    def fake_compile(asn1_path: Path, output_dir: Path, emit_json: bool = True) -> Path:  # noqa: ARG001
        output_dir.mkdir(parents=True, exist_ok=True)
        generated = output_dir / "NR_RRC_Definitions.py"
        generated.write_text("# generated\n", encoding="utf-8")
        return generated

    monkeypatch.setattr(rebuild, "compile_nr_rrc", fake_compile)
    monkeypatch.chdir(tmp_path)

    src = Path("input.asn")
    src.write_text("hello", encoding="utf-8")
    desc = Path("desc.json")
    desc.write_text('{"field_descriptions": {"Foo": "Bar"}}', encoding="utf-8")

    resp = client.post(
        "/compile",
        json={"asn1_files": [str(src)], "description_files": [str(desc)]},
    )
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "ok"
    assert Path(data["merged_asn1"]).exists()
    assert Path(data["module"]).exists()
    assert Path(data["field_descriptions"]).exists()


def test_compile_endpoint_missing_file(client):
    resp = client.post("/compile", json={"asn1_files": ["missing.asn"]})
    assert resp.status_code == 400
    assert "not found" in resp.json()["detail"]


def test_describe_endpoint_success(monkeypatch, client):
    monkeypatch.setattr(server, "_ensure_definitions_ready", lambda compile, asn1_path: None)
    monkeypatch.setattr(server, "load_rrc_definitions", lambda: object())
    monkeypatch.setattr(server, "describe_ie", lambda name, definitions=None: {"ie": name})

    resp = client.get("/ies/TestIE")
    assert resp.status_code == 200
    assert resp.json()["data"] == {"ie": "TestIE"}


def test_describe_endpoint_not_found(monkeypatch, client):
    monkeypatch.setattr(server, "_ensure_definitions_ready", lambda compile, asn1_path: None)
    monkeypatch.setattr(server, "load_rrc_definitions", lambda: object())

    def _raise(*args, **kwargs):
        raise server.IENameError("missing")

    monkeypatch.setattr(server, "describe_ie", _raise)

    resp = client.get("/ies/UnknownIE")
    assert resp.status_code == 404
    assert "missing" in resp.json()["detail"]


def test_tree_endpoint_success(monkeypatch, client):
    monkeypatch.setattr(server, "_ensure_definitions_ready", lambda compile, asn1_path: None)
    fake_definitions = object()
    monkeypatch.setattr(server, "load_rrc_definitions", lambda: fake_definitions)
    monkeypatch.setattr(
        server,
        "search_ie_names",
        lambda leaf, definitions=None: [IESelection(attr_name="foo", display_name="Foo")],
    )
    monkeypatch.setattr(
        server,
        "find_leaf_paths",
        lambda leaf, definitions=None, root_ie_names=None: {"RRCResume/RRCReconfiguration": [["root", "leaf"]]},
    )
    monkeypatch.setattr(server, "format_leaf_paths_as_tree", lambda paths: "TREE")
    monkeypatch.setattr(server, "format_leaf_paths_as_mermaid", lambda paths: "GRAPH")

    resp = client.post(
        "/trees",
        json={"leaf_ie_name": "foo", "include_mermaid": True, "include_markdown": True},
    )
    assert resp.status_code == 200
    payload = resp.json()
    assert payload["status"] == "ok"
    assert payload["tree"] == "TREE"
    assert payload["mermaid"] == "GRAPH"
    assert payload["markdown"] == "TREE"
    assert payload["tree_json"] == {
        "RRCResume/RRCReconfiguration": {
            "name": "RRCResume/RRCReconfiguration",
            "children": [{"name": "leaf", "children": []}],
        }
    }


def test_tree_endpoint_ambiguous(monkeypatch, client):
    monkeypatch.setattr(server, "_ensure_definitions_ready", lambda compile, asn1_path: None)
    monkeypatch.setattr(server, "load_rrc_definitions", lambda: object())
    selections = [
        IESelection(attr_name="Foo", display_name="Foo-v1"),
        IESelection(attr_name="Foo2", display_name="Foo-v2"),
    ]
    monkeypatch.setattr(server, "search_ie_names", lambda leaf, definitions=None: selections)

    resp = client.post("/trees", json={"leaf_ie_name": "Foo"})
    assert resp.status_code == 200
    payload = resp.json()
    assert payload["status"] == "ambiguous_versions"
    assert payload["variants"] == ["Foo-v1", "Foo-v2"]


def test_compile_endpoint_discover_dirs(monkeypatch, tmp_path, client):
    def fake_compile(asn1_path: Path, output_dir: Path, emit_json: bool = True) -> Path:  # noqa: ARG001
        output_dir.mkdir(parents=True, exist_ok=True)
        generated = output_dir / "NR_RRC_Definitions.py"
        generated.write_text("# generated\n", encoding="utf-8")
        return generated

    monkeypatch.setattr(rebuild, "compile_nr_rrc", fake_compile)
    monkeypatch.chdir(tmp_path)

    root = Path("inputs")
    sub = root / "nested"
    other = root / "other"
    sub.mkdir(parents=True)
    other.mkdir(parents=True)
    (sub / "a.asn").write_text("AAA", encoding="utf-8")
    (sub / "a_asn_field_description.json").write_text(
        '{"field_descriptions": {"A": "desc"}}',
        encoding="utf-8",
    )
    (other / "ignored.asn").write_text("IGNORED", encoding="utf-8")

    resp = client.post("/compile", json={"discover_dirs": [str(root)], "subdirs": ["nested"]})
    assert resp.status_code == 200
    data = resp.json()
    assert Path(data["merged_asn1"]).exists()
    assert Path(data["module"]).exists()
    assert Path(data["field_descriptions"]).exists()
    merged_text = Path(data["merged_asn1"]).read_text(encoding="utf-8")
    assert "AAA" in merged_text and "IGNORED" not in merged_text


def test_field_description_endpoint(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    desc_file = Path("asn1/field_descriptions.json")
    desc_file.parent.mkdir(parents=True, exist_ok=True)
    desc_file.write_text(
        json.dumps(
            {
                "ies": {
                    "Foo-IE": {
                        "FooField": "Foo desc",
                    }
                },
                "conditional_presence_flags": {
                    "NeedS": "Needs desc",
                },
            }
        ),
        encoding="utf-8",
    )
    with TestClient(server.app) as local_client:
        resp = local_client.get("/fields/FooField")
        assert resp.status_code == 200, resp.text
        payload = resp.json()
        assert payload["matches"][0]["description"] == "Foo desc"
        assert payload["matches"][0]["ie_name"] == "Foo-IE"
        assert payload["variants"] == []


def test_ie_field_description_endpoint(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    desc_file = Path("asn1/field_descriptions.json")
    desc_file.parent.mkdir(parents=True, exist_ok=True)
    desc_file.write_text(
        json.dumps(
            {
                "ies": {
                    "Foo-IE": {
                        "FooField": "Foo desc",
                    },
                    "Foo-IE-r17": {
                        "FooField": "Foo desc r17",
                    },
                },
            }
        ),
        encoding="utf-8",
    )
    with TestClient(server.app) as local_client:
        resp = local_client.get("/field-descriptions/ies/Foo-IE")
        assert resp.status_code == 200, resp.text
        payload = resp.json()
        assert payload["ie_name"] == "Foo-IE"
        assert "FooField" in payload["fields"]
        assert "Foo-IE-r17" in payload["variants"]


def test_grep_endpoint(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    asn_dir = Path("asn1")
    asn_dir.mkdir(parents=True, exist_ok=True)
    target = asn_dir / "NR-RRC-Definitions.asn"
    target.write_text("LineOne\nRACHConfig here\nAnother RACHConfig\n", encoding="utf-8")

    with TestClient(server.app) as local_client:
        resp = local_client.get("/grep", params={"pattern": "RACHConfig"})
        assert resp.status_code == 200, resp.text
        payload = resp.json()
        assert payload["status"] == "ok"
        assert payload["match_count"] == 2
        assert len(payload["chunks"]) == 2
        assert "RACHConfig here" in payload["chunks"][0]


def test_grep_endpoint_regex(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    asn_dir = Path("asn1")
    asn_dir.mkdir(parents=True, exist_ok=True)
    target = asn_dir / "NR-RRC-Definitions.asn"
    target.write_text("alpha Beta gamma\nBETA delta\n", encoding="utf-8")

    with TestClient(server.app) as local_client:
        resp = local_client.get("/grep", params={"pattern": r"b.ta", "regex": True})
        assert resp.status_code == 200, resp.text
        payload = resp.json()
        assert payload["status"] == "ok"
        assert payload["match_count"] == 2
