# Notes from `proposal.txt` (What we're trying to standardize)

## Problem statement (context)

For NR-NTN *without GNSS*, UE location uncertainty can cause:
- large timing uncertainty (TA) and
- large Doppler / frequency offset

that can exceed what a single-shot PRACH transmission can reliably tolerate (especially with short PRACH formats / high numerologies).

## Core idea: multi-step PRACH with feedback

Instead of a single Msg1→RAR→Msg3 progression, the UE may perform **multiple Msg1 (PRACH) transmissions within one random access attempt**, with **RAR feedback between transmissions**:

- First Msg1: typically **long PRACH** (robust detection, coarse timing).
- RAR feedback: includes **timing and/or frequency adjustment** information.
- Subsequent Msg1: can be **short PRACH** (better timing resolution) using **time/frequency pre-compensation**.
- UE proceeds to Msg3 **only when** it receives an RAR that includes a Msg3 UL grant.

The proposal also mentions:
- **accumulating corrections** across RARs and applying them to future Msg1 and Msg3,
- potential **preamble ID reuse** across Msg1 transmissions in the same attempt,
- **RO grouping**: treating multiple PRACH sequences (potentially with different formats/numerologies) as one "RO group" for a single attempt,
- failure rule: if UE does not receive a RAR corresponding to the *most recent* Msg1, UE declares the attempt failed and does not send further Msg1s in that attempt,
- optional cap on number of Msg1 transmissions in the same attempt (e.g., max 2).

## Implications for 38.321 framing

This is *not* the existing 2-step RA (MsgA/MsgB) procedure. It is a modification/extension of the 4-step RA Msg1 path:

- The MAC Random Access procedure needs an explicit concept of **"Msg1 sequence within an attempt"** (Msg1-1, Msg1-2, …) driven by RAR feedback.
- 38.321 needs to define when **RAR reception is “successful”** vs “progress”:
  - Receiving a Type-2 RAR may be “successful reception” but **not completion** and **not yet the point to allocate TC-RNTI / build Msg3** (unless it also provides Msg3 grant).
- 5.1.4 likely needs to allow **looping back to 5.1.3** (transmit another PRACH) as a *normative branch* on a new RAR indication.

