# Msg1 repetition root hopping — full local extracts + proposed deltas
This file is generated locally by `scripts/build_msg1_root_hopping_delta_doc.py` from `artifacts/spec_sections/*` and is intended for local engineering use.
---

## TS 38.213 §8.1 Random access preamble

## 8 .1    Random access preamble [#](#8-1-random-access-preamble)

Physical random access procedure for a UE is triggered upon request of a PRACH transmission by higher layers or by a PDCCH order or LTM Cell Switch Command MAC CE in clause 6.1.3.75 [11, TS 38.321] for a cell. A configuration by higher layers for a PRACH transmission includes the following:

-    A configuration for PRACH transmission on the cell [4, TS 38.211].

-    A preamble index, a preamble SCS, \(P_{PRACH,\text{target}}\), a corresponding RA-RNTI when applicable [11, TS 38.321], and a PRACH resource for the cell.

-    A number of \(N_{\text{preamble}}^{\text{rep}} > 1\) preamble repetitions for the PRACH transmission if the UE would transmit the PRACH with repetitions.

A UE transmits a PRACH on a cell using the selected="selected" PRACH format with transmission power \(P_{PRACH,b,f,c}(i)\), as described in clause 7.4, on the indicated PRACH resource or on a determined set of \(N_{\text{preamble}}^{\text{rep}}\) resources using a same spatial filter in case of \(N_{\text{preamble}}^{\text{rep}}\) preamble repetitions.

For Type-1 random access procedure, a UE can be provided, by *addl-RACH-Config-Adaptation* in *RACH-ConfigCommon*, parameters for determining time resources and frequency resources for PRACH transmission [4, TS 38.211]. When a PRACH occasion associated with *addl-RACH-Config-Adaptation* has same frequency resource and same time resource as a PRACH occasion in *RACH-ConfigCommon* that is not associated with* addl-RACH-Config-Adaptation*, the former PRACH occasion is not valid and is not considered in the procedures in this clause.

For valid PRACH occasions associated with* addl-RACH-Config-Adaptation* in *RACH-ConfigCommon*, the UE can be additionally provided a PRACH mask index, by *prach-SubsetMask-Index-Adaptation*, that indicates one or more association periods per \(K_{\text{mask}}\) association pattern periods according to Table 8.1-0, where \(K_{\text{mask}}\) is provided by *KforAPPForPRACHsubsetMask*.

Table 8.1-0: Mapping of mask index to association periods per *K**mask* association pattern periods

**Mask Index**

**Association periods (APs) per **\(\mathbf{K}_{\mathbf{m}\mathbf{a}\mathbf{s}\mathbf{k}}\)** association pattern periods (APPs)**

0

First half of APs in \(\mathbf{K}_{\mathbf{m}\mathbf{a}\mathbf{s}\mathbf{k}}\) APPs

1

First quarter of APs in \(\mathbf{K}_{\mathbf{m}\mathbf{a}\mathbf{s}\mathbf{k}}\) APPs

2

First eighth of APs in \(\mathbf{K}_{\mathbf{m}\mathbf{a}\mathbf{s}\mathbf{k}}\) APPs

3

First sixteenth of APs in \(\mathbf{K}_{\mathbf{m}\mathbf{a}\mathbf{s}\mathbf{k}}\) APPs

Valid PRACH occasions associated with* addl-RACH-Config-Adaptation*, and additionally in association periods indicated by *prach-SubsetMask-Index-Adaptation*, if provided, are indicated as available for PRACH transmission based on an indication in a DCI format 1_0 with CRC scrambled by a P-RNTI or a C-RNTI [5, TS 38.212]. For indication by DCI format 1_0 with CRC scrambled by the P-RNTI, the PRACH occasions are available for a duration provided by *validity-DurationForAddlRACHAdaptation*, starting from the first frame of the SI modification period [12, TS 38.331] that includes a PDCCH monitoring occasion where the UE receives a PDCCH providing the DCI format 1_0 with CRC scrambled by the P-RNTI.

In the following, for determining valid PRACH occasions, if a UE is not provided SS/PBCH block indexes by *ssb-PositionsInBurst* in *ServingCellConfigCommon* and is provided *od-ssb-Config*, reference to SS/PBCH blocks is for the union of SS/PBCH blocks provided by each combination of *od-ssb-PositionsInBurst* and *od-ssb-Periodicity *in *od-ssb-Config*. If the UE is provided SS/PBCH block indexes by *ssb-PositionsInBurst* in *ServingCellConfigCommon* and is provided *od-ssb-Config*, reference to SS/PBCH blocks is for the union of SS/PBCH blocks provided by *ssb-Periodicity* and *ssb-PositionsInBurst* in *ServingCellConfigCommon* and by each combination of *od-ssb-PositionsInBurst* and *od-ssb-Periodicity* in *od-ssb-Config*.

In the following, for determining an association between PRACH occasions and SS/PBCH block indexes, if a UE is not provided SS/PBCH block indexes by *ssb-PositionsInBurst* in *ServingCellConfigCommon* and is provided *od-ssb-Config*, reference to SS/PBCH block indexes provided by *ssb-PositionsInBurst* in *ServingCellConfigCommon* is for the union of SS/PBCH block indexes provided by each *od-ssb-PositionsInBurst* in *od-ssb-Config*. If the UE is provided SS/PBCH block indexes by *ssb-PositionsInBurst* in *ServingCellConfigCommon* and is provided *od-ssb-Config*, reference to SS/PBCH block indexes provided by *ssb-PositionsInBurst* in *ServingCellConfigCommon* is for the union of SS/PBCH block indexes provided by *ssb-PositionsInBurst* in *ServingCellConfigCommon* and by each *od-ssb-PositionsInBurst* in *od-ssb-Config*.

For Type-1 random access procedure, a UE is provided a number \(N\) of SS/PBCH block indexes associated with one PRACH occasion and a number \(R\) of contention based preambles per SS/PBCH block index per valid PRACH occasion either by *ssb-perRACH-OccasionAndCB-**PreamblesPerSSB** *or by* ssb-perRACH-OccasionAndCB-PreamblesPerSSB-r19*.

For Type-2 random access procedure with common configuration of PRACH occasions with Type-1 random access procedure, a UE is provided a number \(N\) of SS/PBCH block indexes associated with one PRACH occasion by *ssb-perRACH-OccasionAndCB-**PreamblesPerSSB* and a number \(Q\) of contention based preambles per SS/PBCH block index per valid PRACH occasion by *msgA-CB-PreamblesPerSSB-PerSharedRO*. The PRACH transmission can be on a subset of PRACH occasions associated with a same SS/PBCH block index within an SSB-RO mapping cycle for a UE provided with a PRACH mask index by *msgA-**SSB-S**haredRO-MaskIndex* according to [11, TS 38.321].

For Type-2 random access procedure with separate configuration of PRACH occasions with Type-1 random access procedure, a UE is provided a number \(N\) of SS/PBCH block indexes associated with one PRACH occasion and a number \(R\) of contention based preambles per SS/PBCH block index per valid PRACH occasion by *msgA-SSB-PerRACH-OccasionAndCB-PreamblesPerSSB* when provided; otherwise, by *ssb-perRACH-OccasionAndCB-PreamblesPerSSB*.

For a random access procedure associated with a feature combination indicated by *FeatureCombinationPreambles*, a UE is provided a number \(N\) of SS/PBCH block indexes associated with one PRACH occasion by *ssb-perRACH-OccasionAndCB-PreamblesPerSSB* or *msgA-SSB-PerRACH-OccasionAndCB-PreamblesPerSSB* when provided and a number \(S\) of contention based preambles per SS/PBCH block index per valid PRACH occasion by *startPreambleForThisPartition* and *n**umberOfPreamblesPerSSB-ForThisPartition*. The PRACH transmission can be on a subset of PRACH occasions associated with a same SS/PBCH block index within an SSB-RO mapping cycle for a UE provided with a PRACH mask index by *ssb-SharedRO-MaskIndex* according to [11, TS 38.321].

For Type-1 random access procedure, or for Type-2 random access procedure with separate configuration of PRACH occasions from Type 1 random access procedure, if \(N < 1\), one SS/PBCH block index is mapped to \(1/N\) consecutive valid PRACH occasions and \(R\) contention based preambles with consecutive indexes associated with the SS/PBCH block index per valid PRACH occasion start from preamble index 0. If \(N \geq 1\), \(R\) contention based preambles with consecutive indexes associated with SS/PBCH block index \(n\), \(0 \leq n \leq N - 1\), per valid PRACH occasion start from preamble index \(n{{\cdot N}_{\text{preamble}}^{\text{total}}/N}\) where \(N_{\text{preamble}}^{\text{total}}\) is provided by *totalNumberOfRA-Preambles* for Type-1 random access procedure, or by *msgA-T**otalNumberOfRA-Preambles* for Type-2 random access procedure with separate configuration of PRACH occasions from a Type 1 random access procedure, and is an integer multiple="multiple" of \(N\).

For Type-2 random access procedure with common configuration of PRACH occasions with Type-1 random access procedure, if \(N < 1\), one SS/PBCH block index is mapped to \(1/N\) consecutive valid PRACH occasions and \(Q\) contention based preambles with consecutive indexes associated with the SS/PBCH block index per valid PRACH occasion start from preamble index \(R\). If \(N \geq 1\), \(Q\) contention based preambles with consecutive indexes associated with SS/PBCH block index \(n\), \(0 \leq n \leq N - 1\), per valid PRACH occasion start from preamble index \(n{{\cdot N}_{\text{preamble}}^{\text{total}}/N} + R\), where \(N_{\text{preamble}}^{\text{total}}\) is provided by *totalNumberOfRA-Preambles* for Type-1 random access procedure.

For link recovery, a UE is provided \(N\) SS/PBCH block indexes associated with one PRACH occasion by *ssb-perRACH-Occasion* in *BeamFailureRecoveryConfig*. For a dedicated RACH configuration provided by *RACH-ConfigDedicated*, if *cfra* is provided, a UE is provided \(N\) SS/PBCH block indexes associated with one PRACH occasion by *ssb-perRACH-Occasion* in *occasions*. For the PRACH transmission on a candidate cell [38.213, clause 21], a UE is provided \(N\) SS/PBCH block indexes associated with one PRACH occasion by *ssb-PerRACH-Occasion-r18* in *EarlyUL-SyncConfig*. If \(N < 1\), one SS/PBCH block index is mapped to \(1/N\) consecutive valid PRACH occasions. If \(N \geq 1\), all consecutive \(N\) SS/PBCH block indexes are associated with one PRACH occasion.

SS/PBCH block indexes provided by *ssb-PositionsInBurst* in *S**IB**1* or in *ServingCellConfigCommon* or in *SSB-MTC-AdditionalPCI* or in *LTM-SSB-Config* are mapped to valid PRACH occasions in the following order where the parameters are described in [4, TS 38.211]. The mapping of SS/PBCH block indexes to valid PRACH occasions is separate for valid PRACH occasions determined by *RACH-ConfigCommon* and for valid PRACH occasions determined by *addl-RACH-Config-Adaptation*.

-    First, in increasing order of preamble indexes within a single PRACH occasion

-    Second, in increasing order of frequency resource indexes for frequency multiplexed PRACH occasions

-    Third, in increasing order of time resource indexes for time multiplexed PRACH occasions within a PRACH slot

-    Fourth, in increasing order of indexes for PRACH slots

An association period, starting from frame 0, for mapping SS/PBCH block indexes to PRACH occasions is the smallest integer number in the set determined by the PRACH configuration period according to Table 8.1-1 such that \(N_{\text{Tx}}^{\text{SSB}}\) SS/PBCH block indexes are mapped at least once to the PRACH occasions within the association period, where a UE obtains \(N_{\text{Tx}}^{\text{SSB}}\) from the value of *ssb-PositionsInBurst* in *S**IB**1* or in *ServingCellConfigCommon** *or in *SSB-MTC-AdditionalPCI* or in *LTM-SSB-Config*. If after an integer number of SS/PBCH block indexes to PRACH occasions mapping cycles within the association period there is a set of PRACH occasions or PRACH preambles that are not mapped to \(N_{\text{Tx}}^{\text{SSB}}\) SS/PBCH block indexes, no SS/PBCH block indexes are mapped to the set of PRACH occasions or PRACH preambles. An association pattern period includes one or more association periods and is determined so that a pattern between PRACH occasions and SS/PBCH block indexes repeats at most every 160 msec. PRACH occasions not associated with SS/PBCH block indexes after an integer number of association periods, if any, are not used for PRACH transmissions.

Table 8.1-1: Mapping between PRACH configuration period and SS/PBCH block to PRACH occasion association period

**PRACH configuration period (msec)**

**Association period (number of PRACH configuration periods)**

10

{1, 2, 4, 8, 16}

20

{1, 2, 4, 8}

40

{1, 2, 4}

80

{1, 2}

160

{1}

 

For a PRACH transmission by a UE triggered by a PDCCH order or an LTM cell switch command MAC CE, the PRACH mask index field, if the value of the random access preamble index field is not zero, indicates the PRACH occasion for the PRACH transmission where the PRACH occasions are associated with the SS/PBCH block index indicated by the SS/PBCH block index field of the PDCCH order or the LTM cell switch command MAC CE and, if any, a cell indicator field in PDCCH order [5, TS 38.212] or a Target Configuration ID field in LTM cell switch command MAC CE [11, TS 38.321] indicates a cell for the PRACH transmission. If the UE is provided \(K_{cell,\text{offset}}\) by *c**ellSpecific**Koffset*, the PRACH occasion is after slot \(n + {2^{\mu} \bullet K}_{cell,\text{offset}}\) where \(n\) is the slot of the UL BWP for the PRACH transmission that overlaps with the end of the PDCCH order reception assuming \(T_{\text{TA}} = 0\), and \(\mu\) is the SCS configuration for the PRACH transmission. If the PDCCH reception for the PDCCH order includes two PDCCH candidates from two linked search space sets based on *searchSpaceLinking**Id*, as described in clause 10.1, the last symbol of the PDCCH reception is the last symbol of the PDCCH candidate that ends later. The PDCCH reception includes the two PDCCH candidates also when the UE is not required to monitor one of the two PDCCH candidates as described in clauses 10 (except clause 10.4), 11.1, 11.1.1 and 17.2.

For a PRACH transmission triggered by higher layers, if *ssb-ResourceList* is provided, the PRACH mask index is indicated by *ra-ssb-OccasionMaskIndex* which indicates the PRACH occasions for the PRACH transmission where the PRACH occasions are associated with the selected="selected" SS/PBCH block index.

The PRACH occasions are mapped consecutively per corresponding SS/PBCH block index. The indexing of the PRACH occasion indicated by the mask index value is reset per mapping cycle of consecutive PRACH occasions per SS/PBCH block index. The UE selects for a PRACH transmission the PRACH occasion indicated by PRACH mask index value for the indicated SS/PBCH block index in the first available mapping cycle.

For the indicated preamble index, the ordering of the PRACH occasions is

-    First, in increasing order of frequency resource indexes for frequency multiplexed PRACH occasions

-    Second, in increasing order of time resource indexes for time multiplexed PRACH occasions within a PRACH slot

-    Third, in increasing order of indexes for PRACH slots

For a PRACH transmission with \(N_{\text{preamble}}^{\text{rep}}\) preamble repetitions, a set consists of \(N_{\text{preamble}}^{\text{rep}}\) valid PRACH occasions that are consecutive in time, use same frequency resources, and are associated with same one or more SS/PBCH block index(es), and each SS/PBCH block index is associated with same preamble indexes in all valid PRACH occasions within the set.

For a PRACH transmission with preamble repetitions, a time period, starting from frame 0, is the smallest integer number of association pattern periods such that at least one set of valid PRACH occasions for each of the \(N_{\text{Tx}}^{\text{SSB}}\) SS/PBCH block indexes can be determined within the time period for all configured number of preamble repetitions for each supported feature combination provided in each *RACH-ConfigCommon*. The set(s) of valid PRACH occasions for each configured number of preamble repetitions repeats every time period.

Within a time period, for set(s) of \(N_{\text{preamble}}^{\text{rep}}\) valid PRACH occasions for a PRACH transmission with \(N_{\text{preamble}}^{\text{rep}}\) preamble repetitions

-    the first valid PRACH occasion of the first set is the first valid PRACH occasion

-    the first valid PRACH occasion of subsequent sets, if any, is determined according to an ordering of valid PRACH occasions

-    first, in increasing order of frequency resource indexes for frequency multiplexed PRACH occasions

-    second, in increasing order of time resource indexes for time multiplexed PRACH occasions

where, for each frequency resource index for frequency multiplexed PRACH occasions

-    the first valid PRACH occasion of the first set is the first valid PRACH occasion

-    the first valid PRACH occasion of subsequent sets, if any,

-    is after *msg1-RepetitionTimeOffsetROGroup* consecutive valid PRACH occasions in time from the first valid PRACH occasion of the previous set, where each PRACH occasion is associated with same SS/PBCH block index(es) and each SS/PBCH block index is associated with same preambles, if *msg1-RepetitionTimeOffsetROGroup* is provided

-    is after the PRACH occasions for the previous set, if *msg1-RepetitionTimeOffsetROGroup* is not provided

For a PRACH transmission with preamble repetitions in CFRA procedure, *msg1-RepetitionTimeOffsetROGroup* is determined by the *FeatureCombinationPreambles* indicating *msg1-Repetitions* with same value as *msg1-RepetitionNum* provided by *RACH-ConfigDedicated*.

For a PRACH transmission triggered upon request by higher layers, a value of *ra-OccasionList* [12, TS 38.331], if *csirs-ResourceList* is provided, indicates a list of PRACH occasions for the PRACH transmission where the PRACH occasions are associated with the selected="selected" CSI-RS index indicated by* csi-RS*. The indexing of the PRACH occasions indicated by *ra-OccasionList* is reset per association pattern period.

For paired spectrum or supplementary uplink band all PRACH occasions are valid.

For unpaired spectrum,

-    if a UE is not provided *tdd**-UL-DL-ConfigurationCommon* for a cell, a PRACH occasion for the cell in a PRACH slot is valid if it does not precede a SS/PBCH block in the PRACH slot and starts at least \(N_{\text{gap}}\) symbols after a last SS/PBCH block reception symbol, where \(N_{\text{gap}}\) is provided in Table 8.1-2 and, if *c**hannelAccess**Mode* = "*semi**S**tatic*" is provided, does not overlap with a set of consecutive symbols before the start of a next channel occupancy time where the UE does not transmit [15, TS 37.213]

-    the candidate SS/PBCH block index of the SS/PBCH block corresponds to the SS/PBCH block index provided by *ssb-PositionsInBurst* in *S**IB**1* or in *ServingCellConfigCommon** *or in* SSB-MTC-AdditionalPCI** *corresponding to the cell*, *as described in clause 4.1

-    for each of the candidate cells configured by *LTM-Config*, if a UE is not provided *ltm-**TDD**-UL-DL-ConfigurationCommon*, a PRACH occasion in a PRACH slot for a candidate cell is valid if it does not precede a SS/PBCH block in the PRACH slot and starts at least \(N_{\text{gap}}\) symbols after a last SS/PBCH block reception symbol, where \(N_{\text{gap}}\) is provided in Table 8.1-2

-    the SS/PBCH block index of the SS/PBCH block corresponds to the SS/PBCH block index provided by *ssb-PositionsInBurst* in *LTM-SSB-Config* corresponding to the candidate cell

-    if a UE is provided *tdd**-**UL-DL-**ConfigurationCommon* for a cell, a PRACH occasion for the cell in a PRACH slot is valid if

-    it is only within UL symbols, or

-    it is only within SBFD symbols, that include at least one SBFD symbol indicated as downlink by *tdd-UL-DL-ConfigurationCommon*, and in RBs that are both in the active UL BWP and in the UL sub-band if the UE is provided either *sbfd-RACHSingleConfig* or *sbfd-RACHDualConfig*, or it starts from an SBFD symbol and ends in a non-SBFD symbols and is in RBs that are both in the active UL BWP and in the UL sub-band if the UE is provided *sbfd-RACHDualConfig* and *sbfd-RACHDualConfig-ValidROAcrossSymbolTypes*, or

-    it does not precede a SS/PBCH block in the PRACH slot, if it is only in UL symbols, and starts at least \(N_{\text{gap}}\) symbols after a last downlink symbol and at least \(N_{\text{gap}}\) symbols after a last SS/PBCH block symbol, where \(N_{\text{gap}}\) is provided in Table 8.1-2, and if *c**hannelAccess**Mode* = "*semi**S**tatic*" is provided, does not overlap with a set of consecutive symbols before the start of a next channel occupancy time where there shall not be any transmissions, as described in [15, TS 37.213]

-    the candidate SS/PBCH block index of the SS/PBCH block corresponds to the SS/PBCH block index provided by *ssb-PositionsInBurst* in *S**IB**1* or in *ServingCellConfigCommon** *or in* SSB-MTC-AdditionalPCI** *corresponding to the cell, as described in clause 4.1

-    for each of the candidate cells configured by *LTM-config*, if a UE is provided *ltm-**tdd**-UL-DL-ConfigurationCommon*, a PRACH occasion in a PRACH slot for a candidate cell is valid if

-    it is within UL symbols, or

-    it does not precede a SS/PBCH block in the PRACH slot and starts at least \(N_{\text{gap}}\) symbols after a last downlink symbol and at least \(N_{\text{gap}}\) symbols after a last SS/PBCH block symbol, where \(N_{\text{gap}}\) is provided in Table 8.1-2

-    the SS/PBCH block index of the SS/PBCH block corresponds to the SS/PBCH block index provided by *ssb-PositionsInBurst* in *LTM-SSB-Config* corresponding to the candidate cell.

For preamble format B4 [4, TS 38.211], \(N_{\text{gap}} = 0\).

Table 8.1-2: \(\mathbf{N}_{\mathbf{g}\mathbf{a}\mathbf{p}}\) values for different preamble SCS \(\mathbf{\mu}\)

Preamble SCS

\[\mathbf{N}_{\mathbf{g}\mathbf{a}\mathbf{p}}\]

1.25 kHz or 5 kHz

0

15 kHz or 30 kHz or 60 kHz or 120 kHz

2

480 kHz

8

960 kHz

16

 

If a random access procedure is initiated by a PDCCH order, the UE, if requested by higher layers, transmits a PRACH in the selected="selected" PRACH occasion, as described in [11, TS 38.321], for which a time between the last symbol of the PDCCH order reception and the first symbol of the PRACH transmission is larger than or equal to \(N_{T,2} + \mathrm{\Delta}_{\text{BWPSwitching}} + \mathrm{\Delta}_{\text{Delay}} + T_{\text{switch}} + T_{\text{SSB}} + \mathrm{\Delta}_{RF/BB\text{preparation}}\) msec, where

-    \(N_{T,2}\) is a time duration of \(N_{2}\) symbols corresponding to a PUSCH preparation time for UE processing capability 1 [6, TS 38.214] assuming \(\mu\) corresponds to the smallest SCS configuration between the SCS configuration of the PDCCH order and the SCS configuration of the corresponding PRACH transmission

-    \(\mathrm{\Delta}_{\text{BWPSwitching}} = 0\) if the active UL BWP does not change, or if a cell indicator field in the PDCCH order indicates a non-serving cell [5, TS 38.212], and \(\mathrm{\Delta}_{\text{BWPSwitching}}\) is a time duration of \(T_{\text{BWPswitchDelay}}\) defined in [10, TS 38.133] otherwise

-    \(\mathrm{\Delta}_{\text{Delay}} = 0.5\) msec for FR1 and \(\mathrm{\Delta}_{\text{Delay}} = 0.25\) msec for FR2

-    \(T_{\text{switch}}\) is a switching gap duration as defined in [6, TS 38.214]

-    \(T_{\text{SSB}} = 0\) if a cell indicator field in the PDCCH order indicates a serving cell or if cell indicator field is not present, and \(T_{\text{SSB}}\) is defined in [10, TS 38.133] otherwise

-    \(\mathrm{\Delta}_{RF/BB\text{preparation}} = 0\) if a cell indicator field in the PDCCH order indicates a serving cell or if cell indicator field is not present, and \(\mathrm{\Delta}_{RF/BB\text{preparation}}\) is defined in [10, TS 38.133] otherwise

For a PRACH transmission using 1.25 kHz or 5 kHz SCS, the UE determines \(N_{2}\) assuming SCS configuration \(\mu = 0\).

For single cell operation or for operation with contiguous carrier aggregation in a same frequency band or for operation with non-contiguous carrier aggregation in a same frequency band if the UE is not provided with *intraBandNC-PRACH-simulTx-r17*, a UE

-    does not transmit PRACH and PUSCH/PUCCH/SRS in a same slot with respect to the smallest SCS configuration between the SCS configuration for the UL BWP with the PRACH and the SCS configuration for the UL BWP with the PUSCH/PUCCH/SRS transmissions

-    does not transmit PRACH and PUSCH/PUCCH/SRS when a first or last symbol of a PRACH transmission in a first slot is separated by less than \(N\) symbols from the last or first symbol, respectively, of a PUSCH/PUCCH/SRS transmission in a second slot; for a PRACH transmission with \(N_{\text{preamble}}^{\text{rep}} > 1\) preamble repetitions, this applies to each preamble repetition

-    for a PRACH transmission with \(N_{\text{preamble}}^{\text{rep}} > 1\) preamble repetitions, if the UE does not indicate *prach-Repetition*, the UE does not transmit a first repetition of the PRACH and a second repetition of the PRACH when a first or last symbol of the first repetition of the PRACH in a first slot is separated by less than \(N\) symbols from the last or first symbol, respectively, of the second  repetition of the PRACH in a second slot; otherwise, the UE transmits the first repetition of the PRACH and the second repetition of the PRACH

where \(N = 2\) for \(\mu = 0\) or \(\mu =\)1, \(N = 4\) for \(\mu = 2\) or \(\mu = 3\), \(N = 16\) for \(\mu = 5\), \(N = 32\) for \(\mu = 6\), and \(\mu\) is the smallest SCS configuration between the SCS configuration for the UL BWP with the PRACH and the SCS configuration for the UL BWP with the PUSCH/PUCCH/SRS transmissions. For a PUSCH transmission with repetition Type B, this applies to each actual repetition for PUSCH transmission [6, TS 38.214].

For a UE configured with *SSB-MTC-AdditionalPCI*, it does not transmit PRACH and receive SS/PBCH associated with different cells in a same slot.
---

## TS 38.213 §7.4 Physical random access channel

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
---

## TS 38.321 §5.1 Random Access procedure

## 5.1     Random Access procedure [#](#5-1-random-access-procedure)

### 5.1.1     Random Access procedure initialization [#](#5-1-1-random-access-procedure-initialization)

The Random Access procedure described in this clause is initiated by a PDCCH order, by the MAC entity itself, or by RRC for the events in accordance with TS 38.300 [2]. There is only one Random Access procedure ongoing at any point in time in a MAC entity. The Random Access procedure on an SCell or an LTM candidate cell shall only be initiated by a PDCCH order with *ra-PreambleIndex* different from 0b000000.

NOTE 1:    If a new Random Access procedure is triggered while another is already ongoing in the MAC entity, it is up to UE implementation whether to continue with the ongoing procedure or start with the new procedure (e.g. for SI request).

NOTE 2:    If there was an ongoing Random Access procedure that is triggered by a PDCCH order while the UE receives another PDCCH order for the same serving cell indicating the same Random Access Preamble, PRACH mask index and uplink carrier, the Random Access procedure is considered as the same Random Access procedure as the ongoing one and not initialized again.

When a Random Access procedure is initiated, UE selects a set of Random Access resources as specified in clause 5.1.1b and initialises the following parameters for the Random Access procedure according to the values configured by RRC for the selected="selected" set of Random Access resources:

-    *prach-ConfigurationIndex*: the available set of PRACH occasions for the transmission of the Random Access Preamble for Msg1. These are also applicable to the MSGA PRACH if the PRACH occasions are shared between 2-step and 4-step RA types;

-    *prach-ConfigurationPeriodScaling-IAB*: the scaling factor defined in TS 38.211 [8] and applicable to IAB-MTs, extending the periodicity of the PRACH occasions baseline configuration indicated by *prach-ConfigurationIndex*;

-    *prach-ConfigurationFrameOffset-IAB*: the frame offset defined in TS 38.211 [8] and applicable to IAB-MTs, altering the ROs frame defined in the baseline configuration indicated by *prach-ConfigurationIndex*;

-    *prach-ConfigurationSOffset-IAB*: the subframe/slot offset defined in TS 38.211 [8] and applicable to IAB-MTs, altering the ROs subframe or slot defined in the baseline configuration indicated by *prach-ConfigurationIndex*;

-    *msgA-**PRACH**-ConfigurationIndex*: the available set of PRACH occasions for the transmission of the Random Access Preamble for MSGA in 2-step RA type;

-    *preambleReceivedTargetPower*: initial Random Access Preamble power for 4-step RA type;

-    *sbfd-RACH-SingleConfig-preambleReceivedTargetPower*: initial Random Access Preamble power for 4-step RA type associated with the second PRACH occasions as defined in TS 38.213 [6];

-    *msgA-PreambleReceivedTargetPower*: initial Random Access Preamble power for 2-step RA type;

-    *rsrp-ThresholdSSB*: an RSRP threshold for the selection of the SSB for 4-step RA type. If the Random Access procedure is initiated for beam failure recovery, *rsrp-ThresholdSSB* used for the selection of the SSB within *candidateBeamRSList* refers to *rsrp-ThresholdSSB* in *BeamFailureRecoveryConfig* IE;

-    *rsrp-ThresholdCSI-RS*: an RSRP threshold for the selection of CSI-RS for 4-step RA type. If the Random Access procedure is initiated for beam failure recovery, *rsrp-ThresholdCSI-RS* is equal to *rsrp-ThresholdSSB* in *BeamFailureRecoveryConfig* IE;

-    *msgA-RSRP-ThresholdSSB*: an RSRP threshold for the selection of the SSB for 2-step RA type;

-    *rsrp-ThresholdSSB-SUL*: an RSRP threshold for the selection between the NUL carrier and the SUL carrier;

*-*    *msgA-RSRP-Threshold*: an RSRP threshold for selection between 2-step RA type and 4-step RA type when both 2-step and 4-step RA type Random Access Resources are configured in the UL BWP;

*-*    *rsrp-ThresholdMsg1-RepetitionNum2*: an RSRP threshold for Msg1 repetition with repetition number 2 (see clause 5.1.1b);

*-*    *rsrp-ThresholdMsg1-RepetitionNum4*: an RSRP threshold for Msg1 repetition with repetition number 4 (see clause 5.1.1b);

*-*    *rsrp-ThresholdMsg1-RepetitionNum8*: an RSRP threshold for Msg1 repetition with repetition number 8 (see clause 5.1.1b);

*-*    *sbfd-RSRP-ThresholdMsg1-RepetitionNum2*: an RSRP threshold for Msg1 repetition with repetition number 2 associated with the second PRACH occasions as defined in TS 38.213 [6] (see clause 5.1.1b);

*-*    *sbfd-RSRP-ThresholdMsg1-RepetitionNum4*: an RSRP threshold for Msg1 repetition with repetition number 4 associated with the second PRACH occasions as defined in TS 38.213 [6] (see clause 5.1.1b);

*-*    *sbfd-RSRP-ThresholdMsg1-RepetitionNum8*: an RSRP threshold for Msg1 repetition with repetition number 8 associated with the second PRACH occasions as defined in TS 38.213 [6] (see clause 5.1.1b);

*-*    *rsrp-ThresholdMsg3*: an RSRP threshold for Msg3 repetition (see clause 5.1.1b);

*-*    *sbfd-RSRP-ThresholdRO-Type*: an RSRP threshold for the selection of the initial RO type between the first PRACH occasions and the second PRACH occasions as defined in TS 38.213 [6] in contention-based Random Access procedure;

*-*    *sbfd-RSRP-ThresholdRO-TypeUsage*: indicates how *sbfd-RSRP-ThresholdRO-Type* is used in initial RO type selection;

-    *sib1-rsrp-ThresholdSSB*: an RSRP threshold for the selection of the SSB for SIB1 request;

*-*    *FeatureCombination*: feature or a combination of features associated with a set of Random Access resources;

*-*    *featurePriorities*: priorities for features, such as (e)RedCap, Slicing, etc. (see clause 5.1.1d);

-    *msgA-TransMax*: The maximum number of MSGA transmissions when both 4-step and 2-step RA type Random Access Resources are configured;

-    *candidateBeamRSList*: a list of reference signals (CSI-RS and/or SSB) identifying the candidate beams for recovery and the associated Random Access parameters;

-    *recoverySearchSpaceId*: the search space identity for monitoring the response of the beam failure recovery request;

-    *powerRampingStep*: the power-ramping factor;

-    *msgA-PreamblePowerRampingStep*: the power ramping factor for MSGA preamble;

-    *powerRampingStepHighPriority*: the power-ramping factor in case of prioritized Random Access procedure;

-    *scalingFactorBI*: a scaling factor for prioritized Random Access procedure;

-    *ra-PreambleIndex*: Random Access Preamble;

-    *ra-ssb-OccasionMaskIndex*: defines PRACH occasion(s) associated with an SSB in which the MAC entity may transmit a Random Access Preamble (see clause 7.4);

-    *msgA-SSB-SharedRO-MaskIndex*: Indicates the subset of 4-step RA type PRACH occasions shared with 2-step RA type PRACH occasions for each SSB. If 2-step RA type PRACH occasions are shared with 4-step RA type PRACH occasions and *msgA-SSB-SharedRO-MaskIndex* is not configured, then all 4-step RA type PRACH occasions are available for 2-step RA type (see clause 7.4);

-    *ssb-SharedRO-MaskIndex*: defines PRACH occasions, on which preambles are allocated for a feature or a combination of features, associated with an SSB in which the MAC entity may transmit a Random Access Preamble (see clause 7.4);

-    *ra-OccasionList*: defines PRACH occasion(s) associated with a CSI-RS in which the MAC entity may transmit a Random Access Preamble;

-    *ra-PreambleStartIndex*: the starting index of Random Access Preamble(s) for on-demand SI request;

-    *sib1-RA-PreambleStartIndex*: the starting index of Random Access Preamble(s) for SIB1 request;

-    *startPreambleForThisPartition*: the first preamble associated with the set of Random Access Resources applicable to the Random Access procedure;

-    *preambleTransMax*: the maximum number of Random Access Preamble transmission;

-    *preambleTransMax-Msg1-Repetition*: the maximum number of Random Access Preamble transmissions with a given Msg1 repetition number before switching to Msg1 repetition with the next available higher Msg1 repetition number;

-    *preambleTransMaxRO-Type*: the maximum number of Random Access Preamble transmissions before switching RO type between the first PRACH occasions and the second PRACH occasions as defined in TS 38.213 [6];

-    *ssb-perRACH-OccasionAndCB-PreamblesPerSSB*: defines the number of SSBs mapped to each PRACH occasion for 4-step RA type and the number of contention-based Random Access Preambles mapped to each SSB;

-    *msgA-CB-PreamblesPerSSB-PerSharedRO*: defines the number of contention-based Random Access Preambles for 2-step RA type mapped to each SSB when the PRACH occasions are shared between 2-step and 4-step RA types;

-    *msgA-**SSB-PerRACH-OccasionAndCB-PreamblesPerSSB*: defines the number of SSBs mapped to each PRACH occasion for 2-step RA type and the number of contention-based Random Access Preambles mapped to each SSB;

-    *numberOfPreamblesPerSSB-ForThisPartition*: defines the number of consecutive preambles for a feature or a combination of features mapped to each SSB;

-    *msgA-PUSCH-ResourceGroupA*: defines MSGA PUSCH resources that the UE shall use when performing MSGA transmission using Random Access Preambles group A;

-    *msgA-PUSCH-ResourceGroupB*: defines MSGA PUSCH resources that the UE shall use when performing MSGA transmission using Random Access Preambles group B;

-    *msgA-PUSCH-**R**esource-Index*: identifies the index of the PUSCH resource used for MSGA in case of contention-free Random Access with 2-step RA type;

-    if *groupBconfigured* is configured, then Random Access Preambles group B is configured for 4-step RA type.

-    Amongst the contention-based Random Access Preambles associated with an SSB (as defined in TS 38.213 [6]), the first *numberOfRA-PreamblesGroupA* included in *groupBconfigured* Random Access Preambles belong to Random Access Preambles group A. The remaining Random Access Preambles associated with the SSB belong to Random Access Preambles group B (if configured).

-    if *groupB-ConfiguredTwoStepRA* is configured, then Random Access Preambles group B is configured for 2-step RA type.

-    Amongst the contention-based Random Access Preambles for 2-step RA type associated with an SSB (as defined in TS 38.213 [6]), the first *numberOfRA-PreamblesGroupA* included in *GroupB-ConfiguredTwoStepRA* Random Access Preambles belong to Random Access Preambles group A. The remaining Random Access Preambles associated with the SSB belong to Random Access Preambles group B (if configured).

NOTE 3:    If Random Access Preambles group B is supported by the cell Random Access Preambles group B is included for each SSB.

-    if Random Access Preambles group B is configured for 4-step RA type:

-    *ra-Msg3SizeGroupA*: the threshold to determine the groups of Random Access Preambles for 4-step RA type;

-    *msg3-DeltaPreamble*: ∆*PREAMBLE_Msg3* in TS 38.213 [6];

-    *messagePowerOffsetGroupB*: the power offset for preamble selection included in *groupBconfigured*;

-    *numberOfRA-PreamblesGroupA*: defines the number of Random Access Preambles in Random Access Preamble group A for each SSB included in *groupBconfigured*.

-    if Random Access Preambles group B is configured for 2-step RA type:

-    *msgA-DeltaPreamble*: ∆*MsgA**_PUSCH* in TS 38.213 [6];

-    *messagePowerOffsetGroupB*: the power offset for preamble selection included in *GroupB-ConfiguredTwoStepRA*;

-    *numberOfRA-PreamblesGroupA*: defines the number of Random Access Preambles in Random Access Preamble group A for each SSB included in *GroupB-ConfiguredTwoStepRA*;

-    *ra-MsgA**-**SizeGroupA*: the threshold to determine the groups of Random Access Preambles for 2-step RA type.

-    the set of Random Access Preambles and/or PRACH occasions for SI request, if any;

-    the set of Random Access Preambles and/or PRACH occasions for SIB1 request, if any;

-    the set of Random Access Preambles and/or PRACH occasions for beam failure recovery request, if any;

-    the set of Random Access Preambles and/or PRACH occasions for reconfiguration with sync, if any;

-    *ra-ResponseWindow*: the time window to monitor RA response(s) (SpCell only);

-    *ra-ContentionResolutionTimer*: the Contention Resolution Timer (SpCell only);

-    *msgB-ResponseWindow*: the time window to monitor RA response(s) for 2-step RA type (SpCell only).

In addition, the following information for related Serving Cell is assumed to be available for UEs:

-    if Random Access Preambles group B is configured:

-    if the Serving Cell for the Random Access procedure is configured with supplementary uplink as specified in TS 38.331 [5], and SUL carrier is selected="selected" for performing Random Access Procedure:

-    PCMAX,f,c of the SUL carrier as specified in TS 38.101-1 [14], TS 38.101-2 [15], and TS 38.101-3 [16].

-    else:

-    PCMAX,f,c of the NUL carrier as specified in TS 38.101-1 [14], TS 38.101-2 [15], and TS 38.101-3 [16].

The following UE variables are used for the Random Access procedure:

-    *PREAMBLE_INDEX*;

-    *PREAMBLE_TRANSMISSION_COUNTER*;

-    *PREAMBLE_POWER_RAMPING_COUNTER*;

-    *PREAMBLE_POWER_RAMPING_STEP*;

-    *PREAMBLE_RECEIVED_TARGET_POWER*;

-    *PREAMBLE_BACKOFF*;

-    *PCMAX*;

-    *SCALING_FACTOR_BI*;

-    *TEMPORARY_C-RNTI*;

-    *RA_TYPE*;

-    *POWER_OFFSET_2STEP_RA*;

-    *MSGA_**PREAMBLE_POWER_RAMPING_STEP*;

-    *RO_TYPE*;

-    *POWER_OFFSET_RO_TYPE*;

-    *PREVIOUS_RO_TYPE_PREAMBLE_POWER_RAMPING_STEP*.

When the Random Access procedure is initiated on a Serving Cell or for an LTM candidate cell, the MAC entity shall:

1>	    flush the Msg3 buffer;

1>	    flush the MSGA buffer;

1>	    set the *PREAMBLE_TRANSMISSION_COUNTER* to 1;

1>	    if the Random Access procedure is initiated on a Serving Cell; or

1>	    if the Random Access procedure is initiated by the PDCCH order for an LTM candidate cell and the PDCCH order indicates preamble initial transmission; or

1>	    if the Random Access procedure is initiated by the PDCCH order for an LTM candidate cell, which is different from the cell to which the MAC entity performed the last Random Access Preamble transmission, and the PDCCH order indicates preamble re-transmission:

	2>	    set the *PREAMBLE_POWER_RAMPING_COUNTER* to 1;

1>	    set the *PREAMBLE_BACKOFF* to 0 ms;

1>	    set *POWER_OFFSET_2STEP_RA* to 0 dB;

1>	    set *POWER_OFFSET_RO_TYPE* to 0 dB;

1>	    if the carrier to use for the Random Access procedure is explicitly signalled:

	2>	    select the signalled carrier for performing Random Access procedure;

	2>	    set the *PCMAX* to PCMAX,f,c of the signalled carrier.

1>	    else if the carrier to use for the Random Access procedure is not explicitly signalled; and

1>	    if the Serving Cell for the Random Access procedure is configured with supplementary uplink as specified in TS 38.331 [5]; and

1>	    if the RSRP of the downlink pathloss reference is less than *rsrp-ThresholdSSB-SUL*:

	2>	    select the SUL carrier for performing Random Access procedure;

	2>	    set the *PCMAX* to PCMAX,f,c of the SUL carrier.

1>	    else:

	2>	    select the NUL carrier for performing Random Access procedure;

	2>	    set the *PCMAX* to PCMAX,f,c of the NUL carrier.

NOTE 4:    Void.

1>	    perform the BWP operation as specified in clause 5.15, except when the Random Access procedure is initiated by the PDCCH order for an LTM candidate cell;

1>	    if the Random Access procedure is initiated by PDCCH order and if the *ra-PreambleIndex* explicitly provided by PDCCH is not 0b000000 and if the RACH occasion indicator is set to 1 (as specified in TS 38.212 [9]); or

1>	    if the Random Access procedure was initiated for SpCell beam failure recovery (as specified in clause 5.17) and if the contention-free Random Access Resources for beam failure recovery request for 4-step RA type have been explicitly provided by RRC for the BWP selected="selected" for Random Access procedure and if the *ra-OccasionType* is set to *sbfd* for the Random Access procedure (as specified in TS 38.331 [5]); or

1>	    if the Random Access procedure was initiated for reconfiguration with sync not initiated for recovery using an LTM candidate configuration as specified in TS 38.331 [5] clause 5.3.7.3 and if the contention-free Random Access Resources for 4-step RA type have been explicitly provided in *rach-ConfigDedicated* for the BWP selected="selected" for Random Access procedure and if the *ra-OccasionType* is set to *sbfd* for the Random Access procedure (as specified in TS 38.331 [5]):

	2>	    set the *RO_TYPE* to *2nd-RO*.

1>	    else if neither contention-free Random Access Resources nor Random Access resources for SI request have been provided for this Random Access procedure and either *sbfd-RACH-SingleConfig* or *sbfd-RACH-DualConfig* is configured by RRC for the Random Access procedure (as specified in TS 38.331 [5]):

	2>	    if the *sbfd-RO-Type* is set to *sbfd* for the Random Access procedure (as specified in TS 38.331 [5]):

		3>	    set the *RO_TYPE* to *2nd-RO*.

	2>	    else if the *sbfd-RO-Type* is set to *non-**sbfd* for the Random Access procedure (as specified in TS 38.331 [5]):

		3>	    set the *RO_TYPE* to *1st-RO*.

	2>	    else if the *sbfd-RO-Type* is not configured for the Random Access procedure:

		3>	    if *sbfd-RSRP-ThresholdRO-Type* and *sbfd-RSRP-ThresholdRO-TypeUsage* are configured for the Random Access procedure (see TS 38.331 [5]):

			4>	    if the RSRP of the downlink pathloss reference is below *sbfd-RSRP-ThresholdRO-Type*, and *sbfd-RSRP-ThresholdRO-TypeUsage* is set to *below* (as specified in TS 38.331 [5]); or

			4>	    if the RSRP of the downlink pathloss reference is above *sbfd-RSRP-ThresholdRO-Type*, and *sbfd-RSRP-ThresholdRO-TypeUsage* is set to *above* (as specified in TS 38.331 [5]):

				5>	    set the *RO_TYPE* to *2nd-RO*.

			4>	    else:

				5>	    set the *RO_TYPE* to *1st-RO*.

NOTE 5:    If *sbfd-RO-Type*, *sbfd-RSRP-ThresholdRO-Type*, and *sbfd-RSRP-ThresholdRO-TypeUsage* are not configured for the Random Access procedure, it is up to UE implementation how to set the *RO_TYPE* between *1st-RO* and *2nd-RO* as the initial RO type for the Random Access procedure.

1>	    else:

	2>	    set the *RO_TYPE* to *1st-RO*.

1>	    select the set of Random Access resources applicable to the current Random Access procedure according to clause 5.1.1b;

1>	    if the Random Access procedure is initiated by PDCCH order and if the *ra-PreambleIndex* explicitly provided by PDCCH is not 0b000000; or

1>	    if the Random Access procedure was initiated for SI request (as specified in TS 38.331 [5]) and the Random Access Resources for SI request have been explicitly provided by RRC; or

1>	    if the Random Access procedure was initiated for SpCell beam failure recovery (as specified in clause 5.17) and if the contention-free Random Access Resources for beam failure recovery request for 4-step RA type have been explicitly provided by RRC for the BWP selected="selected" for Random Access procedure; or

1>	    if the Random Access procedure was initiated for reconfiguration with sync not initiated for recovery using an LTM candidate configuration as specified in TS 38.331 [5] clause 5.3.7.3 and if the contention-free Random Access Resources for 4-step RA type have been explicitly provided in *rach-ConfigDedicated* for the BWP selected="selected" for Random Access procedure; or

1>	    if the contention-free Random Access Resources have been explicitly provided in the (Enhanced) LTM Cell Switch Command MAC CE; or

1>	    if the *RO_TYPE* is set to *2nd-RO*; or

1>	    if the Random Access procedure was initiated for SIB1 request (as specified in TS 38.331 [5]) and the Random Access Resources for SIB1 request have been provided by RRC:

	2>	    set the *RA_TYPE* to *4-stepRA*.

1>	    else if the BWP selected="selected" for Random Access procedure is configured with both 2-step and 4-step RA type Random Access Resources within the selected="selected" set of Random Access resources (as specified in clause 5.1.1b) and the RSRP of the downlink pathloss reference is above *msgA-RSRP-Threshold*; or

1>	    if the BWP selected="selected" for Random Access procedure is only configured with 2-step RA type Random Access resources within the selected="selected" set of Random Access resources according to clause 5.1.1b; or

1>	    if the Random Access procedure was initiated for reconfiguration with sync not initiated for recovery using an LTM candidate configuration as specified in TS 38.331 [5] clause 5.3.7.3 and if the contention-free Random Access Resources for 2-step RA type have been explicitly provided in *rach-ConfigDedicated* for the BWP selected="selected" for Random Access procedure:

	2>	    set the *RA_TYPE* to *2-stepRA*.

1>	    else:

	2>	    set the *RA_TYPE* to *4-stepRA*.

1>	    perform initialization of variables specific to Random Access type as specified in clause 5.1.1a;

1>	    if *RA_TYPE* is set to *2-stepRA*:

	2>	    perform the Random Access Resource selection procedure for 2-step RA type (see clause 5.1.2a).

1>	    else:

	2>	    perform the Random Access Resource selection procedure (see clause 5.1.2).

### 5.1.1a     Initialization of variables specific to Random Access type [#](#5-1-1a-initialization-of-variables-specific-to-random-access-type)

The MAC entity shall:

1>	    if *RA_TYPE* is set to *2-stepRA*:

	2>	    set *PREAMBLE_POWER_RAMPING_STEP* to *msgA-PreamblePowerRampingStep*;

	2>	    set *SCALING_FACTOR_BI* to 1;

	2>	    apply *preambleTransMax* included in the *RACH-ConfigGenericTwoStepRA*;

	2>	    if the Random Access procedure was initiated for reconfiguration with sync not initiated for recovery using an LTM candidate configuration as specified in TS 38.331 [5] clause 5.3.7.3 or for SCG activation; and

	2>	    if *cfra-TwoStep* is configured for the selected="selected" carrier:

		3>	    if *msgA-TransMax* is configured in the *cfra-TwoStep*:

			4>	    apply *msgA-TransMax* configured in the *cfra-TwoStep*.

	2>	    else if *msgA-TransMax* is included in the *RACH-ConfigCommonTwoStepRA*:

		3>	    apply *msgA-TransMax* included in the *RACH-ConfigCommonTwoStepRA*.

	2>	    if the Random Access procedure was initiated for SpCell beam failure recovery (as specified in clause 5.17); and

	2>	    if *beamFailureRecoveryConfig* is configured for the active UL BWP of the selected="selected" carrier; and

	2>	    if *ra-PrioritizationTwoStep* is configured in the *beamFailureRecoveryConfig*:

		3>	    set *PREAMBLE_POWER_RAMPING_STEP* to the *powerRampingStepHighPriority* included in the *ra-PrioritizationTwoStep* in *beamFailureRecoveryConfig*;

		3>	    if *scalingFactorBI* is configured in the *ra-PrioritizationTwoStep* in *beamFailureRecoveryConfig*:

			4>	    set *SCALING_FACTOR_BI* to the *scalingFactorBI*.

	2>	    else if the Random Access procedure was initiated for reconfiguration with sync not initiated for recovery using an LTM candidate configuration as specified in TS 38.331 [5] clause 5.3.7.3 or for SCG activation; and

	2>	    if *rach-ConfigDedicated* is configured for the selected="selected" carrier; and

	2>	    if *ra-PrioritizationTwoStep* is configured in the *rach-ConfigDedicated*:

		3>	    set *PREAMBLE_POWER_RAMPING_STEP* to the *powerRampingStepHighPriority* included in the *ra-PrioritizationTwoStep* in *rach-ConfigDedicated*;

		3>	    if *scalingFactorBI* is configured in *ra-PrioritizationTwoStep* in the *rach-ConfigDedicated*:

			4>	    set *SCALING_FACTOR_BI* to the *scalingFactorBI*.

	2>	    else if both *ra-PrioritizationForSlicingTwoStep* for a *NSAG-ID* and *ra-PrioritizationForAccessIdentityTwoStep* are configured for the selected="selected" carrier; and

	2>	    if the MAC entity is provided by upper layers with both this *NSAG-ID* and Access Identity 1 or 2; and

	2>	    if for at least one of these Access Identities the corresponding bit in the *ra-**PrioritizationForAI* is set to *one*:

		3>	    if *enableRA-PrioritizationForSlicing* is set to *true*:

			4>	    if *powerRampingStepHighPriority* is configured in the *ra-PrioritizationForSlicingTwoStep* for this *NSAG-ID*:

				5>	    set *PREAMBLE_POWER_RAMPING_STEP* to the *powerRampingStepHighPriority*.

			4>	    if *scalingFactorBI* is configured in the *ra-PrioritizationForSlicingTwoStep* for this *NSAG-ID*:

				5>	    set *SCALING_FACTOR_BI* to the *scalingFactorBI*.

		3>	    else if *enableRA-PrioritizationForSlicing* is set to *false*:

			4>	    if *powerRampingStepHighPriority* is configured in the *ra-PrioritizationForAccessIdentityTwoStep*:

				5>	    set *PREAMBLE_POWER_RAMPING_STEP* to the *powerRampingStepHighPriority*.

			4>	    if *scalingFactorBI* is configured in the *ra-PrioritizationForAccessIdentityTwoStep*:

				5>	    set *SCALING_FACTOR_BI* to the *scalingFactorBI*.

	2>	    else if *ra-PrioritizationForSlicingTwoStep* for a *NSAG-ID* is configured for the selected="selected" carrier; and

	2>	    if the MAC entity is provided by upper layers with this *NSAG-ID*:

		3>	    if *powerRampingStepHighPriority* is configured in the *ra-PrioritizationForSlicingTwoStep* for this *NSAG-ID*:

			4>	    set *PREAMBLE_POWER_RAMPING_STEP* to the *powerRampingStepHighPriority*.

		3>	    if *scalingFactorBI* is configured in the *ra-PrioritizationForSlicingTwoStep* for this *NSAG-ID*:

			4>	    set *SCALING_FACTOR_BI* to the *scalingFactorBI*.

	2>	    else if *ra-PrioritizationForAccessIdentityTwoStep* is configured for the selected="selected" carrier; and

	2>	    if the MAC entity is provided by upper layers with Access Identity 1 or 2; and

	2>	    if for at least one of these Access Identities the corresponding bit in the *ra-**PrioritizationForAI* is set to *one*:

		3>	    if *powerRampingStepHighPriority* is configured in the *ra-PrioritizationForAccessIdentityTwoStep*:

			4>	    set *PREAMBLE_POWER_RAMPING_STEP* to the *powerRampingStepHighPriority*.

		3>	    if *scalingFactorBI* is configured in the *ra-PrioritizationForAccessIdentityTwoStep*:

			4>	    set *SCALING_FACTOR_BI* to the *scalingFactorBI*.

	2>	    set *MSGA_PREAMBLE_POWER_RAMPING_STEP* to *PREAMBLE_POWER_RAMPING_STEP*.

1>	    else (i.e. *RA_TYPE* is set to *4-stepRA*):

	2>	    set *PREAMBLE_POWER_RAMPING_STEP* to *powerRampingStep*;

	2>	    set *SCALING_FACTOR_BI* to 1;

	2>	    set *preambleTransMax* to *preambleTransMax* included in the *RACH-ConfigGeneric*;

	2>	    if the Random Access procedure was initiated for SpCell beam failure recovery (as specified in clause 5.17); and

	2>	    if *beamFailureRecoveryConfig* is configured for the active UL BWP of the selected="selected" carrier:

		3>	    start the *beamFailureRecoveryTimer*, if configured;

		3>	    apply the parameters *powerRampingStep*, *preambleReceivedTargetPower*, and *preambleTransMax* configured in the *beamFailureRecoveryConfig*.

	2>	    if the Random Access procedure was initiated for beam failure recovery (as specified in clause 5.17); and

	2>	    if *beamFailureRecoveryConfig* is configured for the active UL BWP of the selected="selected" carrier; and

	2>	    if *ra-Prioritization* is configured in the *beamFailureRecoveryConfig*:

		3>	    set *PREAMBLE_POWER_RAMPING_STEP* to the *powerRampingStepHighPriority* included in the *ra-Prioritization* in *beamFailureRecoveryConfig*;

		3>	    if *scalingFactorBI* is configured in *ra-Prioritization* in the *beamFailureRecoveryConfig*:

			4>	    set *SCALING_FACTOR_BI* to the *scalingFactorBI*.

	2>	    else if the Random Access procedure was initiated for reconfiguration with sync not initiated for recovery using an LTM candidate configuration as specified in TS 38.331 [5] clause 5.3.7.3 or for SCG activation; and

	2>	    if *rach-ConfigDedicated* is configured for the selected="selected" carrier; and

	2>	    if *ra-Prioritization* is configured in the *rach-ConfigDedicated*:

		3>	    set *PREAMBLE_POWER_RAMPING_STEP* to the *powerRampingStepHighPriority* included in the *ra-Prioritization* in *rach-ConfigDedicated*;

		3>	    if *scalingFactorBI* is configured in *ra-Prioritization* in the *rach-ConfigDedicated*:

			4>	    set *SCALING_FACTOR_BI* to the *scalingFactorBI*.

	2>	    else if both *ra-PrioritizationForSlicing* for a *NSAG-ID* and *ra-PrioritizationForAccessIdentity* are configured for the selected="selected" carrier; and

	2>	    if the MAC entity is provided by upper layers with both this *NSAG-ID* and Access Identity 1 or 2; and

	2>	    if for at least one of these Access Identities the corresponding bit in the *ra-**PrioritizationForAI* is set to *one*:

		3>	    if *enableRA-PrioritizationForSlicing* is set to *true*:

			4>	    if *powerRampingStepHighPriority* is configured in the *ra-PrioritizationForSlicing* for this *NSAG-ID*:

				5>	    set *PREAMBLE_POWER_RAMPING_STEP* to the *powerRampingStepHighPriority*.

			4>	    if *scalingFactorBI* is configured in the *ra-PrioritizationForSlicing* for this *NSAG-ID*:

				5>	    set *SCALING_FACTOR_BI* to the *scalingFactorBI*.

		3>	    else if *enableRA-PrioritizationForSlicing* is set to *false*:

			4>	    if *powerRampingStepHighPriority* is configured in the *ra-PrioritizationForAccessIdentity*:

				5>	    set *PREAMBLE_POWER_RAMPING_STEP* to the *powerRampingStepHighPriority*.

			4>	    if *scalingFactorBI* is configured in the *ra-PrioritizationForAccessIdentity*:

				5>	    set *SCALING_FACTOR_BI* to the *scalingFactorBI*.

	2>	    else if *ra-PrioritizationForSlicing* for a *NSAG-ID* is configured for the selected="selected" carrier; and

	2>	    if the MAC entity is provided by upper layers with this *NSAG-ID*:

		3>	    if *powerRampingStepHighPriority* is configured in the *ra-PrioritizationForSlicing* for this *NSAG-ID*:

			4>	    set *PREAMBLE_POWER_RAMPING_STEP* to the *powerRampingStepHighPriority*.

		3>	    if *scalingFactorBI* is configured in the *ra-PrioritizationForSlicing* for this *NSAG-ID*:

			4>	    set *SCALING_FACTOR_BI* to the *scalingFactorBI*.

	2>	    else if *ra-PrioritizationForAccessIdentity* is configured for the selected="selected" carrier; and

	2>	    if the MAC entity is provided by upper layers with Access Identity 1 or 2; and

	2>	    if for at least one of these Access Identities the corresponding bit in the *ra-**PrioritizationForAI* is set to *one*:

		3>	    if *powerRampingStepHighPriority* is configured in the *ra-PrioritizationForAccessIdentity*:

			4>	    set *PREAMBLE_POWER_RAMPING_STEP* to the *powerRampingStepHighPriority*.

		3>	    if *scalingFactorBI* is configured in the *ra-PrioritizationForAccessIdentity*:

			4>	    set *SCALING_FACTOR_BI* to the *scalingFactorBI*.

	2>	    if *RA_TYPE* is switched from *2-stepRA* to *4-stepRA* during this Random Access procedure:

		3>	    set *POWER_OFFSET_2STEP_RA* to (*PREAMBLE_POWER_RAMPING_COUNTER* – 1) × (*MSGA_PREAMBLE_POWER_RAMPING_STEP* – *PREAMBLE_POWER_RAMPING**_STEP*).

NOTE:    If *enableRA-PrioritizationForSlicing* is not configured in *BWP-UplinkCommon* and if both the provided *NSAG-ID* and the provided Access Identity whose corresponding bit in the *ra-**PrioritizationForAI* is set to *one* are configured with *ra-Prioritization* either in *RACH-ConfigCommon* or *RACH-ConfigCommonTwoStepRA*, it is up to UE implementation how to determine the values of *PREAMBLE_POWER_RAMPING_STEP* and *SCALING_FACTOR_BI*.

### 5.1.1b     Selection of the set of Random Access resources for the Random Access procedure [#](#5-1-1b-selection-of-the-set-of-random-access-resources-for-the-random-access-procedure)

The MAC entity shall:

1>	    if the BWP selected="selected" for Random Access procedure is configured with both set(s) of Random Access resources with *msg3-Repetitions* set to *true* and set(s) of Random Access resources without *msg3-Repetitions* set to *true* and the RSRP of the downlink pathloss reference is less than *rsrp-ThresholdMsg3*; or

1>	    if the BWP selected="selected" for Random Access procedure is only configured with the set(s) of Random Access resources with *msg3-Repetitions* set to *true*:

	2>	    assume Msg3 repetition is applicable for the current Random Access procedure.

1>	    else:

	2>	    assume Msg3 repetition is not applicable for the current Random Access procedure.

1>	    if contention-free Random Access Resources have been provided for this Random Access procedure in the (Enhanced) LTM Cell Switch Command MAC CE and a non-zero Msg1 repetition number is indicated in the (Enhanced) LTM Cell Switch Command MAC CE:

	2>	    assume that Msg1 repetition is applicable and that the Msg1 repetition number applicable for the current Random Access procedure is the Msg1 repetition number indicated in the (Enhanced) LTM Cell Switch Command MAC CE.

1>	    else if contention-free Random Access Resources have been provided for this Random Access procedure and a Msg1 repetition number is indicated in *rach-ConfigDedicated*:

	2>	    assume Msg1 repetition is applicable and Msg1 repetition number applicable for the current Random Access procedure is the Msg1 repetition number indicated in *rach-ConfigDedicated*.

1>	    else if contention free Random Access Resources have not been provided for this Random Access procedure and the BWP selected="selected" for the Random Access procedure is configured with set(s) of Random Access resources with *msg1-Repetitions* set to *true* and set(s) of Random Access resources without *msg1-Repetitions* set to *true* for the selected="selected" RO type:

	2>	    if the *RO_TYPE* is set to *2nd-RO* and *sbfd-RACH-SingleConfig* is configured for the Random Access procedure (see TS 38.331 [5]):

		3>	    if the BWP selected="selected" for the Random Access procedure is configured with set(s) of Random Access resources associated with Msg1 repetition number 8, and the RSRP of the downlink pathloss reference is less than *sbfd-RSRP-ThresholdMsg1-RepetitionNum8* if configured, or less than *rsrp-ThresholdMsg1-RepetitionNum8* otherwise:

			4>	    assume Msg1 repetition is applicable and Msg1 repetition number applicable for the current Random Access procedure includes 8.

		3>	    if the BWP selected="selected" for the Random Access procedure is configured with set(s) of Random Access resources associated with Msg1 repetition number 4, and the RSRP of the downlink pathloss reference is less than *sbfd-RSRP-ThresholdMsg1-RepetitionNum4* if configured, or less than *rsrp-ThresholdMsg1-RepetitionNum4* otherwise:

			4>	    assume Msg1 repetition is applicable and Msg1 repetition number applicable for the current Random Access procedure includes 4.

		3>	    if the BWP selected="selected" for the Random Access procedure is configured with set(s) of Random Access resources associated with Msg1 repetition number 2, and the RSRP of the downlink pathloss reference is less than *sbfd-RSRP-ThresholdMsg1-RepetitionNum2* if configured, or less than *rsrp-ThresholdMsg1-RepetitionNum2* otherwise:

			4>	    assume Msg1 repetition is applicable and Msg1 repetition number applicable for the current Random Access procedure includes 2.

		3>	    else if the RSRP of the downlink pathloss reference is not less than any configured *sbfd-**RSRP-ThresholdMsg1-RepetitionNumX*, and not less than any configured *rsrp-ThresholdMsg1-RepetitionNumX* if the *sbfd-**RSRP-ThresholdMsg1-RepetitionNumX* is not configured for the corresponding Msg1 repetition number:

			4>	    assume Msg1 repetition is not applicable for the current Random Access procedure.

	2>	    else if the *RO_TYPE* is set to *2nd-RO* and *sbfd-RACH-DualConfig* is configured for the Random Access procedure (see TS 38.331 [5]):

		3>	    if the BWP selected="selected" for the Random Access procedure is configured with set(s) of Random Access resources associated with Msg1 repetition number 8, and the RSRP of the downlink pathloss reference is less than *sbfd-RSRP-ThresholdMsg1-RepetitionNum8*:

			4>	    assume Msg1 repetition is applicable and Msg1 repetition number applicable for the current Random Access procedure includes 8.

		3>	    if the BWP selected="selected" for the Random Access procedure is configured with set(s) of Random Access resources associated with Msg1 repetition number 4, and the RSRP of the downlink pathloss reference is less than *sbfd-RSRP-ThresholdMsg1-RepetitionNum4*:

			4>	    assume Msg1 repetition is applicable and Msg1 repetition number applicable for the current Random Access procedure includes 4.

		3>	    if the BWP selected="selected" for the Random Access procedure is configured with set(s) of Random Access resources associated with Msg1 repetition number 2, and the RSRP of the downlink pathloss reference is less than *sbfd-RSRP-ThresholdMsg1-RepetitionNum2*:

			4>	    assume Msg1 repetition is applicable and Msg1 repetition number applicable for the current Random Access procedure includes 2.

		3>	    else if the RSRP of the downlink pathloss reference is not less than any configured *sbfd-**RSRP-ThresholdMsg1-RepetitionNumX*:

			4>	    assume Msg1 repetition is not applicable for the current Random Access procedure.

	2>	    else:

		3>	    if the BWP selected="selected" for the Random Access procedure is configured with set(s) of Random Access resources associated with Msg1 repetition number 8 and the RSRP of the downlink pathloss reference is less than *rsrp-ThresholdMsg1-RepetitionNum8*:

			4>	    assume Msg1 repetition is applicable and Msg1 repetition number applicable for the current Random Access procedure includes 8.

		3>	    if the BWP selected="selected" for the Random Access procedure is configured with set(s) of Random Access resources associated with Msg1 repetition number 4 and the RSRP of the downlink pathloss reference is less than *rsrp-ThresholdMsg1-RepetitionNum4*:

			4>	    assume Msg1 repetition is applicable and Msg1 repetition number applicable for the current Random Access procedure includes 4.

		3>	    if the BWP selected="selected" for the Random Access procedure is configured with set(s) of Random Access resources associated with Msg1 repetition number 2 and the RSRP of the downlink pathloss reference is less than *rsrp-ThresholdMsg1-RepetitionNum2*:

			4>	    assume Msg1 repetition is applicable and Msg1 repetition number applicable for the current Random Access procedure includes 2.

		3>	    else if the RSRP of the downlink pathloss reference is not less than any configured *rsrp-ThresholdMsg1-RepetitionNumX*:

			4>	    assume Msg1 repetition is not applicable for the current Random Access procedure.

1>	    else if the BWP selected="selected" for Random Access procedure is configured only with the set(s) of Random Access resources with *msg1-Repetitions* set to *true* for the selected="selected" RO type:

	2>	    assume Msg1 repetition is applicable for the current Random Access procedure;

	2>	    if the *RO_TYPE* is set to *2nd-RO* and *sbfd-RACH-SingleConfig* is configured for the Random Access procedure (see TS 38.331 [5]):

		3>	    if at least one of sbfd-RSRP-ThresholdMsg1-RepetitionNumX or one of rsrp-ThresholdMsg1-RepetitionNumX is configured:

			4>	    if *sbfd*-*RSRP-ThresholdMsg1-RepetitionNum8* is configured and the RSRP of the downlink pathloss reference is less than *sbfd*-*RSRP-ThresholdMsg1-RepetitionNum8*; or

			4>	    if *sbfd*-*RSRP-ThresholdMsg1-RepetitionNum8* is not configured, and *rsrp-ThresholdMsg1-RepetitionNum8* is configured, and the RSRP of the downlink pathloss reference is less than *rsrp-ThresholdMsg1-RepetitionNum8*:

				5>	    assume Msg1 repetition number applicable for the current Random Access procedure includes 8.

			4>	    if *sbfd*-*RSRP-ThresholdMsg1-RepetitionNum4* is configured and the RSRP of the downlink pathloss reference is less than *sbfd*-*RSRP-ThresholdMsg1-RepetitionNum4*; or

			4>	    if *sbfd*-*RSRP-ThresholdMsg1-RepetitionNum4* is not configured, and *rsrp-ThresholdMsg1-RepetitionNum4* is configured, and the RSRP of the downlink pathloss reference is less than *rsrp-ThresholdMsg1-RepetitionNum4*:

				5>	    assume Msg1 repetition number applicable for the current Random Access procedure includes 4.

			4>	    if *sbfd*-*RSRP-ThresholdMsg1-RepetitionNum2* is configured and the RSRP of the downlink pathloss reference is less than *sbfd*-*RSRP-ThresholdMsg1-RepetitionNum2*; or

			4>	    if *sbfd*-*RSRP-ThresholdMsg1-RepetitionNum2* is not configured, and *rsrp-ThresholdMsg1-RepetitionNum2* is configured, and the RSRP of the downlink pathloss reference is less than *rsrp-ThresholdMsg1-RepetitionNum2*:

				5>	    assume Msg1 repetition number applicable for the current Random Access procedure includes 2.

			4>	    else if the RSRP of the downlink pathloss reference is not less than any configured *sbfd-RSRP-ThresholdMsg1-RepetitionNumX*, and not less than any configured *rsrp-ThresholdMsg1-RepetitionNumX* if the *sbfd-RSRP-ThresholdMsg1-RepetitionNumX* is not configured for the corresponding Msg1 repetition number:

				5>	    assume Msg1 repetition number applicable for the current Random Access procedure is the lowest Msg1 repetition number configured for this BWP.

		3>	    else (i.e., none of sbfd-RSRP-ThresholdMsg1-RepetitionNumX and rsrp-ThresholdMsg1-RepetitionNumX are configured):

			4>	    assume Msg1 repetition number applicable for the current Random Access procedure is the Msg1 repetition number that configured for this BWP.

	2>	    else if the *RO_TYPE* is set to *2nd-RO* and *sbfd-RACH-DualConfig* is configured for the Random Access procedure (see TS 38.331 [5]):

		3>	    if at least one of sbfd-RSRP-ThresholdMsg1-RepetitionNumX is configured:

			4>	    if *sbfd*-*RSRP-ThresholdMsg1-RepetitionNum8* is configured and the RSRP of the downlink pathloss reference is less than *sbfd*-*RSRP-ThresholdMsg1-RepetitionNum8*:

				5>	    assume Msg1 repetition number applicable for the current Random Access procedure includes 8.

			4>	    if *sbfd*-*RSRP-ThresholdMsg1-RepetitionNum4* is configured and the RSRP of the downlink pathloss reference is less than *sbfd*-*RSRP-ThresholdMsg1-RepetitionNum4*:

				5>	    assume Msg1 repetition number applicable for the current Random Access procedure includes 4.

			4>	    if *sbfd*-*RSRP-ThresholdMsg1-RepetitionNum2* is configured and the RSRP of the downlink pathloss reference is less than *sbfd*-*RSRP-ThresholdMsg1-RepetitionNum2*:

				5>	    assume Msg1 repetition number applicable for the current Random Access procedure includes 2.

			4>	    else if the RSRP of the downlink pathloss reference is not less than any configured *sbfd-RSRP-ThresholdMsg1-RepetitionNumX*:

				5>	    assume Msg1 repetition number applicable for the current Random Access procedure is the lowest Msg1 repetition number configured for this BWP.

		3>	    else (i.e., none of *sbfd-RSRP-ThresholdMsg1-RepetitionNumX* is configured):

			4>	    assume Msg1 repetition number applicable for the current Random Access procedure is the Msg1 repetition number that configured for this BWP.

	2>	    else:

																															32>	    if at least one of *rsrp-ThresholdMsg1-RepetitionNumX* is configured:

			4>	    if *rsrp-ThresholdMsg1-RepetitionNum8* is configured and the RSRP of the downlink pathloss reference is less than *rsrp-ThresholdMsg1-RepetitionNum8*;

				5>	    assume Msg1 repetition number applicable for the current Random Access procedure includes 8.

			4>	    if *rsrp-ThresholdMsg1-RepetitionNum4* is configured and the RSRP of the downlink pathloss reference is less than *rsrp-ThresholdMsg1-RepetitionNum4*:

				5>	    assume Msg1 repetition number applicable for the current Random Access procedure includes 4.

			4>	    if *rsrp-ThresholdMsg1-RepetitionNum2* is configured and the RSRP of the downlink pathloss reference is less than *rsrp-ThresholdMsg1-RepetitionNum2*:

				5>	    assume Msg1 repetition number applicable for the current Random Access procedure includes 2.

			4>	    else if the RSRP of the downlink pathloss reference is not less than any configured *rsrp-ThresholdMsg1-RepetitionNumX*:

				5>	    assume Msg1 repetition number applicable for the current Random Access procedure is the lowest Msg1 repetition number configured for this BWP.

		3>	    else (none of *rsrp-ThresholdMsg1-RepetitionNumX* is configured):

			4>	    assume Msg1 repetition number applicable for the current Random Access procedure is the Msg1 repetition number that configured for this BWP.

1>	    if the Random Access procedure was initiated by SI request, SIB1 request, reconfiguration with sync, beam failure recovery, LTM Cell Switch, a PDCCH order for an LTM candidate cell, or a PDCCH order with the *PRACH association indicator* field in DCI set to 1; or

1>	    if Msg1 repetition is applicable for the current Random Access procedure:

	2>	    PRACH occasions configured by *addlRACH-Config-Adapt* in *RACH-ConfigCommon* of a set of Random Access resources are not applicable for this Random Access procedure.

1>	    else:

	2>	    PRACH occasions configured by *addlRACH-Config-Adapt* in *RACH-ConfigCommon* of a set of Random Access resources are applicable for this Random Access procedure, if available (as specified in TSs 38.213 [6] and 38.212 [9]).

NOTE 1:    Void.

1>	    if neither contention-free Random Access Resources nor Random Access Resources for SI request have been provided for this Random Access procedure and one or more of the features including (e)RedCap and/or Slicing and/or SDT and/or MSG3 repetition and/or MSG1 repetition is applicable for this Random Access procedure:

NOTE 2:    The applicability of SDT is determined by MAC entity according to clause 5.27. The applicability of *NSAG-ID* is determined by upper layers when the Random Access procedure is initiated. The applicability of (e)RedCap is also determined by upper layers when Random Access procedure is initiated and it is applicable to the Random Access procedures initiated by PDCCH orders and any Random Access procedure initiated by the MAC entity.

NOTE 3:    SDT is not applicable for the Random Access procedure initiated by upper layers for MT-SDT.

	2>	    if none of the sets of Random Access resources are available for any feature applicable to the current Random Access procedure (as specified in clause 5.1.1c):

		3>	    select the set(s) of Random Access resources that are not associated with any feature indication (as specified in clause 5.1.1c) for this Random Access procedure.

	2>	    else if there is one set of Random Access resources available which can be used for indicating all features triggering this Random Access procedure:

		3>	    select this set of Random Access resources for this Random Access procedure.

	2>	    else if there are more than one set of Random Access resources available which can be used for indicating all features triggering this Random Access procedure and Msg1 repetition is applicable for this Random Access procedure:

		3>	    select the set of Random Access resources that associated with highest repetition number among the sets of Random Access resources.

	2>	    else (i.e. there are one or more sets of Random Access resources available that are configured with indication(s) for a subset of all features triggering this Random Access procedure):

		3>	    select a set of Random Access resources from the available set(s) of Random Access resources based on the priority order indicated by upper layers as specified in clause 5.1.1d for this Random Access Procedure.

1>	    else if this Random Access procedure is initiated by PDCCH order with the *PRACH association indicator* field in DCI set to 1 and *SSB-MTC-AdditionalPCI* is configured by upper layers, as specified in clause 7.3.1.2.1 of TS 38.212 [9]:

	2>	    select the set of Random Access resources corresponding to the *additionalPCI* associated with active TCI states.

1>	    else if this Random Access procedure is initiated by PDCCH order for an LTM candidate cell:

	2>	    select the set of Random Access resources configured in *EarlyUL-SyncConfig* corresponding to the carrier and the cell indicated by the field *UL/SUL indicator* and the field *Cell indicator* in the PDCCH order respectively, as specified in TS 38.212 [9].

1>	    else if contention-free Random Access Resources have been provided for this Random Access procedure by PDCCH order:

	2>	    if RedCap is applicable for the current Random Access procedure:

		3>	    if there is one set of Random Access resources available that is only configured with RedCap indication:

			4>	    select this set of Random Access resources for this Random Access procedure.

		3>	    else:

			4>	    select the set of Random Access resources that is not associated with any feature indication (as specified in clause 5.1.1c) for this Random Access procedure.

	2>	    else if eRedCap is applicable for the current Random Access procedure:

		3>	    if there is one set of Random Access resources available that is only configured with eRedCap indication:

			4>	    select this set of Random Access resources for this Random Access procedure.

		3>	    else if there is one set of Random Access resources available that is only configured with RedCap indication:

			4>	    select this set of Random Access resources for this Random Access procedure.

		3>	    else:

			4>	    select the set of Random Access resources that is not associated with any feature indication (as specified in clause 5.1.1c) for this Random Access procedure.

	2>	    else:

		3>	    select the set of Random Access resources that is not associated with any feature indication (as specified in clause 5.1.1c) for this Random Access procedure.

1>	    else if contention-free Random Access Resources have been provided for this Random Access procedure in the (Enhanced) LTM Cell Switch Command MAC CE:

	2>	    if RedCap is applicable for this Random Access procedure:

		3>	    if a non-zero Msg1 repetition number is indicated in the (Enhanced) LTM Cell Switch Command MAC CE:

			4>	    select the set of Random Access resources that is only configured with RedCap indication and Msg1 repetition indication and associated with the indicated Msg1 repetition number for this Random Access procedure.

		3>	    else:

			4>	    if there is one set of Random Access resources available that is only configured with RedCap indication:

				5>	    select this set of Random Access resources for this Random Access procedure.

			4>	    else:

				5>	    select the set of Random Access resources that is not associated with any feature indication (as specified in clause 5.1.1c) for this Random Access procedure.

	2>	    else if eRedCap is applicable for this Random Access procedure:

		3>	    if a non-zero Msg1 repetition number is indicated in the (Enhanced) LTM Cell Switch Command MAC CE:

			4>	    select the set of Random Access resources that is only configured with eRedCap indication and Msg1 repetition indication and associated with the indicated Msg1 repetition number for this Random Access procedure.

		3>	    else:

			4>	    if there is one set of Random Access resources available that is only configured with eRedCap indication:

				5>	    select this set of Random Access resources for this Random Access procedure.

			4>	    else if there is one set of Random Access resources available that is only configured with RedCap indication:

				5>	    select this set of Random Access resources for this Random Access procedure.

			4>	    else:

				5>	    select the set of Random Access resources that is not associated with any feature indication (as specified in clause 5.1.1c) for this Random Access procedure.

	2>	    else:

		3>	    if a non-zero Msg1 repetition number is indicated in the (Enhanced) LTM Cell Switch Command MAC CE:

			4>	    select the set of Random Access resources that is only configured with Msg1 repetition indication and associated with the indicated Msg1 repetition number for this Random Access procedure.

		3>	    else:

			4>	    select the set of Random Access resources that is not associated with any feature indication (as specified in clause 5.1.1c) for this Random Access procedure.

1>	    else if contention-free Random Access Resources have been provided for this Random Access procedure in *rach-ConfigDedicated*:

	2>	    if RedCap is applicable for this Random Access procedure:

		3>	    if Msg1 repetition number is indicated in *rach-ConfigDedicated*:

			4>	    select the set of Random Access resources that is only configured with RedCap indication and Msg1 repetition indication and associated with the indicated Msg1 repetition number for this Random Access procedure.

		3>	    else:

			4>	    if there is one set of Random Access resources available that is only configured with RedCap indication:

				5>	    select this set of Random Access resources for this Random Access procedure.

			4>	    else:

				5>	    select the set of Random Access resources that is not associated with any feature indication (as specified in clause 5.1.1c) for this Random Access procedure.

	2>	    else if eRedCap is applicable for this Random Access procedure:

		3>	    if Msg1 repetition number is indicated in *rach-ConfigDedicated*:

			4>	    select the set of Random Access resources that is only configured with eRedCap indication and Msg1 repetition indication and associated with the indicated Msg1 repetition number for this Random Access procedure.

		3>	    else:

			4>	    if there is one set of Random Access resources available that is only configured with eRedCap indication:

				5>	    select this set of Random Access resources for this Random Access procedure.

			4>	    else if there is one set of Random Access resources available that is only configured with RedCap indication:

				5>	    select this set of Random Access resources for this Random Access procedure.

			4>	    else:

				5>	    select the set of Random Access resources that not is associated with any feature indication (as specified in clause 5.1.1c) for this Random Access procedure.

	2>	    else:

		3>	    if Msg1 repetition number is indicated in *rach-ConfigDedicated*:

			4>	    select the set of Random Access resources that is only configured with Msg1 repetition indication and associated with the indicated Msg1 repetition number for this Random Access procedure.

		3>	    else:

			4>	    select the set of Random Access resources that is not associated with any feature indication (as specified in clause 5.1.1c) for this Random Access procedure.

1>	    else if contention-free Random Access Resources have been provided for this Random Access procedure in the *BeamFailureRecoveryConfig*:

	2>	    if RedCap is applicable for this Random Access procedure:

		3>	    if there is one set of Random Access resources available that is only configured with RedCap indication:

			4>	    select this set of Random Access resources for this Random Access procedure.

		3>	    else:

			4>	    select the set of Random Access resources that is not associated with any feature indication (as specified in clause 5.1.1c) for this Random Access procedure.

	2>	    else if eRedCap is applicable for this Random Access procedure:

		3>	    if there is one set of Random Access resources available that is only configured with eRedCap indication:

			4>	    select this set of Random Access resources for this Random Access procedure.

		3>	    else if there is one set of Random Access resources available that is only configured with RedCap indication:

			4>	    select this set of Random Access resources for this Random Access procedure.

		3>	    else:

			4>	    select the set of Random Access resources that is not associated with any feature indication (as specified in clause 5.1.1c) for this Random Access procedure.

	2>	    else:

		3>	    select the set of Random Access resources that is not associated with any feature indication (as specified in clause 5.1.1c) for this Random Access procedure.

1>	    else if Random Access resources for SI request have been provided for this Random Access procedure:

	2>	    if Random Access Resources associated with Msg1 repetition for SI request and Msg1 repetition number have been provided for this Random Access procedure:

		3>	    if the BWP selected="selected" for Random Access procedure is indicated by *initialUplinkBWP-RedCap*:

			4>	    if RedCap is applicable for the current Random Access procedure:

				5>	    select the set of Random Access Resources that is only configured with RedCap indication and Msg1 repetition indication and associated with the indicated Msg1 repetition number for this Random Access procedure.

			4>	    else if eRedCap is applicable for the current Random Access procedure:

				5>	    if there is one set of Random Access resources available that is only configured with RedCap indication and Msg1 repetition indication and associated with the indicated Msg1 repetition number:

					6>	    select this set of Random Access resources for this Random Access procedure.

				5>	    else:

					6>	    select the set of Random Access Resources that is only configured with eRedCap indication and Msg1 repetition indication and associated with the indicated Msg1 repetition number for this Random Access procedure.

		3>	    else:

			4>	    select the set of Random Access resources that is only configured with Msg1 repetition indication and associated with the indicated Msg1 repetition number for this Random Access procedure.

	2>	    else:

		3>	    select the set of Random Access resources that is not associated with any feature indication (as specified in clause 5.1.1c) for the current Random Access procedure.

1>	    else:

	2>	    select the set of Random Access resources that is not associated with any feature indication (as specified in clause 5.1.1c) for the current Random Access procedure.

### 5.1.1c     Availability of the set of Random Access resources [#](#5-1-1c-availability-of-the-set-of-random-access-resources)

The MAC entity shall for each set of configured Random Access resources:

1>	    if *eRedCap* is set to *true* for a set of Random Access resources:

	2>	    consider the set of Random Access resources as not available for a Random Access procedure for which eRedCap is not applicable.

1>	    if *redCap* is set to *true* for a set of Random Access resources:

	2>	    consider the set of Random Access resources as not available for a Random Access procedure for which RedCap is not applicable.

1>	    if *smallData* is set to *true* for a set of Random Access resources:

	2>	    consider the set of Random Access resources as not available for the Random Access procedure which is not triggered for RA-SDT by MO-SDT as specified in TS 38.331 [5].

1>	    if *NSAG-List* is configured for a set of Random Access resources:

	2>	    consider the set of Random Access resources as not available for the Random Access procedure unless it is triggered for any one of the *NSAG**-ID*(s) in the *NSAG-List*.

1>	    if *msg3-Repetitions* is set to *true* for a set of Random Access resources:

	2>	    consider the set of Random Access resources as not available for the Random Access procedure if Msg3 repetition is not applicable.

1>	    if *msg1-Repetitions* is set to *true* for a set of Random Access resources:

	2>	    if Msg1 repetition is not applicable to the current Random Access procedure; or

	2>	    if the set of Random Access resources is not associated with any of the Msg1 repetition number that is applicable to the current Random Access procedure:

		3>	    consider the set of Random Access resources as not available for the Random Access procedure.

1>	    if a set of Random Access resources is not configured with *FeatureCombination*:

	2>	    consider the set of Random Access resources to not associated with any feature.

### 5.1.1d     Selection of the set of Random Access resources based on feature prioritization [#](#5-1-1d-selection-of-the-set-of-random-access-resources-based-on-feature-prioritization)

The MAC entity shall:

1>	    among the available sets of Random Access resources for this Random Access procedure (as specified in clause 5.1.1c), identify those configured with a feature which has the highest priority assigned in *featurePriorities* among all the features applicable to this Random Access procedure as specified in TS 38.331 [5].

1>	    if a single set of Random Access resources is identified:

	2>	    select this set of Random Access resources.

1>	    else if more than one set of Random Access resources is identified:

	2>	    if all the identified sets of Random Access resources are configured with Msg1 repetition indication and the same *featureCombination*:

		3>	    select the set of Random Access resources that associated with highest Msg1 repetition number among the identified sets of Random Access resources.

	2>	    else:

		3>	    repeat the procedure taking as an input the identified sets of Random Access resources and the feature applicable to the current Random Access procedure with the highest priority assigned in *featurePriorities* among all the features applicable to this Random Access procedure, except the features considered already.

1>	    else (i.e. no set of Random Access resources is identified):

	2>	    repeat the procedure taking as an input the previous identified available sets of Random Access resources and the feature applicable to the current Random Access procedure with the highest priority assigned in *featurePriorities* among all the features applicable to this Random Access procedure, except the features considered already.

### 5.1.1e     Selection of Msg1 repetition for SI request [#](#5-1-1e-selection-of-msg1-repetition-for-si-request)

The MAC entity shall:

1>	    if *si-RequestResourcesRepetitionNum8* is configured and the RSRP of the downlink pathloss reference is less than *rsrp-ThresholdMsg1-RepetitionNum8*:

	2>	    criteria to apply Msg1 repetition for SI request is considered met and Msg1 repetition number applicable is 8.

1>	    else if *si-RequestResourcesRepetitionNum4* is configured and the RSRP of the downlink pathloss reference is less than *rsrp-ThresholdMsg1-RepetitionNum4*:

	2>	    criteria to apply Msg1 repetition for SI request is considered met and Msg1 repetition number applicable is 4.

1>	    else if *si-RequestResourcesRepetitionNum2* is configured and the RSRP of the downlink pathloss reference is less than *rsrp-ThresholdMsg1-RepetitionNum2*:

	2>	    criteria to apply Msg1 repetition for SI request is considered met and Msg1 repetition number applicable is 2.

1>	    else:

	2>	    criteria to apply Msg1 repetition for SI request is considered not met.

### 5.1.2     Random Access Resource selection [#](#5-1-2-random-access-resource-selection)

If the selected="selected" *RA_TYPE* is set to *4-stepRA*, the MAC entity shall:

1>	    if the Random Access procedure was initiated for SpCell beam failure recovery (as specified in clause 5.17); and

1>	    if the *beamFailureRecoveryTimer* (in clause 5.17) is either running or not configured; and

1>	    if the contention-free Random Access Resources for beam failure recovery request associated with any of the SSBs and/or CSI-RSs have been explicitly provided by RRC; and

1>	    if at least one of the SSBs with SS-RSRP above *rsrp-ThresholdSSB* amongst the SSBs in *candidateBeamRSList* or the CSI-RSs with CSI-RSRP above *rsrp-ThresholdCSI-RS* amongst the CSI-RSs in *candidateBeamRSList* is available:

	2>	    select an SSB with SS-RSRP above *rsrp-ThresholdSSB* amongst the SSBs in *candidateBeamRSList* or a CSI-RS with CSI-RSRP above *rsrp-ThresholdCSI-RS* amongst the CSI-RSs in *candidateBeamRSList*;

	2>	    if CSI-RS is selected, and there is no *ra-PreambleIndex* associated with the selected="selected" CSI-RS:

		3>	    set the *PREAMBLE_INDEX* to a *ra-PreambleIndex* corresponding to the SSB in *candidateBeamRSList* which is quasi-colocated with the selected="selected" CSI-RS as specified in TS 38.214 [7].

	2>	    else:

		3>	    set the *PREAMBLE_INDEX* to a *ra-PreambleIndex* corresponding to the selected="selected" SSB or CSI-RS from the set of Random Access Preambles for beam failure recovery request.

1>	    else if the *ra-PreambleIndex* has been explicitly provided by PDCCH; and

1>	    if the *ra-PreambleIndex* is not 0b000000:

	2>	    set the *PREAMBLE_INDEX* to the signalled *ra-PreambleIndex*;

	2>	    select the SSB signalled by PDCCH.

1>	    else if contention-free Random Access Resources have been explicitly provided by an(Enhanced) LTM Cell Switch Command MAC CE and the SS-RSRP of the SSB signalled by the (Enhanced) LTM Cell Switch Command MAC CE is above *rsrp-ThresholdSSB*:

	2>	    set the *PREAMBLE_INDEX* to the Random Access Preamble index signalled by the (Enhanced) LTM Cell Switch Command MAC CE;

	2>	    select the SSB signalled by the (Enhanced) LTM Cell Switch Command MAC CE.

1>	    else if contention-free Random Access Resources have not been explicitly provided by an (Enhanced) LTM Cell Switch Command MAC CE, the Random Access procedure was not initiated for recovery using an LTM candidate configuration as specified in TS 38.331 [5] clause 5.3.7.3, contention-free Random Access Resources associated with SSBs have been explicitly provided in *rach-ConfigDedicated* and at least one SSB with SS-RSRP above *rsrp-ThresholdSSB* amongst the associated SSBs is available:

	2>	    select an SSB with SS-RSRP above *rsrp-ThresholdSSB* amongst the associated SSBs;

	2>	    set the *PREAMBLE_INDEX* to a *ra-PreambleIndex* corresponding to the selected="selected" SSB.

1>	    else if contention-free Random Access Resources have not been explicitly provided by an (Enhanced) LTM Cell Switch Command MAC CE, the Random Access procedure was not initiated for recovery using an LTM candidate configuration as specified in TS 38.331 [5] clause 5.3.7.3, contention-free Random Access Resources associated with CSI-RSs have been explicitly provided in *rach-ConfigDedicated* and at least one CSI-RS with CSI-RSRP above *rsrp-ThresholdCSI-RS* amongst the associated CSI-RSs is available:

	2>	    select a CSI-RS with CSI-RSRP above *rsrp-ThresholdCSI-RS* amongst the associated CSI-RSs;

	2>	    set the *PREAMBLE_INDEX* to a *ra-PreambleIndex* corresponding to the selected="selected" CSI-RS.

1>	    else if the Random Access procedure was initiated for SI request (as specified in TS 38.331 [5]); and

1>	    if the Random Access Resources for SI request have been explicitly provided by RRC:

	2>	    if at least one of the SSBs with SS-RSRP above *rsrp-ThresholdSSB* is available:

		3>	    select an SSB with SS-RSRP above *rsrp-ThresholdSSB*.

	2>	    else:

		3>	    select any SSB.

	2>	    select a Random Access Preamble corresponding to the selected="selected" SSB, from the Random Access Preamble(s) determined according to *ra-PreambleStartIndex* as specified in TS 38.331 [5];

	2>	    set the *PREAMBLE_INDEX* to selected="selected" Random Access Preamble.

1>	    if the Random Access procedure was initiated for SIB1 request (as specified in TS 38.331 [5]); and

1>	    if the Random Access Resources for SIB1 request have been provided by RRC:

	2>	    if at least one of the SSBs with SS-RSRP above *sib1-rsrp-ThresholdSSB* is available:

		3>	    select an SSB with SS-RSRP above *sib1-rsrp-ThresholdSSB*.

	2>	    else:

		3>	    select any SSB.

	2>	    select a Random Access Preamble corresponding to the selected="selected" SSB, from the Random Access Preamble(s) determined according to *sib1-RA-PreambleStartIndex* as specified in TS 38.331 [5];

	2>	    set the *PREAMBLE_INDEX* to selected="selected" Random Access Preamble.

1>	    else (i.e. for the contention-based Random Access preamble selection):

	2>	    if at least one of the SSBs with SS-RSRP above *rsrp-ThresholdSSB* is available:

		3>	    select an SSB with SS-RSRP above *rsrp-ThresholdSSB*.

	2>	    else:

		3>	    select any SSB.

	2>	    if the *RA_TYPE* is switched from *2-stepRA* to *4-stepRA*:

		3>	    if a Random Access Preambles group was selected="selected" during the current Random Access procedure:

			4>	    select the same group of Random Access Preambles as was selected="selected" for the 2-step RA type.

		3>	    else:

			4>	    if Random Access Preambles group B is configured; and

			4>	    if the transport block size of the MSGA payload configured in the *rach-ConfigDedicated* corresponds to the transport block size of the MSGA payload associated with Random Access Preambles group B:

				5>	    select the Random Access Preambles group B.

			4>	    else:

				5>	    select the Random Access Preambles group A.

	2>	    else if Msg3 buffer is empty:

		3>	    if Random Access Preambles group B is configured:

			4>	    if the *RO_TYPE* is set to *2nd-RO* and *sbfd-RACH-SingleConfig-preambleReceivedTargetPower* is configured for the Random Access procedure, and the potential Msg3 size (UL data available for transmission plus MAC subheader(s) and, where required, MAC CEs) is greater than *ra-Msg3SizeGroupA* and the pathloss is less than *PCMAX* (of the Serving Cell performing the Random Access Procedure) – *sbfd-RACH-SingleConfig-preambleReceivedTargetPower* – *msg3-DeltaPreamble* – *messagePowerOffsetGroupB*; or

			4>	    if the *RO_TYPE* is set to *2nd-RO* and *sbfd-RACH-DualConfig* is configured for the Random Access procedure, and the potential Msg3 size (UL data available for transmission plus MAC subheader(s) and, where required, MAC CEs) is greater than *ra-Msg3SizeGroupA* and the pathloss is less than *PCMAX* (of the Serving Cell performing the Random Access Procedure) – *preambleReceivedTargetPower* (included in the *sbfd-RACH-DualConfig*) – *msg3-DeltaPreamble* – *messagePowerOffsetGroupB*; or

			4>	    if the *RO_TYPE* is set to *2nd-RO* and *sbfd-RACH-SingleConfig* is configured and *sbfd-RACH-SingleConfig-preambleReceivedTargetPower* is not configured for the Random Access procedure, and the potential Msg3 size (UL data available for transmission plus MAC subheader(s) and, where required, MAC CEs) is greater than *ra-Msg3SizeGroupA* and the pathloss is less than *PCMAX* (of the Serving Cell performing the Random Access Procedure) – *preambleReceivedTargetPower* – *msg3-DeltaPreamble* *–* *messagePowerOffsetGroupB*; or

			4>	    if the *RO_TYPE* is set to *1st-RO*, and the potential Msg3 size (UL data available for transmission plus MAC subheader(s) and, where required, MAC CEs) is greater than *ra-Msg3SizeGroupA* and the pathloss is less than *PCMAX* (of the Serving Cell performing the Random Access Procedure) – *preambleReceivedTargetPower* – *msg3-DeltaPreamble* – *messagePowerOffsetGroupB*; or

			4>	    if the Random Access procedure was initiated for the CCCH logical channel and the CCCH SDU size plus MAC subheader is greater than *ra-Msg3SizeGroupA*:

				5>	    select the Random Access Preambles group B.

			4>	    else:

				5>	    select the Random Access Preambles group A.

		3>	    else:

			4>	    select the Random Access Preambles group A.

	2>	    else (i.e. Msg3 is being retransmitted):

		3>	    select the same group of Random Access Preambles as was used for the Random Access Preamble transmission attempt corresponding to the first transmission of Msg3.

	2>	    select a Random Access Preamble randomly with equal probability from the Random Access Preambles associated with the selected="selected" SSB and the selected="selected" Random Access Preambles group;

	2>	    set the *PREAMBLE_INDEX* to the selected="selected" Random Access Preamble.

1>	    if the Random Access procedure was initiated for SI request (as specified in TS 38.331 [5]); and

1>	    if *ra-AssociationPeriodIndex* and *si-RequestPeriod* are configured:

	2>	    determine the next available PRACH occasion from the PRACH occasions corresponding to the selected="selected" SSB in the association period given by *ra-AssociationPeriodIndex* in the *si-RequestPeriod* permitted by the restrictions given by the *ra-ssb-OccasionMaskIndex* if configured (the MAC entity shall select a PRACH occasion randomly with equal probability amongst the consecutive PRACH occasions according to clause 8.1 of TS 38.213 [6] corresponding to the selected="selected" SSB).

1>	    if the Random Access procedure was initiated for SIB1 request (as specified in TS 38.331 [5]); and

1>	    if *sib1-RA-SSB-OccasionMaskIndex* and *sib1-RequestPeriod* are configured:

	2>	    determine the next available PRACH occasion from the PRACH occasions corresponding to the selected="selected" SSB in the association period given by *sib1-RA-SSB-OccasionMaskIndex* in the *sib1-RequestPeriod* permitted by the restrictions given by the *ra-ssb-OccasionMaskIndex**Sib1* if configured (the MAC entity shall select a PRACH occasion randomly with equal probability amongst the consecutive PRACH occasions according to clause 8.1 of TS 38.213 [6] corresponding to the selected="selected" SSB).

1>	    else if an SSB is selected="selected" above:

	2>	    if the set of Random Access resources associated with Msg1 repetition is selected="selected" for this Random Access procedure:

		3>	    determine the next available set of PRACH occasions of the selected="selected" RO type (as specified in TS 38.213 [6]) for the Msg1 repetition number applicable for this Random Access procedure corresponding to the selected="selected" SSB (the MAC entity shall select a set of PRACH occasions randomly with equal probability amongst sets of PRACH occasions of the selected="selected" RO type according to clause 8.1 of TS 38.213 [6] regardless the FR2 UL gap, corresponding to the selected="selected" SSB and selected="selected" Msg1 repetition number for this Random Access procedure; the MAC entity may take into account the possible occurrence of measurement gaps and MUSIM gaps when determining the next available set of PRACH occasions of the selected="selected" RO type corresponding to the selected="selected" SSB).

	2>	    else:

		3>	    determine the next available PRACH occasion from the PRACH occasions of the selected="selected" RO type corresponding to the selected="selected" SSB permitted by the restrictions given by the *ra-ssb-OccasionMaskIndex* if configured, or *ssb-SharedRO-MaskIndex* if configured, or indicated by PDCCH, or indicated by the (Enhanced) LTM Cell Switch Command MAC CE (the MAC entity shall select a PRACH occasion randomly with equal probability amongst the consecutive PRACH occasions of the selected="selected" RO type according to clause 8.1 of TS 38.213 [6] regardless the FR2 UL gap, corresponding to the selected="selected" SSB; the MAC entity may take into account the possible occurrence of measurement gaps and MUSIM gaps when determining the next available PRACH occasion of the selected="selected" RO type corresponding to the selected="selected" SSB).

1>	    else if a CSI-RS is selected="selected" above:

	2>	    if there is no contention-free Random Access Resource associated with the selected="selected" CSI-RS:

		3>	    determine the next available PRACH occasion from the PRACH occasions of the selected="selected" RO type, permitted by the restrictions given by the *ra-ssb-OccasionMaskIndex* if configured, corresponding to the SSB in *candidateBeamRSList* which is quasi-colocated with the selected="selected" CSI-RS as specified in TS 38.214 [7] (the MAC entity shall select a PRACH occasion randomly with equal probability amongst the consecutive PRACH occasions of the selected="selected" RO type, according to clause 8.1 of TS 38.213 [6] regardless the FR2 UL gap, corresponding to the SSB which is quasi-colocated with the selected="selected" CSI-RS; the MAC entity may take into account the possible occurrence of measurement gaps and MUSIM gaps when determining the next available PRACH occasion of the selected="selected" RO type, corresponding to the SSB which is quasi-colocated with the selected="selected" CSI-RS).

	2>	    else:

		3>	    determine the next available PRACH occasion from the PRACH occasions of the selected="selected" RO type, in *ra-OccasionList* corresponding to the selected="selected" CSI-RS (the MAC entity shall select a PRACH occasion randomly with equal probability amongst the PRACH occasions of the selected="selected" RO type, occurring simultaneously but on different subcarriers regardless the FR2 UL gap, corresponding to the selected="selected" CSI-RS; the MAC entity may take into account the possible occurrence of measurement gaps and MUSIM gaps when determining the next available PRACH occasion of the selected="selected" RO type, corresponding to the selected="selected" CSI-RS).

1>	    perform the Random Access Preamble transmission procedure (see clause 5.1.3).

NOTE 1:    When the UE determines if there is an SSB with SS-RSRP above *rsrp-ThresholdSSB* or a CSI-RS with CSI-RSRP above *rsrp-ThresholdCSI-RS*, the UE uses the latest unfiltered L1-RSRP measurement.

NOTE 2:    Void.

NOTE 3:    If an (e)RedCap UE in RRC_IDLE or RRC_INACTIVE mode is configured with a BWP indicated by *initialDownlinkBWP-RedCap* which is not associated with any SSB, SS-RSRP measurement is performed based on the SSB associated with the BWP indicated by *initialDownlinkBWP*. If an (e)RedCap UE in RRC_INACTIVE mode is configured with SDT and with a BWP indicated by *initialDownlinkBWP-RedCap* which is associated with NCD-SSB, SS-RSRP measurement can also be performed based on this NCD-SSB during SDT.

NOTE 4:    If an (e)RedCap UE in RRC_IDLE or RRC_INACTIVE mode is configured with a BWP indicated by *initialDownlinkBWP-RedCap* which is not associated with any SSB for RACH, it is up to the UE implementation to perform a new RSRP measurements before Msg1/MsgA retransmission.

NOTE 5:    If an RO selected="selected" for preamble transmission is configured by *addlRACH-Config-Adapt* and *ssb-perRACH-OccasionAndCB-PreamblesPerSSB* is configured in *addlRACH-Config-Adapt*, UE selects preamble corresponding to selected="selected" SSB amongst the preambles determined according to *ssb-perRACH-OccasionAndCB-PreamblesPerSSB* in *addlRACH-Config-Adapt*.

### 5.1.2a     Random Access Resource selection for 2-step RA type [#](#5-1-2a-random-access-resource-selection-for-2-step-ra-type)

If the selected="selected" *RA_TYPE* is set to *2-stepRA*, the MAC entity shall:

1>	    if the Random access procedure was not initiated for recovering using an LTM candidate configuration as specified in TS 38.331 [5] clause 5.3.7.3 and if the contention-free 2-step RA type Resources associated with SSBs have been explicitly provided in *rach-ConfigDedicated* and at least one SSB with SS-RSRP above *msgA-RSRP-ThresholdSSB* amongst the associated SSBs is available:

	2>	    select an SSB with SS-RSRP above *msgA-RSRP-ThresholdSSB* amongst the associated SSBs;

	2>	    set the *PREAMBLE_INDEX* to a *ra-PreambleIndex* corresponding to the selected="selected" SSB.

1>	    else (i.e. for the contention-based Random Access Preamble selection):

	2>	    if at least one of the SSBs with SS-RSRP above *msgA-**RSRP**-ThresholdSSB* is available:

		3>	    select an SSB with SS-RSRP above *msgA-**RSRP**-ThresholdSSB*.

	2>	    else:

		3>	    select any SSB.

	2>	    if contention-free Random Access Resources for 2-step RA type have not been configured and if Random Access Preambles group has not yet been selected="selected" during the current Random Access procedure:

		3>	    if Random Access Preambles group B for 2-step RA type is configured:

			4>	    if the potential MSGA payload size (UL data available for transmission plus MAC subheader and, where required, MAC CEs) is greater than the *ra-MsgA-SizeGroupA* and the pathloss is less than *PCMAX* (of the Serving Cell performing the Random Access Procedure) – *msgA-PreambleReceivedTargetPower* – *msgA-DeltaPreamble* – *messagePowerOffsetGroupB*; or

			4>	    if the Random Access procedure was initiated for the CCCH logical channel and the CCCH SDU size plus MAC subheader is greater than *ra-MsgA**-**SizeGroupA*:

				5>	    select the Random Access Preambles group B.

			4>	    else:

				5>	    select the Random Access Preambles group A.

		3>	    else:

			4>	    select the Random Access Preambles group A.

	2>	    else if contention-free Random Access Resources for 2-step RA type have been configured and if Random Access Preambles group has not yet been selected="selected" during the current Random Access procedure:

		3>	    if Random Access Preambles group B for 2-step RA type is configured; and

		3>	    if the transport block size of the MSGA payload configured in the *rach-ConfigDedicated* corresponds to the transport block size of the MSGA payload associated with Random Access Preambles group B:

			4>	    select the Random Access Preambles group B.

		3>	    else:

			4>	    select the Random Access Preambles group A.

	2>	    else (i.e. Random Access preambles group has been selected="selected" during the current Random Access procedure):

		3>	    select the same group of Random Access Preambles as was used for the Random Access Preamble transmission attempt corresponding to the earlier transmission of MSGA.

	2>	    select a Random Access Preamble randomly with equal probability from the 2-step RA type Random Access Preambles associated with the selected="selected" SSB and the selected="selected" Random Access Preambles group;

	2>	    set the *PREAMBLE_INDEX* to the selected="selected" Random Access Preamble.

1>	    determine the next available PRACH occasion from the PRACH occasions corresponding to the selected="selected" SSB permitted by the restrictions given by the *msgA-SSB-SharedRO-MaskIndex* if configured, or *ra-ssb-OccasionMaskIndex* if configured, or *ssb-SharedRO-MaskIndex* if configured (the MAC entity shall select a PRACH occasion randomly with equal probability among the consecutive PRACH occasions allocated for 2-step RA type according to clause 8.1 of TS 38.213 [6] regardless the FR2 UL gap, corresponding to the selected="selected" SSB; the MAC entity may take into account the possible occurrence of measurement gaps and MUSIM gaps when determining the next available PRACH occasion corresponding to the selected="selected" SSB);

1>	    if the Random Access Preamble was not selected="selected" by the MAC entity among the contention-based Random Access Preamble(s):

	2>	    select a PUSCH occasion from the PUSCH occasions configured in *msgA-CFRA-PUSCH* corresponding to the PRACH slot of the selected="selected" PRACH occasion, according to *msgA-PUSCH-**R**esource-Index* corresponding to the selected="selected" SSB;

	2>	    determine the UL grant and the associated HARQ information for the MSGA payload in the selected="selected" PUSCH occasion;

	2>	    deliver the UL grant and the associated HARQ information to the HARQ entity.

1>	    else:

	2>	    select a PUSCH occasion corresponding to the selected="selected" preamble and PRACH occasion according to clause 8.1A of TS 38.213 [6];

	2>	    determine the UL grant for the MSGA payload according to the PUSCH configuration associated with the selected="selected" Random Access Preambles group and determine the associated HARQ information;

	2>	    if the selected="selected" preamble and PRACH occasion is mapped to a valid PUSCH occasion as specified in clause 8.1A of TS 38.213 [6]:

		3>	    deliver the UL grant and the associated HARQ information to the HARQ entity.

1>	    perform the MSGA transmission procedure (see clause 5.1.3a).

NOTE 1:    To determine if there is an SSB with *SS-RSRP* above *msgA-RSRP-ThresholdSSB*, the UE uses the latest unfiltered *L1-RSRP* measurement.

NOTE 2:    If an (e)RedCap UE in RRC_IDLE or RRC_INACTIVE mode is configured with a BWP indicated by *initialDownlinkBWP-RedCap* which is not associated with any SSB, SS-RSRP measurement is performed based on the SSB associated with the BWP indicated by *initialDownlinkBWP*. If an (e)RedCap UE in RRC_INACTIVE mode is configured with SDT and with a BWP indicated by *initialDownlinkBWP-RedCap* which is associated with NCD-SSB, SS-RSRP measurement can also be performed based on this NCD-SSB during SDT.

NOTE 3:    If an (e)RedCap UE in RRC_IDLE or RRC_INACTIVE mode is configured with a BWP indicated by *initialDownlinkBWP-RedCap* which is not associated with any SSB for RACH, it is up to the UE implementation to perform a new RSRP measurements before Msg1/MsgA retransmission.

### 5.1.3     Random Access Preamble transmission [#](#5-1-3-random-access-preamble-transmission)

The MAC entity shall, for each Random Access Preamble:

1>	    if *PREAMBLE_TRANSMISSION_COUNTER* is greater than one; and

1>	    if the notification of suspending power ramping counter has not been received from lower layers; and

1>	    if LBT failure indication was not received from lower layers for the last Random Access Preamble transmission; and

1>	    if SSB or CSI-RS selected="selected" is not changed from the selection in the last Random Access Preamble transmission; and

1>	    if the Random Access procedure is not initiated by the PDCCH order for an LTM candidate cell:

	2>	    increment *PREAMBLE_POWER_RAMPING_COUNTER* by 1.

1>	    if the Random Access procedure is initiated by the PDCCH order for an LTM candidate cell as preamble re-transmission; and

1>	    if the PDCCH order indicates the same LTM candidate cell and the same SSB as the last Random Access Preamble transmission:

	2>	    increment *PREAMBLE_POWER_RAMPING_COUNTER* by 1.

1>	    select the value of *DELTA_PREAMBLE* according to clause 7.3;

1>	    if the selected="selected" PRACH occasion is of the second PRACH occasions (as defined in TS 38.213 [6]) and *sbfd-RACH-SingleConfig-preambleReceivedTargetPower* is configured for the Random Access Procedure:

	2>	    set *PREAMBLE_RECEIVED_TARGET_POWER* to *sbfd-RACH-SingleConfig-preambleReceivedTargetPower* + *DELTA_PREAMBLE* + (*PREAMBLE_POWER_RAMPING_COUNTER* – 1) × *PREAMBLE_POWER_RAMPING_STEP* + *POWER_OFFSET_2STEP_RA* + *POWER_OFFSET_RO_TYPE*.

1>	    else if the selected="selected" PRACH occasion is of the second PRACH occasions (as defined in TS 38.213 [6]) and *sbfd-RACH-DualConfig* is configured for the Random Access Procedure:

	2>	    set *PREAMBLE_RECEIVED_TARGET_POWER* to *preambleReceivedTargetPower* (included in the *sbfd-RACH-DualConfig*) + *DELTA_PREAMBLE* + (*PREAMBLE_POWER_RAMPING_COUNTER* – 1) × *PREAMBLE_POWER_RAMPING_STEP* + *POWER_OFFSET_2STEP_RA* + *POWER_OFFSET_RO_TYPE*.

1>	    else:

	2>	    set *PREAMBLE_RECEIVED_TARGET_POWER* to *preambleReceivedTargetPower* + *DELTA_PREAMBLE* + (*PREAMBLE_POWER_RAMPING_COUNTER* – 1) × *PREAMBLE_POWER_RAMPING_STEP* + *POWER_OFFSET_2STEP_RA* + *POWER_OFFSET_RO_TYPE*.

1>	    except for contention-free Random Access Preamble for beam failure recovery request and contention-free Random Access Preamble triggered by a PDCCH order for an LTM candidate cell, compute the RA-RNTI associated with the PRACH occasion in which the Random Access Preamble is transmitted;

1>	    instruct the physical layer to transmit the Random Access Preamble using the selected="selected" PRACH occasion, corresponding RA-RNTI (if available), *PREAMBLE_INDEX*, and *PREAMBLE_RECEIVED_TARGET_POWER*.

1>	    if the Random Access Procedure is triggered by a PDCCH order for an LTM candidate cell:

	2>	    consider this Random Access procedure completed.

1>	    if LBT failure indication is received from lower layers for this Random Access Preamble transmission:

	2>	    if *lbt-FailureRecoveryConfig* is configured:

		3>	    perform the Random Access Resource selection procedure (see clause 5.1.2).

	2>	    else:

		3>	    increment *PREAMBLE_TRANSMISSION_COUNTER* by 1;

		3>	    if *PREAMBLE_TRANSMISSION_COUNTER* = *preambleTransMax* + 1:

			4>	    if the Random Access Preamble is transmitted on the SpCell:

				5>	    indicate a Random Access problem to upper layers;

				5>	    if this Random Access procedure was triggered for SI request:

					6>	    consider the Random Access procedure unsuccessfully completed.

			4>	    else if the Random Access Preamble is transmitted on an SCell:

				5>	    consider the Random Access procedure unsuccessfully completed.

		3>	    if the Random Access procedure is not completed:

			4>	    perform the Random Access Resource selection procedure (see clause 5.1.2).

The RA-RNTI associated with the PRACH occasion in which the Random Access Preamble is transmitted or the RA-RNTI associated with the last valid PRACH occasion in the set of PRACH occasions (as specified in TS 38.213 [6]) for Msg1 repetition, is computed as:

    RA-RNTI = 1 + s_id + 14 × t_id + 14 × 80 × f_id + 14 × 80 × 8 × ul_carrier_id

where s_id is the index of the first OFDM symbol of the PRACH occasion (0 ≤ s_id < 14), t_id is the index of the first slot of the PRACH occasion in a system frame (0 ≤ t_id < 80), where the subcarrier spacing to determine t_id is based on the value of μ specified in clause 5.3.2 in TS 38.211 [8] for μ = {0, 1, 2, 3}, and for μ = {5, 6}, t_id is the index of the 120 kHz slot in a system frame that contains the PRACH occasion (0 ≤ t_id < 80), f_id is the index of the PRACH occasion in the frequency domain (0 ≤ f_id < 8), and ul_carrier_id is the UL carrier used for Random Access Preamble transmission (0 for NUL carrier, and 1 for SUL carrier).

### 5.1.3a     MSGA transmission [#](#5-1-3a-msga-transmission)

The MAC entity shall, for each MSGA:

1>	    if *PREAMBLE_TRANSMISSION_COUNTER* is greater than one; and

1>	    if the notification of suspending power ramping counter has not been received from lower layers; and

1>	    if LBT failure indication was not received from lower layers for the last MSGA Random Access Preamble transmission; and

1>	    if SSB selected="selected" is not changed from the selection in the last Random Access Preamble transmission:

	2>	    increment *PREAMBLE_POWER_RAMPING_COUNTER* by 1.

1>	    select the value of *DELTA_PREAMBLE* according to clause 7.3;

1>	    set *PREAMBLE_RECEIVED_TARGET_POWER* to *msgA-P**reambleReceivedTargetPower* + *DELTA_PREAMBLE* + (*PREAMBLE_POWER_RAMPING_COUNTER* – 1) × *PREAMBLE_POWER_RAMPING_STEP*;

1>	    if this is the first MSGA transmission within this Random Access procedure:

	2>	    if the transmission is not being made for the CCCH logical channel:

		3>	    indicate to the Multiplexing and assembly entity to include a C-RNTI MAC CE in the subsequent uplink transmission.

	2>	    if the Random Access procedure was initiated for SpCell beam failure recovery and *spCell-BFR-CBRA* with value *true* is configured:

		3>	    if there is at least one Serving Cell of this MAC entity configured with two BFD-RS sets:

			4>	    indicate to the Multiplexing and assembly entity to include an Enhanced BFR MAC CE or a Truncated Enhanced BFR MAC CE in the subsequent uplink transmission.

		3>	    else:

			4>	    indicate to the Multiplexing and assembly entity to include a BFR MAC CE or a Truncated BFR MAC CE in the subsequent uplink transmission.

	2>	    else if the Random Access procedure was initiated for beam failure recovery of both BFD-RS sets of SpCell:

		3>	    indicate to the Multiplexing and assembly entity to include an Enhanced BFR MAC CE or a Truncated Enhanced BFR MAC CE in the subsequent uplink transmission.

	2>	    obtain the MAC PDU to transmit from the Multiplexing and assembly entity according to the HARQ information determined for the MSGA payload (see clause 5.1.2a) and store it in the MSGA buffer.

1>	    compute the MSGB-RNTI associated with the PRACH occasion in which the Random Access Preamble is transmitted;

1>	    instruct the physical layer to transmit the MSGA using the selected="selected" PRACH occasion and the associated PUSCH resource of MSGA (if the selected="selected" preamble and PRACH occasion is mapped to a valid PUSCH occasion), using the corresponding RA-RNTI, MSGB-RNTI, *PREAMBLE_INDEX*, *PREAMBLE_RECEIVED_TARGET_POWER*, *msgA-P**reambleReceivedTargetPower*, and the amount of power ramping applied to the latest MSGA preamble transmission (i.e. (*PREAMBLE_POWER_RAMPING_COUNTER* – 1) × *PREAMBLE_POWER_RAMPING_STEP*);

1>	    if LBT failure indication is received from lower layers for the transmission of this MSGA Random Access Preamble:

	2>	    instruct the physical layer to cancel the transmission of the MSGA payload on the associated PUSCH resource;

	2>	    if *lbt-FailureRecoveryConfig* is configured:

		3>	    perform the Random Access Resource selection procedure for 2-step RA type (see clause 5.1.2a).

	2>	    else:

		3>	    increment *PREAMBLE_TRANSMISSION_COUNTER* by 1;

		3>	    if *PREAMBLE_TRANSMISSION_COUNTE*R = *preambleTransMax* + 1:

			4>	    indicate a Random Access problem to upper layers;

			4>	    if this Random Access procedure was triggered for SI request:

				5>	    consider this Random Access procedure unsuccessfully completed.

		3>	    if the Random Access procedure is not completed:

			4>	    if *msgA-TransMax* is applied (see clause 5.1.1a) and *PREAMBLE_TRANSMISSION_COUNTER* = *msgA-TransMax* + 1:

				5>	    set the *RA_TYPE* to *4-stepRA*;

				5>	    perform initialization of variables specific to Random Access type as specified in clause 5.1.1a;

				5>	    if the Msg3 buffer is empty:

					6>	    obtain the MAC PDU to transmit from the MSGA buffer and store it in the Msg3 buffer;

				5>	    flush HARQ buffer used for the transmission of MAC PDU in the MSGA buffer;

				5>	    discard explicitly signalled contention-free 2-step RA type Random Access Resources, if any;

				5>	    perform the Random Access Resource selection procedure as specified in clause 5.1.2.

			4>	    else:

				5>	    perform the Random Access Resource selection procedure for 2-step RA type (see clause 5.1.2a).

NOTE:    The MSGA transmission includes the transmission of the PRACH Preamble as well as the contents of the MSGA buffer in the PUSCH resource corresponding to the selected="selected" PRACH occasion and *PREAMBLE_INDEX* (see TS 38.213 [6])

The MSGB-RNTI associated with the PRACH occasion in which the Random Access Preamble is transmitted, is computed as:

    MSGB-RNTI = 1 + s_id + 14 × t_id + 14 × 80 × f_id + 14 × 80 × 8 × ul_carrier_id + 14 × 80 × 8 × 2

where s_id is the index of the first OFDM symbol of the PRACH occasion (0 ≤ s_id < 14), t_id is the index of the first slot of the PRACH occasion in a system frame (0 ≤ t_id < 80), where the subcarrier spacing to determine t_id is based on the value of μ specified in clause 5.3.2 in TS 38.211 [8] for μ = {0, 1, 2, 3}, and for μ = {5, 6}, t_id is the index of the 120 kHz slot in a system frame that contains the PRACH occasion (0 ≤ t_id < 80), f_id is the index of the PRACH occasion in the frequency domain (0 ≤ f_id < 8), and ul_carrier_id is the UL carrier used for Random Access Preamble transmission (0 for NUL carrier, and 1 for SUL carrier). The RA-RNTI is calculated as specified in clause 5.1.3.

### 5.1.4     Random Access Response reception [#](#5-1-4-random-access-response-reception)

Once the Random Access Preamble is transmitted and regardless of the possible occurrence of a measurement gap, the MAC entity shall:

1>	    if the contention-free Random Access Preamble for beam failure recovery request was transmitted by the MAC entity:

	2>	    if the contention-free Random Access Preamble for beam failure recovery request was transmitted on a non-terrestrial network:

		3>	    start the *ra-ResponseWindow* configured in *BeamFailureRecoveryConfig* at the PDCCH occasion as specified in TS 38.213 [6].

	2>	    else:

		3>	    start the *ra-ResponseWindow* configured in *BeamFailureRecoveryConfig* at the first PDCCH occasion as specified in TS 38.213 [6] from the end of the Random Access Preamble transmission.

	2>	    monitor for a PDCCH transmission on the search space indicated by *recoverySearchSpaceId* of the SpCell identified by the C-RNTI while *ra-ResponseWindow* is running.

1>	    else:

	2>	    if the Random Access Preamble was transmitted on a non-terrestrial network:

		3>	    if the Random Access Preamble is transmitted with repetitions:

			4>	    start the *ra-ResponseWindow* configured in *RACH-ConfigCommon* at the PDCCH occasion from the end of all repetitions of the Random Access Preamble transmission as specified in TS 38.213 [6].

		3>	    else:

			4>	    start the *ra-ResponseWindow* configured in *RACH-ConfigCommon* at the PDCCH occasion as specified in TS 38.213 [6].

	2>	    else if the Random Access Preamble is transmitted with repetitions:

		3>	    start the *ra-ResponseWindow* configured in *RACH-ConfigCommon* at the first PDCCH occasion from the end of all repetitions of the Random Access Preamble transmission as specified in TS 38.213 [6].

	2>	    else if the Random Access Preamble is transmitted for SIB1 request:

		3>	    start the *ra-ResponseWindow* configured in *RACH-ConfigSIB1* at the first PDCCH occasion from the end of the Random Access Preamble transmission as specified in TS 38.213 [6].

	2>	    else:

		3>	    start the *ra-ResponseWindow* configured in *RACH-ConfigCommon* at the first PDCCH occasion as specified in TS 38.213 [6] from the end of the Random Access Preamble transmission.

	2>	    monitor the PDCCH of the SpCell for Random Access Response(s) identified by the RA-RNTI while the *ra-ResponseWindow* is running.

1>	    if notification of a reception of a PDCCH transmission on the search space indicated by *recoverySearchSpaceId* is received from lower layers on the Serving Cell where the preamble was transmitted; and

1>	    if PDCCH transmission is addressed to the C-RNTI; and

1>	    if the contention-free Random Access Preamble for beam failure recovery request was transmitted by the MAC entity:

	2>	    consider the Random Access procedure successfully completed.

1>	    else if a valid (as specified in TS 38.213 [6]) downlink assignment has been received on the PDCCH for the RA-RNTI and the received TB is successfully decoded:

	2>	    if the Random Access Response contains a MAC subPDU with Backoff Indicator:

		3>	    if the Random Access procedure was initiated for SIB1 request:

			4>	    set the *PREAMBLE_BACKOFF* to 0 ms.

		3>	    else:

			4>	    set the *PREAMBLE_BACKOFF* to value of the BI field of the MAC subPDU using Table 7.2-1, multiplied with *SCALING_FACTOR_BI*.

	2>	    else:

		3>	    set the *PREAMBLE_BACKOFF* to 0 ms.

	2>	    if the Random Access Response contains a MAC subPDU with Random Access Preamble identifier corresponding to the transmitted *PREAMBLE_INDEX* (see clause 5.1.3):

		3>	    consider this Random Access Response reception successful.

	2>	    if the Random Access Response reception is considered successful:

		3>	    if the Random Access Response includes a MAC subPDU with RAPID only:

			4>	    consider this Random Access procedure successfully completed;

			4>	    if the Random Access procedure was initiated for SIB1 request:

				5>	    indicate the reception of an acknowledgement for SIB1 request to upper layers.

			4>	    else if the Random Access procedure was initiated for SI request:

				5>	    indicate the reception of an acknowledgement for SI request to upper layers.

		3>	    else:

			4>	    apply the following actions for the Serving Cell where the Random Access Preamble was transmitted:

				5>	    process the received Timing Advance Command (see clause 5.2);

				5>	    if the received UL grant indicates that the corresponding PUSCH transmission is in SBFD symbols as specified in clause 11.1 of TS 38.213 [6]:

					6>	    if *sbfd-RACH-SingleConfig* (see TS 38.331 [5]) is configured for the Random Access procedure:

						7>	    indicate the *sbfd-RACH-SingleConfig-preambleReceivedTargetPower* if configured, or the *preambleReceivedTargetPower* otherwise, and the amount of power ramping applied to the latest Random Access Preamble transmission to lower layers (i.e. (*PREAMBLE_POWER_RAMPING_COUNTER* – 1) × *PREAMBLE_POWER_RAMPING_STEP* *+* *POWER_OFFSET_2STEP_RA* + *POWER_OFFSET_RO_TYPE*).

					6>	    else if *sbfd-RACH-DualConfig* (see TS 38.331 [5]) is configured for the Random Access procedure:

						7>	    indicate the *preambleReceivedTargetPower* included in the *sbfd-RACH-DualConfig*, and the amount of power ramping applied to the latest Random Access Preamble transmission to lower layers (i.e. (*PREAMBLE_POWER_RAMPING_COUNTER* – 1) × *PREAMBLE_POWER_RAMPING_STEP* *+* *POWER_OFFSET_2STEP_RA* + *POWER_OFFSET_RO_TYPE*).

					6>	    else:

						7>	    indicate the *preambleReceivedTargetPower* and the amount of power ramping applied to the latest Random Access Preamble transmission to lower layers (i.e. (*PREAMBLE_POWER_RAMPING_COUNTER* – 1) × *PREAMBLE_POWER_RAMPING_STEP* *+* *POWER_OFFSET_2STEP_RA* + *POWER_OFFSET_RO_TYPE*).

				5>	    else (i.e., the received UL grant indicates that the corresponding PUSCH transmission is in non-SBFD symbols as specified in clause 11.1 of TS 38.213 [6]):

					6>	    indicate the *preambleReceivedTargetPower* and the amount of power ramping applied to the latest Random Access Preamble transmission to lower layers (i.e. (*PREAMBLE_POWER_RAMPING_COUNTER* – 1) × *PREAMBLE_POWER_RAMPING_STEP* *+* *POWER_OFFSET_2STEP_RA* + *POWER_OFFSET_RO_TYPE*).

				5>	    if the Random Access procedure for an SCell is performed on uplink carrier where *pusch-Config* is not configured:

					6>	    ignore the received UL grant.

				5>	    else:

					6>	    process the received UL grant value and indicate it to the lower layers.

			4>	    if the Random Access Preamble was not selected="selected" by the MAC entity among the contention-based Random Access Preamble(s):

				5>	    consider the Random Access procedure successfully completed.

			4>	    else:

				5>	    set the *TEMPORARY_C-RNTI* to the value received in the Random Access Response;

				5>	    if this is the first successfully received Random Access Response within this Random Access procedure:

					6>	    if the transmission is not being made for the CCCH logical channel:

						7>	    indicate to the Multiplexing and assembly entity to include a C-RNTI MAC CE in the subsequent uplink transmission.

					6>	    if the Random Access procedure was initiated for SpCell beam failure recovery and *spCell-BFR-CBRA* with value *true* is configured:

						7>	    if there is at least one Serving Cell of this MAC entity configured with two BFD-RS sets:

							8>	    indicate to the Multiplexing and assembly entity to include an Enhanced BFR MAC CE or a Truncated Enhanced BFR MAC CE in the subsequent uplink transmission.

						7>	    else:

							8>	    indicate to the Multiplexing and assembly entity to include a BFR MAC CE or a Truncated BFR MAC CE in the subsequent uplink transmission.

					6>	    else if the Random Access procedure was initiated for beam failure recovery of both BFD-RS sets of SpCell:

						7>	    indicate to the Multiplexing and assembly entity to include an Enhanced BFR MAC CE or a Truncated Enhanced BFR MAC CE in the subsequent uplink transmission.

					6>	    obtain the MAC PDU to transmit from the Multiplexing and assembly entity and store it in the Msg3 buffer.

NOTE 1:    If within a Random Access procedure, an uplink grant provided in the Random Access Response for the same group of contention-based Random Access Preambles has a different size than the first uplink grant allocated during that Random Access procedure, the UE behavior is not defined.

1>	    if *ra-ResponseWindow* configured in *BeamFailureRecoveryConfig* expires and if a PDCCH transmission on the search space indicated by *recoverySearchSpaceId* addressed to the C-RNTI has not been received on the Serving Cell where the preamble was transmitted; or

1>	    if *ra-ResponseWindow* configured in *RACH-ConfigCommon* or *RACH-ConfigSIB1* expires, and if the Random Access Response containing Random Access Preamble identifiers that matches the transmitted *PREAMBLE_INDEX* has not been received:

	2>	    consider the Random Access Response reception not successful;

	2>	    increment *PREAMBLE_TRANSMISSION_COUNTER* by 1;

	2>	    if *PREAMBLE_TRANSMISSION_COUNTER* = *preambleTransMax* + 1:

		3>	    if the Random Access Preamble is transmitted on the SpCell:

			4>	    indicate a Random Access problem to upper layers;

			4>	    if this Random Access procedure was triggered for SI request or SIB1 request:

				5>	    consider the Random Access procedure unsuccessfully completed.

		3>	    else if the Random Access Preamble is transmitted on an SCell:

			4>	    consider the Random Access procedure unsuccessfully completed.

	2>	    if the Random Access procedure is not completed:

		3>	    if *preambleTransMaxRO-Type* is applied, and neither contention-free Random Access Resources nor Random Access resources for SI request have been provided for this Random Access procedure, and *PREAMBLE_TRANSMISSION_COUNTER* = *preambleTransMaxRO-Type* + 1:

			4>	    if the *RO_TYPE* is set to *2nd-RO*, and set of Random Access resources associated with the same feature or feature combination, and with the same or higher Msg1 repetition number (if the Random Access Preamble is transmitted with repetitions), than the current set of Random Access resources, is available for the first PRACH occasions as defined in TS 38.213 [6]:

				5>	    set the *RO_TYPE* to *1st-RO*;

				5>	    select the set of Random Access resources associated with the same feature or feature combination, and with the same Msg1 repetition number if available, or with the next higher Msg1 repetition number otherwise (if the Random Access Preamble is transmitted with repetitions), for this Random Access procedure;

				5>	    if *sbfd-RACH-DualConfig* is configured for the Random Access procedure (see TS 38.331 [5]):

					6>	    set *PREVIOUS_RO_TYPE_PREAMBLE_POWER_RAMPING_STEP* to *PREAMBLE_POWER_RAMPING_STEP*;

					6>	    (re-)initialize the parameters specified in clause 5.1.1 for the Random Access procedure according to the values configured by RRC for the selected="selected" set of Random Access resources;

					6>	    re-initialize *PREAMBLE_POWER_RAMPING_STEP* and *SCALING_FACTOR_BI* as specified in clause 5.1.1a;

					6>	    set *POWER_OFFSET_RO_TYPE* to (*PREAMBLE_POWER_RAMPING_COUNTER* – 1) × (*PREVIOUS**_RO_TYPE_PREAMBLE_POWER_RAMPING_STEP* – *PREAMBLE_POWER_RAMPING_STEP*).

			4>	    else if the *RO_TYPE* is set to *1st-RO*, and set of Random Access resources associated with the same feature or feature combination, and with the same or higher Msg1 repetition number (if the Random Access Preamble is transmitted with repetitions), than the current set of Random Access resources, is available for the second PRACH occasions as defined in TS 38.213 [6]:

				5>	    set the *RO_TYPE* to *2nd-RO*;

				5>	    select the set of Random Access resources associated with the same feature or feature combination, and with the same Msg1 repetition number if available, or with the next higher Msg1 repetition number otherwise (if the Random Access Preamble is transmitted with repetitions), for this Random Access procedure;

				5>	    if *sbfd-RACH-DualConfig* is configured for the Random Access procedure (see TS 38.331 [5]):

					6>	    set *PREVIOUS_RO_TYPE_PREAMBLE_POWER_RAMPING_STEP* to *PREAMBLE_POWER_RAMPING_STEP*;

					6>	    (re-)initialize the parameters specified in clause 5.1.1 for the Random Access procedure according to the values configured by RRC for the selected="selected" set of Random Access resources;

					6>	    re-initialize *PREAMBLE_POWER_RAMPING_STEP* and *SCALING_FACTOR_BI* as specified in clause 5.1.1a;

					6>	    set *POWER_OFFSET_RO_TYPE* to (*PREAMBLE_POWER_RAMPING_COUNTER* – 1) × (*PREVIOUS**_RO_TYPE_PREAMBLE_POWER_RAMPING_STEP* – *PREAMBLE_POWER_RAMPING_STEP*).

		3>	    if the Random Access Preamble is transmitted with repetitions and neither contention-free Random Access Resources nor Random Access resources for SI request have been provided for this Random Access procedure:

			4>	    if *PREAMBLE_TRANSMISSION_COUNTER* = [*preambleTransMax-Msg1-Repetition*] + 1; or

			4>	    if *PREAMBLE_TRANSMISSION_COUNTER* = 2 × [*preambleTransMax-Msg1-Repetition*] + 1:

				5>	    if set of Random Access resources configured with the same *prach-ConfigurationIndex* and associated with a higher Msg1 repetition number with the same feature or feature combination as the current set of Random Access resources is available:

					6>	    select the set of Random Access resources associated with the next higher Msg1 repetition number with the same feature or feature combination for this Random Access procedure;

					6>	    initialize *startPreambleForThisPartition*, *numberOfPreamblesPerSSB-ForThisPartition*, *numberOfRA-PreamblesGroupA* and *msg1-RepetitionTimeOffsetROGroup* parameters for the Random Access procedure according to the values configured by RRC for the selected="selected" set of Random Access resources.

		3>	    select a random backoff time according to a uniform distribution between 0 and the *PREAMBLE_BACKOFF*;

		3>	    if the criteria (as defined in clause 5.1.2) to select contention-free Random Access Resources is met during the backoff time:

			4>	    perform the Random Access Resource selection procedure (see clause 5.1.2).

		3>	    else if the Random Access procedure for an SCell is performed on uplink carrier where *pusch-Config* is not configured:

			4>	    delay the subsequent Random Access transmission until the Random Access Procedure is triggered by a PDCCH order with the same *ra-PreambleIndex*, *ra-ssb-OccasionMaskIndex*, and UL/SUL indicator TS 38.212 [9].

		3>	    else:

			4>	    perform the Random Access Resource selection procedure (see clause 5.1.2) after the backoff time.

The MAC entity may stop *ra-ResponseWindow* (and hence monitoring for Random Access Response(s)) after successful reception of a Random Access Response containing Random Access Preamble identifiers that matches the transmitted *PREAMBLE_INDEX*.

HARQ operation is not applicable to the Random Access Response reception.

NOTE 2:    For the case that RAR PDSCH bandwidth is larger than the bandwidth the eRedCap UE can receive or process per slot, and the UL grant in RAR indicates that the time is not enough for Msg3 transmission, as specified in TS 38.213 [6], it is up to UE implementation, e.g. either to consider the Random Access Response reception not successful, or transmit Msg3.

### 5.1.4a     MSGB reception and contention resolution for 2-step RA type [#](#5-1-4a-msgb-reception-and-contention-resolution-for-2-step-ra-type)

Once the MSGA preamble is transmitted, regardless of the possible occurrence of a measurement gap, the MAC entity shall:

1>	    start the *m**sgB**-ResponseWindow* at the PDCCH occasion as specified in TS 38.213 [6], clause 8.2A;

1>	    monitor the PDCCH of the SpCell for a Random Access Response identified by MSGB-RNTI while the *msgB**-ResponseWindow* is running;

1>	    if C-RNTI MAC CE was included in the MSGA:

	2>	    monitor the PDCCH of the SpCell for Random Access Response identified by the C-RNTI while the *msgB-ResponseWindow* is running.

1>	    if notification of a reception of a PDCCH transmission of the SpCell is received from lower layers:

	2>	    if the C-RNTI MAC CE was included in MSGA:

		3>	    if the Random Access procedure was initiated for SpCell beam failure recovery or for beam failure recovery of both BFD-RS sets of SpCell (as specified in clause 5.17) and the PDCCH transmission is addressed to the C-RNTI; or

		3>	    if the Random Access procedure was initiated for SDT beam failure recovery (as specified in clause 5.27.1) and the PDCCH transmission is addressed to the C-RNTI:

			4>	    consider this Random Access Response reception successful;

			4>	    stop the *msgB-ResponseWindow*;

			4>	    consider this Random Access procedure successfully completed.

		3>	    else if the *timeAlignmentTimer* associated with at least one PTAG is running; or

		3>	    if CG-SDT procedure is ongoing and *cg-SDT-TimeAlignmentTimer* is running:

			4>	    if the PDCCH transmission is addressed to the C-RNTI and contains a UL grant for a new transmission:

				5>	    consider this Random Access Response reception successful;

				5>	    stop the *msgB-ResponseWindow*;

				5>	    consider this Random Access procedure successfully completed.

		3>	    else:

			4>	    if a downlink assignment has been received on the PDCCH for the C-RNTI and the received TB is successfully decoded:

				5>	    if the MAC PDU contains the Absolute Timing Advance Command MAC CE:

					6>	    process the received Timing Advance Command (see clause 5.2);

					6>	    consider this Random Access Response reception successful;

					6>	    stop the *msgB-ResponseWindow*;

					6>	    consider this Random Access procedure successfully completed and finish the disassembly and demultiplexing of the MAC PDU.

	2>	    if a valid (as specified in TS 38.213 [6]) downlink assignment has been received on the PDCCH for the MSGB-RNTI and the received TB is successfully decoded:

		3>	    if the MSGB contains a MAC subPDU with Backoff Indicator:

			4>	    set the *PREAMBLE_BACKOFF* to value of the BI field of the MAC subPDU using Table 7.2-1, multiplied with *SCALING_FACTOR_BI*.

		3>	    else:

			4>	    set the *PREAMBLE_BACKOFF* to 0 ms.

		3>	    if the MSGB contains a fallbackRAR MAC subPDU; and

		3>	    if the Random Access Preamble identifier in the MAC subPDU matches the transmitted *PREAMBLE_INDEX* (see clause 5.1.3a):

			4>	    consider this Random Access Response reception successful;

			4>	    apply the following actions for the SpCell:

				5>	    process the received Timing Advance Command (see clause 5.2);

				5>	    indicate the *msgA-P**reambleReceivedTargetPower* and the amount of power ramping applied to the latest Random Access Preamble transmission to lower layers (i.e. (*PREAMBLE_POWER_RAMPING_COUNTER* – 1) × *PREAMBLE_POWER_RAMPING_STEP*);

				5>	    if the Random Access Preamble was not selected="selected" by the MAC entity among the contention-based Random Access Preamble(s):

					6>	    consider the Random Access procedure successfully completed;

					6>	    process the received UL grant value and indicate it to the lower layers.

				5>	    else:

					6>	    set the *TEMPORARY_C-RNTI* to the value received in the Random Access Response;

					6>	    if the Msg3 buffer is empty:

						7>	    obtain the MAC PDU to transmit from the MSGA buffer and store it in the Msg3 buffer;

					6>	    process the received UL grant value and indicate it to the lower layers and proceed with Msg3 transmission.

NOTE:    If within a 2-step RA type procedure, an uplink grant provided in the fallback RAR has a different size than the MSGA payload, the UE behavior is not defined.

		3>	    else if the MSGB contains a successRAR MAC subPDU; and

		3>	    if the CCCH SDU was included in the MSGA and the UE Contention Resolution Identity in the MAC subPDU matches the CCCH SDU:

			4>	    stop *msgB-ResponseWindow*;

			4>	    if this Random Access procedure was initiated for SI request:

				5>	    indicate the reception of an acknowledgement for SI request to upper layers.

			4>	    else:

				5>	    set the C-RNTI to the value received in the *successRAR*;

				5>	    apply the following actions for the SpCell:

					6>	    process the received Timing Advance Command (see clause 5.2);

					6>	    indicate the *msgA-P**reambleReceivedTargetPower* and the amount of power ramping applied to the latest Random Access Preamble transmission to lower layers (i.e. (*PREAMBLE_POWER_RAMPING_COUNTER* – 1) × *PREAMBLE_POWER_RAMPING_STEP*).

			4>	    deliver the *TPC*, *PUCCH resource Indicator*, *ChannelAccess-CPext* (if indicated), and *HARQ feedback Timing Indicator* received in successRAR to lower layers.

			4>	    consider this Random Access Response reception successful;

			4>	    consider this Random Access procedure successfully completed;

			4>	    finish the disassembly and demultiplexing of the MAC PDU.

1>	    if *msgB-ResponseWindow* expires, and the Random Access Response Reception has not been considered as successful based on descriptions above:

	2>	    increment *PREAMBLE_TRANSMISSION_COUNTER* by 1;

	2>	    if *PREAMBLE_TRANSMISSION_COUNTE**R* = *preambleTransMax* + 1:

		3>	    indicate a Random Access problem to upper layers;

		3>	    if this Random Access procedure was triggered for SI request:

			4>	    consider this Random Access procedure unsuccessfully completed.

	2>	    if the Random Access procedure is not completed:

		3>	    if *msgA-TransMax* is applied (see clause 5.1.1a) and *PREAMBLE_TRANSMISSION_COUNTER* = *msgA-TransMax* + 1:

			4>	    set the *RA_TYPE* to *4-stepRA*;

			4>	    perform initialization of variables specific to Random Access type as specified in clause 5.1.1a;

			4>	    if the Msg3 buffer is empty:

				5>	    obtain the MAC PDU to transmit from the MSGA buffer and store it in the Msg3 buffer;

			4>	    flush HARQ buffer used for the transmission of MAC PDU in the MSGA buffer;

			4>	    discard explicitly signalled contention-free 2-step RA type Random Access Resources, if any;

			4>	    perform the Random Access Resource selection procedure as specified in clause 5.1.2.

		3>	    else:

			4>	    select a random backoff time according to a uniform distribution between 0 and the *PREAMBLE_BACKOFF*;

			4>	    if the criteria (as defined in clause 5.1.2a) to select contention-free Random Access Resources is met during the backoff time:

				5>	    perform the Random Access Resource selection procedure for 2-step RA type Random Access (see clause 5.1.2a).

			4>	    else:

				5>	    perform the Random Access Resource selection procedure for 2-step RA type Random Access (see clause 5.1.2a) after the backoff time.

Upon receiving a fallbackRAR, the MAC entity may stop *msgB-ResponseWindow* once the Random Access Response reception is considered as successful.

### 5.1.5     Contention Resolution [#](#5-1-5-contention-resolution)

Once Msg3 is transmitted the MAC entity shall:

1>	    if the Msg3 transmission (i.e. initial transmission or HARQ retransmission) is scheduled with PUSCH repetition Type A:

	2>	    if Msg3 is transmitted on a non-terrestrial network:

		3>	    start or restart the ra-ContentionResolutionTimer in the first symbol after the end of all repetitions of the Msg3 transmission plus the UE-gNB RTT.

	2>	    else:

		3>	    start or restart the *ra-ContentionResolutionTimer* in the first symbol after the end of all repetitions of the Msg3 transmission.

1>	    else if Msg3 transmission (i.e. initial transmission or HARQ retransmission) is transmitted on a non-terrestrial network:

	2>	    start or restart the ra-ContentionResolutionTimer in the first symbol after the end of the Msg3 transmission plus the UE-gNB RTT.

1>	    else:

	2>	    start or restart the *ra-ContentionResolutionTimer* in the first symbol after the end of the Msg3 transmission.

1>	    monitor the PDCCH while the *ra-ContentionResolutionTimer* is running regardless of the possible occurrence of a measurement gap;

1>	    if notification of a reception of a PDCCH transmission of the SpCell is received from lower layers:

	2>	    if the C-RNTI MAC CE was included in Msg3:

		3>	    if the Random Access procedure was initiated for SpCell beam failure recovery or for beam failure recovery of both BFD-RS sets of SpCell (as specified in clause 5.17) and the PDCCH transmission is addressed to the C-RNTI; or

		3>	    if the Random Access procedure was initiated by a PDCCH order and the PDCCH transmission is addressed to the C-RNTI; or

		3>	    if the Random Access procedure was initiated for SDT beam failure recovery (as specified in clause 5.27.1) and the PDCCH transmission is addressed to the C-RNTI; or

		3>	    if the Random Access procedure was initiated by the MAC sublayer itself or by the RRC sublayer and the PDCCH transmission is addressed to the C-RNTI and contains a UL grant for a new transmission:

			4>	    consider this Contention Resolution successful;

			4>	    stop *ra-ContentionResolutionTimer*;

			4>	    discard the *TEMPORARY_C-RNTI*;

			4>	    consider this Random Access procedure successfully completed.

	2>	    else if the CCCH SDU was included in Msg3 and the PDCCH transmission is addressed to its *TEMPORARY_C-RNTI*:

		3>	    if the MAC PDU is successfully decoded:

			4>	    stop *ra-ContentionResolutionTimer*;

			4>	    if the MAC PDU contains a UE Contention Resolution Identity MAC CE; and

			4>	    if the UE Contention Resolution Identity in the MAC CE matches the CCCH SDU transmitted in Msg3:

				5>	    consider this Contention Resolution successful and finish the disassembly and demultiplexing of the MAC PDU;

				5>	    if this Random Access procedure was initiated for SI request:

					6>	    indicate the reception of an acknowledgement for SI request to upper layers.

				5>	    else:

					6>	    set the C-RNTI to the value of the *TEMPORARY_C-RNTI*;

				5>	    discard the *TEMPORARY_C-RNTI*;

				5>	    consider this Random Access procedure successfully completed.

			4>	    else:

				5>	    discard the *TEMPORARY_C-RNTI*;

				5>	    consider this Contention Resolution not successful and discard the successfully decoded MAC PDU.

		3>	    else, for eRedCap UE, if lower layer detects that PDSCH transmission scheduled by PDCCH has a larger bandwidth than UE can receive or process per slot:

			4>	    stop *ra-ContentionResolutionTimer*;

			4>	    discard the *TEMPORARY_C-RNTI*;

			4>	    consider this Contention Resolution not successful.

1>	    if *ra-ContentionResolutionTimer* expires:

	2>	    if Msg3 transmission was transmitted on a non-terrestrial network:

		3>	    if no PDCCH addressed to TC-RNTI indicating uplink grant for a Msg3 retransmission is received after the start of the *ra-ContentionResolutionTimer*:

			4>	    discard the *TEMPORARY_C-RNTI*;

			4>	    consider the Contention Resolution not successful.

	2>	    else:

		3>	    discard the *TEMPORARY_C-RNTI*;

		3>	    consider the Contention Resolution not successful.

1>	    if the Contention Resolution is considered not successful:

	2>	    flush the HARQ buffer used for transmission of the MAC PDU in the Msg3 buffer;

	2>	    increment *PREAMBLE_TRANSMISSION_COUNTER* by 1;

	2>	    if *PREAMBLE_TRANSMISSION_COUNTER* = *preambleTransMax* + 1:

		3>	    indicate a Random Access problem to upper layers.

		3>	    if this Random Access procedure was triggered for SI request:

			4>	    consider the Random Access procedure unsuccessfully completed.

	2>	    if the Random Access procedure is not completed:

		3>	    if the *RA_TYPE* is set to *4-stepRA*:

			4>	    if *preambleTransMaxRO-Type* is applied, and contention-free Random Access Resources have not been provided for this Random Access procedure, and *PREAMBLE_TRANSMISSION_COUNTER* = *preambleTransMaxRO-Type* + 1:

				5>	    if the *RO_TYPE* is set to *2nd-RO*, and set of Random Access resources associated with the same feature or feature combination, and with the same or higher Msg1 repetition number (if the Random Access Preamble is transmitted with repetitions), than the current set of Random Access resources, is available for the first PRACH occasions as defined in TS 38.213 [6]:

					6>	    set the *RO_TYPE* to *1st-RO*;

					6>	    select the set of Random Access resources associated with the same feature or feature combination, and with the same Msg1 repetition number if available, or with the next higher Msg1 repetition number otherwise (if the Random Access Preamble is transmitted with repetitions), for this Random Access procedure;

					6>	    if *sbfd-RACH-DualConfig* is configured for the Random Access procedure (see TS 38.331 [5]):

						7>	    set *PREVIOUS**_RO_TYPE_PREAMBLE_POWER_RAMPING_STEP* to *PREAMBLE_POWER_RAMPING_STEP*;

						7>	    (re-)initialize the parameters specified in clause 5.1.1 for the Random Access procedure according to the values configured by RRC for the selected="selected" set of Random Access resources;

						7>	    re-initialize *PREAMBLE_POWER_RAMPING_STEP* and *SCALING_FACTOR_BI* as specified in clause 5.1.1a;

						7>	    set *POWER_OFFSET_RO_TYPE* to (*PREAMBLE_POWER_RAMPING_COUNTER* – 1) × (*PREVIOUS**_RO_TYPE_PREAMBLE_POWER_RAMPING_STEP* – *PREAMBLE_POWER_RAMPING_STEP*).

				5>	    else if the *RO_TYPE* is set to *1st-RO*, and set of Random Access resources associated with the same feature or feature combination, and with the same or higher Msg1 repetition number (if the Random Access Preamble is transmitted with repetitions), than the current set of Random Access resources, is available for the second PRACH occasions as defined in TS 38.213 [6]:

					6>	    set the *RO_TYPE* to *2nd-RO*;

					6>	    select the set of Random Access resources associated with the same feature or feature combination, and with the same Msg1 repetition number if available, or with the next higher Msg1 repetition number otherwise (if the Random Access Preamble is transmitted with repetitions), for this Random Access procedure;

					6>	    if *sbfd-RACH-DualConfig* is configured for the Random Access procedure (see TS 38.331 [5]):

						7>	    set *PREVIOUS**_RO_TYPE_PREAMBLE_POWER_RAMPING_STEP* to *PREAMBLE_POWER_RAMPING_STEP*;

						7>	    (re-)initialize the parameters specified in clause 5.1.1 for the Random Access procedure according to the values configured by RRC for the selected="selected" set of Random Access resources;

						7>	    re-initialize *PREAMBLE_POWER_RAMPING_STEP* and *SCALING_FACTOR_BI* as specified in clause 5.1.1a;

						7>	    set *POWER_OFFSET_RO_TYPE* to (*PREAMBLE_POWER_RAMPING_COUNTER* – 1) × (*PREVIOUS**_RO_TYPE_PREAMBLE_POWER_RAMPING_STEP* – *PREAMBLE_POWER_RAMPING_STEP*).

			4>	    if the Random Access Preamble is transmitted with repetitions and contention-free Random Access Resources have not been provided for this Random Access procedure:

				5>	    if *PREAMBLE_TRANSMISSION_COUNTER* = [*preambleTransMax-Msg1-Repetition*] + 1; or

				5>	    if *PREAMBLE_TRANSMISSION_COUNTER* = 2 × [*preambleTransMax-Msg1-Repetition*] + 1:

					6>	    if set of Random Access resources configured with the same *prach-ConfigurationIndex* and associated with a higher Msg1 repetition number with the same feature or feature combination as the current set of Random Access resources is available:

						7>	    select the set of Random Access resources associated with the next higher Msg1 repetition number with the same feature or feature combination for this Random Access procedure;

						7>	    initialize *startPreambleForThisPartition*, *numberOfPreamblesPerSSB-ForThisPartition*, *numberOfRA-PreamblesGroupA* and *msg1-RepetitionTimeOffsetROGroup* parameters for the Random Access procedure according to the values configured by RRC for the selected="selected" set of Random Access resources.

			4>	    select a random backoff time according to a uniform distribution between 0 and the *PREAMBLE_BACKOFF*;

			4>	    if the criteria (as defined in clause 5.1.2) to select contention-free Random Access Resources is met during the backoff time:

				5>	    perform the Random Access Resource selection procedure (see clause 5.1.2);

			4>	    else:

				5>	    perform the Random Access Resource selection procedure (see clause 5.1.2) after the backoff time.

		3>	    else (i.e. the *RA_TYPE* is set to *2-stepRA*):

			4>	    if *msgA-TransMax* is applied (see clause 5.1.1a) and *PREAMBLE_TRANSMISSION_COUNTER* = *msgA-TransMax* + 1:

				5>	    set the *RA_TYPE* to *4-stepRA*;

				5>	    perform initialization of variables specific to Random Access type as specified in clause 5.1.1a;

				5>	    flush HARQ buffer used for the transmission of MAC PDU in the MSGA buffer;

				5>	    discard explicitly signalled contention-free 2-step RA type Random Access Resources, if any;

				5>	    perform the Random Access Resource selection as specified in clause 5.1.2.

			4>	    else:

				5>	    select a random backoff time according to a uniform distribution between 0 and the *PREAMBLE_BACKOFF*;

				5>	    if the criteria (as defined in clause 5.1.2a) to select contention-free Random Access Resources is met during the backoff time:

					6>	    perform the Random Access Resource selection procedure for 2-step RA type as specified in clause 5.1.2a.

				5>	    else:

					6>	    perform the Random Access Resource selection for 2-step RA type procedure (see clause 5.1.2a) after the backoff time.

### 5.1.6     Completion of the Random Access procedure [#](#5-1-6-completion-of-the-random-access-procedure)

Upon completion of the Random Access procedure, the MAC entity shall:

1>	    discard any explicitly signalled contention-free Random Access Resources for 2-step RA type and 4-step RA type except the 4-step RA type contention-free Random Access Resources for beam failure recovery request, if any;

1>	    flush the HARQ buffer used for transmission of the MAC PDU in the Msg3 buffer and the MSGA buffer.

Upon successful completion of the Random Access procedure initiated for DAPS handover, the target MAC entity shall:

1>	    indicate the successful completion of the Random Access procedure to the upper layers.

Upon successful completion of the Random Access procedure initiated for LTM cell switch, the MAC entity shall:

1>	    indicate the successful completion of the LTM cell switch to upper layers.
---

## TS 38.331 FeatureCombinationPreambles

#### –     *FeatureCombinationPreambles* [#](#featurecombinationpreambles)

The IE* FeatureCombinationPreambles *associates* *a set of preambles with a feature combination. For parameters which can be provided in this IE, the UE applies this field value when performing Random Access using a preamble in this featureCombinationPreambles, otherwise the UE applies the corresponding value as determined by applicable Need Code, e.g. Need S. On a specific BWP, there can be at most one set of preambles associated with a given feature combination per RA Type (i.e. 4-step RACH or 2-step RACH) per MSG1 repetition number.

*FeatureCombinationPreambles** *information element

ASN.1📋

```
`-- TAG-FEATURECOMBINATIONPREAMBLES-START
 FeatureCombinationPreambles-r17 ::=   SEQUENCE {    featureCombination-r17                FeatureCombination-r17,
startPreambleForThisPartition-r17     INTEGER (0..63),
numberOfPreamblesPerSSB-ForThisPartition-r17 INTEGER (1..64),
ssb-SharedRO-MaskIndex-r17            INTEGER (1..15)                                           OPTIONAL,
-- Need S    groupBconfigured-r17                  SEQUENCE {        ra-SizeGroupA-r17                     ENUMERATED {b56, b144, b208, b256, b282, b480, b640,                                                        b800, b1000, b72, spare6, spare5,spare4, spare3, spare2, spare1},
messagePowerOffsetGroupB-r17          ENUMERATED { minusinfinity, dB0, dB5, dB8, dB10, dB12, dB15, dB18},        numberOfRA-PreamblesGroupA-r17        INTEGER (1..64)    }                                                                                               OPTIONAL,
-- Need R    separateMsgA-PUSCH-Config-r17         MsgA-PUSCH-Config-r16                                     OPTIONAL,
-- Cond MsgAConfigCommon    msgA-RSRP-Threshold-r17               RSRP-Range                                                OPTIONAL,
-- Need R    rsrp-ThresholdSSB-r17                 RSRP-Range                                                OPTIONAL,
-- Need R    deltaPreamble-r17                     INTEGER (-1..6)                                           OPTIONAL,
-- Need R    ...,
[[    msg1-RepetitionNum-r18                ENUMERATED {n2, n4, n8, spare1}                                   OPTIONAL,
-- Cond Msg1Rep2    msg1-RepetitionTimeOffsetROGroup-r18  ENUMERATED {n4, n8, n16, spare1}                             OPTIONAL  -- Cond Msg1Rep3    ]]} -- TAG-FEATURECOMBINATIONPREAMBLES-STOP`
```

 

*FeatureCombinationPreambles** *field descriptions

***deltaPreamble***

Power offset between msg3 or msgA-PUSCH and RACH preamble transmission. If configured, this parameter overrides *msg3-DeltaPreamble* or *msgA-DeltaPreamble*, Actual value = field value * 2 [dB] (see TS 38.213 [13], clause 7.1). If *msgA-DeltaPreamble* is configured in *separateMsgA-PUSCH-Config-r17*, this field is absent. This field is set to the same value for all *FeatureCombinationPreambles* for MSG1 repetitions.

***featureCombination***

Indicates which combination of features that the preambles indicated by this IE are associated with. Network ensures that at least one field within the *featureCombination* is configured. The UE ignores a RACH resource defined by this *FeatureCombinationPreambles* if any feature within the *featureCombination* is not supported by the UE or if any of the spare fields within the *featureCombination* is set to *true*.

***messagePowerOffsetGroupB***

Threshold for preamble selection. Value is in dB. Value *minusinfinity* corresponds to –infinity. Value *dB0* corresponds to 0 dB, *dB5* corresponds to 5 dB and so on (see TS 38.321 [3], clause 5.1.2).

***msg1-RepetitionNum***

Indicates which MSG1-repetition number that this *FeatureCombinationPreambles* is associated with.

***msg1-RepetitionTimeOffsetROGroup***

Indicates a time offset of the starting ROs between two successive RO groups for a given repetition number (2, 4 or 8) associated with this *FeatureCombinationPreambles* for each frequency resource index within a time period (see TS 38.213 [13]). If this field is absent, the time offset is implicitly determined (see TS 38.213 [13]).

 

For each MSG1 repetition number, the following values are applicable.

•    {n16}, for RO groups for MSG1 repetition number 8

•    {n8, n16}, for RO groups for MSG1 repetition number 4

•    {n4, n8, n16}, for RO groups for MSG1 repetition number 2

***msgA-RSRP-Threshold***

The UE selects 2-step random access type to perform random access based on this threshold (see TS 38.321 [3], clause 5.1.1). This field is only present if both 2-step and 4-step RA type are configured for the concerned feature combination in the BWP. If configured, this parameter overrides *msgA-RSRP-Threshold-r16*. If absent, the UE applies *msgA-RSRP-Threshold-r16*, if configured

***numberOfPreambles******PerSSB-******ForThisPartition***

It determines how many consecutive preambles are associated to the Feature Combination starting from the starting preamble(s) per SSB.

***numberOfRA-PreamblesGroupA***

It determines how many consecutive preambles per SSB are associated to Group A starting from the starting preamble(s). The remaining preambles associated to the Feature Combination are associated to Group B

***ra-SizeGroupA***

Transport Blocks size threshold in bits below which the UE shall use a contention-based RA preamble of group A. (see TS 38.321 [3], clause 5.1.2). If this feature combination preambles are associated to a *RACH-ConfigCommon-twostepRA*, this field correspond to *ra-MsgA-SizeGroupA*, otherwise it corresponds to *ra-Msg3SizeGroupA*.

***rsrp-ThresholdSSB***

UE may select the SS block and corresponding PRACH resource for path-loss estimation and (re)transmission based on SS blocks that satisfy the threshold (see TS 38.213 [13]). If this parameter is included in *FeatureCombinationPreambles* which is included in *RACH-ConfigCommonTwoStepRA*, it corresponds to *msgA-RSRP-ThresholdSSB*, as defined in TS 38.321 [3]. If this parameter is included in *FeatureCombinationPreambles* which is included in *RACH-ConfigCommon*, it it corresponds to *rsrp-ThresholdSSB*, as defined in TS 38.321 [3]. If this parameter is not included in *FeatureCombinationPreambles* which is included in *RACH-ConfigCommon*, the UE applies *rsrp-ThresholdSSB* included in the *RACH-ConfigCommon *which includes this* FeatureCombinationPreambles*. If this parameter is not included in *FeatureCombinationPreambles* which is included in *RACH-ConfigCommonTwoStepRA*, the UE applies *msgA-RSRP-ThresholdSSB* included in the *RACH-ConfigCommonTwoStepRA** *which includes this* FeatureCombinationPreambles*.

***separateMsgA-PUSCH-Config***

If present, it specifies how the 2-step RACH preambles identified by this *FeatureCombinationPreambles* are mapped to a PUSCH slot separate from the one defined in MsgA-ConfigCommon-r16. If the field is absent, the UE should apply the corresponding parameter in the *RACH-ConfigCommonTwoStepRA *of the BWP which includes the* FeatureCombinationPreambles IE*.

***ssb-SharedRO-MaskIndex***

Mask index (see TS 38.321 [3]).

Indicates a subset of ROs where preambles are allocated for this feature combination.

If this field is configured within *FeatureCombinationPreambles* which is included in *RACH-ConfigCommonTwoStepRA*:

-     in case of separate ROs are configured for 4-step and 2-step random access, this field indicates a subset of ROs configured within this *RACH-ConfigCommonTwoStepRA*;

-     in case shared ROs are used for 4-step and 2-step random access, it indicates the subset of ROs configured within *RACH-ConfigCommon*, which are the subset of ROs configured for 2-step random access.

This field is configured when there is more than one RO per SSB. If the field is absent, all ROs configured in *RACH-ConfigCommon* or *RACH-ConfigCommonTwoStepRA* containing this *FeatureCombinationPreambles* are shared. The network does not configure this field, if the field *msg1-RepetitionNum* is configured.

***startPreambleForThisPartition***

It defines the first preamble associated with the Feature Combination. If the UE is provided with a number N of SSB block indexes associated with one PRACH occasion, and N<1, the first preamble in each PRACH occasion is the one having the same index as indicated by this field. If N>=1, N blocks of preambles associated with the Feature Combination are defined, each having start index + *startPreambleForThisPartition*, where n refers to SSB block index (see TS 38.213 [13], clause 8.1).

 

Conditional Presence

Explanation

*MsgAConfigCommon*

The field is optionally present, Need S, if *FeatureCombinationPreambles* is included in *RACH-ConfigCommonTwoStepRA*. Otherwise, it is absent. If the field is absent in *FeatureCombinationPreambles* included in *RACH-ConfigCommonTwoStepRA*, the UE applies *MsgA-PUSCH-Config* included in the corresponding *MsgA-ConfigCommon*.

*Msg1Rep2*

The field is mandatory present, if *msg1-Repetitions* is included in *FeatureCombination* for this concerned *FeatureCombinationPreambles*. Otherwise, it is absent.

*Msg1Rep3*

The field is optionally present, Need S, if *msg1-Repetitions* is included in *FeatureCombination* for this concerned *FeatureCombinationPreambles*. Otherwise, it is absent.
---

## TS 38.331 RACH-ConfigDedicated / CFRA

#### –     *RACH-ConfigDedicated* [#](#rach-configdedicated)

The IE *RACH-ConfigDedicated* is used to specify the dedicated random access parameters.

*RACH-ConfigDedicated* information element

ASN.1📋

```
`-- TAG-RACH-CONFIGDEDICATED-START
  RACH-ConfigDedicated ::=        SEQUENCE {    cfra                            CFRA                                                                    OPTIONAL, -- Need S    ra-Prioritization               RA-Prioritization                                                       OPTIONAL, -- Need N    ...,    [[    ra-PrioritizationTwoStep-r16    RA-Prioritization                                                       OPTIONAL, -- Need N    cfra-TwoStep-r16                CFRA-TwoStep-r16                                                        OPTIONAL  -- Need S    ]]} CFRA ::=                    SEQUENCE {    occasions                       SEQUENCE {        rach-ConfigGeneric              RACH-ConfigGeneric,
ssb-perRACH-Occasion            ENUMERATED {oneEighth, oneFourth, oneHalf, one, two, four, eight, sixteen}                                                                                                            OPTIONAL  -- Cond Mandatory    }                                                                                                       OPTIONAL,
-- Need S    resources                       CHOICE {        ssb                             SEQUENCE {            ssb-ResourceList                SEQUENCE (SIZE(1..maxRA-SSB-Resources)) OF CFRA-SSB-Resource,            ra-ssb-OccasionMaskIndex        INTEGER (0..15)        },
csirs                           SEQUENCE {            csirs-ResourceList              SEQUENCE (SIZE(1..maxRA-CSIRS-Resources)) OF CFRA-CSIRS-Resource,            rsrp-ThresholdCSI-RS            RSRP-Range        }    },
...,
[[    totalNumberOfRA-Preambles INTEGER (1..63)                                                             OPTIONAL -- Cond Occasions    ]],
[[    msg1-RepetitionNum-r18          ENUMERATED {n2, n4, n8, spare1}                                               OPTIONAL -- Cond 4StepCFRArep    ]]} CFRA-TwoStep-r16 ::=                    SEQUENCE {    occasionsTwoStepRA-r16                  SEQUENCE {        rach-ConfigGenericTwoStepRA-r16         RACH-ConfigGenericTwoStepRA-r16,
ssb-PerRACH-OccasionTwoStepRA-r16       ENUMERATED {oneEighth, oneFourth, oneHalf, one,                                                            two, four, eight, sixteen}    }                                                                                                     OPTIONAL,
-- Need S    msgA-CFRA-PUSCH-r16                     MsgA-PUSCH-Resource-r16,
msgA-TransMax-r16                       ENUMERATED {n1, n2, n4, n6, n8, n10, n20, n50, n100, n200}    OPTIONAL,
-- Need S    resourcesTwoStep-r16                    SEQUENCE {        ssb-ResourceList                        SEQUENCE (SIZE(1..maxRA-SSB-Resources)) OF CFRA-SSB-Resource,        ra-ssb-OccasionMaskIndex                INTEGER (0..15)    },    ...} CFRA-SSB-Resource ::=           SEQUENCE {    ssb                             SSB-Index,    ra-PreambleIndex                INTEGER (0..63),    ...,    [[    msgA-PUSCH-Resource-Index-r16   INTEGER (0..3071)     OPTIONAL  -- Cond 2StepCFRA    ]] } CFRA-CSIRS-Resource ::=         SEQUENCE {    csi-RS                          CSI-RS-Index,    ra-OccasionList                 SEQUENCE (SIZE(1..maxRA-OccasionsPerCSIRS)) OF INTEGER (0..maxRA-Occasions-1),    ra-PreambleIndex                INTEGER (0..63),    ...} -- TAG-RACH-CONFIGDEDICATED-STOP`
```

 

*CFRA-CSIRS-Resource *field descriptions

***csi-RS***

The ID of a CSI-RS resource defined in the measurement object associated with this serving cell.

***ra-OccasionList***

RA occasions that the UE shall use when performing CF-RA upon selecting the candidate beam identified by this CSI-RS. The network ensures that the RA occasion indexes provided herein are also configured by prach-ConfigurationIndex and msg1-FDM. Each RACH occasion is sequentially numbered, first, in increasing order of frequency resource indexes for frequency multiplexed PRACH occasions; second, in increasing order of time resource indexes for time multiplexed PRACH occasions within a PRACH slot and Third, in increasing order of indexes for PRACH slots.

***ra-PreambleIndex***

The RA preamble index to use in the RA occasions associated with this CSI-RS.

 

*CFRA *field descriptions

***msg1-RepetitionNum***

Indicates the MSG1 repetition number used for contention free 4-step random access type in TS 38.321 [3]. If this field is absent, the UE performs contention free 4-step random access without MSG1-Repetitions.

***occasions***

RA occasions for contention free random access. If the field is absent, the UE uses the RA occasions configured in *RACH-ConfigCommon* in the first active UL BWP.

***ra-ssb-OccasionMaskIndex***

Explicitly signalled PRACH Mask Index for RA Resource selection in TS 38.321 [3]. The mask is valid for all SSB resources signalled in *ssb-ResourceList*. The UE shall ignore this field if the field *msg1-RepetitionNum* included in *CFRA* is configured.

***rach-ConfigGeneric***

Configuration of contention free random access occasions for CFRA. The UE shall ignore *preambleReceivedTargetPower*, *preambleTransMax*, *powerRampingStep*, *ra-ResponseWindow* signaled within this field and use the corresponding values provided in *RACH-ConfigCommon*.

***ssb-perRACH-Occasion***

Number of SSBs per RACH occasion.

***totalNumberOfRA-Preambles***

Total number of preambles used for contention free random access in the RACH resources defined in CFRA, excluding preambles used for other purposes (e.g. for SI request). If the field is absent but the field *occasions* is present, the UE may assume all the 64 preambles are for RA. The setting should be consistent with the setting of *ssb-perRACH-Occasion*, if present, i.e. it should be a multiple="multiple" of the number of SSBs per RACH occasion.

 

*CFRA-SSB-Resource *field descriptions

***msgA-PUSCH-******R******esource-Index***

Identifies the index of the PUSCH resource used for MSGA CFRA. The PUSCH resource index indicates a valid PUSCH occasion (as specified in TS 38.213 [13], clause 8.1A) and the associated DMRS resources corresponding to a PRACH slot. The PUSCH resource indexes are sequentially numbered and are mapped to valid PUSCH occasions corresponding to a PRACH slot which are ordered, first, in increasing order of frequency resource indexes for frequency multiplexed PUSCH occasions; second, in increasing order of DMRS resource indexes within a PUSCH occasion, where a *DMR*\(\mathbf{S}_{\mathbf{i}\mathbf{d}}\) resource index is determined first in an ascending order of a DMRS port index and then in an ascending order of a DMRS sequence index, third in increasing order of time resource indexes for time multiplexed PUSCH occasions within a PUSCH slot and fourth, in increasing order of indexes for PUSCH slots. For the case of contention free 2-step random access type, if this field is absent, the UE shall use the value 0.

***ra-PreambleIndex***

The preamble index that the UE shall use when performing CF-RA upon selecting the candidate beams identified by this SSB.

***ssb***

The ID of an SSB transmitted by this serving cell.

 

*CFRA-TwoStep *field descriptions

***msgA-CFRA-PUSCH***

PUSCH resource configuration(s) for msgA CFRA.

***msgA-TransMax***

Max number of MsgA preamble transmissions performed before switching to 4-step type random access (see TS 38.321 [3], clauses 5.1.1). This field is only applicable when 2-step and 4-step RA type are configured and switching to 4-step type RA is supported. If the field is absent in *cfra-TwoStep*, switching from 2-step RA type to 4-step RA type is not allowed.

***occasionsTwoStepRA***

RA occasions for contention free random access. If the field is absent, the UE uses the RA occasions configured in *RACH-ConfigCommonTwoStepRA* in the first active UL BWP.

***ra-SSB-OccasionMaskIndex***

Explicitly signalled PRACH Mask Index for RA Resource selection in TS 38.321 [3]. The mask is valid for all SSB resources signalled in *ssb-ResourceList*.

***rach-ConfigGenericTwoStepRA***

Configuration of contention free random access occasions for CFRA 2-step random access type.

***ssb-PerRACH-OccasionTwoStep***

Number of SSBs per RACH occasion for 2-step random access type.

 

*RACH-ConfigDedicated *field descriptions

***cfra***

Parameters for contention free random access to a given target cell. If this field and *cfra-TwoStep* are absent, the UE performs contention based random access.

***cfra-TwoStep***

Parameters for contention free 2-step random access type to a given target cell. Network ensures that *cfra* and *cfra-TwoStep* are not configured at the same time. If this field and *cfra* are absent, the UE performs contention based random access.

***ra-prioritization***

Parameters which apply for prioritized random access procedure to a given target cell (see TS 38.321 [3], clause 5.1.1).

***ra-PrioritizationTwoStep***

Parameters which apply for prioritized 2-step random access type procedure to a given target cell (see TS 38.321 [3], clause 5.1.1).

 

Conditional Presence

Explanation

*Mandatory*

The field is mandatory present.

*Occasions*

The field is optionally present, Need S, if the field *occasions* is present, otherwise it is absent.

*2StepCFRA*

The field is optionally present for the case of 2-step RA type contention free random access, Need S, otherwise it is absent.

*4StepCFRArep*

For non-(e)RedCap UEs, the field is optionally present, Need S, if *resources* is set to *ssb* and there is one *FeatureCombinationPreambles* entry indicating only *msg1-Repetitions* which is associated with the same Msg1 repetition number.

For RedCap UEs or if RedCap is considered to be applicable for this Random Access procedure for eRedCap UEs, the field is optionally present, Need S, if *resources* is set to *ssb* and there is one *FeatureCombinationPreambles* entry indicating only *redCap* and *msg1-Repetitions* which is associated with the same Msg1 repetition number.

For eRedCap UEs, if eRedCap is considered to be applicable for this Random Access procedure, the field is optional present, Need S, if *resource* is set to *ssb* and there is one *FeatureCombinationPreambles* entry indicating only *eRedCap* and *msg1-Repetitions* which is associated with the same Msg1 repetition number.

Otherwise, it is absent.
---

## Proposed deltas (diff style)

```diff
--- TS 38.213 §8.1 (current)
+++ TS 38.213 §8.1 (proposed: Msg1 repetition root hopping)
@@ Higher-layer configuration for PRACH with repetitions @@
+ Add higher-layer parameter:
+ - msg1-RepetitionRootSequenceIndexList (optional)
+   - size equals N_preamble^rep
+   - each entry is a PRACH rootSequenceIndex (same family across the list)
+
+ UE behavior when PRACH is transmitted with repetitions (N_preamble^rep > 1):
+ - If msg1-RepetitionRootSequenceIndexList is provided:
+     repetition index i is the i-th PRACH occasion within the repetition set, in increasing time order;
+     UE uses msg1-RepetitionRootSequenceIndexList[i] as the rootSequenceIndex for PRACH sequence generation for repetition i.
+ - Else:
+     UE uses the configured PRACH rootSequenceIndex for all repetitions.
+
+ Clarify that “same preambles” in repetition-set semantics refers to same preamble *index* (RAPID),
+ not necessarily identical ZC root across repetitions when configured.

--- TS 38.213 §7.4 (current)
+++ TS 38.213 §7.4 (proposed: clarification only)
@@ RAR-not-received / “preamble sequence transmitted” wording @@
+ Clarify that for PRACH with repetitions, “preamble sequence transmitted” applies per repetition,
+ while the PRACH attempt remains identified by the configured preamble index (RAPID) and repetition set timing.

--- TS 38.321 §5.1 (current)
+++ TS 38.321 §5.1 (proposed: clarification only)
@@ Msg1 repetition and PHY configuration @@
+ Add a clarification note:
+ - When Msg1 is transmitted with repetitions, lower layers may be configured (by RRC) to use
+   different PRACH root sequence indexes per repetition; MAC variables and procedure behavior are unchanged
+   because PREAMBLE_INDEX (RAPID) and repetition-set timing semantics are unchanged.
+
@@ MAC-to-PHY instruction for PRACH transmission @@
+ Clarify that when msg1-RepetitionRootSequenceIndexList is configured, the UE provides lower layers
+ with the per-repetition root sequence index such that repetition i within the repetition set uses list entry i
+ (repetition index per TS 38.213 §8.1).

--- TS 38.331 / NR-RRC-Definitions (current)
+++ TS 38.331 / NR-RRC-Definitions (proposed: Msg1 repetition root hopping)
@@ New type(s) @@
+ Msg1-RepetitionRootSequenceIndex-rXX ::= CHOICE {
+   l839  INTEGER(0..837),
+   l139  INTEGER(0..137),
+   l571  INTEGER(0..569),
+   l1151 INTEGER(0..1149)
+ }
+
+ Msg1-RepetitionRootSequenceIndexList-rXX ::= SEQUENCE (SIZE (1..8)) OF Msg1-RepetitionRootSequenceIndex-rXX
+
@@ FeatureCombinationPreambles-r17 extension group @@
+ Add msg1-RepetitionRootSequenceIndexList-rXX OPTIONAL alongside msg1-RepetitionNum-r18 and msg1-RepetitionTimeOffsetROGroup-r18.
+
@@ CFRA extension group @@
+ Add msg1-RepetitionRootSequenceIndexList-rXX OPTIONAL alongside msg1-RepetitionNum-r18.
+
@@ UE capability gating @@
+ Add per-band capability flag msg1-RepetitionRootHoppingSupport-rXX {supported} OPTIONAL.
+ Network configures the list only if UE indicated support.
```
---

## Proposed IE field descriptions (new IEs)

### `msg1-RepetitionRootSequenceIndexList-rXX`

Indicates the PRACH root sequence index to be used for each Msg1 repetition within a repetition set (see TS 38.213, clause 8.1).

If present, for repetition index *i* (0..Nrep−1) within the repetition set (in increasing time order of PRACH occasions), the UE shall use the *i*-th entry of this list as the root sequence index for PRACH preamble sequence generation. All other PRACH parameters (e.g., PRACH format, subcarrier spacing, PRACH resources/occasions, spatial filter, and preamble index) remain as configured.

If absent, the UE shall use the configured `prach-RootSequenceIndex` (or `prach-RootSequenceIndex-r16`, where applicable) for all repetitions.

Constraints (normative intent):

- The list size shall match the configured Msg1 repetition number.
- All entries shall use the same root-length family and be consistent with the configured PRACH configuration.

### `msg1-RepetitionRootHoppingSupport-rXX`

If present, indicates that the UE supports configuration of different PRACH root sequence indexes across Msg1 repetitions using `msg1-RepetitionRootSequenceIndexList-rXX`.

Network usage rule (normative intent): the network shall configure `msg1-RepetitionRootSequenceIndexList-rXX` only if the UE indicated `msg1-RepetitionRootHoppingSupport-rXX` for the serving band.
