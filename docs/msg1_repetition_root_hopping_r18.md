# Msg1 Repetition “Root Hopping” (future `_rXX`) — Findings + Proposal (Option 1)

This note captures:

1) **What the current NR-RRC ASN.1 exposes today** (as compiled and introspected locally with `asntools`).
2) A **concrete Option 1** proposal: reuse the Msg1 repetition framework but allow a different PRACH root sequence index per repetition (e.g., rep#1 uses root=1, rep#2 uses root=2).
3) The **normative changes needed** in TS 38.213 §8.1 and the **RRC message structure** (TS 38.331 / `NR-RRC-Definitions.asn`).

Naming note:

- Any *new* IE introduced by this proposal is suffixed with **`_rXX`** to indicate a future release number that is not fixed yet.

---

## 1) Current RRC “as-is” (what we found via `asntools`)

### 1.1 PRACH root sequence index is configured *once per RACH config*

In `RACH-ConfigCommon`, `prach-RootSequenceIndex` exists as a single field:

- `prach-RootSequenceIndex` is a `CHOICE` (sequence length family selection):
  - `l839 INTEGER (0..837)`
  - `l139 INTEGER (0..137)`

This indicates a **single configured root sequence index** selection for the PRACH configuration.

Also, for some configurations (e.g., FR2-2 / specific initial-BWP conditions), `RACH-ConfigCommon` includes an additional variant:

- `prach-RootSequenceIndex-r16` (`CHOICE`):
  - `l571 INTEGER (0..569)`
  - `l1151 INTEGER (0..1149)`

How to reproduce:

- `asntools --show RACH-ConfigCommon` and search for `prach-RootSequenceIndex`
- `asntools --tree prach-RootSequenceIndex`

### 1.2 Msg1 repetition knobs exist (Rel-18)

In `FeatureCombinationPreambles-r17`, we observed the Msg1 repetition related fields:

- `msg1-RepetitionNum-r18` (ENUMERATED: `n2`, `n4`, `n8`, …)
- `msg1-RepetitionTimeOffsetROGroup-r18` (ENUMERATED: `n4`, `n8`, `n16`, …)

How to reproduce:

- `asntools --show FeatureCombinationPreambles-r17`
- `asntools --tree msg1-RepetitionNum-r18`

### 1.3 Where the feature-combination preamble configs sit in the tree

`featureCombinationPreamblesList-r17` appears under RACH common configuration paths such as:

- `... initialUplinkBWP -> rach-ConfigCommon -> setup -> featureCombinationPreamblesList-r17`
- and also under related configs (e.g., additional RACH config list, RedCap initial UL BWP, etc.)

How to reproduce:

- `asntools --tree featureCombinationPreamblesList-r17`

### 1.4 Summary: no per-repetition “root selection” exists today

From the above, NR-RRC (as compiled here) provides:

- A single `prach-RootSequenceIndex` in RACH config, and
- Msg1 repetition count/offset selection,

but **no RRC field to vary the root sequence index per repetition**.

---

## 2) Option 1 Proposal: Per-repetition root sequence index list (RRC + 38.213)

### 2.1 Goal

Reuse Msg1 repetition framework with `N_preamble^rep = 2`, but transmit:

- repetition #1: root index = 1
- repetition #2: root index = 2

while still treating this as **one PRACH attempt with repetitions**, not two unrelated PRACH transmissions.

### 2.2 RRC message structure change (TS 38.331 / `NR-RRC-Definitions`)

Add a new optional IE that provides the root sequence index **per repetition**.

**Proposed new IE (conceptual, new `_rXX`):**

- `msg1-RepetitionRootSequenceIndexList-rXX`
  - type: `Msg1-RepetitionRootSequenceIndexList-rXX`

**Proposed new type (conceptual, new `_rXX`):**

- `Msg1-RepetitionRootSequenceIndexList-rXX ::= SEQUENCE (SIZE (1..8)) OF Msg1-RepetitionRootSequenceIndex-rXX`

**Proposed new element type (conceptual, new `_rXX`):**

- `Msg1-RepetitionRootSequenceIndex-rXX ::= CHOICE { l839 INTEGER(0..837), l139 INTEGER(0..137), l571 INTEGER(0..569), l1151 INTEGER(0..1149) }`

Rationale for duplicating the `CHOICE`:

- In the current ASN.1 we inspected, `prach-RootSequenceIndex` is an **inline** `CHOICE` inside `RACH-ConfigCommon` (i.e., it is not a standalone named type we can reference directly).
- Defining a new named type for it and refactoring existing fields to use it would be a larger, cross-cutting RRC change. The proposal above keeps the delta localized.

**Proposed placement (recommended):**

- Add this IE in `FeatureCombinationPreambles-r17`, inside the existing extension group that already contains the Msg1 repetition fields:
  - `msg1-RepetitionNum-r18`
  - `msg1-RepetitionTimeOffsetROGroup-r18`
  - `msg1-RepetitionRootSequenceIndexList_rXX`  ← new

In the merged `NR-RRC-Definitions.asn` we inspected, this is the relevant excerpt (existing Rel-18 fields shown, plus the proposed new `_rXX` field appended):

```asn1
FeatureCombinationPreambles-r17 ::= SEQUENCE {
    ...
    ...,
    [[
      msg1-RepetitionNum-r18               ENUMERATED {n2, n4, n8, spare1} OPTIONAL,
      msg1-RepetitionTimeOffsetROGroup-r18 ENUMERATED {n4, n8, n16, spare1} OPTIONAL,
      msg1-RepetitionRootSequenceIndexList-rXX Msg1-RepetitionRootSequenceIndexList-rXX OPTIONAL
    ]]
}
```

Compatibility note:

- Adding the new field **at the end of the extension group** minimizes churn in extension-addition ordering across releases.

**RRC-level constraints / normative rules (needed, because ASN.1 can’t express them fully):**

- If `msg1-RepetitionRootSequenceIndexList_rXX` is present:
  - `SIZE(list)` shall equal the configured Msg1 repetition count:
    - `n2` → size 2
    - `n4` → size 4
    - `n8` → size 8
- All entries shall use the same sequence-length family (`l839` or `l139`) and shall be consistent with the PRACH sequence length family used for the configured PRACH transmission on that cell.
- If `msg1-RepetitionRootSequenceIndexList_rXX` is absent, the UE behavior is unchanged (single configured `prach-RootSequenceIndex` applies to all repetitions).

**Example for Nrep=2:**

- `msg1-RepetitionNum-r18 = n2`
- `msg1-RepetitionRootSequenceIndexList_rXX = [ l839:1, l839:2 ]`

### 2.2.1 Backwards compatibility / UE capability gating (RRC impact)

This change is **not safe to “blindly configure”** for legacy UEs:

- A UE that does not understand the new IE would ignore it and still repeat with a single root sequence index.
- A gNB expecting root-hopping would then correlate/detect against the wrong sequences for repetitions.

Therefore the RRC impact must include **capability gating**. Typical options:

- Introduce a new UE capability bit/flag (new `_rXX` IE) indicating support for *Msg1 repetition root hopping*.
- Network shall only configure `msg1-RepetitionRootSequenceIndexList_rXX` if the UE has indicated support.

Where to carry the UE capability is a separate design choice (e.g., under `UE-NR-Capability` in an appropriate RACH/PRACH capability container). The key requirement is: **do not configure the new IE unless UE support is known**.

In the `NR-RRC-Definitions.asn` we have locally, there are already PRACH-related capability flags (e.g., `prach-Repetition-r18`, `prach-CoverageEnh-r18`) under the UE capability parameter trees. A pragmatic approach is to add a sibling flag such as:

- `msg1-RepetitionRootHoppingSupport_rXX  ENUMERATED {supported} OPTIONAL`

inside the same UE capability container that already hosts other PRACH capability flags, and specify:

- The network shall only configure `msg1-RepetitionRootSequenceIndexList_rXX` if the UE indicated `msg1-RepetitionRootHoppingSupport_rXX`.

### 2.2.2 Where this impacts actual RRC signalling (SIB1 + dedicated reconfiguration)

Because the Msg1 repetition knobs (`msg1-RepetitionNum-r18`, `msg1-RepetitionTimeOffsetROGroup-r18`) live in `FeatureCombinationPreambles-r17`, and `FeatureCombinationPreambles-r17` is referenced under `featureCombinationPreamblesList-r17` inside `RACH-ConfigCommon`, the new `_rXX` list has these practical consequences:

- **Initial access / SIB1 path:** the configuration can be broadcast as part of the common RACH configuration used for initial uplink BWP (via the `uplinkConfigCommon` chain where `rach-ConfigCommon` appears).
- **Connected mode updates:** the same configuration can be updated via dedicated RRC reconfiguration when the cell updates common configuration or applies dedicated common overlays.
- **Versioning/change control:** if the network changes the list, it is effectively changing the PRACH preamble generation rule for Msg1 repetitions; system information change handling needs to treat it like other `RACH-ConfigCommon` updates.

### 2.2.3 RRC behavioural contract (what the UE shall do with the new IE)

To make the change implementable (and interoperable), the RRC specification text needs to explicitly define:

- **Precedence:** if `msg1-RepetitionRootSequenceIndexList_rXX` is present, the UE shall use the list entries for Msg1 repetitions; otherwise the UE shall use the single `prach-RootSequenceIndex` configured in `RACH-ConfigCommon`.
- **Scope:** the list applies to the same Msg1 repetition configuration instance that provides `msg1-RepetitionNum-r18` / `msg1-RepetitionTimeOffsetROGroup-r18` (i.e., per `FeatureCombinationPreambles-r17` entry).
- **Invalid/mismatched configuration handling:** if `SIZE(list)` does not match `msg1-RepetitionNum-r18`, the UE behaviour should be specified (recommended: treat as “not configured” and fall back to `prach-RootSequenceIndex`, to avoid undefined behaviour).
- **Family consistency:** all list entries shall use the same root-length family (e.g., all `l839`, or all `l139`, or all `l571`, or all `l1151`); mixing families inside the list should be forbidden by normative text.

Note: there is also a `msg1-RepetitionNum-r18` that appears in the `CFRA` container (for CFRA repetition use). If root hopping is intended to apply to CFRA as well, the RRC spec needs either:

- an additional `msg1-RepetitionRootSequenceIndexList_rXX` field under `CFRA`, or
- explicit text that the list in `FeatureCombinationPreambles-r17` also applies when CFRA repetitions are used (less clean, because CFRA configuration is structurally separate).

This proposal uses the first approach (explicit CFRA field), to keep configuration self-contained and avoid cross-container coupling.

#### Proposed CFRA ASN.1 delta (conceptual, new `_rXX`)

In the current ASN.1 we compiled locally, `CFRA` has an extension group containing `msg1-RepetitionNum-r18`. Add the new field in the same extension group:

```asn1
CFRA ::= SEQUENCE {
  ...
  [[
    msg1-RepetitionNum-r18  ENUMERATED {n2, n4, n8, spare1} OPTIONAL,
    msg1-RepetitionRootSequenceIndexList-rXX  Msg1-RepetitionRootSequenceIndexList-rXX OPTIONAL
  ]]
}
```

Constraints (same intent as for `FeatureCombinationPreambles-r17`):

- If `msg1-RepetitionRootSequenceIndexList_rXX` is present in `CFRA`, `SIZE(list)` shall equal the configured `msg1-RepetitionNum-r18` value.
- If absent, the UE uses the configured `prach-RootSequenceIndex` (and other PRACH parameters) for all repetitions.

### 2.3 Normative changes in TS 38.213 §8.1 (“Random access preamble”)

TS 38.213 §8.1 already defines PRACH transmission and PRACH “preamble repetitions” (`N_preamble^rep > 1`) over a set of PRACH occasions/resources using the same spatial filter.

To support root-hopping, add text specifying:

#### (A) UE behavior: which root index is used per repetition

When the UE transmits PRACH with repetitions (`N_preamble^rep > 1`):

- If the higher layer parameter `msg1-RepetitionRootSequenceIndexList_rXX` is provided:
  - For repetition index `i` within the repetition set (0..`N_preamble^rep`-1), the UE shall generate the PRACH preamble using:
    - `rootSequenceIndex = msg1-RepetitionRootSequenceIndexList_rXX[i]`
  - All other PRACH parameters are unchanged from the configured PRACH transmission (format, SCS, PRACH resources, spatial filter, etc.).
- If the list is not configured:
  - behavior is unchanged (use the single configured `prach-RootSequenceIndex` for all repetitions).

#### (B) “Set” semantics

§8.1 defines a “set” of `N_preamble^rep` PRACH occasions for repeated PRACH. Clarify that:

- the repetition index `i` is counted within each set, in increasing time order of the PRACH occasions that form the set, and
- the per-repetition root selection repeats per set (if multiple sets exist in a time period).

#### (C) gNB interpretation / detectability

Add normative behavior that the gNB shall interpret repetitions as belonging to the same PRACH attempt even when the root sequence index differs across repetitions as configured, i.e.:

- the gNB correlates/combines the configured repetition set using the configured per-repetition roots.

### 2.3.1 Normative change in TS 38.213 §7.4 (“Physical random access channel”) — wording clarification

TS 38.213 §7.4 uses “preamble sequence transmitted” wording in power-ramping / RAR-not-received contexts. With per-repetition root hopping, a PRACH attempt with repetitions may include *multiple* preamble sequences (one per repetition). A small clarification is needed to avoid misinterpretation:

- For PRACH with repetitions, “preamble sequence transmitted” applies per repetition, while the attempt remains identified by the configured preamble index (RAPID) and repetition-set timing.

### 2.3.2 Normative change in TS 38.321 §5.1 (“Random Access procedure”) — MAC/PHY interface clarification

This feature is primarily **PHY-facing** (root sequence selection for PRACH sequence generation) and does not change the MAC random access state machine. However, TS 38.321 §5.1 is where “MAC instructs PHY to transmit PRACH” behavior is normatively defined, so a small clarification is needed for implementability:

- When Msg1 is transmitted with repetitions and `msg1-RepetitionRootSequenceIndexList-rXX` is configured, the UE MAC shall provide lower layers with the per-repetition root sequence index such that repetition *i* uses list entry *i* (with repetition index defined in TS 38.213 §8.1 set semantics).
- MAC procedure behavior remains unchanged: the attempt is still keyed by `PREAMBLE_INDEX` (RAPID), RA-RNTI and response window timing are based on PRACH occasion / repetition set semantics, and RAR matching still uses the transmitted `PREAMBLE_INDEX`.

### 2.4 Why Option 1 keeps RRC deltas small (but still needs cross-spec alignment)

Option 1 changes only *which root sequence index is used* per repetition, keeping:

- PRACH resources/occasion selection rules unchanged (still governed by the existing Msg1 repetition framework),
- PRACH preamble index unchanged (still one preamble index repeated),
- and the UE MAC random access state machine unchanged (still one RA attempt with repetitions).

However, the root sequence index directly impacts PRACH sequence generation and detection, so **38.213 text alone is not enough**: the “higher layer parameter” must be precisely defined in RRC (TS 38.331) and any PRACH sequence generation references (e.g., in 38.211) must allow “varying root across repetitions” when configured.

---

## 3) Important adjacent spec touchpoints (beyond 38.213 + RRC)

Even if you place configuration in RRC and procedure text in 38.213, this feature also likely needs updates elsewhere:

- **TS 38.211 (PRACH sequence generation):** to define sequence generation when root sequence index varies across repetitions.
- **TS 38.321 (MAC random access):** to clarify this is still one RA attempt (same RA-RNTI/procedure) and how HARQ/RA state treats repetition sets when roots differ.

In practice, the impact on TS 38.321 §5.1 is expected to be **clarification-only** (MAC continues to key off `PREAMBLE_INDEX`, repetition-set timing, and RA-RNTI/response window semantics).

---

## 4) Next steps (implementation-oriented)

1) Draft an exact `NR-RRC-Definitions` ASN.1 delta (new field addition and constraints).
2) Draft the normative 38.213 §8.1 text that:
   - defines the repetition index,
   - binds repetition `i` to root list entry `i`,
   - and clarifies gNB/UE expectations.
3) Decide whether to:
   - allow *only* root changes, or
   - allow a broader per-repetition “preamble recipe” (root + cyclic shift/preamble index), which would require more invasive changes.

---

## Appendix A) Suggested field descriptions (for `*_asn_field_description.json`)

Your field description JSONs appear to key many fields without the `-rNN` suffix (e.g., `msg1-RepetitionNum`, `msg1-RepetitionTimeOffsetROGroup`). The following suggested keys mirror that style.

- `msg1-RepetitionRootSequenceIndexList`:
  - “Indicates the PRACH root sequence index to be used for each MSG1 repetition within a repetition set (see TS 38.213). If present, for repetition index *i* (0..Nrep−1) the UE shall use the *i*-th entry of this list as the root sequence index for PRACH preamble generation, while all other PRACH parameters (e.g., PRACH format/resources) remain as configured. If absent, the UE uses `prach-RootSequenceIndex` for all repetitions. The list size shall match the configured MSG1 repetition number. This field may be provided in `FeatureCombinationPreambles` and/or `CFRA`.”

- `msg1-RepetitionRootHoppingSupport`:
  - “If present, indicates that the UE supports configuration of different PRACH root sequence indexes across MSG1 repetitions using `msg1-RepetitionRootSequenceIndexList`.”
