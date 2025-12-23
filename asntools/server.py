"""FastAPI server exposing NR-RRC ASN.1 tooling."""
from __future__ import annotations

from pathlib import Path
from threading import Lock
from typing import List, Optional

import uvicorn
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field

from . import DEFAULT_ASN1_PATH, DEFAULT_OUTPUT_DIR, __version__
from .compile_rrc import compile_nr_rrc
from .field_descriptions import FieldDescriptionStore, load_field_descriptions
from .introspect import (
    IENameError,
    describe_ie,
    find_leaf_paths,
    format_leaf_paths_as_mermaid,
    format_leaf_paths_as_nested,
    format_leaf_paths_as_tree,
    has_version_suffix,
    list_ie_names,
    load_rrc_definitions,
    normalize_ie_name,
    search_ie_names,
)
from .rebuild import ASNSourceError, discover_input_files, rebuild_rrc_modules
from .search_asn import search_asn_text

app = FastAPI(title="asntools", version=__version__)
_COMPILE_LOCK = Lock()
_TREE_FILE_LOCK = Lock()

HELP_ENTRIES = [
    {
        "name": "asntools_compile",
        "method": "POST",
        "path": "/compile",
        "description": "Merge ASN.1 + field-description inputs and rebuild pycrate artifacts.",
        "request": {
            "body": {
                "asn1_files": "List[str] (optional)",
                "description_files": "List[str] (optional)",
                "discover_dirs": "List[str] (optional)",
                "subdirs": "List[str] (optional)",
            }
        },
        "response": {
            "status": "ok",
            "merged_asn1": "str path",
            "module": "str path",
            "field_descriptions": "str path | null",
        },
    },
    {
        "name": "asntools_show",
        "method": "GET",
        "path": "/ies/{ie_name}",
        "description": "Return the JSON structure for an IE (CLI --show).",
        "request": {
            "path": {"ie_name": "str"},
            "query": {"compile": "bool (default true)", "asn1_path": "Optional[str]"},
        },
        "response": {"status": "ok", "ie_name": "str", "data": "dict describing IE"},
    },
    {
        "name": "asntools_search",
        "method": "GET",
        "path": "/ies/search",
        "description": "Find IE names containing a substring or pattern.",
        "request": {
            "query": {
                "pattern": "str",
                "compile": "bool (default true)",
                "asn1_path": "Optional[str]",
            }
        },
        "response": {"status": "ok", "pattern": "str", "matches": "List[str]", "count": "int"},
    },
    {
        "name": "asntools_tree",
        "method": "POST",
        "path": "/trees",
        "description": "Build root→leaf paths, ASCII trees, Mermaid, and Markdown (CLI --tree).",
        "request": {
            "body": {
                "leaf_ie_name": "str",
                "roots": "Optional[List[str]]",
                "all_roots": "bool",
                "tree_depth": "Optional[int]",
                "include_tree": "bool",
                "include_mermaid": "bool",
                "include_tree_json": "bool",
                "include_markdown": "bool",
                "wrap_markdown": "bool",
                "pretty_file": "bool",
                "markdown_path": "Optional[str]",
                "allow_version_aggregation": "bool",
                "compile": "bool",
                "asn1_path": "Optional[str]",
            }
        },
        "response": {
            "status": "ok | ambiguous_versions | not_found",
            "query": "str",
            "paths": "dict",
            "tree": "str?",
            "mermaid": "str?",
            "tree_json": "dict?",
            "markdown": "str?",
            "pretty_file_path": "str?",
            "suggestions": "List[str]? (not_found)",
            "variants": "List[str]? (ambiguous_versions)",
        },
    },
    {
        "name": "asntools_describe_field",
        "method": "GET",
        "path": "/fields/{field_name}",
        "description": "Look up narrative field descriptions across IEs (CLI --describe-field).",
        "request": {"path": {"field_name": "str"}},
        "response": {
            "status": "ok",
            "query": "str",
            "matches": "List[dict(name, ie_name, kind, description)]",
            "variants": "List[str]",
            "source": "str path",
        },
    },
    {
        "name": "asntools_describe_ie",
        "method": "GET",
        "path": "/field-descriptions/ies/{ie_name}",
        "description": "Dump the field-description table for one IE (CLI --describe-ie).",
        "request": {"path": {"ie_name": "str"}},
        "response": {
            "status": "ok",
            "query": "str",
            "ie_name": "str",
            "fields": "dict",
            "variants": "List[str]",
            "source": "str path",
        },
    },
    {
        "name": "asntools_grep",
        "method": "GET",
        "path": "/grep",
        "description": "Search the merged ASN.1 text for a pattern (CLI --grep).",
        "request": {
            "query": {
                "pattern": "str (required)",
                "asn1_path": "Optional[str]",
                "regex": "bool (default false)",
            }
        },
        "response": {
            "status": "ok | not_found",
            "query": "str",
            "asn1_path": "str path",
            "match_count": "int",
            "matches": "List[dict(index,line,char_offset,message_length,message)]",
            "chunks": "List[str] (one per match)",
        },
    },
]

class CompileRequest(BaseModel):
    asn1_files: List[str] = Field(
        default_factory=list,
        description="Absolute or relative paths to the ASN.1 files to merge and compile.",
    )
    description_files: Optional[List[str]] = Field(
        default=None,
        description="Optional JSON files containing field descriptions to merge.",
    )
    discover_dirs: Optional[List[str]] = Field(
        default=None,
        description="Directories to scan recursively for ASN.1/description files.",
    )
    subdirs: Optional[List[str]] = Field(
        default=None,
        description="Optional subfolder filters (relative to each discover directory).",
    )


class TreeRequest(BaseModel):
    leaf_ie_name: str
    roots: Optional[List[str]] = None
    all_roots: bool = False
    allow_version_aggregation: bool = False
    include_tree: bool = True
    include_mermaid: bool = False
    include_tree_json: bool = True
    include_markdown: bool = False
    wrap_markdown: bool = True
    pretty_file: bool = False
    markdown_path: Optional[str] = None
    compile: bool = True
    asn1_path: Optional[str] = None


def _ensure_definitions_ready(auto_compile: bool, asn1_path: Optional[str]) -> None:
    module_file = Path(DEFAULT_OUTPUT_DIR) / "NR_RRC_Definitions.py"
    if module_file.exists():
        return
    if not auto_compile:
        raise HTTPException(
            status_code=503,
            detail="pycrate module missing. Compile on the server or enable the compile flag.",
        )
    source = Path(asn1_path or DEFAULT_ASN1_PATH)
    try:
        with _COMPILE_LOCK:
            compile_nr_rrc(source, Path(DEFAULT_OUTPUT_DIR))
    except FileNotFoundError as exc:  # pragma: no cover - surfaced to client
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/help")
def help_endpoint() -> dict:
    return {"status": "ok", "tools": HELP_ENTRIES}


@app.get("/grep", operation_id="asntools_grep")
def grep_endpoint(
    pattern: str = Query(..., min_length=1),
    asn1_path: Optional[str] = None,
    regex: bool = Query(False, description="Treat pattern as regex (case-insensitive)."),
) -> dict:
    try:
        return search_asn_text(pattern, asn1_path, use_regex=regex)
    except FileNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@app.post("/compile")
def compile_endpoint(request: CompileRequest) -> dict:
    asn_inputs: list[Path] = []
    desc_inputs: list[Path] = []
    if request.discover_dirs:
        for root in request.discover_dirs:
            asn_found, desc_found = discover_input_files(Path(root), subdirs=request.subdirs or None)
            asn_inputs.extend(asn_found)
            desc_inputs.extend(desc_found)
    asn_inputs.extend(Path(entry) for entry in request.asn1_files)
    if not asn_inputs:
        raise HTTPException(status_code=400, detail="Provide at least one ASN.1 file or discovery directory.")
    if request.description_files:
        desc_inputs.extend(Path(entry) for entry in request.description_files)

    try:
        with _COMPILE_LOCK:
            artifacts = rebuild_rrc_modules(
                tuple(asn_inputs),
                description_files=tuple(desc_inputs) if desc_inputs else None,
            )
    except ASNSourceError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    return {
        "status": "ok",
        "merged_asn1": str(artifacts.merged_asn1),
        "module": str(artifacts.module),
        "field_descriptions": str(artifacts.merged_field_descriptions) if artifacts.merged_field_descriptions else None,
    }


@app.get("/ies/{ie_name}")
def describe_endpoint(
    ie_name: str,
    compile: bool = Query(True, description="Compile default ASN.1 if the module is missing."),
    asn1_path: Optional[str] = Query(None, description="Optional ASN.1 path to compile when needed."),
) -> dict:
    _ensure_definitions_ready(compile, asn1_path)
    definitions = load_rrc_definitions()
    try:
        data = describe_ie(ie_name, definitions=definitions)
    except IENameError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    return {"status": "ok", "ie_name": ie_name, "data": data}


@app.get("/ies/search")
def search_endpoint(
    pattern: str = Query(..., description="Substring or pattern to match IE names."),
    compile: bool = Query(True, description="Compile default ASN.1 if the module is missing."),
    asn1_path: Optional[str] = Query(None, description="Optional ASN.1 path to compile when needed."),
) -> dict:
    _ensure_definitions_ready(compile, asn1_path)
    definitions = load_rrc_definitions()
    matches = search_ie_names(pattern, definitions=definitions)
    return {
        "status": "ok",
        "pattern": pattern,
        "matches": [selection.display_name for selection in matches],
        "count": len(matches),
    }


@app.post("/trees")
def tree_endpoint(request: TreeRequest) -> dict:
    _ensure_definitions_ready(request.compile, request.asn1_path)
    definitions = load_rrc_definitions()

    if request.all_roots:
        root_list = list_ie_names(definitions=definitions)
    elif request.roots:
        root_list = request.roots
    else:
        root_list = None

    matches = search_ie_names(request.leaf_ie_name, definitions=definitions)
    normalized_query = normalize_ie_name(request.leaf_ie_name)
    variant_names = [
        selection.display_name for selection in matches if normalize_ie_name(selection.display_name) == normalized_query
    ]
    if (
        len(variant_names) > 1
        and not request.allow_version_aggregation
        and not has_version_suffix(request.leaf_ie_name)
    ):
        return {
            "status": "ambiguous_versions",
            "query": request.leaf_ie_name,
            "variants": variant_names,
        }

    paths_by_root = find_leaf_paths(
        request.leaf_ie_name,
        definitions=definitions,
        root_ie_names=root_list,
    )

    if not paths_by_root:
        suggestions = [selection.display_name for selection in matches][:20]
        return {
            "status": "not_found",
            "query": request.leaf_ie_name,
            "suggestions": suggestions,
        }

    payload = {
        "status": "ok",
        "query": request.leaf_ie_name,
        "paths": paths_by_root,
    }
    if request.include_tree:
        payload["tree"] = format_leaf_paths_as_tree(paths_by_root)
    if request.include_mermaid:
        payload["mermaid"] = format_leaf_paths_as_mermaid(paths_by_root)
    if request.include_tree_json:
        payload["tree_json"] = format_leaf_paths_as_nested(paths_by_root)
    if request.include_markdown:
        markdown = format_leaf_paths_as_tree(paths_by_root)
        payload["markdown"] = markdown
        if request.pretty_file:
            target = Path(request.markdown_path or _default_tree_markdown_path(request.leaf_ie_name))
            text = markdown if not request.wrap_markdown else f"```text\n{markdown}\n```\n"
            with _TREE_FILE_LOCK:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(text, encoding="utf-8")
            payload["pretty_file_path"] = str(target)
    return payload


@app.get("/fields/{field_name}")
@app.get("/field-descriptions/fields/{field_name}")
def field_description_endpoint(field_name: str) -> dict:
    store = _load_field_store()
    matches = store.lookup_field(field_name)
    if not matches:
        suggestions = _field_suggestions(store, field_name)
        detail: dict[str, object] = {
            "message": f"No description found for '{field_name}'.",
        }
        if suggestions:
            detail["suggestions"] = suggestions
        raise HTTPException(status_code=404, detail=detail)
    return {
        "status": "ok",
        "query": field_name,
        "matches": [
            {
                "name": result.name,
                "ie_name": result.ie_name,
                "kind": result.kind,
                "description": result.description,
            }
            for result in matches
        ],
        "variants": store.related_field_versions(field_name, matches),
        "source": str(store.path),
    }


@app.get("/field-descriptions/ies/{ie_name}")
def ie_field_description_endpoint(ie_name: str) -> dict:
    store = _load_field_store()
    match = store.lookup_ie(ie_name)
    if not match:
        suggestions = _ie_suggestions(store, ie_name)
        detail: dict[str, object] = {
            "message": f"No field description table found for IE '{ie_name}'.",
        }
        if suggestions:
            detail["suggestions"] = suggestions
        raise HTTPException(status_code=404, detail=detail)
    return {
        "status": "ok",
        "query": ie_name,
        "ie_name": match.name,
        "fields": match.fields,
        "variants": store.related_ie_versions(ie_name, match),
        "source": str(store.path),
    }


def serve_forever(host: str = "127.0.0.1", port: int = 8000) -> None:
    """Run the FastAPI application via uvicorn."""

    uvicorn.run(app, host=host, port=port)


def _load_field_store() -> FieldDescriptionStore:
    try:
        return load_field_descriptions()
    except FileNotFoundError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc


def _field_suggestions(store: FieldDescriptionStore, field_name: str) -> list[str]:
    variants = store.related_field_versions(field_name)
    if variants:
        return variants[:5]
    return store.suggest_field_names(field_name, limit=5)


def _ie_suggestions(store: FieldDescriptionStore, ie_name: str) -> list[str]:
    variants = store.related_ie_versions(ie_name)
    if variants:
        return variants[:5]
    return store.suggest_ie_names(ie_name, limit=5)


__all__ = ["app", "serve_forever"]
