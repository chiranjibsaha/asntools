"""Compile NR-RRC ASN.1 using pycrate."""
from __future__ import annotations

from pathlib import Path

import click
from pycrate_asn1c.asnproc import (
    GLOBAL,
    JSONDepGraphGenerator,
    PycrateGenerator,
    compile_text,
    generate_modules,
)

from . import DEFAULT_ASN1_PATH, DEFAULT_OUTPUT_DIR
from .logging_utils import setup_logging


def compile_nr_rrc(asn1_path: Path, output_dir: Path, emit_json: bool = True) -> Path:
    """Compile the NR-RRC ASN.1 into Python modules via pycrate."""

    if not asn1_path.exists():
        raise FileNotFoundError(f"ASN.1 file not found: {asn1_path}")

    output_dir.mkdir(parents=True, exist_ok=True)
    text = asn1_path.read_text(encoding="utf-8")
    compile_text([text], filenames=[asn1_path.name])

    generated_py = output_dir / "NR_RRC_Definitions.py"
    generate_modules(PycrateGenerator, str(generated_py))
    if emit_json:
        generated_json = output_dir / "NR_RRC_Definitions.json"
        generate_modules(JSONDepGraphGenerator, str(generated_json))
    GLOBAL.clear()

    if not generated_py.exists():
        raise RuntimeError("pycrate did not produce NR_RRC_Definitions.py; check ASN.1 contents.")
    return generated_py


@click.command()
@click.option("--asn1-path", type=click.Path(path_type=Path), default=DEFAULT_ASN1_PATH, help="Path to NR-RRC-Definitions.asn")
@click.option("--output-dir", type=click.Path(path_type=Path), default=DEFAULT_OUTPUT_DIR, help="Directory for generated pycrate modules")
@click.option("--emit-json/--no-emit-json", default=True, show_default=True, help="Also emit JSON dependency graph")
def main(asn1_path: Path, output_dir: Path, emit_json: bool) -> None:
    """CLI entrypoint for compiling NR-RRC ASN.1 via pycrate."""

    logger = setup_logging()
    try:
        module_path = compile_nr_rrc(asn1_path, output_dir, emit_json=emit_json)
    except Exception as exc:  # pragma: no cover - log then re-raise
        logger.exception("Compilation failed (asn1_path=%s, output_dir=%s, emit_json=%s)", asn1_path, output_dir, emit_json)
        raise
    click.echo(f"Generated pycrate module: {module_path}")


if __name__ == "__main__":  # pragma: no cover
    main()
