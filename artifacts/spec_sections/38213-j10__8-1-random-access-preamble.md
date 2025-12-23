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
