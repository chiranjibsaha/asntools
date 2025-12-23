# TS 38.321 excerpts with proposed insertions (marked draft)

This file is a patch-style draft: it reproduces **relevant excerpts** (via spec extraction) and inserts new proposal text with `[[ADD]]` / `[[MOD]]` markers.

Spec extractions used (generated under `artifacts/spec_sections/`):
- `artifacts/spec_sections/38321-j00__5-1-random-access-procedure.md`
- `artifacts/spec_sections/38321-j00__6-1-5-mac-pdu-random-access-response.md`
- `artifacts/spec_sections/38321-j00__6-1-5-a-mac-pdu-msgb.md`
- `artifacts/spec_sections/38321-j00__6-2-2-mac-subheader-for-random-access-response.md`
- `artifacts/spec_sections/38321-j00__6-2-3-mac-payload-for-random-access-response.md`

Regeneration commands are captured in `docs/ra_type2_rar_prach_switch/spec_extracts_38321.md`.

Markers:
- `[[ADD]]` new text to be inserted
- `[[MOD]]` change to baseline text
- `[[TBD]]` open item

## 5.1.1 Random Access procedure initialization (UE variables)

Source excerpt: `artifacts/spec_sections/38321-j00__5-1-random-access-procedure.md`.

```
The following UE variables are used for the Random Access procedure:
-	PREAMBLE_INDEX;
-	PREAMBLE_TRANSMISSION_COUNTER;
-	PREAMBLE_POWER_RAMPING_COUNTER;
-	PREAMBLE_POWER_RAMPING_STEP;
-	PREAMBLE_RECEIVED_TARGET_POWER;
-	PREAMBLE_BACKOFF;
-	PCMAX;
-	SCALING_FACTOR_BI;
-	TEMPORARY_C-RNTI;
[[ADD]] -	PRACH_TIME_PRECOMP; -- time pre-compensation from Type-2 MAC RAR
[[ADD]] -	PRACH_FREQ_PRECOMP; -- frequency pre-compensation from Type-2 MAC RAR
[[ADD]] -	MSG1_2_PENDING;     -- indicates Msg1-2 transmission is required
-	RA_TYPE;
-	POWER_OFFSET_2STEP_RA;
-	MSGA_PREAMBLE_POWER_RAMPING_STEP;
-	RO_TYPE;
-	POWER_OFFSET_RO_TYPE;
-	PREVIOUS_RO_TYPE_PREAMBLE_POWER_RAMPING_STEP.
```

### Initialization of the new variables (excerpt location: “When the Random Access procedure is initiated … the MAC entity shall:”)

```
... the MAC entity shall:
1>	flush the Msg3 buffer;
1>	flush the MSGA buffer;
1>	set the PREAMBLE_TRANSMISSION_COUNTER to 1;
...
1>	set the PREAMBLE_BACKOFF to 0 ms;
...
[[ADD]] 1>	set PRACH_TIME_PRECOMP to 0;
[[ADD]] 1>	set PRACH_FREQ_PRECOMP to 0;
[[ADD]] 1>	set MSG1_2_PENDING to false;
```

## 5.1.2 Random Access Resource selection (CBRA preamble selection excerpt)

Source excerpt: `artifacts/spec_sections/38321-j00__5-1-random-access-procedure.md`.

```
1>	else (i.e. for the contention-based Random Access preamble selection):
[[ADD]] 	2>	if MSG1_2_PENDING is set to true:
[[ADD]] 		3>	keep the PREAMBLE_INDEX unchanged (reuse the same preamble id/RAPID as confirmed by the Type-2 MAC RAR for Msg1-1);
[[ADD]] 		3>	-- Msg1-2 is contention-free in the sense that the UE shall not (re-)select a Random Access Preamble; it reuses the existing PREAMBLE_INDEX.
[[ADD]] 		3>	determine the next available PRACH occasion from PRACH occasions of a secondary PRACH configuration (e.g., a second RACH-ConfigGeneric) corresponding to the selected SSB (selection per TS 38.213 [6]);
[[ADD]] 		3>	perform the Random Access Preamble transmission procedure (see clause 5.1.3).
[[ADD]] 	2>	else:
	2>	if at least one of the SSBs with SS-RSRP above rsrp-ThresholdSSB is available:
		3>	select an SSB with SS-RSRP above rsrp-ThresholdSSB.
	2>	else:
		3>	select any SSB.
...
	2>	select a Random Access Preamble randomly with equal probability from the Random Access Preambles associated with the selected SSB and the selected Random Access Preambles group;
	2>	set the PREAMBLE_INDEX to the selected Random Access Preamble.
...
		3>	determine the next available PRACH occasion from the PRACH occasions of the selected RO type corresponding to the selected SSB permitted by the restrictions given by the ra-ssb-OccasionMaskIndex if configured, or ssb-SharedRO-MaskIndex if configured, or indicated by PDCCH, or indicated by the (Enhanced) LTM Cell Switch Command MAC CE (...)
1>	perform the Random Access Preamble transmission procedure (see clause 5.1.3).
```

[[TBD]] The “secondary PRACH configuration” needs a 38.331 hook (e.g., additional/secondary `RACH-ConfigGeneric`) and a rule for the timing reference (user clarification: relative to the subframe/slot carrying the Type-2 RAR).

## 5.1.3 Random Access Preamble transmission (PHY command augmentation)

Source excerpt: `artifacts/spec_sections/38321-j00__5-1-random-access-procedure.md`.

```
1>	except for contention-free Random Access Preamble for beam failure recovery request and contention-free Random Access Preamble triggered by a PDCCH order for an LTM candidate cell, compute the RA-RNTI associated with the PRACH occasion in which the Random Access Preamble is transmitted;
1>	instruct the physical layer to transmit the Random Access Preamble using the selected PRACH occasion, corresponding RA-RNTI (if available), PREAMBLE_INDEX, and PREAMBLE_RECEIVED_TARGET_POWER.
[[ADD]] 1>	if MSG1_2_PENDING is set to true:
[[ADD]] 	2>	instruct the physical layer to apply PRACH_TIME_PRECOMP and PRACH_FREQ_PRECOMP when transmitting the Random Access Preamble.
```

## 5.1.4 Random Access Response reception (Type-2 MAC RAR branch + failure handling)

Source excerpt: `artifacts/spec_sections/38321-j00__5-1-random-access-procedure.md`.

### Successful reception branch (excerpt)

```
	2>	if the Random Access Response contains a MAC subPDU with Random Access Preamble identifier corresponding to the transmitted PREAMBLE_INDEX (see clause 5.1.3):
		3>	consider this Random Access Response reception successful.
	2>	if the Random Access Response reception is considered successful:
		3>	if the Random Access Response includes a MAC subPDU with RAPID only:
			4>	consider this Random Access procedure successfully completed;
...
		3>	else:
[[ADD]] 			4>	if the Random Access Response includes a MAC subPDU with RAPID and Type-2 MAC RAR:
[[ADD]] 				5>	set PRACH_TIME_PRECOMP and PRACH_FREQ_PRECOMP to the values received in the Type-2 MAC RAR; [[TBD]] units/size;
[[ADD]] 				5>	-- timing reference for Msg1-2 resource selection may be derived from the subframe/slot carrying this Type-2 MAC RAR. [[TBD]]
[[ADD]] 				5>	set MSG1_2_PENDING to true;
[[ADD]] 				5>	-- Msg1-2 is contention-free in the sense that the UE shall reuse the RAPID/preamble index confirmed by the Type-2 MAC RAR (no new preamble selection).
[[ADD]] 				5>	-- do not process Timing Advance Command, do not process an UL grant, and do not set TEMPORARY_C-RNTI upon reception of Type-2 MAC RAR.
[[ADD]] 				5>	perform the Random Access Resource selection procedure (see clause 5.1.2);
[[ADD]] 				5>	perform the Random Access Preamble transmission procedure (see clause 5.1.3);
[[ADD]] 				5>	set MSG1_2_PENDING to false;
[[ADD]] 				5>	start the ra-ResponseWindow configured in RACH-ConfigCommon at the first PDCCH occasion as specified in TS 38.213 [6] from the end of the Random Access Preamble transmission;
[[ADD]] 				5>	monitor the PDCCH of the SpCell for Random Access Response(s) identified by the RA-RNTI while the ra-ResponseWindow is running.
[[ADD]] 				5>	-- NOTE: Type-2 MAC RAR does not include TC-RNTI and does not provide Msg3 UL grant; TC-RNTI is provided in the subsequent regular RAR.
[[ADD]] 			4>	else:
			4>	apply the following actions for the Serving Cell where the Random Access Preamble was transmitted:
				5>	process the received Timing Advance Command (see clause 5.2);
...
				5>	set the TEMPORARY_C-RNTI to the value received in the Random Access Response;
...
					6>	obtain the MAC PDU to transmit from the Multiplexing and assembly entity and store it in the Msg3 buffer.
```

### Response window expiry branch (excerpt + insert)

```
NOTE 1:	If within a Random Access procedure, an uplink grant provided in the Random Access Response for the same group of contention-based Random Access Preambles has a different size than the first uplink grant allocated during that Random Access procedure, the UE behavior is not defined.
1>	if ra-ResponseWindow configured in BeamFailureRecoveryConfig expires and if a PDCCH transmission on the search space indicated by recoverySearchSpaceId addressed to the C-RNTI has not been received on the Serving Cell where the preamble was transmitted; or
1>	if ra-ResponseWindow configured in RACH-ConfigCommon or RACH-ConfigSIB1 expires, and if the Random Access Response containing Random Access Preamble identifiers that matches the transmitted PREAMBLE_INDEX has not been received:
	2>	consider the Random Access Response reception not successful;
[[ADD]] 	2>	if PRACH_TIME_PRECOMP and/or PRACH_FREQ_PRECOMP were set from a Type-2 MAC RAR:
[[ADD]] 		3>	clear PRACH_TIME_PRECOMP and PRACH_FREQ_PRECOMP;
[[ADD]] 		3>	-- subsequent RA retries use the primary PRACH configuration (Msg1-1, long PRACH)
	2>	increment PREAMBLE_TRANSMISSION_COUNTER by 1;
	2>	if PREAMBLE_TRANSMISSION_COUNTER = preambleTransMax + 1:
		3>	if the Random Access Preamble is transmitted on the SpCell:
			4>	indicate a Random Access problem to upper layers;
			4>	if this Random Access procedure was triggered for SI request or SIB1 request:
				5>	consider the Random Access procedure unsuccessfully completed.
		3>	else if the Random Access Preamble is transmitted on an SCell:
			4>	consider the Random Access procedure unsuccessfully completed.
	2>	if the Random Access procedure is not completed:
...
			4>	perform the Random Access Resource selection procedure (see clause 5.1.2) after the backoff time.
```

## 6.1.5 MAC PDU (Random Access Response) (Type-2 MAC RAR addition)

Source excerpt: `artifacts/spec_sections/38321-j00__6-1-5-mac-pdu-random-access-response.md`.

```
6.1.5	MAC PDU (Random Access Response)
A MAC PDU consists of one or more MAC subPDUs and optionally padding. Each MAC subPDU consists one of the following:
-	a MAC subheader with Backoff Indicator only;
-	a MAC subheader with RAPID only (i.e. acknowledgment for SI request or SIB1 request);
-	a MAC subheader with RAPID and MAC RAR.
...
A MAC subheader with RAPID consists of three header fields E/T/RAPID as described in Figure 6.1.5-2.
[[ADD]] A MAC RAR may be a regular MAC RAR (see clause 6.2.3) or a Type-2 MAC RAR (see clause 6.2.3.x).
```

```
[[ADD]] 6.2.3.x  Type-2 MAC RAR (proposed)
[[ADD]] A Type-2 MAC RAR carries only PRACH time/frequency pre-compensation and is associated with the RAPID in the subheader.
[[ADD]] It does not provide a Msg3 UL grant and does not provide TC-RNTI; the UE obtains Msg3 UL grant and TC-RNTI in the subsequent regular MAC RAR.
[[ADD]] The Type-2 MAC RAR is of fixed size and octet aligned.
[[ADD]] Identification/discrimination between regular MAC RAR and Type-2 MAC RAR is [[TBD]].
```

## 6.2.2 MAC subheader for Random Access Response (clarification hook)

Source excerpt: `artifacts/spec_sections/38321-j00__6-2-2-mac-subheader-for-random-access-response.md`.

```
... RAPID: ... The size of the RAPID field is 6 bits.
If the RAPID in the MAC subheader ... corresponds to one of the Random Access Preambles configured for SI request or SIB1 request, MAC RAR is not included in the MAC subPDU.
[[ADD]] If MAC RAR is included for a RAPID corresponding to a Random Access Preamble transmission, the MAC RAR payload may be a regular MAC RAR or a Type-2 MAC RAR (see clause 6.2.3 / 6.2.3.x).
```

## 6.2.3 MAC payload for Random Access Response (regular MAC RAR + Type-2 MAC RAR)

Source excerpt: `artifacts/spec_sections/38321-j00__6-2-3-mac-payload-for-random-access-response.md`.

```
The MAC RAR is of fixed size ... and consists of the following fields:
... Timing Advance Command ... 12 bits;
... UL Grant ... 27 bits;
... Temporary C-RNTI ... 16 bits.
...
[[ADD]] Type-2 MAC RAR (proposed):
[[ADD]] The Type-2 MAC RAR is of fixed size and octet aligned.
[[ADD]] The Type-2 MAC RAR contains PRACH_TIME_PRECOMP and PRACH_FREQ_PRECOMP (units/size [[TBD]]).
[[ADD]] The UE shall not interpret Type-2 MAC RAR contents as Timing Advance Command, UL Grant, or Temporary C-RNTI.
[[ADD]] The UE shall reuse the RAPID/preamble id for Msg1-2 (i.e. Msg1-2 is contention-free in the sense of preamble selection), and the gNB shall provide a subsequent regular MAC RAR (with UL grant + TC-RNTI) to schedule Msg3.
[[ADD]] Identification/discrimination mechanism is [[TBD]] (e.g., reserved pattern vs explicit type indication).
```

## 6.1.5a MAC PDU (MSGB) (no change expected)

Source excerpt: `artifacts/spec_sections/38321-j00__6-1-5-a-mac-pdu-msgb.md`.

[[ADD]] No change expected for MSGB (2-step RA) for the current proposal, since the enhancement is on the Msg1/Msg2 (RAR) path of 4-step RA.

## 5.1.6 Completion of the Random Access procedure (cleanup)

Source excerpt: `artifacts/spec_sections/38321-j00__5-1-random-access-procedure.md`.

```
Upon completion of the Random Access procedure, the MAC entity shall:
...
[[ADD]] 1>	clear PRACH_TIME_PRECOMP and PRACH_FREQ_PRECOMP;
[[ADD]] 1>	set MSG1_2_PENDING to false;
```
