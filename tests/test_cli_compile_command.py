"""Tests for the top-level asntools CLI."""
from __future__ import annotations

import json
from pathlib import Path

import pytest
from click.testing import CliRunner

from asntools import DEFAULT_ASN1_PATH, DEFAULT_OUTPUT_DIR, __main__ as cli_main
from asntools.compile_rrc import compile_nr_rrc
import asntools.rebuild as rebuild


def _ensure_rrc_module():
    module_file = Path(DEFAULT_OUTPUT_DIR) / "NR_RRC_Definitions.py"
    if not module_file.exists():
        compile_nr_rrc(Path(DEFAULT_ASN1_PATH), Path(DEFAULT_OUTPUT_DIR))


def test_requires_flag():
    runner = CliRunner()
    result = runner.invoke(cli_main.main, [])
    assert result.exit_code != 0
    assert "--compile" in result.output
    assert "--serve" in result.output


def test_requires_at_least_one_file():
    runner = CliRunner()
    result = runner.invoke(cli_main.main, ["--compile"])
    assert result.exit_code != 0
    assert "Provide at least one ASN.1 file" in result.output


def test_merges_inputs_and_cleans_output(monkeypatch):
    runner = CliRunner()
    generated_files: list[Path] = []

    def fake_compile(asn1_path: Path, output_dir: Path, emit_json: bool = True) -> Path:  # noqa: ARG001
        output_dir.mkdir(parents=True, exist_ok=True)
        generated = output_dir / "NR_RRC_Definitions.py"
        generated.write_text("# generated\n", encoding="utf-8")
        generated_files.append(generated)
        return generated

    monkeypatch.setattr(rebuild, "compile_nr_rrc", fake_compile)

    with runner.isolated_filesystem():
        stale_dir = Path("pycrate_asn1dir")
        stale_dir.mkdir(parents=True)
        (stale_dir / "old.txt").write_text("old", encoding="utf-8")

        first = Path("input_a.asn")
        second = Path("input_b.asn")
        first.write_text("A_TEXT", encoding="utf-8")
        second.write_text("B_TEXT", encoding="utf-8")

        result = runner.invoke(
            cli_main.main,
            ["--compile", str(first), str(second)],
        )

        assert result.exit_code == 0, result.output
        merged = Path("asn1/NR-RRC-Definitions.asn")
        assert merged.read_text(encoding="utf-8") == "A_TEXT\nB_TEXT"
        assert not (stale_dir / "old.txt").exists()
        assert generated_files, "compile_nr_rrc should be called"
        assert "Merged ASN.1" in result.output
        assert "Generated pycrate module" in result.output


def test_single_input_copies_file(monkeypatch):
    runner = CliRunner()

    def fake_compile(asn1_path: Path, output_dir: Path, emit_json: bool = True) -> Path:  # noqa: ARG001
        output_dir.mkdir(parents=True, exist_ok=True)
        generated = output_dir / "NR_RRC_Definitions.py"
        generated.write_text("# generated\n", encoding="utf-8")
        return generated

    monkeypatch.setattr(rebuild, "compile_nr_rrc", fake_compile)

    with runner.isolated_filesystem():
        src = Path("external/definition.asn")
        src.parent.mkdir(parents=True)
        src.write_text("ONLY_TEXT", encoding="utf-8")

        result = runner.invoke(
            cli_main.main,
            ["--compile", str(src)],
        )

        assert result.exit_code == 0, result.output
        copied = Path("asn1/NR-RRC-Definitions.asn")
        assert copied.read_text(encoding="utf-8") == "ONLY_TEXT"


def test_compile_accepts_option_lists(monkeypatch):
    runner = CliRunner()

    def fake_compile(asn1_path: Path, output_dir: Path, emit_json: bool = True) -> Path:  # noqa: ARG001
        output_dir.mkdir(parents=True, exist_ok=True)
        generated = output_dir / "NR_RRC_Definitions.py"
        generated.write_text("# generated\n", encoding="utf-8")
        return generated

    monkeypatch.setattr(rebuild, "compile_nr_rrc", fake_compile)

    with runner.isolated_filesystem():
        first = Path("alpha.asn")
        second = Path("beta.asn")
        first.write_text("AAA", encoding="utf-8")
        second.write_text("BBB", encoding="utf-8")

        result = runner.invoke(
            cli_main.main,
            ["--compile", "--asnfiles", str(first), "--asnfiles", str(second)],
        )

        assert result.exit_code == 0, result.output
        merged = Path("asn1/NR-RRC-Definitions.asn")
        assert merged.read_text(encoding="utf-8") == "AAA\nBBB"


def test_compile_reads_setup_file(monkeypatch):
    runner = CliRunner()

    def fake_compile(asn1_path: Path, output_dir: Path, emit_json: bool = True) -> Path:  # noqa: ARG001
        output_dir.mkdir(parents=True, exist_ok=True)
        generated = output_dir / "NR_RRC_Definitions.py"
        generated.write_text("# generated\n", encoding="utf-8")
        return generated

    monkeypatch.setattr(rebuild, "compile_nr_rrc", fake_compile)

    with runner.isolated_filesystem():
        first = Path("first.asn")
        second = Path("second.asn")
        first.write_text("ONE", encoding="utf-8")
        second.write_text("TWO", encoding="utf-8")
        desc = Path("fields.json")
        desc.write_text('{"field_descriptions": {"Foo": "Bar"}}', encoding="utf-8")

        setup = Path("compile_setup.json")
        setup.write_text(
            json.dumps(
                {
                    "asnfiles": [str(first), str(second)],
                    "field_descriptions": [str(desc)],
                }
            ),
            encoding="utf-8",
        )

        result = runner.invoke(cli_main.main, ["--compile", "--compile-setup", str(setup)])
        assert result.exit_code == 0, result.output

        merged = Path("asn1/NR-RRC-Definitions.asn").read_text(encoding="utf-8")
        assert merged == "ONE\nTWO"
        merged_desc = json.loads(Path("asn1/field_descriptions.json").read_text(encoding="utf-8"))
        assert merged_desc["ies"]["_global"]["Foo"] == "Bar"


def test_serve_invokes_server(monkeypatch):
    runner = CliRunner()
    called = {}

    def fake_serve(host: str, port: int):
        called["host"] = host
        called["port"] = port

    monkeypatch.setattr(cli_main, "serve_forever", fake_serve, raising=False)

    result = runner.invoke(cli_main.main, ["--serve", "--host", "0.0.0.0", "--port", "9000"])
    assert result.exit_code == 0, result.output
    assert called == {"host": "0.0.0.0", "port": 9000}


def test_compile_with_field_descriptions(monkeypatch):
    runner = CliRunner()

    def fake_compile(asn1_path: Path, output_dir: Path, emit_json: bool = True) -> Path:  # noqa: ARG001
        output_dir.mkdir(parents=True, exist_ok=True)
        generated = output_dir / "NR_RRC_Definitions.py"
        generated.write_text("# generated\n", encoding="utf-8")
        return generated

    monkeypatch.setattr(rebuild, "compile_nr_rrc", fake_compile)

    with runner.isolated_filesystem():
        src = Path("foo.asn")
        src.write_text("text", encoding="utf-8")
        desc_a = Path("foo_desc.json")
        desc_b = Path("bar_desc.json")
        desc_a.write_text('{"field_descriptions": {"Foo": "first"}}', encoding="utf-8")
        desc_b.write_text('{"field_descriptions": {"Bar": "second"}}', encoding="utf-8")

        result = runner.invoke(
            cli_main.main,
            [
                "--compile",
                str(src),
                "--asnfielddescriptions",
                str(desc_a),
                "--asnfielddescriptions",
                str(desc_b),
            ],
        )
        assert result.exit_code == 0, result.output
        output = Path("asn1/field_descriptions.json")
        data = json.loads(output.read_text(encoding="utf-8"))
        assert data["ies"]["_global"]["Foo"] == "first"
        assert data["ies"]["_global"]["Bar"] == "second"
        assert "Merged field descriptions" in result.output


def test_compile_with_input_dir(monkeypatch):
    runner = CliRunner()

    def fake_compile(asn1_path: Path, output_dir: Path, emit_json: bool = True) -> Path:  # noqa: ARG001
        output_dir.mkdir(parents=True, exist_ok=True)
        generated = output_dir / "NR_RRC_Definitions.py"
        generated.write_text("# generated\n", encoding="utf-8")
        return generated

    monkeypatch.setattr(rebuild, "compile_nr_rrc", fake_compile)

    with runner.isolated_filesystem():
        nested = Path("inputs/subdir")
        other = Path("inputs/other")
        nested.mkdir(parents=True, exist_ok=True)
        other.mkdir(parents=True, exist_ok=True)
        (nested / "one.asn").write_text("ONE", encoding="utf-8")
        (nested / "two.asn").write_text("TWO", encoding="utf-8")
        (nested / "one_asn_field_description.json").write_text(
            '{"field_descriptions": {"one": "desc"}}',
            encoding="utf-8",
        )
        (other / "ignored.asn").write_text("IGNORED", encoding="utf-8")

        result = runner.invoke(
            cli_main.main,
            ["--compile", "--input-dir", "inputs", "--scan-subdir", "subdir"],
        )
        assert result.exit_code == 0, result.output
        merged = Path("asn1/NR-RRC-Definitions.asn").read_text(encoding="utf-8")
        assert "ONE" in merged and "TWO" in merged and "IGNORED" not in merged
        desc_file = Path("asn1/field_descriptions.json")
        assert desc_file.exists()


def test_describe_field(monkeypatch):
    runner = CliRunner()
    with runner.isolated_filesystem():
        desc_path = Path("asn1")
        desc_path.mkdir(parents=True, exist_ok=True)
        (desc_path / "field_descriptions.json").write_text(
            '{"field_descriptions": {"test-field": "Test description"}}\n',
            encoding="utf-8",
        )
        result = runner.invoke(cli_main.main, ["--describe-field", "test_field"])
        assert result.exit_code == 0, result.output
        payload = json.loads(result.output)
        assert payload["matches"][0]["description"] == "Test description"


def test_describe_field_with_suggestions(monkeypatch):
    runner = CliRunner()
    with runner.isolated_filesystem():
        desc_path = Path("asn1")
        desc_path.mkdir(parents=True, exist_ok=True)
        (desc_path / "field_descriptions.json").write_text(
            '{"field_descriptions": {"test-field": "Test description", "test-field2": "Other"}}\n',
            encoding="utf-8",
        )
        result = runner.invoke(cli_main.main, ["--describe-field", "tset-field"])
        assert result.exit_code != 0
        assert "Suggestions" in result.output


def test_describe_ie(monkeypatch):
    runner = CliRunner()
    with runner.isolated_filesystem():
        desc_path = Path("asn1")
        desc_path.mkdir(parents=True, exist_ok=True)
        (desc_path / "field_descriptions.json").write_text(
            json.dumps(
                {
                    "ies": {
                        "Foo-IE": {
                            "fieldA": "A",
                            "fieldB": "B",
                        }
                    }
                }
            ),
            encoding="utf-8",
        )
        result = runner.invoke(cli_main.main, ["--describe-ie", "Foo_ie"])
        assert result.exit_code == 0, result.output
        payload = json.loads(result.output)
        assert payload["ie_name"] == "Foo-IE"
        assert payload["fields"]["fieldA"] == "A"


def test_show_ie_outputs_json(monkeypatch):
    _ensure_rrc_module()
    runner = CliRunner()
    result = runner.invoke(cli_main.main, ["--show", "RACH-ConfigGeneric"])
    assert result.exit_code == 0, result.output
    data = json.loads(result.output)
    assert data["name"] == "RACH-ConfigGeneric"
    assert data["asn1_type"] == "SEQUENCE"


def test_show_ie_missing(monkeypatch):
    _ensure_rrc_module()
    runner = CliRunner()
    result = runner.invoke(cli_main.main, ["--show", "DefinitelyNotRealIE"])
    assert result.exit_code != 0
    assert "not found" in result.output.lower()


def test_show_ie_lpp(monkeypatch):
    _ensure_rrc_module()
    runner = CliRunner()
    result = runner.invoke(cli_main.main, ["--show", "CommonIEsProvideLocationInformation"])
    assert result.exit_code == 0, result.output
    data = json.loads(result.output)
    assert data["name"] == "CommonIEsProvideLocationInformation"
    assert any(field["name"] == "locationEstimate" for field in data["fields"])


def test_tree_command_outputs_json(monkeypatch):
    _ensure_rrc_module()
    runner = CliRunner()
    result = runner.invoke(cli_main.main, ["--tree", "rach-ConfigCommon"])
    assert result.exit_code == 0, result.output
    payload = json.loads(result.output)
    assert payload["status"] == "ok"
    assert payload["tree_json"]
    assert "parent_counts" in payload


def test_tree_command_ambiguous(monkeypatch):
    _ensure_rrc_module()
    runner = CliRunner()
    result = runner.invoke(cli_main.main, ["--tree", "RRCReconfiguration"])
    assert result.exit_code == 0, result.output
    payload = json.loads(result.output)
    assert payload["status"] in {"ok", "ambiguous_versions"}


def test_tree_command_lpp_ie(monkeypatch):
    _ensure_rrc_module()
    runner = CliRunner()
    result = runner.invoke(cli_main.main, ["--tree", "CommonIEsProvideLocationInformation"])
    assert result.exit_code == 0, result.output
    payload = json.loads(result.output)
    assert payload["status"] == "ok"
    assert "LPP-Message" in payload["paths"]


def test_tree_command_with_depth(monkeypatch):
    _ensure_rrc_module()
    runner = CliRunner()
    result = runner.invoke(cli_main.main, ["--tree", "EllipsoidPointWithAltitudeAndUncertaintyEllipsoid", "--tree-depth", "1"])
    assert result.exit_code == 0, result.output
    payload = json.loads(result.output)
    assert payload["status"] == "ok"
    for paths in payload["paths"].values():
        for path in paths:
            # root + (tree_depth ancestors) + leaf
            assert len(path) <= 1 + 1 + 1
def test_tree_command_pretty(monkeypatch, tmp_path):
    _ensure_rrc_module()
    runner = CliRunner()
    output = tmp_path / "tree.md"
    result = runner.invoke(cli_main.main, ["--tree", "rach-ConfigCommon", "--tree-markdown-output", str(output)])
    assert result.exit_code == 0, result.output
    assert output.exists()
    content = output.read_text(encoding="utf-8")
    assert "RRCResume/RRCReconfiguration" in content
