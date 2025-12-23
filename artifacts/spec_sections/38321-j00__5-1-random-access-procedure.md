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
