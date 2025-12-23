"""Utilities for searching ASN.1 source text."""
from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from . import DEFAULT_ASN1_PATH


def search_asn_text(pattern: str, asn1_path: str | Path | None = None, *, use_regex: bool = False) -> dict[str, Any]:
    """Search the ASN.1 file for a pattern (substring or regex) and return structured JSON matches."""

    if not pattern:
        raise ValueError("Pattern must be non-empty.")

    target = Path(asn1_path or DEFAULT_ASN1_PATH)
    if not target.exists():
        raise FileNotFoundError(f"ASN.1 file not found at {target}")

    text = target.read_text(encoding="utf-8")
    if use_regex:
        try:
            compiled = re.compile(pattern, re.IGNORECASE)
        except re.error as exc:
            raise ValueError(f"invalid regex: {exc}") from exc
    else:
        pattern_lower = pattern.lower()

    matches: list[dict[str, Any]] = []
    char_offset = 0

    for line_number, line in enumerate(text.splitlines(), start=1):
        if use_regex:
            for match in compiled.finditer(line):
                idx = match.start()
                matches.append(
                    {
                        "index": len(matches) + 1,
                        "line": line_number,
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
                        "line": line_number,
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
            "query": pattern,
            "asn1_path": str(target),
            "match_count": 0,
            "matches": [],
            "chunks": [],
        }

    return {
        "status": "ok",
        "query": pattern,
        "asn1_path": str(target),
        "match_count": len(matches),
        "matches": matches,
        "chunks": [entry["message"] for entry in matches],
    }


__all__ = ["search_asn_text"]
