"""CLI for generating leaf-to-root NR-RRC IE trees."""
from __future__ import annotations

import json
from pathlib import Path

import click

from . import DEFAULT_ASN1_PATH, DEFAULT_OUTPUT_DIR
from .compile_rrc import compile_nr_rrc
from .introspect import (
    find_leaf_paths,
    format_leaf_paths_as_mermaid,
    format_leaf_paths_as_tree,
    has_version_suffix,
    list_ie_names,
    load_rrc_definitions,
    normalize_ie_name,
    search_ie_names,
)


@click.command()
@click.argument("leaf_ie_name")
@click.option(
    "--root",
    "roots",
    multiple=True,
    help="Limit traversal to the provided root IE names (repeatable).",
)
@click.option(
    "--all-roots/--no-all-roots",
    default=False,
    show_default=True,
    help="Traverse every IE as a potential root (slower).",
)
@click.option(
    "--asn1-path",
    type=click.Path(path_type=Path),
    help="Path to NR-RRC-Definitions.asn (compile if needed).",
)
@click.option(
    "--compile/--no-compile",
    default=True,
    show_default=True,
    help="Compile ASN.1 if the pycrate module is missing.",
)
@click.option(
    "--show-empty/--hide-empty",
    default=False,
    show_default=True,
    help="Print a notice instead of failing when no paths are found.",
)
@click.option(
    "--markdown-output",
    type=click.Path(path_type=Path),
    help="Write the tree to a Markdown file (wrapped in a code fence).",
)
@click.option(
    "--json/--no-json",
    "print_json",
    default=False,
    show_default=True,
    help="Print the structured root→leaf paths as JSON.",
)
@click.option(
    "--json-output",
    type=click.Path(path_type=Path),
    help="Write the structured root→leaf paths to a JSON file.",
)
@click.option(
    "--mermaid/--no-mermaid",
    "print_mermaid",
    default=False,
    show_default=True,
    help="Print a Mermaid graph (graph TD) to stdout.",
)
@click.option(
    "--mermaid-output",
    type=click.Path(path_type=Path),
    help="Write the Mermaid graph to a file.",
)
@click.option(
    "--allow-version-aggregation/--require-version-selection",
    default=False,
    show_default=True,
    help="When multiple versioned IEs match the query, aggregate them automatically instead of prompting.",
)
def main(
    leaf_ie_name: str,
    roots: tuple[str, ...],
    all_roots: bool,
    asn1_path: Path | None,
    compile: bool,
    show_empty: bool,
    markdown_output: Path | None,
    print_json: bool,
    json_output: Path | None,
    print_mermaid: bool,
    mermaid_output: Path | None,
    allow_version_aggregation: bool,
) -> None:
    """Print an ASCII tree from the leaf IE back to its RRC roots."""

    output_dir = Path(DEFAULT_OUTPUT_DIR)
    module_file = output_dir / "NR_RRC_Definitions.py"
    if not module_file.exists():
        if not compile:
            raise click.ClickException(
                "pycrate module missing. Provide --asn1-path or run asntools-compile-rrc first."
            )
        if asn1_path is None:
            asn1_path = Path(DEFAULT_ASN1_PATH)
        compile_nr_rrc(asn1_path, output_dir)

    definitions = load_rrc_definitions()

    if all_roots:
        root_list = list_ie_names(definitions=definitions)
    elif roots:
        root_list = list(roots)
    else:
        root_list = None

    matches = search_ie_names(leaf_ie_name, definitions=definitions)
    normalized_query = normalize_ie_name(leaf_ie_name)
    variant_names = [sel.display_name for sel in matches if normalize_ie_name(sel.display_name) == normalized_query]
    if (
        len(variant_names) > 1
        and not allow_version_aggregation
        and not has_version_suffix(leaf_ie_name)
    ):
        structured_result = {
            "status": "ambiguous_versions",
            "query": leaf_ie_name,
            "variants": variant_names,
            "instruction": "Specify one of the variant names explicitly or rerun with --allow-version-aggregation to include all versions.",
        }
        json_payload = None
        if print_json or json_output is not None:
            json_payload = json.dumps(structured_result, indent=2)
            if json_output is not None:
                json_output.parent.mkdir(parents=True, exist_ok=True)
                json_output.write_text(json_payload + "\n", encoding="utf-8")
                click.echo(f"Wrote {json_output}")
            if print_json:
                click.echo(json_payload)
        message = (
            "Multiple versioned IEs match this name: "
            + ", ".join(variant_names)
            + ". Specify a variant explicitly or rerun with --allow-version-aggregation."
        )
        click.echo(message)
        return

    paths_by_root = find_leaf_paths(
        leaf_ie_name,
        definitions=definitions,
        root_ie_names=root_list,
    )

    json_payload: str | None = None

    if not paths_by_root:
        suggestions = [sel.display_name for sel in matches]
        structured_result = {
            "status": "not_found",
            "query": leaf_ie_name,
            "suggestions": suggestions[:20],
        }
        if print_json or json_output is not None:
            json_payload = json.dumps(structured_result, indent=2)
            if json_output is not None:
                json_output.parent.mkdir(parents=True, exist_ok=True)
                json_output.write_text(json_payload + "\n", encoding="utf-8")
                click.echo(f"Wrote {json_output}")
            if print_json:
                click.echo(json_payload)
        message = (
            f"No occurrences of {leaf_ie_name} were found."
            + (
                f" Closest matches: {', '.join(suggestions[:10])}."
                if suggestions
                else ""
            )
        )
        click.echo(message)
        return

    tree = format_leaf_paths_as_tree(paths_by_root)
    mermaid_graph: str | None = None
    if print_mermaid or mermaid_output is not None:
        mermaid_graph = format_leaf_paths_as_mermaid(paths_by_root)

    if print_json or json_output is not None:
        structured_result = {
            "status": "ok",
            "query": leaf_ie_name,
            "paths": paths_by_root,
        }
        json_payload = json.dumps(structured_result, indent=2)
        if json_output is not None:
            json_output.parent.mkdir(parents=True, exist_ok=True)
            json_output.write_text(json_payload + "\n", encoding="utf-8")
            click.echo(f"Wrote {json_output}")
        if print_json:
            click.echo(json_payload)

    if markdown_output is not None:
        markdown_output.parent.mkdir(parents=True, exist_ok=True)
        markdown_output.write_text(f"```text\n{tree}\n```\n", encoding="utf-8")
        click.echo(f"Wrote {markdown_output}")

    if mermaid_output is not None and mermaid_graph is not None:
        mermaid_output.parent.mkdir(parents=True, exist_ok=True)
        mermaid_output.write_text(mermaid_graph + "\n", encoding="utf-8")
        click.echo(f"Wrote {mermaid_output}")
    if print_mermaid and mermaid_graph is not None:
        click.echo(mermaid_graph)

    click.echo(tree)


if __name__ == "__main__":  # pragma: no cover
    main()
