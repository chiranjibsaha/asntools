"""Shared utilities for rebuilding NR-RRC pycrate modules."""
from __future__ import annotations

import json
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence, Tuple

from . import DEFAULT_ASN1_PATH, DEFAULT_FIELD_DESCRIPTION_PATH, DEFAULT_OUTPUT_DIR
from .compile_rrc import compile_nr_rrc
from .field_descriptions import parse_field_description_payload


class ASNSourceError(Exception):
    """Raised when ASN.1 inputs are missing or invalid."""


@dataclass
class CompilationArtifacts:
    merged_asn1: Path
    module: Path
    merged_field_descriptions: Path | None = None


def discover_input_files(root: Path, subdirs: Sequence[str] | None = None) -> Tuple[list[Path], list[Path]]:
    """Recursively discover ASN.1 and field-description files under the given root."""

    root_path = Path(root).expanduser()
    if not root_path.exists():
        raise ASNSourceError(f"Input directory not found: {root_path}")
    if not root_path.is_dir():
        raise ASNSourceError(f"Input path is not a directory: {root_path}")

    target_dirs: list[Path] = []
    if subdirs:
        for rel in subdirs:
            candidate = (root_path / rel).expanduser()
            if not candidate.exists():
                raise ASNSourceError(f"Specified subdirectory not found: {candidate}")
            if not candidate.is_dir():
                raise ASNSourceError(f"Specified subdirectory is not a directory: {candidate}")
            target_dirs.append(candidate)
    else:
        target_dirs.append(root_path)

    asn_files: list[Path] = []
    description_files: list[Path] = []

    seen_paths: set[Path] = set()
    for directory in target_dirs:
        for path in directory.rglob("*"):
            if not path.is_file():
                continue
            resolved = path.resolve()
            if resolved in seen_paths:
                continue
            seen_paths.add(resolved)
            lower_name = path.name.lower()
            if lower_name.endswith(".asn"):
                asn_files.append(path)
            elif lower_name.endswith("_asn_field_description.json"):
                description_files.append(path)

    if not asn_files:
        raise ASNSourceError(
            f"No ASN.1 files found under {root_path if not subdirs else ', '.join(str(d) for d in target_dirs)}"
        )
    return asn_files, description_files


def _ensure_existing_file(path: Path) -> Path:
    expanded = path.expanduser()
    if not expanded.is_file():
        raise ASNSourceError(f"ASN.1 file not found: {expanded}")
    return expanded


def _read_description_file(path: Path) -> tuple[dict[str, dict[str, str]], dict[str, str]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    ie_fields, conditional_flags = parse_field_description_payload(data)
    if not ie_fields and not conditional_flags:
        raise ASNSourceError(f"Invalid field description format in {path}")
    return ie_fields, conditional_flags


def _write_merged_asn1(sources: Sequence[Path], destination: Path) -> Path:
    destination.parent.mkdir(parents=True, exist_ok=True)
    if len(sources) == 1:
        src = sources[0]
        if src.resolve() != destination.resolve():
            shutil.copyfile(src, destination)
        return destination

    texts = [source.read_text(encoding="utf-8") for source in sources]
    merged_text = "\n".join(texts)
    destination.write_text(merged_text, encoding="utf-8")
    return destination


def _merge_field_descriptions(sources: Sequence[Path], destination: Path) -> Path:
    destination.parent.mkdir(parents=True, exist_ok=True)
    merged_ies: dict[str, dict[str, str]] = {}
    merged_flags: dict[str, str] = {}
    source_list: list[str] = []
    for path in sources:
        desc_path = path.expanduser()
        if not desc_path.is_file():
            raise ASNSourceError(f"Field description file not found: {desc_path}")
        ie_fields, conditional_flags = _read_description_file(desc_path)
        for ie_name, fields in ie_fields.items():
            target = merged_ies.setdefault(ie_name, {})
            target.update(fields)
        merged_flags.update(conditional_flags)
        source_list.append(str(desc_path))
    if not merged_ies and not merged_flags:
        return destination
    payload = {
        "sources": source_list,
        "ies": merged_ies,
        "conditional_presence_flags": merged_flags,
    }
    destination.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return destination


def rebuild_rrc_modules(
    asn1_files: Sequence[Path],
    *,
    description_files: Sequence[Path] | None = None,
) -> CompilationArtifacts:
    """Merge the provided ASN.1 files and rebuild the pycrate outputs."""

    if not asn1_files:
        raise ASNSourceError("Provide at least one ASN.1 file.")

    resolved_sources = tuple(_ensure_existing_file(Path(entry)) for entry in asn1_files)

    output_dir = Path(DEFAULT_OUTPUT_DIR)
    if output_dir.exists():
        shutil.rmtree(output_dir)

    destination = Path(DEFAULT_ASN1_PATH)
    merged_path = _write_merged_asn1(resolved_sources, destination)
    module_path = compile_nr_rrc(merged_path, output_dir)

    merged_desc: Path | None = None
    if description_files:
        desc_sources = tuple(Path(entry).expanduser() for entry in description_files)
        merged_desc = _merge_field_descriptions(desc_sources, Path(DEFAULT_FIELD_DESCRIPTION_PATH))

    return CompilationArtifacts(
        merged_asn1=merged_path,
        module=module_path,
        merged_field_descriptions=merged_desc,
    )


__all__ = [
    "ASNSourceError",
    "CompilationArtifacts",
    "discover_input_files",
    "rebuild_rrc_modules",
]
