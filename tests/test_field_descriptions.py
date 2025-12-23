"""Tests for field/flag description utilities."""
from __future__ import annotations

import json
from pathlib import Path

import pytest

from asntools.field_descriptions import FieldDescriptionStore, load_field_descriptions, parse_field_description_payload


def test_load_field_descriptions_supports_new_schema(tmp_path: Path):
    payload = tmp_path / "field_descriptions.json"
    payload.write_text(
        json.dumps(
            {
                "ies": {"Foo-IE": {"foo-field": "Foo description"}},
                "conditional_presence_flags": {"NeedS": "Needs description"},
            }
        ),
        encoding="utf-8",
    )
    store = load_field_descriptions(payload)
    matches = store.lookup_field("foo-field")
    assert len(matches) == 1
    assert matches[0].ie_name == "Foo-IE"
    assert store.lookup_field("NeedS")[0].kind == "conditional_presence_flag"


def test_lookup_field_across_multiple_ies(tmp_path: Path):
    payload = tmp_path / "field_descriptions.json"
    payload.write_text(
        json.dumps(
            {
                "_metadata": {},
                "Foo-IE": {"shared-field": "Foo"},
                "Foo-IE-r17": {"shared-field": "Foo r17"},
                "conditional-presence-flags": {"NeedS": "desc"},
            }
        ),
        encoding="utf-8",
    )
    store = load_field_descriptions(payload)
    matches = store.lookup_field("shared-field")
    assert {match.ie_name for match in matches} == {"Foo-IE", "Foo-IE-r17"}
    ie_variants = store.related_ie_versions("Foo-IE")
    assert "Foo-IE-r17" in ie_variants


def test_parse_field_description_payload_accepts_legacy():
    ie_fields, flags = parse_field_description_payload({"field_descriptions": {"foo": "bar"}})
    assert "_global" in ie_fields
    assert not flags
