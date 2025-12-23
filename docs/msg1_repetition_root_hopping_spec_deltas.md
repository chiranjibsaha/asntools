# Msg1 Repetition Root Hopping — Spec Extracts (Pointers) + Proposed Deltas

This document is a working note for introducing *per-repetition PRACH root sequence index* selection when Msg1 is transmitted with repetitions.

## Why this doc does not inline full spec text

I can’t reproduce full verbatim 3GPP spec sections here (or in a generated Markdown note) due to copyright. Instead:

- This doc points to the **full local extracts** already present in your repo under `artifacts/spec_sections/`.
- It includes **very short verbatim snippets** only as anchors.
- The proposed changes are shown in **diff-style** blocks that reference the relevant clauses/IEs.

To view the full extracted clause text locally:

- `less artifacts/spec_sections/38213-j10__8-1-random-access-preamble.md`
- `less artifacts/spec_sections/38213-j10__7-4-physical-random-access-channel.md`
- `less artifacts/spec_sections/38321-j00__5-1-random-access-procedure.md`
- `less artifacts/spec_sections/38331-i60__featurecombinationpreambles.md`
- `less artifacts/spec_sections/38331-i60__rach-configdedicated.md`

To build a **single local Markdown** that concatenates the full extracted texts and appends the proposed diff block:

- `python3 scripts/build_msg1_root_hopping_delta_doc.py`
- Output: `artifacts/msg1_repetition_root_hopping_fulltext_with_deltas.md`

That generated file also includes a section:

- `## Proposed IE field descriptions (new IEs)` (appended after the diff block)

To (re)generate those extracts from `docs/*.html` + `*_toc.json`:

- `python3 -c "from asntools.spec_cli import extract; extract.main(['38213-j10','8-1-random-access-preamble'], standalone_mode=False)"`
- `python3 -c "from asntools.spec_cli import extract; extract.main(['38213-j10','7-4-physical-random-access-channel'], standalone_mode=False)"`
- `python3 -c "from asntools.spec_cli import extract; extract.main(['38321-j00','5-1-random-access-procedure'], standalone_mode=False)"`
- `python3 -c "from asntools.spec_cli import extract; extract.main(['38331-i60','featurecombinationpreambles'], standalone_mode=False)"`
- `python3 -c "from asntools.spec_cli import extract; extract.main(['38331-i60','rach-configdedicated'], standalone_mode=False)"`

---

## TS 38.213 (RAN4) — PRACH procedure and power control

### Full local extracts (verbatim, in-repo)

- §8.1: `artifacts/spec_sections/38213-j10__8-1-random-access-preamble.md`
- §7.4: `artifacts/spec_sections/38213-j10__7-4-physical-random-access-channel.md`

### Anchor snippets (verbatim, short)

From §8.1 “Random access preamble” (`artifacts/spec_sections/38213-j10__8-1-random-access-preamble.md:9`):

> “A number of \(N_{\text{preamble}}^{\text{rep}} > 1\) preamble repetitions for the PRACH transmission …”

From §7.4 “Physical random access channel” (`artifacts/spec_sections/38213-j10__7-4-physical-random-access-channel.md:51`):

> “If the UE transmits less than \(N_{\text{preamble}}^{\text{rep}}\) preamble repetitions …”

### Proposed delta (diff style)

```diff
--- TS 38.213 §8.1 (current)
+++ TS 38.213 §8.1 (proposed: Msg1 repetition root hopping)
@@ Higher-layer configuration for PRACH with repetitions @@
+ Add higher-layer parameter:
+ - msg1-RepetitionRootSequenceIndexList (optional)
+   - size equals N_preamble^rep
+   - each entry is a PRACH rootSequenceIndex (same family across the list)
+
+ UE behavior when PRACH is transmitted with repetitions (N_preamble^rep > 1):
+ - If msg1-RepetitionRootSequenceIndexList is provided:
+     repetition index i is the i-th PRACH occasion within the repetition set, in increasing time order;
+     UE uses msg1-RepetitionRootSequenceIndexList[i] as the rootSequenceIndex for PRACH sequence generation for repetition i.
+ - Else:
+     UE uses the configured PRACH rootSequenceIndex for all repetitions.
+
+ Clarify that “same preambles” in repetition-set semantics refers to same preamble *index* (RAPID), not necessarily identical ZC root across repetitions when configured.

--- TS 38.213 §7.4 (current)
+++ TS 38.213 §7.4 (proposed: clarification only)
@@ RAR-not-received / “preamble sequence transmitted” wording @@
+ Clarify that for PRACH with repetitions, “preamble sequence transmitted” applies per repetition,
+ while the PRACH attempt remains identified by the configured preamble index (RAPID) and repetition set timing.
```

Notes:
- The normative “root sequence index → sequence generation” details likely also require alignment text in TS 38.211; this doc focuses on 38.213/38.321/38.331 deltas only.

---

## TS 38.321 (RAN2) — MAC random access procedure

### Full local extract (verbatim, in-repo)

- §5.1: `artifacts/spec_sections/38321-j00__5-1-random-access-procedure.md`

### Anchor snippet (verbatim, short)

From §5.1 “Random Access procedure” (`artifacts/spec_sections/38321-j00__5-1-random-access-procedure.md:1339`):

> “The RA-RNTI … or the RA-RNTI associated with the last valid PRACH occasion … for Msg1 repetition …”

From §5.1 (`artifacts/spec_sections/38321-j00__5-1-random-access-procedure.md:1469`):

> “start the *ra-ResponseWindow* … from the end of all repetitions …”

### Proposed delta (diff style)

```diff
--- TS 38.321 §5.1 (current)
+++ TS 38.321 §5.1 (proposed: clarification only)
@@ Msg1 repetition and PHY configuration @@
+ Add a clarification note:
+ - When Msg1 is transmitted with repetitions, lower layers may be configured (by RRC) to use
+   different PRACH root sequence indexes per repetition; MAC variables and procedure behavior are unchanged
+   because PREAMBLE_INDEX (RAPID) and repetition-set timing semantics are unchanged.
+
+@@ MAC-to-PHY instruction for PRACH transmission @@
++ Clarify that when `msg1-RepetitionRootSequenceIndexList` is configured, the UE provides lower layers
++ with the per-repetition root sequence index such that repetition i within the repetition set uses list entry i
++ (repetition index per TS 38.213 §8.1).
```

---

## TS 38.331 (RAN2) — RRC signalling / NR-RRC-Definitions ASN.1

### Full local extracts (verbatim, in-repo)

- `FeatureCombinationPreambles`: `artifacts/spec_sections/38331-i60__featurecombinationpreambles.md`
- `RACH-ConfigDedicated` / `CFRA`: `artifacts/spec_sections/38331-i60__rach-configdedicated.md`

### Anchor snippets (verbatim, short)

From `FeatureCombinationPreambles-r17` (`artifacts/spec_sections/38331-i60__featurecombinationpreambles.md:22`):

> “msg1-RepetitionNum-r18 … OPTIONAL”

> “msg1-RepetitionTimeOffsetROGroup-r18 … OPTIONAL”

### Proposed delta (diff style, ASN.1-focused)

```diff
--- NR-RRC-Definitions (current)
+++ NR-RRC-Definitions (proposed: Msg1 repetition root hopping)
@@ New type(s) @@
+ Msg1-RepetitionRootSequenceIndex-rXX ::= CHOICE {
+   l839  INTEGER(0..837),
+   l139  INTEGER(0..137),
+   l571  INTEGER(0..569),
+   l1151 INTEGER(0..1149)
+ }
+
+ Msg1-RepetitionRootSequenceIndexList-rXX ::= SEQUENCE (SIZE (1..8)) OF Msg1-RepetitionRootSequenceIndex-rXX
+
@@ FeatureCombinationPreambles-r17 extension group (Rel-18 area) @@
  FeatureCombinationPreambles-r17 ::= SEQUENCE {
    ...
    [[
      msg1-RepetitionNum-r18                 ENUMERATED {n2, n4, n8, spare1} OPTIONAL,
      msg1-RepetitionTimeOffsetROGroup-r18   ENUMERATED {n4, n8, n16, spare1} OPTIONAL,
+     msg1-RepetitionRootSequenceIndexList-rXX Msg1-RepetitionRootSequenceIndexList-rXX OPTIONAL
    ]]
  }
+
+ Constraint text (normative, in field description / procedure):
+ - If msg1-RepetitionRootSequenceIndexList-rXX is present:
+     SIZE(list) equals the configured msg1-RepetitionNum-r18 value.
+     All list entries use the same root-length family, consistent with PRACH configuration.
+ - If absent: UE uses configured prach-RootSequenceIndex (or prach-RootSequenceIndex-r16 where applicable) for all repetitions.
+
@@ CFRA (under RACH-ConfigDedicated) extension group @@
  CFRA ::= SEQUENCE {
    ...
    [[
      msg1-RepetitionNum-r18                  ENUMERATED {n2, n4, n8, spare1} OPTIONAL,
+     msg1-RepetitionRootSequenceIndexList-rXX Msg1-RepetitionRootSequenceIndexList-rXX OPTIONAL
    ]]
  }
+
@@ UE capability gating (per-band) @@
+ Add per-band capability flag (same container as prach-Repetition-r18):
+ - msg1-RepetitionRootHoppingSupport-rXX  ENUMERATED {supported} OPTIONAL
+
+ RRC rule:
+ - Network shall configure msg1-RepetitionRootSequenceIndexList-rXX only if UE indicated msg1-RepetitionRootHoppingSupport-rXX for the serving band.
```

### Where it is signalled (paths)

- Broadcast (SIB1): `SIB1 -> servingCellConfigCommon -> uplinkConfigCommon -> initialUplinkBWP -> rach-ConfigCommon -> featureCombinationPreamblesList-r17 -> FeatureCombinationPreambles-r17`.
- Dedicated (connected): via common config updates (same `rach-ConfigCommon` chain under `RRCReconfiguration`) and via `reconfigurationWithSync -> rach-ConfigDedicated` for CFRA.

---

## Proposed IE field descriptions (new IEs)

This is the narrative text intended for `*_asn_field_description.json` (typically keyed without the `-rNN` suffix).

### `msg1-RepetitionRootSequenceIndexList`

Indicates the PRACH root sequence index to be used for each Msg1 repetition within a repetition set (see TS 38.213, clause 8.1).

If present, for repetition index *i* (0..Nrep−1) within the repetition set (in increasing time order of PRACH occasions), the UE shall use the *i*-th entry of this list as the root sequence index for PRACH preamble sequence generation. All other PRACH parameters (e.g., PRACH format, subcarrier spacing, PRACH resources/occasions, spatial filter, and preamble index) remain as configured.

If absent, the UE shall use the configured `prach-RootSequenceIndex` (or `prach-RootSequenceIndex-r16`, where applicable) for all repetitions.

Constraints (normative intent):

- The list size shall match the configured Msg1 repetition number.
- All entries shall use the same root-length family and be consistent with the configured PRACH configuration.

### `msg1-RepetitionRootHoppingSupport`

If present, indicates that the UE supports configuration of different PRACH root sequence indexes across Msg1 repetitions using `msg1-RepetitionRootSequenceIndexList`.

Network usage rule (normative intent): the network shall configure `msg1-RepetitionRootSequenceIndexList` only if the UE indicated `msg1-RepetitionRootHoppingSupport` for the serving band.
