"""Utilities to introspect pycrate-generated NR-RRC definitions."""
from __future__ import annotations

import json
import re
from dataclasses import dataclass
from difflib import get_close_matches
from importlib import import_module
from typing import Any, Dict, Iterable, List, Optional, Sequence, Set

from pycrate_asn1rt.dictobj import ASN1Dict
from pycrate_asn1rt.setobj import ASN1Set

DEFAULT_MODULE = "pycrate_asn1dir.NR_RRC_Definitions"
# Include NR_InterNodeDefinitions to cover IEs like UERadioPagingInformation that live
# outside the main NR_RRC_Definitions module.
DEFAULT_CLASSES: Sequence[str] = (
    "NR_RRC_Definitions",
    "NR_InterNodeDefinitions",
    "LPP_PDU_Definitions",
    "LPP_Broadcast_Definitions",
)
DEFAULT_RRC_ROOT_IE_NAMES: Sequence[str] = ("RRCReconfiguration", "RRCResume")
DEFAULT_LPP_ROOT_IE_NAMES: Sequence[str] = ("LPP-Message",)
DEFAULT_ROOT_IE_NAMES: Sequence[str] = DEFAULT_RRC_ROOT_IE_NAMES + DEFAULT_LPP_ROOT_IE_NAMES
DEFAULT_ALIAS_ROOTS: Sequence[str] = DEFAULT_RRC_ROOT_IE_NAMES
ROOT_ALIAS_LABEL = "RRCResume/RRCReconfiguration"
_LEAF_VERSION_SUFFIX = re.compile(r"-v[0-9]+$")


class IENameError(KeyError):
    """Raised when an IE name cannot be found in the compiled definitions."""


@dataclass
class IESelection:
    attr_name: str
    display_name: str


class _CombinedDefinitions:
    """Aggregate multiple pycrate definition classes into a unified view."""

    def __init__(self, sources: Sequence[Any]):
        if not sources:
            raise ValueError("Combined definitions require at least one source class.")
        self._sources = tuple(sources)

    def __getattr__(self, item: str):
        for source in self._sources:
            if hasattr(source, item):
                return getattr(source, item)
        raise AttributeError(item)

    def __dir__(self) -> List[str]:
        entries: Set[str] = set(super().__dir__())
        for source in self._sources:
            entries.update(dir(source))
        return sorted(entries)


def load_rrc_definitions(
    module_path: str = DEFAULT_MODULE,
    class_name: Sequence[str] | str = DEFAULT_CLASSES,
):
    """Load the pycrate definitions, combining NR-RRC and LPP namespaces."""

    try:
        module = import_module(module_path)
    except ModuleNotFoundError as exc:  # pragma: no cover - environment error
        raise RuntimeError(
            "NR-RRC definitions module not found. Run asntools-compile-rrc to generate it."
        ) from exc
    class_names: Sequence[str]
    if isinstance(class_name, str):
        class_names = (class_name,)
    else:
        class_names = tuple(class_name)

    sources = []
    missing = []
    for entry in class_names:
        try:
            sources.append(getattr(module, entry))
        except AttributeError:
            missing.append(entry)
    if not sources:
        joined = ", ".join(class_names)
        raise RuntimeError(f"Module {module_path} is missing definitions: {joined}")
    if len(sources) == 1:
        return sources[0]
    return _CombinedDefinitions(tuple(sources))


def describe_ie(ie_name: str, definitions=None) -> Dict[str, Any]:
    """Return a JSON-serializable description for the requested IE."""

    definitions = definitions or load_rrc_definitions()
    selection = _resolve_ie_name(definitions, ie_name)
    obj = getattr(definitions, selection.attr_name)
    return _describe_obj(obj)


def search_ie_names(pattern: str, definitions=None) -> List[IESelection]:
    """Return IE selections whose names match the given pattern (case-insensitive)."""

    definitions = definitions or load_rrc_definitions()
    attrs = _list_ie_attrs(definitions)
    normalized = pattern.replace('-', '_').lower()
    matches: List[IESelection] = []
    for attr in attrs:
        canonical = attr.lower()
        hyphenated = attr.replace('_', '-').lower()
        if normalized in canonical or normalized in hyphenated:
            obj = getattr(definitions, attr)
            display = getattr(obj, "_name", attr.replace('_', '-'))
            matches.append(IESelection(attr_name=attr, display_name=display))
    return matches


def _resolve_ie_name(definitions, requested: str) -> IESelection:
    candidates = _build_ie_name_candidates(requested)
    attrs = _list_ie_attrs(definitions)
    attr_map = {name: name for name in attrs}
    for cand in candidates:
        if cand in attr_map:
            obj = getattr(definitions, cand)
            display = getattr(obj, "_name", cand.replace('_', '-'))
            return IESelection(attr_name=cand, display_name=display)
    # try case-insensitive lookup
    lowered = {name.lower(): name for name in attrs}
    key = requested.replace('-', '_').lower()
    if key in lowered:
        name = lowered[key]
        obj = getattr(definitions, name)
        display = getattr(obj, "_name", name.replace('_', '-'))
        return IESelection(attr_name=name, display_name=display)
    suggestions = get_close_matches(requested.replace('-', '_'), attrs, n=3, cutoff=0.6)
    hint = f" Available IEs similar to '{requested}': {', '.join(suggestions)}" if suggestions else ''
    raise IENameError(f"IE '{requested}' not found.{hint}")


def _build_ie_name_candidates(requested: str) -> List[str]:
    variants = [requested]
    normalized = requested.replace('-', '_')
    if normalized not in variants:
        variants.append(normalized)
    hyphenated = requested.replace('_', '-')
    if hyphenated not in variants:
        variants.append(hyphenated)
    return variants


def _list_ie_attrs(definitions) -> List[str]:
    return [name for name in dir(definitions) if not name.startswith('_')]


def _describe_obj(obj, stack: Optional[Set[int]] = None) -> Dict[str, Any]:
    if stack is None:
        stack = set()
    obj_id = id(obj)
    if obj_id in stack:
        return {
            "name": getattr(obj, "_name", None),
            "asn1_type": getattr(obj, "TYPE", None),
            "note": "recursive reference",
        }
    stack.add(obj_id)
    try:
        data: Dict[str, Any] = {
            "name": getattr(obj, "_name", None),
            "asn1_type": getattr(obj, "TYPE", None),
        }
        optional = getattr(obj, "_opt", None)
        if optional is not None:
            data["optional"] = bool(optional)
        default = getattr(obj, "_def", None)
        if default not in (None, {}):
            data["default"] = _serialize_value(default)
        constraints = _extract_constraints(obj)
        if constraints:
            data["constraints"] = constraints

        asn1_type = getattr(obj, "TYPE", None)
        if asn1_type in {"SEQUENCE", "CHOICE"}:
            data["fields"] = [_describe_obj(child, stack) for child in _iter_mapped_children(obj)]
        elif asn1_type == "SEQUENCE OF":
            element = getattr(obj, "_cont", None)
            if element is not None:
                data["element"] = _describe_obj(element, stack)
        elif asn1_type == "BIT STRING":
            named_bits = getattr(obj, "_cont", None)
            if isinstance(named_bits, ASN1Dict):
                data["named_bits"] = _serialize_asn1dict(named_bits)
        elif asn1_type == "ENUMERATED":
            enum_dict = getattr(obj, "_cont", None)
            if isinstance(enum_dict, ASN1Dict):
                data["symbols"] = _serialize_asn1dict(enum_dict)
        return data
    finally:
        stack.remove(obj_id)


def _iter_mapped_children(obj) -> Iterable:
    cont = getattr(obj, "_cont", None)
    if isinstance(cont, ASN1Dict):
        for _, child in cont.items():
            yield child
    elif isinstance(cont, dict):
        for child in cont.values():
            yield child


def _extract_constraints(obj) -> Optional[Dict[str, Any]]:
    get_const = getattr(obj, "get_const", None)
    if not callable(get_const):
        return None
    raw = get_const()
    if not raw:
        return None
    constraints: Dict[str, Any] = {}
    for key, value in raw.items():
        if isinstance(value, ASN1Set):
            constraints[key] = _serialize_asn1set(value)
        else:
            constraints[key] = _serialize_value(value)
    return constraints or None


def _serialize_asn1set(asn_set: ASN1Set) -> Dict[str, Any]:
    def convert(values: Optional[Sequence[Any]]):
        if not values:
            return None
        converted: List[Any] = []
        for item in values:
            if hasattr(item, "lb") and hasattr(item, "ub"):
                converted.append(
                    {
                        "type": "range",
                        "min": _serialize_value(item.lb),
                        "max": _serialize_value(item.ub),
                    }
                )
            else:
                converted.append({"type": "value", "value": _serialize_value(item)})
        return converted

    result: Dict[str, Any] = {}
    root = convert(getattr(asn_set, "root", None))
    if root:
        result["root"] = root
    ext = convert(getattr(asn_set, "ext", None))
    if ext:
        result["ext"] = ext
    return result


def _serialize_asn1dict(asn_dict: ASN1Dict) -> List[Dict[str, Any]]:
    return [{"name": name, "value": _serialize_value(value)} for name, value in asn_dict.items()]


def _serialize_value(value: Any) -> Any:
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    if isinstance(value, ASN1Dict):
        return {key: _serialize_value(val) for key, val in value.items()}
    if isinstance(value, ASN1Set):
        return _serialize_asn1set(value)
    if isinstance(value, (list, tuple)):
        return [_serialize_value(item) for item in value]
    if isinstance(value, dict):
        return {key: _serialize_value(val) for key, val in value.items()}
    if hasattr(value, "_name") and hasattr(value, "TYPE"):
        return {"name": value._name, "asn1_type": value.TYPE}
    return str(value)


def list_ie_names(definitions=None) -> List[str]:
    """Return all available IE attribute names."""

    definitions = definitions or load_rrc_definitions()
    return _list_ie_attrs(definitions)


def find_leaf_paths(
    leaf_ie_name: str,
    definitions=None,
    root_ie_names: Optional[Sequence[str]] = None,
) -> Dict[str, List[List[str]]]:
    """Return all root-to-leaf paths that end with the requested IE name.

    The returned mapping uses the resolved root IE display name as the key and
    lists every path (as a list of IE display names) that traverses from that
    root down to the matching leaf.
    """

    definitions = definitions or load_rrc_definitions()
    roots = list(root_ie_names) if root_ie_names else list(DEFAULT_ROOT_IE_NAMES)
    normalized_leaf = _normalize_leaf_name(leaf_ie_name)
    results: Dict[str, List[List[str]]] = {}
    for root_name in roots:
        try:
            selection = _resolve_ie_name(definitions, root_name)
        except IENameError:
            continue
        root_obj = getattr(definitions, selection.attr_name)
        paths: List[List[str]] = []
        _collect_leaf_paths(
            root_obj,
            selection.display_name,
            normalized_leaf,
            current_path=[],
            visited=set(),
            results=paths,
        )
        if paths:
            results[selection.display_name] = paths
    return results


def limit_leaf_path_depth(
    paths_by_root: Dict[str, List[List[str]]],
    max_depth: Optional[int],
) -> Dict[str, List[List[str]]]:
    """Limit each path to the root plus the last ``max_depth`` ancestors and the leaf."""

    if max_depth is None:
        return paths_by_root
    if max_depth < 0:
        raise ValueError("max_depth must be non-negative")
    limited: Dict[str, List[List[str]]] = {}
    tail_length = max_depth + 1  # include the leaf itself
    for root, paths in paths_by_root.items():
        trimmed: List[List[str]] = []
        for path in paths:
            if not path:
                continue
            if tail_length >= len(path):
                trimmed.append(list(path))
                continue
            tail = path[-tail_length:]
            root_name = path[0]
            if tail and tail[0] == root_name:
                trimmed.append(list(tail))
            else:
                trimmed.append([root_name, *tail])
        if trimmed:
            limited[root] = trimmed
    return limited


def format_leaf_paths_as_tree(
    paths_by_root: Dict[str, List[List[str]]],
    *,
    alias_roots: Optional[Sequence[str]] = None,
    alias_label: str = ROOT_ALIAS_LABEL,
) -> str:
    """Format the collected paths as an ASCII tree rooted at the leaf IE."""

    display_entries = _prepare_display_paths(paths_by_root, alias_roots, alias_label)
    if not display_entries:
        return ""
    blocks: List[str] = []
    for display_root, paths in display_entries:
        tree = _build_tree_from_paths([tuple(path) for path in paths])
        lines = _format_tree_lines(tree)
        blocks.append("\n".join(lines))
    return "\n\n".join(blocks)


def format_leaf_paths_as_mermaid(
    paths_by_root: Dict[str, List[List[str]]],
    *,
    alias_roots: Optional[Sequence[str]] = None,
    alias_label: str = ROOT_ALIAS_LABEL,
) -> str:
    """Render the collected paths as a Mermaid graph."""

    display_entries = _prepare_display_paths(paths_by_root, alias_roots, alias_label)
    if not display_entries:
        return ""
    edges: Set[tuple[str, str]] = set()
    for _, paths in display_entries:
        for path in paths:
            for parent, child in zip(path, path[1:]):
                edges.add((parent, child))
    lines = ["graph TD"]
    for parent, child in sorted(edges):
        lines.append(f'    "{_mermaid_escape(parent)}" --> "{_mermaid_escape(child)}"')
    return "\n".join(lines)


def _build_tree_from_paths(paths: Sequence[Sequence[str]]) -> Dict[str, Any]:
    tree: Dict[str, Any] = {}
    for path in paths:
        node = tree
        for part in path:
            node = node.setdefault(part, {})
    return tree


def format_leaf_paths_as_nested(
    paths_by_root: Dict[str, List[List[str]]],
    *,
    alias_roots: Optional[Sequence[str]] = None,
    alias_label: str = ROOT_ALIAS_LABEL,
) -> Dict[str, Dict[str, Any]]:
    """Return a nested tree representation suitable for JSON serialization."""

    display_entries = _prepare_display_paths(paths_by_root, alias_roots, alias_label)
    result: Dict[str, Dict[str, Any]] = {}
    for display_root, paths in display_entries:
        tree = _build_tree_from_paths([tuple(path) for path in paths])
        result[display_root] = _tree_dict_to_nested(tree)
    return result


def _tree_dict_to_nested(tree: Dict[str, Any]) -> Dict[str, Any]:
    items = sorted(tree.items())
    if not items:
        return {}
    if len(items) == 1:
        name, children = items[0]
        return {
            "name": name,
            "children": _tree_children_to_nested(children),
        }
    return {
        "name": "",
        "children": [
            {"name": name, "children": _tree_children_to_nested(children)}
            for name, children in items
        ],
    }


def _tree_children_to_nested(children: Dict[str, Any]) -> List[Dict[str, Any]]:
    return [
        {"name": name, "children": _tree_children_to_nested(grandchildren)}
        for name, grandchildren in sorted(children.items())
    ]


def _format_tree_lines(tree: Dict[str, Any], prefix: str = "") -> List[str]:
    lines: List[str] = []
    items = sorted(tree.items())
    total = len(items)
    for idx, (name, children) in enumerate(items):
        connector = "└─ " if idx == total - 1 else "├─ "
        lines.append(f"{prefix}{connector}{name}")
        if children:
            extension = "   " if idx == total - 1 else "│  "
            lines.extend(_format_tree_lines(children, prefix + extension))
    return lines


def _collect_leaf_paths(
    obj,
    current_name: str,
    target_base: str,
    current_path: List[str],
    visited: Set[int],
    results: List[List[str]],
) -> None:
    obj_id = id(obj)
    if obj_id in visited:
        return
    visited.add(obj_id)
    current_path.append(current_name)
    if _normalize_leaf_name(current_name) == target_base:
        results.append(list(current_path))
    asn_type = getattr(obj, "TYPE", None)
    if asn_type in {"SEQUENCE", "CHOICE"}:
        for child_name, child in _iter_named_children_with_names(obj):
            _collect_leaf_paths(child, child_name, target_base, current_path, visited, results)
    elif asn_type == "SEQUENCE OF":
        element = getattr(obj, "_cont", None)
        if element is not None:
            child_name = _get_obj_display_name(element)
            _collect_leaf_paths(element, child_name, target_base, current_path, visited, results)
    const_cont = getattr(obj, "_const_cont", None)
    if const_cont is not None:
        typeref = getattr(const_cont, "_typeref", None)
        if typeref is not None:
            ref_obj = typeref.get()
            child_name = _get_obj_display_name(ref_obj)
            _collect_leaf_paths(ref_obj, child_name, target_base, current_path, visited, results)
        else:
            child_name = _get_obj_display_name(const_cont)
            _collect_leaf_paths(const_cont, child_name, target_base, current_path, visited, results)
    current_path.pop()
    visited.remove(obj_id)


def _iter_named_children_with_names(obj) -> Iterable[tuple[str, Any]]:
    cont = getattr(obj, "_cont", None)
    if isinstance(cont, ASN1Dict):
        for _, child in cont.items():
            yield _get_obj_display_name(child), child
    elif isinstance(cont, dict):
        for child in cont.values():
            yield _get_obj_display_name(child), child


def _normalize_leaf_name(name: str) -> str:
    normalized = name.replace('_', '-').lower()
    return _LEAF_VERSION_SUFFIX.sub("", normalized)


def _get_obj_display_name(obj, fallback: Optional[str] = None) -> str:
    name = getattr(obj, "_name", None)
    if isinstance(name, str) and name:
        return name
    return fallback or obj.__class__.__name__


def normalize_ie_name(name: str) -> str:
    """Normalize an IE name for comparison (case/format/version agnostic)."""

    return _normalize_leaf_name(name)


def has_version_suffix(name: str) -> bool:
    """Return True if the IE name ends with a version suffix (-v###)."""

    normalized = name.replace('_', '-').lower()
    return bool(_LEAF_VERSION_SUFFIX.search(normalized))


def _prepare_display_paths(
    paths_by_root: Dict[str, List[List[str]]],
    alias_roots: Optional[Sequence[str]],
    alias_label: str,
) -> List[tuple[str, List[List[str]]]]:
    if not paths_by_root:
        return []
    alias_set = {
        _normalize_leaf_name(name)
        for name in (alias_roots or DEFAULT_ALIAS_ROOTS)
    }
    merged: Dict[str, Set[tuple[str, ...]]] = {}
    for original_root, paths in paths_by_root.items():
        root_key = _normalize_leaf_name(original_root)
        display_root = alias_label if root_key in alias_set else original_root
        dedup = merged.setdefault(display_root, set())
        for path in paths:
            if not path:
                continue
            normalized_path = list(path)
            normalized_path[0] = display_root
            dedup.add(tuple(normalized_path))
    entries: List[tuple[str, List[List[str]]]] = []
    for display_root, dedup in sorted(merged.items(), key=lambda item: item[0]):
        if dedup:
            entries.append((display_root, [list(seq) for seq in sorted(dedup)]))
    return entries


def _mermaid_escape(label: str) -> str:
    return label.replace('"', '\"')


def normalize_ie_name(name: str) -> str:
    """Normalize an IE name for comparison (case/format/version agnostic)."""

    return _normalize_leaf_name(name)


def has_version_suffix(name: str) -> bool:
    """Return True if the IE name ends with a version suffix (-v###)."""

    return bool(_LEAF_VERSION_SUFFIX.search(name.replace('_', '-').lower()))


def as_json(ie_name: str, definitions=None, **json_kwargs) -> str:
    """Return a JSON string for the requested IE."""

    data = describe_ie(ie_name, definitions=definitions)
    kwargs = {"indent": 2, "sort_keys": False}
    kwargs.update(json_kwargs)
    return json.dumps(data, **kwargs)
