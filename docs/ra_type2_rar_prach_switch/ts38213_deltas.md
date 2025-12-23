# TS 38.213 impact assessment (RAProc38213.txt)

## Summary

Your impression is mostly right: **38.213 changes can likely be minimal**, because the proposal keeps the PHY Random Access procedure as **Type-1 RA** (PRACH-only) and does not change Msg3/PUSCH scheduling rules; it adds a *new higher-layer behaviour* that triggers a **second PRACH (Msg1-2)** with **time/frequency pre-compensation** after receiving a **Type-2 MAC RAR** in 38.321.

The main 38.213 edits are likely:

1. Extend the *higher layers → L1 PRACH transmission configuration* to include **optional PRACH time/frequency pre-compensation parameters** (for Msg1-2 only).
2. Add (or reference) a **timing requirement** for how quickly L1 must be ready to transmit Msg1-2 after receiving the Type-2 RAR (similar in style to existing “ready to transmit PRACH no later than …” text that exists for other RA transitions).
3. Clarify terminology to avoid confusion with existing **Type-2 L1 random access procedure** (MsgA/MsgB); our “Type-2 RAR” is a MAC-layer RAR type, not the L1 Type-2 RA procedure.

## Candidate clause touchpoints (from RAProc38213.txt)

### Clause 8 (Random access procedure) / 8.1 (Random access preamble)

RAProc38213.txt already says higher layers provide, for a PRACH transmission:
- PRACH transmission parameters (format/time/frequency resources),
- preamble index, preamble SCS, `P_(PRACH,target)`, corresponding `RA-RNTI` (when applicable), and PRACH resource,
- number of PRACH repetitions (if any).

**Likely addition:**
- optional `PRACH_TIME_PRECOMP` and `PRACH_FREQ_PRECOMP` provided by higher layers for a PRACH transmission (Msg1-2).

This can be framed as:
- “When instructed by higher layers for a PRACH transmission, Layer 1 may additionally receive time/frequency pre-compensation to apply for the PRACH transmission.”

### Timing for Msg1-2 after Type-2 RAR

RAProc38213.txt contains timing-style requirements for being ready to transmit PRACH after certain windows/decodes (the excerpt includes a “ready to transmit a PRACH no later than …” requirement in the 2-step RA context).

**Likely minimal addition:**
- a similar readiness requirement for Msg1-2 PRACH following reception of a Type-2 MAC RAR (exact deadline TBD; depends on your intended RAR→PRACH spacing and UE processing assumptions).

### Clauses 8.3/8.4 (PUSCH via RAR UL grant, contention resolution)

These clauses are **mostly unaffected** because:
- Type-2 MAC RAR does **not** carry UL grant or `TC-RNTI` (by your clarification),
- Msg3 UL grant and `TC-RNTI` come from the subsequent **regular** RAR (step 4), so existing Msg3 timing/scrambling rules remain intact.

Possible editorial clarification only:
- ensure wording doesn’t imply that *every* RAR reception leads to a RAR UL grant / `TC-RNTI` availability.

## What I would *not* change in 38.213 (based on current scope)

- No change to the definition of **Type-1** vs **Type-2** L1 random access procedures (keep existing Msg1/MsgA split).
- No change to Msg3 PUSCH timing (`n+k2+Δ+…`) and `TC-RNTI` scrambling rules, since those apply once the regular RAR is received.

## Open items that might force more than “minimal” changes

- If you need 38.213 to normatively define **how pre-comp is applied to PRACH** (beyond “provided by higher layers”), that may spill into 38.211/38.214 or require explicit PHY behaviour text here.
- If Msg1-2 can use a different numerology/format than Msg1-1, 38.213 may need to clarify how “configuration for PRACH transmission” is switched between the two within a single RA attempt (likely still “higher layers provide configuration,” so minimal).

