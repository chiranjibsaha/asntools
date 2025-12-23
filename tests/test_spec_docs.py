from __future__ import annotations

import json
from pathlib import Path

import pytest

from asntools import spec_config
from asntools.spec_docs import (
    SpecDocError,
    extract_section_html,
    html_fragment_to_markdown,
    html_fragment_to_text,
    load_toc_entries,
    load_toc_json,
    resolve_doc_paths,
    resolve_section_html_id,
)


def _write_fixture(docs_dir: Path) -> tuple[Path, Path]:
    html_path = docs_dir / "doc.html"
    toc_path = docs_dir / "doc_toc.json"

    html_path.write_text(
        "\n".join(
            [
                "<html><body>",
                '<h2 id="4-7-1-architecture">4.7.1 \u00a0\u00a0\u00a0\u00a0Architecture <a href="#4-7-1-architecture">#</a></h2>',
                "<p>First paragraph.</p>",
                '<h3 id="4-7-1-1-sub">4.7.1.1 Sub</h3>',
                "<p>Sub text.</p>",
                '<h2 id="4-7-2-next">4.7.2 Next</h2>',
                "<p>Next text.</p>",
                "</body></html>",
            ]
        ),
        encoding="utf-8",
    )

    toc_json = {
        "metadata": {"document": "doc"},
        "table_of_contents": [
            {
                "clause_id": "4.7.1",
                "clause_title": "Architecture",
                "level": 2,
                "id": "4-7-1-architecture",
                "children": [
                    {
                        "clause_id": "4.7.1.1",
                        "clause_title": "Sub",
                        "level": 3,
                        "id": "4-7-1-1-sub",
                        "children": [],
                    }
                ],
            },
            {
                "clause_id": "4.7.2",
                "clause_title": "Next",
                "level": 2,
                "id": "4-7-2-next",
                "children": [],
            },
        ],
    }
    toc_path.write_text(json.dumps(toc_json, indent=2), encoding="utf-8")
    return html_path, toc_path


def test_resolve_doc_paths(tmp_path: Path) -> None:
    docs_dir = tmp_path / "docs"
    docs_dir.mkdir()
    html_path, toc_path = resolve_doc_paths("doc", docs_dir=docs_dir)
    assert html_path == docs_dir / "doc.html"
    assert toc_path == docs_dir / "doc_toc.json"


def test_resolve_doc_paths_uses_config(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    config_path = tmp_path / "spec_config.json"
    config_path.write_text(json.dumps({"specs_dir": "custom_docs"}), encoding="utf-8")
    monkeypatch.setattr(spec_config, "_project_root", lambda: tmp_path)

    html_path, toc_path = resolve_doc_paths("doc")
    assert html_path == (tmp_path / "custom_docs" / "doc.html")
    assert toc_path == (tmp_path / "custom_docs" / "doc_toc.json")


def test_resolve_section_html_id_and_extract(tmp_path: Path) -> None:
    docs_dir = tmp_path / "docs"
    docs_dir.mkdir()
    html_path, toc_path = _write_fixture(docs_dir)

    toc_json = load_toc_json(toc_path)
    entries = load_toc_entries(toc_json)

    assert resolve_section_html_id(entries, "4.7.1") == "4-7-1-architecture"
    assert resolve_section_html_id(entries, "4-7-1") == "4-7-1-architecture"
    assert resolve_section_html_id(entries, "4-7-1-architecture") == "4-7-1-architecture"

    fragment = extract_section_html(html_path, "4-7-1", include_heading=True)
    assert "First paragraph." in fragment
    assert "Sub text." in fragment
    assert "Next text." not in fragment

    fragment_no_heading = extract_section_html(html_path, "4-7-1", include_heading=False)
    assert 'id="4-7-1-architecture"' not in fragment_no_heading
    assert "First paragraph." in fragment_no_heading

    text = html_fragment_to_text(fragment)
    assert "First paragraph." in text
    assert "Sub text." in text

    md = html_fragment_to_markdown(fragment)
    assert "First paragraph." in md
    assert "Sub text." in md


def test_missing_section_raises(tmp_path: Path) -> None:
    docs_dir = tmp_path / "docs"
    docs_dir.mkdir()
    _write_fixture(docs_dir)
    html_path = docs_dir / "doc.html"

    with pytest.raises(SpecDocError):
        extract_section_html(html_path, "9-9-9")
