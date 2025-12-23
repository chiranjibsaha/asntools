# Open Questions (Type-2 RAR Triggered Second Msg1)

## Type-2 RAR definition (38.321)

- Avoid terminology collision with existing NR "Type-2 random access procedure" (= 2-step RA with MsgA/MsgB in 38.213/38.321). Here "Type-2 RAR" is a new **RAR payload type** name placeholder.

- Where is Type-2 RAR defined: as a new RAR payload type under 6.1.5, or as a new MAC CE, or by reusing the existing RAR with a new `T` value?
- What are the exact field encodings and semantics?
  - time pre-compensation: **present** (units/range TBD; octet-aligned for now)
  - frequency pre-compensation: **present** (units/range TBD; octet-aligned for now)
  - `TC-RNTI`: **absent** in Type-2 RAR (provided later in the subsequent regular RAR)
  - `RAPID`: **present** and equals the RAPID used for the first Msg1; UE uses the **same RAPID/preamble id** for Msg1-2
  - PRACH format for Msg1-2: **not signalled in Type-2 RAR**; UE derives it from a separate configured PRACH configuration (e.g., a "second RACH-ConfigGeneric")
  - 38.321 §6.2.3 says the existing MAC RAR payload is **fixed size** and contains (R/TI), TA command, UL grant, and TC-RNTI; Type-2 MAC RAR therefore needs either:
    - an in-band type discrimination while keeping the same fixed-size payload, or
    - a new subPDU/subheader format in the Random Access Response MAC PDU.

## MAC behaviour / procedure

- **Resolved (clarification):** `Msg1-2` is *contention-free* in the sense that the UE does **not** (re-)select a preamble; it reuses the same `RAPID`/preamble index confirmed by the Type-2 RAR. Note: this does not necessarily mean the overall Random Access procedure becomes the existing NR CFRA procedure; contention resolution may still apply later depending on the subsequent regular RAR / Msg3 flow.
- Does the UE apply TA from the first RAR immediately, or only use it to derive the pre-comp?
- Does the UE compute a new `RA-RNTI` for Msg1-2 from the Msg1-2 PRACH occasion (baseline formula), and does the gNB address the subsequent RAR using that new `RA-RNTI`?
- How does the UE select the first available Msg1-2 RO? Clarification: UE derives the next RO from the **second PRACH format configuration** (per 38.213); timing reference is the subframe used to carry the RAR (exact 38.321 hooks TBD).
- If multiple Msg1 transmissions are allowed in one attempt, what is the **maximum** and where is it configured (RRC vs hardcoded)?
- Clarification: UE reuses the same `RAPID`/preamble id across Msg1-1 and Msg1-2.
- What happens if UE receives:
  - multiple RAR subPDUs matching its `PREAMBLE_INDEX` in the same window?
  - a legacy RAR (normal) when it expected a Type-2 RAR?
- Does reception of Type-2 RAR count as "RAR reception successful" for purposes of backoff?

## Interaction with later steps

- Clarification: `TEMPORARY_C-RNTI` (TC-RNTI) is provided by the **subsequent regular RAR** (step 4 in the proposed 6-step), not by Type-2 RAR.
- Which UL grant schedules `Msg3` (subsequent regular RAR only)?
- Are time/frequency corrections applied to Msg3 in addition to Msg1-2 (proposal suggests yes)?

## Cross-spec impacts (deferred)

- 38.331: how to configure a secondary PRACH configuration for Msg1-2 (likely via a new optional container under `RACH-ConfigCommon`), and whether it needs independent root sequence length (l839 vs l139).
- 38.213: PRACH occasion mapping / RA-RNTI timing for the second preamble and any new pre-comp processing assumptions.





## User Clarification (round 1) (captured above)

- Type-2 RAR carries only time/frequency pre-compensation (octet-aligned for now; units TBD).
- Type-2 RAR includes RAPID for Msg1-1; UE reuses the same RAPID/preamble id for Msg1-2, but uses a different PRACH format/config (e.g., a second RACH-ConfigGeneric).
- Msg1-2 RO is derived from the second PRACH format/config per 38.213, with timing reference relative to the subframe carrying the RAR (exact 38.321 text hooks TBD).
- Type-2 RAR omits TC-RNTI; TC-RNTI is provided by the subsequent regular RAR (step 4 in the proposed 6-step).
