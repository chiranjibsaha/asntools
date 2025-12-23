"""Primary CLI entrypoint for asntools."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import click

from . import DEFAULT_ASN1_PATH, DEFAULT_OUTPUT_DIR
from .compile_rrc import compile_nr_rrc
from .field_descriptions import FieldDescriptionResult, FieldDescriptionStore, load_field_descriptions
from .logging_utils import setup_logging
from .introspect import (
    describe_ie,
    find_leaf_paths,
    format_leaf_paths_as_nested,
    format_leaf_paths_as_tree,
    has_version_suffix,
    IENameError,
    limit_leaf_path_depth,
    list_ie_names,
    load_rrc_definitions,
    normalize_ie_name,
    search_ie_names,
)
from .rebuild import ASNSourceError, discover_input_files, rebuild_rrc_modules
from .server import serve_forever
from .search_asn import search_asn_text


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.option(
    "--compile",
    "compile_flag",
    is_flag=True,
    help="Merge the provided ASN.1 files, wipe existing pycrate outputs, and recompile NR-RRC.",
)
@click.option(
    "--asnfiles",
    "asnfiles",
    type=click.Path(path_type=None),
    multiple=True,
    help="Explicit list of ASN.1 files to merge (overrides positional arguments).",
)
@click.option(
    "--asnfielddescriptions",
    "description_files",
    type=click.Path(path_type=None),
    multiple=True,
    help="Optional field description JSON files to merge alongside compilation.",
)
@click.option(
    "--input-dir",
    "input_dirs",
    type=click.Path(path_type=None),
    multiple=True,
    help="Recursively discover ASN.1 and description files under this directory (repeatable).",
)
@click.option(
    "--scan-subdir",
    "scan_subdirs",
    type=str,
    multiple=True,
    help="Restrict discovery to these subfolders (relative to each --input-dir).",
)
@click.option(
    "--serve",
    "serve_flag",
    is_flag=True,
    help="Run the FastAPI server to expose the NR-RRC tooling over HTTP.",
)
@click.option(
    "--host",
    default="127.0.0.1",
    show_default=True,
    help="Host/IP to bind when running in server mode.",
)
@click.option(
    "--port",
    default=8000,
    show_default=True,
    type=int,
    help="Port to bind when running in server mode.",
)
@click.option(
    "--describe-field",
    "field_name",
    type=str,
    help="Print the description for the requested ASN.1 field (requires merged description JSON).",
)
@click.option(
    "--describe-ie",
    "describe_ie_name",
    type=str,
    help="Print every field narrative captured for the requested IE (requires merged description JSON).",
)
@click.option(
    "--show",
    "show_ie_name",
    type=str,
    help="Print the JSON structure for the requested IE (NR-RRC or LPP).",
)
@click.option(
    "--tree",
    "tree_ie_name",
    type=str,
    help="Return the NR-RRC tree for the specified IE as machine-readable JSON.",
)
@click.option(
    "--tree-pretty",
    "tree_pretty",
    is_flag=True,
    help="Write the ASCII tree to artifacts/<ie>_tree.md (or use --tree-markdown-output).",
)
@click.option(
    "--tree-markdown-output",
    type=click.Path(path_type=Path),
    help="Explicit Markdown path for the ASCII tree output when using --tree.",
)
@click.option(
    "--tree-depth",
    "tree_depth",
    type=int,
    help="Limit output to the last N ancestors above the leaf (e.g., 1 shows only immediate parents).",
)
@click.option(
    "--tree-root",
    "tree_roots",
    multiple=True,
    help="Limit tree traversal to the provided root IE names (repeatable).",
)
@click.option(
    "--tree-all-roots/--tree-default-roots",
    "tree_all_roots",
    default=False,
    show_default=True,
    help="Traverse every IE as a potential tree root when resolving --tree.",
)
@click.option(
    "--tree-asn1-path",
    type=click.Path(path_type=Path),
    help="Path to NR-RRC-Definitions.asn when compiling for --tree.",
)
@click.option(
    "--tree-compile/--tree-no-compile",
    "tree_should_compile",
    default=True,
    show_default=True,
    help="Compile ASN.1 automatically when building a tree and the pycrate module is missing.",
)
@click.option(
    "--tree-allow-version-aggregation/--tree-require-version-selection",
    "tree_allow_version_aggregation",
    default=False,
    show_default=True,
    help="Aggregate every matching IE variant automatically when building a tree.",
)
@click.option(
    "--grep",
    "grep_pattern",
    type=str,
    help="Search the merged NR-RRC ASN.1 text for a pattern and emit structured JSON.",
)
@click.option(
    "--grep-asn1-path",
    type=click.Path(path_type=Path),
    help="ASN.1 file to search with --grep (defaults to asn1/NR-RRC-Definitions.asn).",
)
@click.option(
    "--grep-regex/--grep-literal",
    "grep_regex",
    default=False,
    show_default=True,
    help="Treat --grep pattern as a regex (case-insensitive).",
)
@click.argument("asn1_files", type=click.Path(path_type=None), nargs=-1)
def main(
    compile_flag: bool,
    asnfiles: tuple[str, ...],
    description_files: tuple[str, ...],
    input_dirs: tuple[str, ...],
    scan_subdirs: tuple[str, ...],
    serve_flag: bool,
    host: str,
    port: int,
    field_name: str | None,
    describe_ie_name: str | None,
    show_ie_name: str | None,
    tree_ie_name: str | None,
    tree_pretty: bool,
    tree_markdown_output: Path | None,
    tree_depth: int | None,
    tree_roots: tuple[str, ...],
    tree_all_roots: bool,
    tree_asn1_path: Path | None,
    tree_should_compile: bool,
    tree_allow_version_aggregation: bool,
    grep_pattern: str | None,
    grep_asn1_path: Path | None,
    grep_regex: bool,
    asn1_files: tuple[str, ...],
) -> None:
    """Top-level CLI supporting compile and server workflows."""

    logger = setup_logging()

    try:
        actions = sum(
            bool(flag)
            for flag in (
                compile_flag,
                serve_flag,
                field_name,
                describe_ie_name,
                tree_ie_name,
                show_ie_name,
                grep_pattern,
            )
        )
        if actions > 1:
            raise click.UsageError(
                "Choose only one action among --compile, --serve, --describe-field, --show, --tree, or --grep."
            )

        if field_name:
            _handle_describe_field(field_name)
            return

        if describe_ie_name:
            _handle_describe_ie(describe_ie_name)
            return

        if show_ie_name:
            _ensure_rrc_module(True, None)
            definitions = load_rrc_definitions()
            try:
                data = describe_ie(show_ie_name, definitions=definitions)
            except IENameError as exc:
                raise click.ClickException(str(exc)) from exc
            click.echo(json.dumps(data, indent=2))
            return

        if tree_ie_name:
            if tree_depth is not None and tree_depth < 0:
                raise click.ClickException("--tree-depth must be zero or a positive integer")
            _ensure_rrc_module(tree_should_compile, tree_asn1_path)
            definitions = load_rrc_definitions()
            if tree_all_roots:
                root_list = list_ie_names(definitions=definitions)
            elif tree_roots:
                root_list = list(tree_roots)
            else:
                root_list = None
            payload = _build_tree_payload(
                tree_ie_name,
                definitions=definitions,
                root_ie_names=root_list,
                allow_version_aggregation=tree_allow_version_aggregation,
                max_depth=tree_depth,
            )
            if (
                payload.get("status") == "ok"
                and (tree_pretty or tree_markdown_output is not None)
                and payload.get("paths")
            ):
                target = tree_markdown_output or _default_tree_markdown_path(tree_ie_name)
                _write_tree_markdown(target, payload["paths"])
            click.echo(json.dumps(payload, indent=2))
            return

        if grep_pattern:
            payload = _handle_grep(grep_pattern, grep_asn1_path, grep_regex)
            click.echo(json.dumps(payload, indent=2, ensure_ascii=False))
            return

        if serve_flag:
            serve_forever(host, port)
            return

        if compile_flag:
            discovered_asn: list[Path] = []
            discovered_desc: list[Path] = []
            for root in input_dirs:
                asn_found, desc_found = discover_input_files(Path(root), subdirs=scan_subdirs or None)
                discovered_asn.extend(asn_found)
                discovered_desc.extend(desc_found)

            explicit_sources = list(asnfiles) or list(asn1_files)
            all_asn_sources = _deduplicate_paths(
                [*discovered_asn, *map(Path, explicit_sources)]
            )
            if not all_asn_sources:
                raise click.UsageError("Provide at least one ASN.1 file (via positional args, --asnfiles, or --input-dir).")

            desc_sources = _deduplicate_paths(
                [*map(Path, description_files), *discovered_desc]
            )
            try:
                artifacts = rebuild_rrc_modules(
                    all_asn_sources,
                    description_files=desc_sources or None,
                )
            except ASNSourceError as exc:
                raise click.ClickException(str(exc)) from exc
            click.echo(f"Merged ASN.1: {artifacts.merged_asn1}")
            click.echo(f"Generated pycrate module: {artifacts.module}")
            if artifacts.merged_field_descriptions is not None:
                click.echo(f"Merged field descriptions: {artifacts.merged_field_descriptions}")
            return

        raise click.UsageError(
            "Specify --compile path1 path2 ... to rebuild the NR-RRC modules, --serve to start the HTTP API, "
            "--describe-field <name> to search across IE field descriptions, --describe-ie <name> to dump a field-description table, "
            "--show <ie_name> to dump an IE definition, "
            "--tree <ie_name> [--tree-depth N] to emit a machine-readable tree, "
            "or --grep <pattern> to search the merged ASN.1 text."
        )
    except Exception as exc:  # pragma: no cover - passthrough to Click after logging
        logger.exception("Fatal error during asntools CLI execution")
        raise


if __name__ == "__main__":  # pragma: no cover
    main()


def _handle_describe_field(field_name: str) -> None:
    store = _load_field_store()
    matches = store.lookup_field(field_name)
    if not matches:
        _raise_field_not_found(store, field_name)
    payload = {
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
    }
    click.echo(json.dumps(payload, indent=2, ensure_ascii=False))


def _handle_describe_ie(ie_name: str) -> None:
    store = _load_field_store()
    match = store.lookup_ie(ie_name)
    if not match:
        _raise_ie_not_found(store, ie_name)
    payload = {
        "query": ie_name,
        "ie_name": match.name,
        "fields": match.fields,
        "variants": store.related_ie_versions(ie_name, match),
    }
    click.echo(json.dumps(payload, indent=2, ensure_ascii=False))


def _raise_field_not_found(store: FieldDescriptionStore, field_name: str) -> None:
    variants = store.related_field_versions(field_name)
    suggestions = variants or store.suggest_field_names(field_name)
    suggestion_text = f" Suggestions: {', '.join(suggestions[:5])}" if suggestions else ""
    raise click.ClickException(f"No description found for field '{field_name}'.{suggestion_text}")


def _raise_ie_not_found(store: FieldDescriptionStore, ie_name: str) -> None:
    variants = store.related_ie_versions(ie_name)
    suggestions = variants or store.suggest_ie_names(ie_name)
    suggestion_text = f" Suggestions: {', '.join(suggestions[:5])}" if suggestions else ""
    raise click.ClickException(f"No field description table found for IE '{ie_name}'.{suggestion_text}")


def _load_field_store() -> FieldDescriptionStore:
    try:
        return load_field_descriptions()
    except (FileNotFoundError, ValueError) as exc:
        raise click.ClickException(str(exc)) from exc


def _deduplicate_paths(paths: list[Path]) -> list[Path]:
    unique: list[Path] = []
    seen: set[Path] = set()
    for path in paths:
        resolved = path.expanduser().resolve()
        if resolved in seen:
            continue
        seen.add(resolved)
        unique.append(path)
    return unique


def _ensure_rrc_module(should_compile: bool, asn1_path: Path | None) -> None:
    module_file = Path(DEFAULT_OUTPUT_DIR) / "NR_RRC_Definitions.py"
    if module_file.exists():
        return
    if not should_compile:
        raise click.ClickException(
            "pycrate module missing. Run asntools --compile first or rerun with --tree-compile."
        )
    source = Path(asn1_path or DEFAULT_ASN1_PATH)
    compile_nr_rrc(source, Path(DEFAULT_OUTPUT_DIR))


def _default_tree_markdown_path(ie_name: str) -> Path:
    safe = ie_name.replace('/', '_').replace(' ', '_')
    return Path("artifacts") / f"{safe}_tree.md"


def _write_tree_markdown(path: Path, paths_by_root: dict[str, list[list[str]]]) -> None:
    tree_text = format_leaf_paths_as_tree(paths_by_root)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"```text\n{tree_text}\n```\n", encoding="utf-8")
    click.echo(f"Wrote {path}")


def _handle_grep(pattern: str, asn1_path: Path | None, use_regex: bool) -> dict:
    """Search the ASN.1 source text for the provided pattern and emit structured JSON."""

    if not pattern:
        raise click.ClickException("--grep requires a non-empty pattern.")
    try:
        return search_asn_text(pattern, asn1_path, use_regex=use_regex)
    except FileNotFoundError as exc:
        raise click.ClickException(
            f"{exc}. Run --compile first or pass --grep-asn1-path."
        ) from exc
    except ValueError as exc:
        raise click.ClickException(str(exc)) from exc


def _summarize_parent_counts(paths_by_root: dict[str, list[list[str]]]) -> dict[str, list[dict[str, Any]]]:
    summary: dict[str, list[dict[str, Any]]] = {}
    for root, paths in paths_by_root.items():
        counts: dict[str, int] = {}
        for path in paths:
            if not path:
                continue
            parent = path[-2] if len(path) >= 2 else path[-1]
            counts[parent] = counts.get(parent, 0) + 1
        summary[root] = [
            {"parent": name, "count": count}
            for name, count in sorted(counts.items(), key=lambda item: (-item[1], item[0]))
        ]
    return summary


def _build_tree_payload(
    leaf_ie_name: str,
    *,
    definitions: Any,
    root_ie_names: list[str] | None,
    allow_version_aggregation: bool,
    max_depth: int | None,
) -> dict:
    matches = search_ie_names(leaf_ie_name, definitions=definitions)
    normalized_query = normalize_ie_name(leaf_ie_name)
    variant_names = [
        selection.display_name for selection in matches if normalize_ie_name(selection.display_name) == normalized_query
    ]
    if (
        len(variant_names) > 1
        and not allow_version_aggregation
        and not has_version_suffix(leaf_ie_name)
    ):
        return {
            "status": "ambiguous_versions",
            "query": leaf_ie_name,
            "variants": variant_names,
        }

    paths_by_root = find_leaf_paths(
        leaf_ie_name,
        definitions=definitions,
        root_ie_names=root_ie_names,
    )
    paths_by_root = limit_leaf_path_depth(paths_by_root, max_depth)
    if not paths_by_root:
        suggestions = [selection.display_name for selection in matches][:20]
        return {
            "status": "not_found",
            "query": leaf_ie_name,
            "suggestions": suggestions,
        }

    payload = {
        "status": "ok",
        "query": leaf_ie_name,
        "paths": paths_by_root,
        "tree_json": format_leaf_paths_as_nested(paths_by_root),
        "parent_counts": _summarize_parent_counts(paths_by_root),
    }
    return payload
