"""Tests for --grep ASN.1 search."""
from __future__ import annotations

import json
import sys
from pathlib import Path
import types

from click.testing import CliRunner

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Stub pycrate imports used during asntools CLI import so tests don't require the dependency.
stub_asnproc = types.ModuleType("pycrate_asn1c.asnproc")
stub_asnproc.GLOBAL = {}
stub_asnproc.JSONDepGraphGenerator = object
stub_asnproc.PycrateGenerator = object
stub_asnproc.compile_text = lambda *args, **kwargs: None
stub_asnproc.generate_modules = lambda *args, **kwargs: None

sys.modules.setdefault("pycrate_asn1c", types.ModuleType("pycrate_asn1c"))
sys.modules["pycrate_asn1c"].asnproc = stub_asnproc
sys.modules["pycrate_asn1c.asnproc"] = stub_asnproc

stub_dictobj = types.ModuleType("pycrate_asn1rt.dictobj")
stub_dictobj.ASN1Dict = dict
stub_setobj = types.ModuleType("pycrate_asn1rt.setobj")
stub_setobj.ASN1Set = set
sys.modules.setdefault("pycrate_asn1rt", types.ModuleType("pycrate_asn1rt"))
sys.modules["pycrate_asn1rt"].dictobj = stub_dictobj
sys.modules["pycrate_asn1rt"].setobj = stub_setobj
sys.modules["pycrate_asn1rt.dictobj"] = stub_dictobj
sys.modules["pycrate_asn1rt.setobj"] = stub_setobj

from asntools.__main__ import main as cli_main


def test_grep_finds_matches():
    runner = CliRunner()
    with runner.isolated_filesystem():
        asn_path = Path("asn1")
        asn_path.mkdir(parents=True, exist_ok=True)
        target = asn_path / "NR-RRC-Definitions.asn"
        target.write_text("FooBar baz\nanother bar line\n", encoding="utf-8")

        result = runner.invoke(cli_main, ["--grep", "bar"])
        assert result.exit_code == 0, result.output
        payload = json.loads(result.output)
        assert payload["status"] == "ok"
        assert payload["match_count"] == 2
        assert len(payload["chunks"]) == payload["match_count"]
        first = payload["matches"][0]
        assert first["line"] == 1
        assert first["message_length"] == len("FooBar baz")
        assert "bar" in first["message"].lower()
        assert payload["chunks"][0] == first["message"]


def test_grep_not_found():
    runner = CliRunner()
    with runner.isolated_filesystem():
        asn_path = Path("asn1")
        asn_path.mkdir(parents=True, exist_ok=True)
        (asn_path / "NR-RRC-Definitions.asn").write_text("Only content here\n", encoding="utf-8")

        result = runner.invoke(cli_main, ["--grep", "missing"])
        assert result.exit_code == 0, result.output
        payload = json.loads(result.output)
        assert payload["status"] == "not_found"
        assert payload["match_count"] == 0
        assert payload["matches"] == []
        assert payload["chunks"] == []


def test_grep_regex():
    runner = CliRunner()
    with runner.isolated_filesystem():
        asn_path = Path("asn1")
        asn_path.mkdir(parents=True, exist_ok=True)
        (asn_path / "NR-RRC-Definitions.asn").write_text("alpha Beta gamma\nBETA delta\n", encoding="utf-8")

        result = runner.invoke(cli_main, ["--grep", r"b.ta", "--grep-regex"])
        assert result.exit_code == 0, result.output
        payload = json.loads(result.output)
        assert payload["status"] == "ok"
        assert payload["match_count"] == 2
