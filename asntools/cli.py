"""Command-line interface for NR-RRC IE introspection."""
from __future__ import annotations

import json
from pathlib import Path

import click

from . import DEFAULT_ASN1_PATH, DEFAULT_OUTPUT_DIR
from .compile_rrc import compile_nr_rrc
from .introspect import IENameError, describe_ie, load_rrc_definitions, search_ie_names


@click.command()
@click.argument("ie_name")
@click.option("--asn1-path", type=click.Path(path_type=Path), help="Path to NR-RRC-Definitions.asn (compile if needed)")
@click.option("--output", type=click.Path(path_type=Path), help="Write JSON output to file instead of stdout")
@click.option("--compact/--pretty", default=False, show_default=True, help="Toggle compact JSON vs readable")
@click.option("--compile/--no-compile", default=True, show_default=True, help="Compile ASN.1 if module missing")
@click.option("--search", is_flag=True, help="Treat IE name as a pattern and list matches")
def main(ie_name: str, asn1_path: Path | None, output: Path | None, compact: bool, compile: bool, search: bool) -> None:
    """Resolve an IE by name and print its structure as JSON."""

    output_dir = Path(DEFAULT_OUTPUT_DIR)
    module_file = output_dir / "NR_RRC_Definitions.py"
    if not module_file.exists():
        if not compile:
            raise click.ClickException(
                "pycrate module missing. Provide --asn1-path or run asntools-compile-rrc before invoking the CLI."
            )
        if asn1_path is None:
            asn1_path = Path(DEFAULT_ASN1_PATH)
        compile_nr_rrc(asn1_path, output_dir)

    definitions = load_rrc_definitions()

    if search:
        matches = search_ie_names(ie_name, definitions=definitions)
        if not matches:
            raise click.ClickException(f"No IEs found matching {ie_name}.")
        for selection in matches:
            click.echo(selection.display_name)
        return
    try:
        data = describe_ie(ie_name, definitions=definitions)
    except IENameError as err:
        raise click.ClickException(str(err)) from err

    json_kwargs = {"indent": None if compact else 2, "ensure_ascii": False}
    if compact:
        json_kwargs["separators"] = (",", ":")
    payload = json.dumps(data, **json_kwargs)

    if output:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(payload, encoding="utf-8")
        click.echo(f"Wrote {output}")
    else:
        click.echo(payload)


if __name__ == "__main__":  # pragma: no cover
    main()
