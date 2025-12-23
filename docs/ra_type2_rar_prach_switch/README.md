# Type-2 RAR Triggered Second Msg1 (Design Notes)

This folder is for working notes on a proposed Random Access enhancement (motivated by GNSS-resilient NR-NTN access):

1. UE transmits `Msg1` using a long PRACH format.
2. UE receives a Random Access Response (RAR).
3. If the RAR is a **new Type-2 RAR** (proposal), UE transmits **Msg1-2** using a different PRACH format/config (e.g., short PRACH from a second RACH config), applying **time/frequency pre-compensation** values signalled in the Type-2 RAR (Type-2 RAR does not carry `TC-RNTI`).
4. UE receives a (regular) RAR for Msg1-2 (with TA + UL grant + `TC-RNTI`), then transmits `Msg3` and continues with contention resolution (baseline 4-step flow).

Inputs used:
- `randomaccess.txt` (TS 38.321 excerpts)
- `random_access_38300.txt` (TS 38.300 context)
- `RAProc38213.txt` (TS 38.213 excerpts, deferred)
- `proposal.txt` (high-level problem statement + proposed multi-step PRACH idea)

Next: capture the required MAC procedure deltas in `mac_procedure_deltas.md`.

Working set:
- `docs/ra_type2_rar_prach_switch/mac_procedure_deltas.md`
- `docs/ra_type2_rar_prach_switch/open_questions.md`
- `docs/ra_type2_rar_prach_switch/next_steps.md`
- `docs/ra_type2_rar_prach_switch/proposal_notes.md`
- `docs/ra_type2_rar_prach_switch/ts38321_detailed_changes.md`
- `docs/ra_type2_rar_prach_switch/ts38321_marked_excerpts.md`
- `docs/ra_type2_rar_prach_switch/ts38213_deltas.md`
- `docs/ra_type2_rar_prach_switch/ts38331_deltas.md`
- `docs/ra_type2_rar_prach_switch/ts38331_marked_excerpts.md`
- `docs/ra_type2_rar_prach_switch/ts38300_deltas.md`
- `docs/ra_type2_rar_prach_switch/ts38300_marked_excerpts.md`
- `docs/ra_type2_rar_prach_switch/spec_extracts_38321.md`
- `docs/ra_type2_rar_prach_switch/spec_extracts_38331.md`
