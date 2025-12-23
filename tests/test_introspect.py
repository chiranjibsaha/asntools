from pathlib import Path

import pytest

from asntools import DEFAULT_ASN1_PATH, DEFAULT_OUTPUT_DIR
from asntools.compile_rrc import compile_nr_rrc
from asntools.introspect import (
    IENameError,
    describe_ie,
    find_leaf_paths,
    format_leaf_paths_as_tree,
    load_rrc_definitions,
)


@pytest.fixture(scope="session")
def definitions():
    module_file = Path(DEFAULT_OUTPUT_DIR) / "NR_RRC_Definitions.py"
    if not module_file.exists():
        compile_nr_rrc(Path(DEFAULT_ASN1_PATH), Path(DEFAULT_OUTPUT_DIR))
    return load_rrc_definitions()


def test_describe_sequence_includes_fields(definitions):
    data = describe_ie("RACH_ConfigGeneric", definitions=definitions)
    assert data["asn1_type"] == "SEQUENCE"
    field_map = {field["name"]: field for field in data["fields"]}
    assert "prach-ConfigurationIndex" in field_map
    idx = field_map["prach-ConfigurationIndex"]
    assert idx["asn1_type"] == "INTEGER"
    constraint = idx["constraints"]["val"]["root"][0]
    assert constraint == {"type": "range", "min": 0, "max": 255}


def test_describe_sequence_includes_enums(definitions):
    data = describe_ie("RACH_ConfigGeneric", definitions=definitions)
    field_map = {field["name"]: field for field in data["fields"]}
    enum_field = field_map["msg1-FDM"]
    assert enum_field["asn1_type"] == "ENUMERATED"
    symbols = enum_field["symbols"]
    assert symbols[0] == {"name": "one", "value": 0}
    assert symbols[-1]["name"] == "eight"


def test_choice_ie_lists_branches(definitions):
    data = describe_ie("ApplicableDisasterInfo_r17", definitions=definitions)
    assert data["asn1_type"] == "CHOICE"
    branch_names = [field["name"] for field in data["fields"]]
    assert "noDisasterRoaming-r17" in branch_names
    assert "commonPLMNs-r17" in branch_names


def test_sequence_of_ie_has_element_descriptor(definitions):
    data = describe_ie("ATG_NeighCellConfigList_r18", definitions=definitions)
    assert data["asn1_type"] == "SEQUENCE OF"
    elem = data["element"]
    assert elem["asn1_type"] == "SEQUENCE"
    assert elem["name"] == "_item_"


def test_describe_lpp_ie(definitions):
    data = describe_ie("CommonIEsProvideLocationInformation", definitions=definitions)
    assert data["asn1_type"] == "SEQUENCE"
    assert data["name"] == "CommonIEsProvideLocationInformation"
    field_names = {field["name"] for field in data["fields"]}
    assert "locationEstimate" in field_names


def test_missing_ie_raises(definitions):
    with pytest.raises(IENameError):
        describe_ie("NotARealIE", definitions=definitions)


def test_find_leaf_paths_returns_data(definitions):
    paths_by_root = find_leaf_paths("pdcch-ConfigCommon", definitions=definitions)
    assert paths_by_root
    flattened = [segment for paths in paths_by_root.values() for path in paths for segment in path]
    assert any("pdcch-configcommon" in segment.lower() for segment in flattened)


def test_find_leaf_paths_handles_lpp_roots(definitions):
    paths_by_root = find_leaf_paths("CommonIEsProvideLocationInformation", definitions=definitions)
    assert "LPP-Message" in paths_by_root
    sample_path = paths_by_root["LPP-Message"][0]
    assert sample_path[0] == "LPP-Message"
    assert sample_path[-1].lower() == "commoniesprovidelocationinformation".lower()


def test_format_leaf_paths_aliases_rrc_roots():
    sample = {
        "RRCReconfiguration": [["RRCReconfiguration", "branch", "leaf"]],
        "OtherRoot": [["OtherRoot", "branch", "leaf"]],
        "RRCResume": [["RRCResume", "branch2", "leaf"]],
    }
    rendered = format_leaf_paths_as_tree(sample)
    assert rendered.count("RRCResume/RRCReconfiguration") == 1
    assert "branch2" in rendered
    assert "OtherRoot" in rendered
