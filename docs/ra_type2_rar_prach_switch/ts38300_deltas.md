# TS 38.300 impact assessment (Random Access overview)

## Scope

38.300 is descriptive (architecture/overview), so changes should be **high level**:
- describe the new behaviour at the “procedure” level, and
- avoid MAC bitfield details (38.321) and PRACH mapping specifics (38.213/38.211).

## What changes in the 38.300 RA description

The current overview says:
- “Two types of random access procedure are supported: 4-step RA type with MSG1 and 2-step RA type with MSGA.”
- For 4-step RA: MSG1(PRACH) → RAR → MSG3 → contention resolution.

With the new enhancement, we do **not** introduce a third RA type; instead we extend the **4-step RA type** with an optional PRACH refinement step:

- After the initial MSG1 (PRACH), the gNB may respond with a **Type-2 Random Access Response** (Type-2 RAR, proposal).
- Upon receiving the Type-2 RAR, the UE transmits **another PRACH preamble (Msg1-2)** using a different preamble format/config (e.g., short PRACH), applying time/frequency pre-compensation signalled in the Type-2 RAR.
- The gNB then transmits a (regular) RAR to schedule Msg3 and provide TC-RNTI, and the procedure continues as baseline.

This is consistent with:
- keeping the “MsgA/MsgB 2-step RA type” unchanged, and
- framing the feature as a **coverage/NTN robustness enhancement** for the Msg1-based path.

## Where to touch the 38.300 text in `random_access_38300.txt`

The most natural insertion point is in the paragraph that explains MSG1 for the 4-step RA type:

- after: “After MSG1 transmission, the UE monitors for a response…”
- before: transition into the MSGA (2-step RA type) description

The draft insertion is captured as a marked excerpt in `ts38300_marked_excerpts.md`.

