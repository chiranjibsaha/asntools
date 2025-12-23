"""Utilities for loading and querying ASN.1 field and flag descriptions."""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from difflib import get_close_matches
from pathlib import Path
from typing import Dict, Iterable, Mapping, Optional

from . import DEFAULT_FIELD_DESCRIPTION_PATH


FieldKind = str  # Literal["field", "conditional_presence_flag"] when typing module allows it


@dataclass(frozen=True)
class FieldDescriptionResult:
    name: str
    description: str
    ie_name: Optional[str]
    kind: FieldKind


@dataclass
class IELookupResult:
    name: str
    fields: Dict[str, str]


@dataclass
class FieldDescriptionStore:
    path: Path
    ie_fields: Dict[str, Dict[str, str]]
    conditional_flags: Dict[str, str]
    _field_index: Dict[str, list[FieldDescriptionResult]] = field(init=False, repr=False)
    _all_field_names: list[str] = field(init=False, repr=False)
    _field_variants: Dict[str, set[str]] = field(init=False, repr=False)
    _ie_lookup_map: Dict[str, str] = field(init=False, repr=False)
    _all_ie_names: list[str] = field(init=False, repr=False)
    _ie_variants: Dict[str, set[str]] = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self._field_index = {}
        self._field_variants = {}
        self._all_field_names = []
        for ie_name, fields in self.ie_fields.items():
            for field_name, description in fields.items():
                self._register_field(field_name, description, ie_name, kind="field")
        for flag_name, description in self.conditional_flags.items():
            self._register_field(flag_name, description, ie_name=None, kind="conditional_presence_flag")
        self._all_ie_names = list(self.ie_fields.keys())
        self._ie_lookup_map = {}
        self._ie_variants = {}
        for ie_name in self._all_ie_names:
            normalized = _normalize_key(ie_name)
            self._ie_lookup_map.setdefault(normalized, ie_name)
            base_key = _normalize_key(_base_name(ie_name))
            self._ie_variants.setdefault(base_key, set()).add(ie_name)

    def _register_field(self, field_name: str, description: str, ie_name: Optional[str], *, kind: FieldKind) -> None:
        normalized = _normalize_key(field_name)
        entry = FieldDescriptionResult(name=field_name, description=description, ie_name=ie_name, kind=kind)
        self._field_index.setdefault(normalized, []).append(entry)
        self._all_field_names.append(field_name)
        base_key = _normalize_key(_base_name(field_name))
        self._field_variants.setdefault(base_key, set()).add(field_name)

    def lookup_field(self, name: str) -> list[FieldDescriptionResult]:
        matches: list[FieldDescriptionResult] = []
        seen: set[tuple[str, Optional[str], str]] = set()
        for candidate in _build_candidate_names(name):
            normalized = _normalize_key(candidate)
            for result in self._field_index.get(normalized, []):
                key = (result.kind, result.ie_name, result.name)
                if key not in seen:
                    matches.append(result)
                    seen.add(key)
        return matches

    def lookup_ie(self, name: str) -> Optional[IELookupResult]:
        for candidate in _build_candidate_names(name):
            if candidate in self.ie_fields:
                return IELookupResult(name=candidate, fields=self.ie_fields[candidate])
        for candidate in _build_candidate_names(name):
            normalized = _normalize_key(candidate)
            actual = self._ie_lookup_map.get(normalized)
            if actual:
                return IELookupResult(name=actual, fields=self.ie_fields[actual])
        return None

    def suggest_field_names(self, name: str, *, limit: int = 5) -> list[str]:
        return _suggest_names(name, self._all_field_names, limit=limit)

    def suggest_ie_names(self, name: str, *, limit: int = 5) -> list[str]:
        return _suggest_names(name, self._all_ie_names, limit=limit)

    def related_field_versions(self, name: str, matches: Iterable[FieldDescriptionResult] | None = None) -> list[str]:
        base_key = _normalize_key(_base_name(name))
        variants = sorted(self._field_variants.get(base_key, set()))
        if matches:
            matched = {result.name for result in matches}
            variants = [variant for variant in variants if variant not in matched]
        else:
            normalized_query = _normalize_key(name)
            variants = [variant for variant in variants if _normalize_key(variant) != normalized_query]
        return variants

    def related_ie_versions(self, name: str, match: Optional[IELookupResult] = None) -> list[str]:
        base_key = _normalize_key(_base_name(name))
        variants = sorted(self._ie_variants.get(base_key, set()))
        if match:
            variants = [variant for variant in variants if variant != match.name]
        else:
            normalized_query = _normalize_key(name)
            variants = [variant for variant in variants if _normalize_key(variant) != normalized_query]
        return variants


def load_field_descriptions(path: Path | None = None) -> FieldDescriptionStore:
    """Load the merged field/flag descriptions JSON file."""

    description_path = Path(path or DEFAULT_FIELD_DESCRIPTION_PATH)
    if not description_path.exists():
        raise FileNotFoundError(f"Field description file not found: {description_path}")
    data = json.loads(description_path.read_text(encoding="utf-8"))
    ie_fields, conditional_flags = parse_field_description_payload(data)
    if not ie_fields and not conditional_flags:
        raise ValueError(f"Invalid field description format in {description_path}")
    return FieldDescriptionStore(path=description_path, ie_fields=ie_fields, conditional_flags=conditional_flags)


def parse_field_description_payload(data: Mapping[str, object]) -> tuple[dict[str, dict[str, str]], dict[str, str]]:
    """Normalize various input schemas into a single IE/flag mapping."""

    ie_fields: dict[str, dict[str, str]] = {}
    conditional_flags: dict[str, str] = {}

    existing_ies = data.get("ies")
    if isinstance(existing_ies, Mapping):
        for ie_name, fields in existing_ies.items():
            if isinstance(fields, Mapping):
                ie_fields[str(ie_name)] = _stringify_mapping(fields)
    existing_flags = data.get("conditional_presence_flags")
    if isinstance(existing_flags, Mapping):
        conditional_flags = _stringify_mapping(existing_flags)
    if ie_fields or conditional_flags:
        return ie_fields, conditional_flags

    legacy = data.get("field_descriptions")
    if isinstance(legacy, Mapping):
        ie_fields["_global"] = _stringify_mapping(legacy)
        return ie_fields, conditional_flags

    for key, value in data.items():
        if key == "_metadata":
            continue
        if key == "conditional-presence-flags" and isinstance(value, Mapping):
            conditional_flags = _stringify_mapping(value)
            continue
        if isinstance(value, Mapping):
            ie_fields[str(key)] = _stringify_mapping(value)
    return ie_fields, conditional_flags


def _stringify_mapping(payload: Mapping[object, object]) -> dict[str, str]:
    return {str(key): str(value) for key, value in payload.items()}


def _suggest_names(name: str, population: Iterable[str], *, limit: int) -> list[str]:
    names = list(population)
    if not names:
        return []
    matches = get_close_matches(name, names, n=limit, cutoff=0.6)
    if len(matches) < limit:
        normalized = _normalize_key(name)
        for candidate in names:
            if candidate in matches:
                continue
            if normalized in _normalize_key(candidate):
                matches.append(candidate)
            if len(matches) >= limit:
                break
    return matches[:limit]


def _build_candidate_names(name: str) -> Iterable[str]:
    variants = [name]
    hyphenated = name.replace("_", "-")
    underscored = name.replace("-", "_")
    for variant in (hyphenated, underscored):
        if variant not in variants:
            variants.append(variant)
    return variants


def _normalize_key(name: str) -> str:
    return name.replace("-", "_").lower()


_VERSION_SUFFIX = re.compile(r"-(?:r|v)\d+[a-z0-9]*$", re.IGNORECASE)


def _base_name(name: str) -> str:
    base = name
    while True:
        match = _VERSION_SUFFIX.search(base)
        if not match:
            break
        base = base[:match.start()]
    return base or name


__all__ = [
    "FieldDescriptionResult",
    "FieldDescriptionStore",
    "IELookupResult",
    "load_field_descriptions",
    "parse_field_description_payload",
]
