# TS 38.331 (RRC) impact assessment + proposed changes (draft)

Goal: enable the UE to perform:
- Msg1-1 using a “primary” PRACH configuration (e.g., long PRACH), then
- if MAC receives a **Type-2 MAC RAR** (38.321), transmit Msg1-2 using a **secondary** PRACH configuration (e.g., short PRACH),
without signalling PRACH format/numerology in the Type-2 MAC RAR (RAR carries only time/freq pre-comp).

## Where the current RACH config comes from (SIB1 path)

In NR-RRC ASN.1, `RACH-ConfigCommon` is broadcast via `SIB1` under:

- `SIB1 -> servingCellConfigCommon -> uplinkConfigCommon -> initialUplinkBWP -> rach-ConfigCommon`
- (also via supplementary uplink and RedCap variants)

This is confirmed by `asntools-rrc-tree RACH-ConfigCommon --root SIB1`.

Spec excerpts backing the above path are extracted under:
- `artifacts/spec_sections/38331-i60__sib1.md`
- `artifacts/spec_sections/38331-i60__servingcellconfigcommonsib.md`
- `artifacts/spec_sections/38331-i60__uplinkconfigcommonsib.md`
- `artifacts/spec_sections/38331-i60__bwp-uplinkcommon.md`

See `docs/ra_type2_rar_prach_switch/spec_extracts_38331.md` for regeneration commands.

## What 38.331 must provide for this feature

Because the Type-2 MAC RAR does **not** carry PRACH format/config (only time/freq pre-comp), RRC must pre-configure:

1. a “primary” PRACH configuration for Msg1-1 (already done via existing `RACH-ConfigCommon`), and
2. a **secondary PRACH configuration** for Msg1-2 (new).

The secondary configuration must be sufficient to derive:
- PRACH occasions (time/frequency resources) for Msg1-2,
- the PRACH preamble generation parameters consistent with the chosen PRACH format (sequence length, root index, Ncs/restricted set, etc).

Clarification: Msg1-2 is contention-free in the sense that the UE does **not** re-select a preamble index; it reuses the `RAPID`/preamble index confirmed by the Type-2 MAC RAR for Msg1-1. Because Msg1-2 uses a different PRACH configuration, the actual PRACH sequence transmitted for the same preamble index is different, and the network must know the Msg1-2 PRACH configuration via RRC.

## Notes from existing field descriptions (sanity checks)

Based on `asntools --describe-ie RACH-ConfigCommon` and `asntools --describe-ie RACH-ConfigGeneric`:

- `RACH-ConfigGeneric.prach-ConfigurationIndex` drives PRACH configuration (and, by implication, PRACH format tables in TS 38.211).
- `RACH-ConfigCommon.msg1-SubcarrierSpacing` can be absent, in which case SCS is derived from `prach-ConfigurationIndex`.
- `RACH-ConfigCommon.prach-RootSequenceIndex` explicitly ties to sequence length choices (L=839/L=139/...), and its consistency with PRACH configuration is called out.

Implication: for Msg1-2 to use a different PRACH “shape” (long vs short, different numerology), it is safer for RRC to provide a **secondary full PRACH configuration context** (not only a second `prach-ConfigurationIndex`), but we do **not** need to mandate that any particular sequence length (e.g., l139) is supported; it is entirely configuration-driven.

The `asntools` description outputs used for these sanity checks are saved under:
- `artifacts/asntools_describe/RACH-ConfigCommon.txt`
- `artifacts/asntools_describe/RACH-ConfigGeneric.txt`
- `artifacts/asntools_describe/BWP-UplinkCommon.txt`

## Proposed ASN.1/IE approach (conceptual)

### Option A (recommended): add a dedicated optional container under `RACH-ConfigCommon` extensions

Add a new optional extension field to `RACH-ConfigCommon` (and likely also to `RACH-ConfigCommon` variants in AdditionalRACH):

`type2RarMsg1-2-Config-rXX` ::= `SEQUENCE { ... }` (placeholder name)

with fields:

- `rach-ConfigGeneric-Msg1-2-rXX` : `RACH-ConfigGeneric`
  - carries `prach-ConfigurationIndex` etc (drives PRACH format/resources per 38.211 tables)
  - carries `msg1-FDM`, `msg1-FrequencyStart`, `zeroCorrelationZoneConfig`, `preambleTransMax`, `powerRampingStep`, `ra-ResponseWindow`
- `prach-RootSequenceIndex-Msg1-2-rXX` : `CHOICE { l839, l139, ... }`
- `msg1-SubcarrierSpacing-Msg1-2-rXX` : `SubcarrierSpacing` (conditional like existing `msg1-SubcarrierSpacing` when `l139`)
- `restrictedSetConfig-Msg1-2-rXX` : `ENUMERATED {unrestrictedSet, restrictedSetTypeA, restrictedSetTypeB}`

Optionally (only if needed):
- `ssb-perRACH-OccasionAndCB-PreamblesPerSSB-Msg1-2-rXX` (if Msg1-2 needs a different SSB↔RO mapping than Msg1-1)

Semantics text to add in 38.331:
- If `type2RarMsg1-2-Config-rXX` is present, the UE shall use it to determine Msg1-2 PRACH resources when instructed by MAC via reception of Type-2 MAC RAR (38.321 changes).
- Msg1-2 uses the same preamble id/RAPID as Msg1-1 (per your clarification), but PRACH format/resources come from the secondary config; therefore, the UE does not perform contention-based preamble selection for Msg1-2.

Marked (patch-style) excerpt draft for this option is in:
- `docs/ra_type2_rar_prach_switch/ts38331_marked_excerpts.md`

### Precedent / alignment notes

- `RACH-ConfigCommon` already carries PRACH parameters split between `rach-ConfigGeneric` and additional top-level fields like `prach-RootSequenceIndex`, `msg1-SubcarrierSpacing`, and `restrictedSetConfig`. This motivates a *container* for Msg1-2 rather than only a second `prach-ConfigurationIndex`.
- `RACH-ConfigTwoTA-r18` (see `artifacts/spec_sections/38331-i60__rach-configtwota.md`) is an example of bundling `RACH-ConfigGeneric` with root-sequence and related PRACH context inside a dedicated IE. The proposed Msg1-2 container follows the same general pattern, but without the “per additional PCI” aspect.

### Option B: reuse `additionalRACH-ConfigList-r17` (not preferred)

`BWP-UplinkCommon` already has `additionalRACH-ConfigList-r17` containing extra `rach-ConfigCommon-r17` entries, but the semantics are “additional RACH configs” tied to feature selection in 38.321.

We could map the Msg1-2 PRACH resources as an “additional” config, but we still need:
- explicit sequential semantics (Msg1-1 then Msg1-2 upon Type-2 RAR), and
- reuse of preamble id/RAPID across the two configs.

That makes Option B awkward and likely to cause ambiguity in 38.321 resource-selection rules.

## Capability / applicability considerations

Likely needed (not drafted yet):
- a UE capability bit indicating support for “Type-2 MAC RAR triggered Msg1-2 PRACH with pre-comp” (especially for NTN).
- applicability gating: only configure this in NTN cells (or only when `ntn-Config` indicates relevant scenarios).

## Open RRC questions (drive the final IE shape)

- Does Msg1-2 need independent `prach-RootSequenceIndex` / sequence-length selection (l839 vs l139) from Msg1-1?
  - If yes, the secondary config must include root sequence + restricted set parameters as above (not only `RACH-ConfigGeneric`).
- Does SSB selection for Msg1-2 follow Msg1-1 SSB strictly, or can it change? (keeping it fixed is simpler and matches “same RAPID” intuition).
- Is the feature only for SIB1/common config, or also for dedicated RA (e.g., reconfigurationWithSync / resume)? If the latter, we may need a corresponding container under relevant dedicated config paths too.
