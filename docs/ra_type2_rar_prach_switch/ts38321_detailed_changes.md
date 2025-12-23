# TS 38.321 detailed changes (draft, procedure-level)

This document expands `mac_procedure_deltas.md` into clause-by-clause deltas for the **6-step PRACH enhancement**:

- Msg1-1 (long PRACH) → RAR(Type-2) carrying only time/freq pre-comp → Msg1-2 (short PRACH, same RAPID) → regular RAR (TA + UL grant + TC-RNTI) → Msg3 → contention resolution.

The exact Type-2 MAC RAR bitfield encoding is TBD; the changes below focus on MAC procedure behaviour.

However, the extracted spec text in `artifacts/spec_sections/38321-j00__6-2-3-mac-payload-for-random-access-response.md` states that the regular MAC RAR payload is **fixed size**, which constrains how Type-2 MAC RAR can be introduced (either fixed-size reinterpretation with a discriminator, or a new subPDU/subheader format).

For a marked-up “patch-style” draft with insertion markers, see `ts38321_marked_excerpts.md`.

## 5.1.1 Random Access procedure initialization

### New internal state/variables (UE implementation variables, but need normative behaviour)

Add the following conceptual variables, initialized when a Random Access procedure is initiated:

- `TYPE2_RAR_PRECOMP_TIME` = 0 (or "not set")
- `TYPE2_RAR_PRECOMP_FREQ` = 0 (or "not set")
- `WAITING_FOR_MSG1_2_RAR` = false
- `MSG1_2_CONFIG_SELECTED` = false (indicates whether the UE has selected the secondary PRACH configuration)

Rationale: 5.1.4 needs to branch on whether a Type-2 RAR was received and whether Msg1-2 is pending.

### No change to "only one RA procedure ongoing"

Keep the existing rule ("There is only one Random Access procedure ongoing at any point in time in a MAC entity.").
Msg1-2 is a continuation *within* the same Random Access procedure.

## 5.1.2 Random Access Resource selection (4-step RA)

Add a new branch for selecting resources for Msg1-2:

- If `WAITING_FOR_MSG1_2_RAR = false`: perform baseline selection (Msg1-1) as today.
- If `WAITING_FOR_MSG1_2_RAR = true`: select resources for Msg1-2 as follows:
  - keep `PREAMBLE_INDEX` unchanged (reuse the same RAPID/preamble id as Msg1-1);
  - keep the same selected SSB/CSI-RS association as Msg1-1 (unless explicitly re-selected by higher layer config; TBD);
  - determine PRACH occasion(s) using a **secondary PRACH configuration** (placeholder: "second RACH-ConfigGeneric") configured by RRC;
  - determine the next available PRACH occasion for Msg1-2 (per TS 38.213 selection rules), with the selection occurring after reception of the Type-2 RAR (so the reference time is effectively the subframe carrying the RAR; see user clarification).

Open item: the exact RRC hook for the secondary PRACH configuration is deferred to 38.331 impact analysis.

## 5.1.3 Random Access Preamble transmission

Extend the MAC→PHY instruction to optionally include Type-2 RAR pre-compensation parameters:

- If `WAITING_FOR_MSG1_2_RAR = true`, the MAC entity shall instruct PHY to transmit Msg1-2 using:
  - the selected PRACH occasion (from the secondary PRACH configuration),
  - the same `PREAMBLE_INDEX` as Msg1-1,
  - `TYPE2_RAR_PRECOMP_TIME` and `TYPE2_RAR_PRECOMP_FREQ`,
  - the computed `RA-RNTI` for the Msg1-2 PRACH occasion (baseline formula still applies).

Power ramping and counters:

- Baseline 5.1.3 increments `PREAMBLE_POWER_RAMPING_COUNTER` depending on retransmission conditions.
- Clarify whether Msg1-2 is treated as:
  - a new "Random Access Preamble" within the same attempt (thus may increment counters), or
  - a special "follow-up preamble" where power ramping is not incremented (TBD).

## 5.1.4 Random Access Response reception

### New Type-2 RAR handling branch

In the branch where a valid DL assignment for `RA-RNTI` is decoded and the RAR contains a matching RAPID (baseline: "consider this Random Access Response reception successful"):

Add:

1. If the matching subPDU is a **Type-2 RAR**:
   - extract and store `TYPE2_RAR_PRECOMP_TIME` and `TYPE2_RAR_PRECOMP_FREQ` (octet-aligned for now; units TBD);
   - do **not** process TA command;
   - do **not** process UL grant;
   - do **not** set `TEMPORARY_C-RNTI` (TC-RNTI is absent in Type-2 RAR by clarification);
   - set `WAITING_FOR_MSG1_2_RAR = true`;
   - select resources for Msg1-2 (invoke the 5.1.2 selection branch for Msg1-2);
   - transmit Msg1-2 (invoke 5.1.3 with pre-compensation);
   - restart (or start) the `ra-ResponseWindow` relative to Msg1-2 transmission and monitor for the subsequent regular RAR addressed to the Msg1-2 `RA-RNTI`.

2. Else (baseline, regular RAR):
   - keep existing behaviour: process TA, process UL grant, set `TEMPORARY_C-RNTI`, store Msg3 buffer, etc.

### Failure handling when waiting for RAR of Msg1-2

When the `ra-ResponseWindow` expires without receiving a matching RAR for Msg1-2:
- apply baseline "RAR reception not successful" behaviour (increment counters, backoff, retry) **but** clarify whether the retry restarts from Msg1-1 (long PRACH) and clears `WAITING_FOR_MSG1_2_RAR` and stored pre-comp values.

User proposal direction suggests: "if no RAR for most recent preamble, declare attempt failure and do not transmit any more Msg1 in the same attempt"; mapping this onto existing `preambleTransMax` / retry logic is TBD.

## 6.1.5 MAC PDU (Random Access Response)

The provided excerpt covers the MAC PDU structure and subheaders but does not include the MAC RAR payload field layout. For Type-2 RAR, 38.321 needs to define:

- how the receiver distinguishes Type-2 RAR from regular RAR (fixed length + type indicator vs new subPDU type), and
- the Type-2 RAR payload fields (time/freq pre-comp) and their encoding.

Minimum agreed semantics (from user clarification):

- Type-2 RAR carries only time/frequency pre-compensation.
- Type-2 RAR includes the RAPID for Msg1-1 (via the normal RAPID subheader) and the UE reuses the same RAPID for Msg1-2.
- Type-2 RAR omits TC-RNTI; TC-RNTI is delivered in the subsequent regular RAR.
