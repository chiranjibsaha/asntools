# Next Steps

## 38.321 (MAC)

- Decide the exact mechanism for **Type-2 RAR** definition (new RAR payload vs new MAC CE).
- Specify normative behaviour for:
  - Msg1-2 resource selection (PRACH occasion, format, preamble index)
  - response window(s) and RA-RNTI handling for Msg1-2
  - counters and power ramping across Msg1-1 → Type-2 RAR → Msg1-2
  - failure handling if the second RAR is not received
- Capture clause-by-clause deltas in `docs/ra_type2_rar_prach_switch/ts38321_detailed_changes.md`.

## 38.331 (RRC)

- Identify where the UE gets configuration for:
  - "Msg1-1 uses long PRACH format"
  - "Msg1-2 uses short PRACH format"
  - any mapping/indexing needed to allow the gNB to reference the Msg1-2 resources in Type-2 RAR

## 38.213 / 38.211 (PHY / PRACH)

- Confirm assumptions around:
  - PRACH occasion timing constraints for Msg1-2 relative to Type-2 RAR reception
  - how time/frequency pre-compensation is applied for PRACH
  - any impact on PRACH occasion mapping / association rules
- Capture minimal 38.213 deltas in `docs/ra_type2_rar_prach_switch/ts38213_deltas.md`.

## 38.300 (overview)

- Update RA overview to describe “4-step RA with PRACH refinement (Type-2 RAR → Msg1-2)” without introducing a new RA type.
- Draft is in `docs/ra_type2_rar_prach_switch/ts38300_deltas.md` and `docs/ra_type2_rar_prach_switch/ts38300_marked_excerpts.md`.
