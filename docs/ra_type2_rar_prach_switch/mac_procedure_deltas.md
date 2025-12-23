# TS 38.321 MAC Procedure Deltas (Draft)

## Baseline reference points (existing 38.321)

- **5.1.3 Random Access Preamble transmission**: MAC selects PRACH occasion/preamble and commands PHY transmit; computes `RA-RNTI`.
- **5.1.4 Random Access Response reception**: MAC starts `ra-ResponseWindow`, monitors `RA-RNTI`, and on successful RAR reception processes TA + UL grant, sets `TEMPORARY_C-RNTI`, builds `Msg3`, etc.
- **6.1.5 MAC PDU (Random Access Response)**: RAR subPDU structure (BI, RAPID-only, RAPID+RAR).

## Proposal summary (new behaviour)

We introduce a **new RAR variant** (placeholder name: **Type-2 RAR**) that, when received in response to an initial `Msg1` PRACH transmission (e.g., long PRACH), instructs the UE to transmit **another `Msg1` PRACH** (e.g., short PRACH) with **time/frequency pre-compensation**.

Primary target (as currently clarified): a **two-PRACH** enhancement within one Random Access attempt:
- `Msg1-1` (e.g., long PRACH) → receive **Type-2 RAR** (time/freq pre-comp only) → `Msg1-2` (e.g., short PRACH using pre-comp) → receive **regular RAR** (with TA + UL grant + TC-RNTI) → `Msg3` → contention resolution.

After successful decoding of a RAR corresponding to the transmitted `PREAMBLE_INDEX`, if the decoded subPDU is a **Type-2 RAR** (definition TBD), MAC shall:

1. Store the signalled **time** and **frequency** pre-compensation parameters.
2. Trigger transmission of `Msg1-2` using a different PRACH preamble format (e.g., short PRACH), applying the signalled pre-compensation.
   - `Msg1-2` is contention-free in the sense that the UE does **not** select a preamble again; it reuses the `RAPID`/preamble index confirmed by the Type-2 RAR for Msg1-1. (The PRACH sequence differs because the PRACH configuration differs.)
3. Start monitoring for the **subsequent regular RAR** corresponding to Msg1-2, then continue with baseline 4-step behaviour (TA + UL grant processing, `TEMPORARY_C-RNTI`, `Msg3`, contention resolution).

Note on naming: this is a *RAR type* ("Type-2 RAR"), not the existing "2-step RA type" / "Type-2 random access procedure" terminology used elsewhere in NR.

## Candidate insertion points in 38.321 text (where deltas likely go)

### 5.1.4 Random Access Response reception

Baseline excerpt anchor from `randomaccess.txt`:
- After "consider this Random Access Response reception successful."
- Before "process the received Timing Advance Command …" and the subsequent UL grant / `TEMPORARY_C-RNTI` handling.

Add a new branch to handle the Type-2 RAR case, conceptually:

- If the successfully received RAR subPDU is a Type-2 RAR:
  - Extract and store time/frequency pre-compensation.
  - Determine the resources for Msg1-2 (PRACH occasion + preamble format + possibly a (re)selected `PREAMBLE_INDEX`) based on Type-2 RAR signalling and/or pre-configured RACH resources.
  - Compute `RA-RNTI` for Msg1-2 PRACH occasion (baseline `RA-RNTI` formula still applies).
  - Command PHY to transmit Msg1-2 with the additional pre-compensation parameters.
  - (Re)start a response window and monitor for a subsequent RAR corresponding to Msg1-2.
  - Do **not** yet perform the baseline "process TA / UL grant / set `TEMPORARY_C-RNTI` / build Msg3" actions until the subsequent RAR is successfully received.

### 5.1.3 Random Access Preamble transmission

Baseline excerpt anchor from `randomaccess.txt`:
- "instruct the physical layer to transmit the Random Access Preamble using the selected PRACH occasion, corresponding RA-RNTI (if available), PREAMBLE_INDEX, and PREAMBLE_RECEIVED_TARGET_POWER."

Extend the PHY command interface to support an additional, optional tuple:
- `prach_time_precomp` (from Type-2 RAR)
- `prach_freq_precomp` (from Type-2 RAR)

and specify that these parameters are applied **only** for Msg1-2 transmissions triggered by Type-2 RAR.

## Draft normative deltas (high level; wording to refine once fields exist)

For a marked-up clause draft with explicit insertion markers, see `ts38321_marked_excerpts.md`.

Spec extraction inputs used for 38.321 are listed in `spec_extracts_38321.md` (generated under `artifacts/spec_sections/`).

### Proposed pseudocode insertion in 5.1.4 (conceptual)

Insert after existing success detection:

- "if the Random Access Response contains a MAC subPDU with Random Access Preamble identifier corresponding to the transmitted `PREAMBLE_INDEX` … consider this Random Access Response reception successful."

and before existing baseline actions (TA/grant/TC-RNTI/Msg3 buffer):

1. If the successfully received RAR subPDU is a Type-2 RAR:
   - store `PRACH_TIME_PRECOMP` and `PRACH_FREQ_PRECOMP` from the Type-2 RAR (units TBD; octet-aligned for now);
   - use the same `RAPID`/preamble id as Msg1-1 (Type-2 RAR carries this RAPID);
   - determine Msg1-2 PRACH occasion and PRACH preamble format from a separate RRC-configured PRACH configuration (e.g., a "second RACH-ConfigGeneric"), not from Type-2 RAR;
   - compute `RA-RNTI` for the Msg1-2 PRACH occasion;
   - instruct PHY to transmit Msg1-2 with the signalled pre-compensation;
   - start (or restart) the response window and monitor for a subsequent RAR addressed to the Msg1-2 `RA-RNTI`;
   - upon successful reception of the subsequent (regular) RAR corresponding to Msg1-2, continue with the baseline TA/grant/`TEMPORARY_C-RNTI`/Msg3 behaviour.

Clarification: Type-2 RAR omits `TC-RNTI`; `TC-RNTI` is provided by the subsequent regular RAR (step 4 in the proposed 6-step flow).

### New state within the Random Access procedure

Introduce a new internal state (name TBD) equivalent to:
- `WAIT_RAR_FOR_MSG1_2` (after receiving Type-2 RAR and transmitting Msg1-2)

so that:
- The Random Access procedure remains a *single* ongoing procedure (consistent with 5.1.1.1).
- The UE does not allocate `TEMPORARY_C-RNTI` or build `Msg3` until it receives the subsequent regular RAR for Msg1-2.

### Response window handling

Specify whether:
- `ra-ResponseWindow` is restarted for Msg1-2 at the first PDCCH occasion from the end of Msg1-2 PRACH transmission (reusing the same timer name), or
- a separate window/timer is introduced for Msg1-2.

### Success/failure accounting

Clarify whether reception of Type-2 RAR:
- counts as "Random Access Response reception successful" for the purpose of stopping the first window and avoiding backoff, and
- how failure to receive the second RAR is handled (retry Msg1? retry Msg1-2? go to backoff?).

## Key MAC-level questions to resolve (needed to write exact normative text)

- **State machine**: is the second Msg1 a new step within the same Random Access procedure instance (same "ongoing RA")?
- **Counters/timers**:
  - Does `PREAMBLE_TRANSMISSION_COUNTER` increment for `Msg1-2`?
  - Is power ramping applied again for `Msg1-2` (same ramp counter or separate)?
  - Is `ra-ResponseWindow` restarted for the second preamble, or is a new window defined?
- **RNTIs**:
  - Is the second preamble monitored with a newly computed `RA-RNTI` (based on its PRACH occasion), while staying within the same procedure context?
- **Backoff / failure handling**:
  - If Type-2 RAR is received but the second RAR is not, is the attempt considered "RAR not successful" vs a new failure cause?
- **CFRA vs CBRA**:
  - Is Type-2 RAR applicable only to CBRA, or also to CFRA cases?

These are tracked in `open_questions.md`.
