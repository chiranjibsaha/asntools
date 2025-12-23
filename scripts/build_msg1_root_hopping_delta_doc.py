#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def build_document(*, repo_root: Path, output_path: Path) -> None:
    sections: list[tuple[str, Path]] = [
        ("TS 38.213 §8.1 Random access preamble", repo_root / "artifacts/spec_sections/38213-j10__8-1-random-access-preamble.md"),
        ("TS 38.213 §7.4 Physical random access channel", repo_root / "artifacts/spec_sections/38213-j10__7-4-physical-random-access-channel.md"),
        ("TS 38.321 §5.1 Random Access procedure", repo_root / "artifacts/spec_sections/38321-j00__5-1-random-access-procedure.md"),
        ("TS 38.331 FeatureCombinationPreambles", repo_root / "artifacts/spec_sections/38331-i60__featurecombinationpreambles.md"),
        ("TS 38.331 RACH-ConfigDedicated / CFRA", repo_root / "artifacts/spec_sections/38331-i60__rach-configdedicated.md"),
    ]

    missing = [str(path) for _, path in sections if not path.exists()]
    if missing:
        raise SystemExit(
            "Missing required extracted spec sections:\n"
            + "\n".join(f"- {item}" for item in missing)
            + "\n\nRegenerate with docs/spec_doc_tools.md + asntools.spec_cli."
        )

    parts: list[str] = []
    parts.append("# Msg1 repetition root hopping — full local extracts + proposed deltas\n")
    parts.append(
        "This file is generated locally by `scripts/build_msg1_root_hopping_delta_doc.py` "
        "from `artifacts/spec_sections/*` and is intended for local engineering use.\n"
    )

    for title, path in sections:
        parts.append(f"---\n\n## {title}\n\n")
        parts.append(_read_text(path).rstrip() + "\n")

    parts.append("---\n\n## Proposed deltas (diff style)\n\n")
    parts.append(
        "```diff\n"
        "--- TS 38.213 §8.1 (current)\n"
        "+++ TS 38.213 §8.1 (proposed: Msg1 repetition root hopping)\n"
        "@@ Higher-layer configuration for PRACH with repetitions @@\n"
        "+ Add higher-layer parameter:\n"
        "+ - msg1-RepetitionRootSequenceIndexList (optional)\n"
        "+   - size equals N_preamble^rep\n"
        "+   - each entry is a PRACH rootSequenceIndex (same family across the list)\n"
        "+\n"
        "+ UE behavior when PRACH is transmitted with repetitions (N_preamble^rep > 1):\n"
        "+ - If msg1-RepetitionRootSequenceIndexList is provided:\n"
        "+     repetition index i is the i-th PRACH occasion within the repetition set, in increasing time order;\n"
        "+     UE uses msg1-RepetitionRootSequenceIndexList[i] as the rootSequenceIndex for PRACH sequence generation for repetition i.\n"
        "+ - Else:\n"
        "+     UE uses the configured PRACH rootSequenceIndex for all repetitions.\n"
        "+\n"
        "+ Clarify that “same preambles” in repetition-set semantics refers to same preamble *index* (RAPID),\n"
        "+ not necessarily identical ZC root across repetitions when configured.\n"
        "\n"
        "--- TS 38.213 §7.4 (current)\n"
        "+++ TS 38.213 §7.4 (proposed: clarification only)\n"
        "@@ RAR-not-received / “preamble sequence transmitted” wording @@\n"
        "+ Clarify that for PRACH with repetitions, “preamble sequence transmitted” applies per repetition,\n"
        "+ while the PRACH attempt remains identified by the configured preamble index (RAPID) and repetition set timing.\n"
        "\n"
        "--- TS 38.321 §5.1 (current)\n"
        "+++ TS 38.321 §5.1 (proposed: clarification only)\n"
        "@@ Msg1 repetition and PHY configuration @@\n"
        "+ Add a clarification note:\n"
        "+ - When Msg1 is transmitted with repetitions, lower layers may be configured (by RRC) to use\n"
        "+   different PRACH root sequence indexes per repetition; MAC variables and procedure behavior are unchanged\n"
        "+   because PREAMBLE_INDEX (RAPID) and repetition-set timing semantics are unchanged.\n"
        "+\n"
        "@@ MAC-to-PHY instruction for PRACH transmission @@\n"
        "+ Clarify that when msg1-RepetitionRootSequenceIndexList is configured, the UE provides lower layers\n"
        "+ with the per-repetition root sequence index such that repetition i within the repetition set uses list entry i\n"
        "+ (repetition index per TS 38.213 §8.1).\n"
        "\n"
        "--- TS 38.331 / NR-RRC-Definitions (current)\n"
        "+++ TS 38.331 / NR-RRC-Definitions (proposed: Msg1 repetition root hopping)\n"
        "@@ New type(s) @@\n"
        "+ Msg1-RepetitionRootSequenceIndex-rXX ::= CHOICE {\n"
        "+   l839  INTEGER(0..837),\n"
        "+   l139  INTEGER(0..137),\n"
        "+   l571  INTEGER(0..569),\n"
        "+   l1151 INTEGER(0..1149)\n"
        "+ }\n"
        "+\n"
        "+ Msg1-RepetitionRootSequenceIndexList-rXX ::= SEQUENCE (SIZE (1..8)) OF Msg1-RepetitionRootSequenceIndex-rXX\n"
        "+\n"
        "@@ FeatureCombinationPreambles-r17 extension group @@\n"
        "+ Add msg1-RepetitionRootSequenceIndexList-rXX OPTIONAL alongside msg1-RepetitionNum-r18 and msg1-RepetitionTimeOffsetROGroup-r18.\n"
        "+\n"
        "@@ CFRA extension group @@\n"
        "+ Add msg1-RepetitionRootSequenceIndexList-rXX OPTIONAL alongside msg1-RepetitionNum-r18.\n"
        "+\n"
        "@@ UE capability gating @@\n"
        "+ Add per-band capability flag msg1-RepetitionRootHoppingSupport-rXX {supported} OPTIONAL.\n"
        "+ Network configures the list only if UE indicated support.\n"
        "```\n"
    )

    parts.append("---\n\n## Proposed IE field descriptions (new IEs)\n\n")
    parts.append("### `msg1-RepetitionRootSequenceIndexList-rXX`\n\n")
    parts.append(
        "Indicates the PRACH root sequence index to be used for each Msg1 repetition within a repetition set "
        "(see TS 38.213, clause 8.1).\n\n"
        "If present, for repetition index *i* (0..Nrep−1) within the repetition set (in increasing time order of PRACH occasions), "
        "the UE shall use the *i*-th entry of this list as the root sequence index for PRACH preamble sequence generation. "
        "All other PRACH parameters (e.g., PRACH format, subcarrier spacing, PRACH resources/occasions, spatial filter, and preamble index) "
        "remain as configured.\n\n"
        "If absent, the UE shall use the configured `prach-RootSequenceIndex` (or `prach-RootSequenceIndex-r16`, where applicable) for all repetitions.\n\n"
        "Constraints (normative intent):\n\n"
        "- The list size shall match the configured Msg1 repetition number.\n"
        "- All entries shall use the same root-length family and be consistent with the configured PRACH configuration.\n\n"
    )

    parts.append("### `msg1-RepetitionRootHoppingSupport-rXX`\n\n")
    parts.append(
        "If present, indicates that the UE supports configuration of different PRACH root sequence indexes across Msg1 repetitions "
        "using `msg1-RepetitionRootSequenceIndexList-rXX`.\n\n"
        "Network usage rule (normative intent): the network shall configure `msg1-RepetitionRootSequenceIndexList-rXX` only if the UE "
        "indicated `msg1-RepetitionRootHoppingSupport-rXX` for the serving band.\n"
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("".join(parts), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build a local Markdown note by concatenating existing extracted spec sections and appending proposed diffs."
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Repository root (defaults to script parent’s parent).",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=Path("artifacts/msg1_repetition_root_hopping_fulltext_with_deltas.md"),
        help="Output path (default: artifacts/msg1_repetition_root_hopping_fulltext_with_deltas.md).",
    )
    args = parser.parse_args()
    build_document(repo_root=args.repo_root, output_path=args.out)
    print(str(args.out))


if __name__ == "__main__":
    main()
