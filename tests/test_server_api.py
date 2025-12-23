"""Focused tests for new API endpoints."""
from __future__ import annotations

import json
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from asntools import server
from asntools.field_descriptions import FieldDescriptionStore
from asntools.introspect import IESelection


@pytest.fixture()
def client():
    return TestClient(server.app)


def _seed_field_store(tmp_path: Path) -> None:
    desc_file = tmp_path / "asn1" / "field_descriptions.json"
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
                "conditional_presence_flags": {
                    "NeedS": "Needs description",
                },
            }
        ),
        encoding="utf-8",
    )


def test_field_endpoint_not_found(tmp_path, monkeypatch, client):
    _seed_field_store(tmp_path)
    monkeypatch.chdir(tmp_path)
    resp = client.get("/fields/UnknownField")
    assert resp.status_code == 404
    detail = resp.json()["detail"]
    assert "No description" in detail["message"]
    assert detail["suggestions"]


def test_ie_endpoint_not_found(tmp_path, monkeypatch, client):
    _seed_field_store(tmp_path)
    monkeypatch.chdir(tmp_path)
    resp = client.get("/field-descriptions/ies/UnknownIE")
    assert resp.status_code == 404
    assert "No field description" in resp.json()["detail"]["message"]


def test_help_endpoint(client):
    resp = client.get("/help")
    assert resp.status_code == 200
    payload = resp.json()
    names = {entry["name"] for entry in payload["tools"]}
    assert "asntools_tree" in names
    tree_info = next(entry for entry in payload["tools"] if entry["name"] == "asntools_tree")
    assert tree_info["method"] == "POST"
    assert "/trees" in tree_info["path"]


def test_tree_endpoint_markdown_variants(monkeypatch, tmp_path, client):
    monkeypatch.setattr(server, "_ensure_definitions_ready", lambda compile, asn1_path: None)
    monkeypatch.setattr(server, "load_rrc_definitions", lambda: object())
    monkeypatch.setattr(
        server,
        "search_ie_names",
        lambda leaf, definitions=None: [IESelection(attr_name="Foo", display_name="Foo")],
    )
    monkeypatch.setattr(
        server,
        "find_leaf_paths",
        lambda leaf, definitions=None, root_ie_names=None: {"Root": [["Root", "Foo"]]},
    )
    monkeypatch.setattr(server, "format_leaf_paths_as_tree", lambda paths: "TREE" if paths else "")
    monkeypatch.setattr(server, "format_leaf_paths_as_nested", lambda paths: {"Root": {"name": "Root"}})
    monkeypatch.setattr(server, "format_leaf_paths_as_mermaid", lambda paths: "graph TD; Root-->Foo;")

    body = {
        "leaf_ie_name": "Foo",
        "include_markdown": True,
        "wrap_markdown": False,
        "pretty_file": True,
        "markdown_path": str(tmp_path / "custom.md"),
    }
    resp = client.post("/trees", json=body)
    assert resp.status_code == 200
    payload = resp.json()
    assert payload["markdown"] == "TREE"
    assert payload["pretty_file_path"].endswith("custom.md")
    assert Path(payload["pretty_file_path"]).read_text(encoding="utf-8").strip() == "TREE"
