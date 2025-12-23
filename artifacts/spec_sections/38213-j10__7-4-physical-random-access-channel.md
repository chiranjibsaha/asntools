## 7.4     Physical random access channel [#](#7-4-physical-random-access-channel)

A UE determines a transmission power for a physical random access channel (PRACH), \(P_{PRACH,b,f,c}(i)\), on active UL BWP \(b\) of carrier \(f\) of cell \(c\) based on DL RS for cell \(c\) in transmission occasion \(i\) as

    \(P_{PRACH,b,f,c}(i) = min\left\{ {P_{CMAX,f,c}(i),P_{PRACH,target,f,c} + {PL}_{b,f,c}} \right\}\) [dBm],

where

-    \(P_{CMAX,f,c}(i)\) is the UE configured maximum output power defined in [8-1, TS 38.101-1], [8-2, TS 38.101-2], [8-3, TS 38.101-3] and [8-5, TS 38.101-5] for carrier \(f\) of cell \(c\) within transmission occasion \(i\),

-    \(P_{PRACH,\text{target},f,c}\) is the PRACH target reception power *PREAMBLE_RECEIVED_TARGET_POWER* provided by higher layers [11, TS 38.321] for the active UL BWP \(b\) of carrier \(f\) of cell \(c\), and

-    \({PL}_{b,f,c}\) is a pathloss for the active UL BWP \(b\) of carrier \(f\) based on the DL RS associated with the PRACH transmission on the active DL BWP of cell \(c\) and calculated by the UE in dB as *referenceSignalPower* – higher layer filtered RSRP in dBm, where RSRP is defined in [7, TS 38.215] and the higher layer filter configuration is defined in [12, TS 38.331]. If the active DL BWP is the initial DL BWP and for SS/PBCH block and CORESET multiplexing pattern 2 or 3 as described in clause 13, or for a non-serving cell, the UE determines \({PL}_{b,f,c}\) based on the SS/PBCH block associated with the PRACH transmission.

If a PRACH transmission from a UE is not in response to a detection of a PDCCH order by the UE, or is in response to a detection of a PDCCH order by the UE that triggers a contention based random access procedure, or is associated with a link recovery procedure where a corresponding index \(q_{\text{new}}\) is associated with a SS/PBCH block, as described in clause 6, *referenceSignalPower* is provided by *ss-PBCH-BlockPower*.

If a PRACH transmission from a UE is in response to a detection of a PDCCH order by the UE that triggers a contention-free random access procedure, and if a pathloss offset indicator field in the PDCCH order [5, TS 38.212] indicates to the UE to apply *pl-Offset* that is included in an indicated *TCI-State* or a *TCI-UL-State* and has value \({PL}_{b,f,c,\text{offset}}\) in dB, where \({PL}_{b,f,c,\text{offset}}\) can be updated by a MAC CE [11, TS 38.321], the UE sets \({PL}_{b,f,c} = {PL}_{b,f,c} - {PL}_{b,f,c,\text{offset}}\) for the PRACH transmission.

If a PRACH transmission from a UE is in response to a detection of a PDCCH order by the UE that triggers a contention-free random access procedure and depending on the DL RS that the DM-RS of the PDCCH order is quasi-collocated with as described in clause 10.1

-    when the PRACH association indicator is not present in the PDCCH order, or

-    when the cell indicator field in the PDCCH order is not present or has value 0, or

-    when a value of a PRACH association indicator field in the PDCCH order is 0 if the UE is not provided *SSB-MTC-AdditionalPCI*, or

-    when the PRACH association indicator field in the PDCCH order indicates a *physCellId* associated with the cell of the PDCCH order reception,

or depending on an indicated SS/PBCH block

-    when the PRACH transmission is on a non-serving cell indicated by the cell indicator field in the PDCCH order, or

-    when a value of a PRACH association indicator field in the PDCCH order is 1 if the UE is not provided *SSB-MTC-Add**i**tionalPCI*, or

-    when the PRACH association indicator field in the PDCCH order indicates a* physCellId* that is different than the *physCellId* associated with the cell of the PDCCH order reception,

*referenceSignalPower* is provided by a corresponding *ss-PBCH-BlockPower*.

When a value of a PRACH association indicator field in the PDCCH order is 1 if the UE is not provided *SSB-MTC-Add**i**tionalPCI*, or when the PRACH association indicator field in the PDCCH order indicates a* physCellId* that is different that the *physCellId* associated with the cell of the PDCCH order reception, the UE expects that the indicated SS/PBCH block in the PDCCH order is configured as *pathlossReferenceRS-Id* of an active TCI state.

If the UE is configured resources for a periodic CSI-RS reception or the PRACH transmission is associated with a link recovery procedure where a corresponding index \(q_{\text{new}}\) is associated with a periodic CSI-RS configuration as described in clause 6, *referenceSignalPower* is obtained by *ss-PBCH-BlockPower* and *powerControlOffsetSS* where *powerControlOffsetSS** *provides an offset of CSI-RS transmission power relative to SS/PBCH block transmission power [6, TS 38.214]. If *powerControlOffsetSS* is not provided to the UE, the UE assumes an offset of 0 dB. If the active TCI state for the PDCCH that provides the PDCCH order includes two RS, the UE expects that one RS is configured with *qcl-Type* set to 'typeD' and the UE uses the one RS when applying a value provided by *powerControlOffsetSS*.

If within a random access response window, as described in clause 8.2, the UE does not receive a random access response that contains a preamble identifier corresponding to the preamble sequence transmitted by the UE, or when a random access response does not exist, the UE determines a transmission power for a subsequent PRACH transmission, if any, as described in [11, TS 38.321].

If prior to a PRACH retransmission, a UE changes the spatial domain transmission filter, Layer 1 notifies higher layers to suspend the power ramping counter as described in [11, TS 38.321].

If due to power allocation to PUSCH/PUCCH/PRACH/SRS transmissions as described in clause 7.5, or due to power allocation in EN-DC or NE-DC or NR-DC operation, or due to slot format determination as described in clause 11.1, or due to the PUSCH/PUCCH/PRACH/SRS transmission occasions are in the same slot or the gap between a PRACH transmission and PUSCH/PUCCH/SRS transmission is small as described in clause 8.1, or due to DAPS operation as described in clause 15, or due to HD-UE operation in paired spectrum as described in clause 17.2, the UE does not transmit a PRACH in a transmission occasion, or does not transmit any of \(N_{\text{preamble}}^{\text{rep}}\) preamble repetitions of a PRACH as described in Clause 8.1, Layer 1 notifies higher layers to suspend the corresponding power ramping counter.

If due to power allocation to PUSCH/PUCCH/PRACH/SRS transmissions as described in clause 7.5, or due to power allocation in EN-DC or NE-DC or NR-DC operation, the UE transmits a PRACH with reduced power in a transmission occasion, or transmits one or more of \(N_{\text{preamble}}^{\text{rep}}\) preamble repetitions of a PRACH with reduced power, Layer 1 may notify higher layers to suspend the corresponding power ramping counter.

If the UE transmits less than \(N_{\text{preamble}}^{\text{rep}}\) preamble repetitions of a PRACH, Layer 1 may notify higher layers to suspend the corresponding power ramping counter.
