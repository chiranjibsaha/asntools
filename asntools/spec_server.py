"""FastAPI server for spec document extraction (sections + tables)."""

from __future__ import annotations

import difflib
import re
from pathlib import Path
from typing import Optional

import uvicorn
from fastapi import FastAPI, HTTPException, Query

from . import __version__
from .spec_docs import (
    SpecDocError,
    extract_section_html,
    extract_table_html,
    filter_toc_entries,
    html_fragment_to_markdown,
    load_toc_entries,
    load_toc_json,
    resolve_doc_paths,
    resolve_section_html_id,
    table_html_to_markdown,
)

DEFAULT_CHUNK_SIZE = 10_000
DEFAULT_SPEC_API_PORT = 8010

app = FastAPI(title="asntools-spec-api", version=__version__)


def _build_chunked_markdown(md: str, chunk_size: int = DEFAULT_CHUNK_SIZE) -> dict:
    if chunk_size < 1:
        raise ValueError("chunk_size must be >= 1")
    if not md:
        md = ""

    chunks = [md[i : i + chunk_size] for i in range(0, len(md), chunk_size)] or [""]
    chunk_items = [
        {"id": idx + 1, "md_snippet": chunk, "length": len(chunk)} for idx, chunk in enumerate(chunks)
    ]

    return {
        "bytes": len(md.encode("utf-8")),
        "chunk_size": chunk_size,
        "chunk_count": len(chunks),
        "md": md,
        "chunks": chunk_items,
    }


def _search_spec_text(pattern: str, html_path: Path, use_regex: bool = False) -> dict:
    if not pattern:
        raise ValueError("pattern must be non-empty")
    if not html_path.exists():
        raise FileNotFoundError(f"Spec HTML not found at {html_path}")

    text = html_path.read_text(encoding="utf-8")
    flags = re.IGNORECASE
    if use_regex:
        try:
            compiled = re.compile(pattern, flags)
        except re.error as exc:
            raise ValueError(f"invalid regex: {exc}") from exc
    else:
        pattern_lower = pattern.lower()

    matches = []
    char_offset = 0
    for line_no, line in enumerate(text.splitlines(), start=1):
        if use_regex:
            for match in compiled.finditer(line):
                idx = match.start()
                matches.append(
                    {
                        "index": len(matches) + 1,
                        "line": line_no,
                        "char_offset": char_offset + idx,
                        "message_length": len(line),
                        "message": line,
                    }
                )
        else:
            search_start = 0
            line_lower = line.lower()
            while True:
                idx = line_lower.find(pattern_lower, search_start)
                if idx == -1:
                    break
                matches.append(
                    {
                        "index": len(matches) + 1,
                        "line": line_no,
                        "char_offset": char_offset + idx,
                        "message_length": len(line),
                        "message": line,
                    }
                )
                search_start = idx + len(pattern_lower) or idx + 1
        char_offset += len(line) + 1

    if not matches:
        return {
            "status": "not_found",
            "match_count": 0,
            "matches": [],
            "chunks": [],
        }

    return {
        "status": "ok",
        "match_count": len(matches),
        "matches": matches,
        "chunks": [m["message"] for m in matches],
    }


def _find_heading_by_title(entries, heading_text: str):
    wanted = heading_text.strip().lower()
    # Exact (case-insensitive) match wins
    for _, entry in filter_toc_entries(entries, search=None):
        if entry.clause_title.strip().lower() == wanted:
            return entry
    # Otherwise any entry containing the substring
    candidates = [e for _, e in filter_toc_entries(entries, search=heading_text)]
    if candidates:
        candidates.sort(key=lambda e: (len(e.clause_title), len(e.html_id)))
        return candidates[0]
    return None


@app.get("/specs/{spec_id}/sections/by-heading", operation_id="spec_sections_by_heading_get")
def get_section_by_heading(
    spec_id: str,
    heading_text: str = Query(..., description="Heading text to match (case-insensitive)."),
    include_heading: bool = Query(True, description="Include the heading tag in the extraction."),
    chunk_size: int = Query(DEFAULT_CHUNK_SIZE, ge=1, description="Maximum characters per markdown chunk."),
    docs_dir: Optional[str] = Query(
        None,
        description="Optional override for the specs directory. Defaults to specs_dir from spec_config.json.",
    ),
) -> dict:
    """Find a section by heading text and return it as markdown with chunk metadata."""
    try:
        html_path, toc_path = _resolve_paths(spec_id, docs_dir)
        toc_json = load_toc_json(toc_path)
        entries = load_toc_entries(toc_json)
        entry = _find_heading_by_title(entries, heading_text)
        if not entry:
            titles = [e.clause_title for _, e in filter_toc_entries(entries, search=None)]
            suggestions = difflib.get_close_matches(heading_text, titles, n=5, cutoff=0.4)
            raise HTTPException(
                status_code=404,
                detail={"message": f"Heading not found: {heading_text}", "suggestions": suggestions},
            )
        section_html_id = entry.html_id
        fragment = extract_section_html(html_path, section_html_id, include_heading=include_heading)
        markdown = html_fragment_to_markdown(fragment)
        payload = _build_chunked_markdown(markdown, chunk_size=chunk_size)
    except SpecDocError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    return {
        "status": "ok",
        "spec_id": spec_id,
        "section_heading": heading_text,
        "html_id": section_html_id,
        "include_heading": include_heading,
        "markdown": payload,
        "source": {"html_path": str(html_path), "toc_path": str(toc_path)},
    }


def _resolve_paths(spec_id: str, docs_dir: Optional[str]) -> tuple[Path, Path]:
    docs_path = Path(docs_dir) if docs_dir else None
    return resolve_doc_paths(spec_id, docs_dir=docs_path)


@app.get("/specs/{spec_id}/toc", operation_id="spec_toc_get")
def get_toc(
    spec_id: str,
    depth: Optional[int] = Query(
        None,
        ge=1,
        description="Limit to this heading depth (1=top level). Applies to tree depth in the TOC.",
    ),
    section_id: Optional[str] = Query(
        None,
        description="Optional clause/html id prefix filter, e.g. '2.2.1' or '2-2-1'.",
    ),
    docs_dir: Optional[str] = Query(
        None,
        description="Optional override for the specs directory. Defaults to specs_dir from spec_config.json.",
    ),
) -> dict:
    try:
        _, toc_path = _resolve_paths(spec_id, docs_dir)
        toc_json = load_toc_json(toc_path)
        entries = load_toc_entries(toc_json)
        items = filter_toc_entries(
            entries,
            prefix=section_id,
            max_depth=(depth - 1) if depth is not None else None,
        )
    except SpecDocError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc

    toc_items = [
        {
            "depth": depth_val,
            "clause_id": entry.clause_id,
            "clause_title": entry.clause_title,
            "level": entry.level,
            "id": entry.html_id,
        }
        for depth_val, entry in items
    ]
    return {
        "status": "ok",
        "spec_id": spec_id,
        "depth_limit": depth,
        "section_filter": section_id,
        "toc": toc_items,
        "source": {"toc_path": str(toc_path)},
    }


@app.get("/health", operation_id="spec_health_get")
def health() -> dict:
    return {"status": "ok"}


@app.get("/specs/{spec_id}/grep", operation_id="spec_grep_get")
def grep_spec(
    spec_id: str,
    pattern: str = Query(..., min_length=1, description="Substring to search (case-insensitive)."),
    regex: bool = Query(
        False, description="Treat pattern as a regex (case-insensitive). Invalid regex returns HTTP 400."
    ),
    docs_dir: Optional[str] = Query(
        None,
        description="Optional override for the specs directory. Defaults to specs_dir from spec_config.json.",
    ),
) -> dict:
    """Search a spec HTML document for a substring and return structured matches."""

    try:
        html_path, toc_path = _resolve_paths(spec_id, docs_dir)
        payload = _search_spec_text(pattern, html_path, use_regex=regex)
    except SpecDocError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except FileNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    payload.update(
        {
            "spec_id": spec_id,
            "query": pattern,
            "source": {"html_path": str(html_path), "toc_path": str(toc_path)},
        }
    )
    return payload


@app.get("/specs/{spec_id}/sections/{section_id}", operation_id="spec_sections_get")
def get_section(
    spec_id: str,
    section_id: str,
    include_heading: bool = Query(True, description="Include the heading tag in the extraction."),
    chunk_size: int = Query(DEFAULT_CHUNK_SIZE, ge=1, description="Maximum characters per markdown chunk."),
    docs_dir: Optional[str] = Query(
        None,
        description="Optional override for the specs directory. Defaults to specs_dir from spec_config.json.",
    ),
) -> dict:
    """Extract a section as Markdown with chunk metadata."""

    try:
        html_path, toc_path = _resolve_paths(spec_id, docs_dir)
        toc_json = load_toc_json(toc_path)
        entries = load_toc_entries(toc_json)
        section_html_id = resolve_section_html_id(entries, section_id)
        fragment = extract_section_html(html_path, section_html_id, include_heading=include_heading)
        markdown = html_fragment_to_markdown(fragment)
        payload = _build_chunked_markdown(markdown, chunk_size=chunk_size)
    except SpecDocError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    return {
        "status": "ok",
        "spec_id": spec_id,
        "section_id": section_id,
        "html_id": section_html_id,
        "include_heading": include_heading,
        "markdown": payload,
        "source": {"html_path": str(html_path), "toc_path": str(toc_path)},
    }


@app.get("/specs/{spec_id}/tables/{table_id}", operation_id="spec_tables_get")
def get_table(
    spec_id: str,
    table_id: str,
    chunk_size: int = Query(DEFAULT_CHUNK_SIZE, ge=1, description="Maximum characters per markdown chunk."),
    docs_dir: Optional[str] = Query(
        None,
        description="Optional override for the specs directory. Defaults to specs_dir from spec_config.json.",
    ),
) -> dict:
    """Extract a specific table as structured Markdown."""

    try:
        html_path, _ = _resolve_paths(spec_id, docs_dir)
        extracted = extract_table_html(html_path, table_id)
        markdown = table_html_to_markdown(extracted.html)
        payload = _build_chunked_markdown(markdown, chunk_size=chunk_size)
    except SpecDocError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    return {
        "status": "ok",
        "spec_id": spec_id,
        "table_id": table_id,
        "caption": extracted.caption,
        "markdown": payload,
        "source": {"html_path": str(html_path)},
        "html": extracted.html,
    }


def main() -> None:  # pragma: no cover
    uvicorn.run("asntools.spec_server:app", host="0.0.0.0", port=DEFAULT_SPEC_API_PORT, reload=False)


if __name__ == "__main__":  # pragma: no cover
    main()
