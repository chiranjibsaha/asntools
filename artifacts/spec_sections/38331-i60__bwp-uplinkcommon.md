#### –     *BWP-UplinkCommon* [#](#bwp-uplinkcommon)

The IE *BWP-UplinkCommon* is used to configure the common parameters of an uplink BWP. They are "cell specific" and the network ensures the necessary alignment with corresponding parameters of other UEs. The common parameters of the initial bandwidth part of the PCell, excluding *additionalRACH-perPCI-ToAddModList* and *additionalRACH-perPCI-ToReleaseList*, are also provided via system information. For all other serving cells, the network provides the common parameters via dedicated signalling.

*BWP-UplinkCommon* information element

ASN.1📋

```
`-- TAG-BWP-UPLINKCOMMON-START
 BWP-UplinkCommon ::=                SEQUENCE {    genericParameters                   BWP,
rach-ConfigCommon                   SetupRelease { RACH-ConfigCommon }                                      OPTIONAL,
-- Need M    pusch-ConfigCommon                  SetupRelease { PUSCH-ConfigCommon }                                     OPTIONAL,
-- Need M    pucch-ConfigCommon                  SetupRelease { PUCCH-ConfigCommon }                                     OPTIONAL,
-- Need M    ...,
[[    rach-ConfigCommonIAB-r16            SetupRelease { RACH-ConfigCommon }                                      OPTIONAL,
-- Need M    useInterlacePUCCH-PUSCH-r16         ENUMERATED {enabled}                                                    OPTIONAL,
-- Need R    msgA-ConfigCommon-r16               SetupRelease { MsgA-ConfigCommon-r16 }                                  OPTIONAL    -- Cond SpCellOnly2    ]],
[[    enableRA-PrioritizationForSlicing-r17 BOOLEAN                                                    OPTIONAL,
-- Cond RA-PrioSliceAI    additionalRACH-ConfigList-r17       SetupRelease { AdditionalRACH-ConfigList-r17 }               OPTIONAL,
-- Cond SpCellOnly2    rsrp-ThresholdMsg3-r17              RSRP-Range                                                   OPTIONAL,
-- Need R    numberOfMsg3-RepetitionsList-r17    SEQUENCE (SIZE (4)) OF NumberOfMsg3-Repetitions-r17                  OPTIONAL,
-- Cond Msg3Rep    mcs-Msg3-Repetitions-r17            SEQUENCE (SIZE (8)) OF INTEGER (0..31)                               OPTIONAL   -- Cond Msg3Rep    ]],
[[    additionalRACH-perPCI-ToAddModList-r18   SEQUENCE (SIZE (1.. maxNrofAdditionalPRACHConfigs-r18)) OF  RACH-ConfigTwoTA-r18                                                                                                             OPTIONAL,
-- Cond 2TA-Only    additionalRACH-perPCI-ToReleaseList-r18  SEQUENCE (SIZE (1.. maxNrofAdditionalPRACHConfigs-r18)) OF AdditionalPCIIndex-r17                                                                                                             OPTIONAL,
-- Need N    rsrp-ThresholdMsg1-RepetitionNum2-r18    RSRP-Range                                                      OPTIONAL,
-- Need R    rsrp-ThresholdMsg1-RepetitionNum4-r18    RSRP-Range                                                      OPTIONAL,
-- Need R    rsrp-ThresholdMsg1-RepetitionNum8-r18    RSRP-Range                                                      OPTIONAL,
-- Need R    preambleTransMax-Msg1-Repetition-r18     ENUMERATED {n1, n2, n4, n6, n8, n10, n20, n50, n100, n200}      OPTIONAL   -- Cond Msg1Rep1    ]]} AdditionalRACH-ConfigList-r17 ::=       SEQUENCE (SIZE(1..maxAdditionalRACH-r17)) OF AdditionalRACH-Config-r17 AdditionalRACH-Config-r17 ::=       SEQUENCE {    rach-ConfigCommon-r17               RACH-ConfigCommon                                                   OPTIONAL,  -- Need R    msgA-ConfigCommon-r17               MsgA-ConfigCommon-r16                                               OPTIONAL,  -- Need R    ...} NumberOfMsg3-Repetitions-r17::=         ENUMERATED {n1, n2, n3, n4, n7, n8, n12, n16} -- TAG-BWP-UPLINKCOMMON-STOP`
```

 

*BWP-UplinkCommon *field descriptions

***additionalRACH-Config******List***

List of feature or feature combination-specific RACH configurations, i.e. the RACH configurations configured in addition to the one configured by *rach-ConfigCommon* and by *msgA-ConfigCommon*. The network associates all possible preambles of an additional RACH configuration to one or more feature(s) or feature combination(s). The network does not configure this list to have more than 16 entries. If both *rach-ConfigCommon* and *msgA-ConfigCommon* are configured for a specific *FeatureCombination*, the network always provides them in the same *additionalRACH-Config*.

***additionalRACH-perPCI-ToAddModList******, additionalRACH-perPCI-ToReleaseList***

List of RACH configurations for the additional PCIs. The RACH configuration for an additional PCI is applied for Random Access procedure initiated by PDCCH order towards to the additional PCI, as specified in TS 38.321 clause 5.1.1b. This list includes the same number of elements like *additionalPCI-ToAddModList* for this serving cell and the *n*-th element of this list is for the PCI in the *n*-th element of *additionalPCI-ToAddModList*. Either the network does not configure any RACH configuration for any additional PCI, or the network configures a RACH configuration for each additional PCI. When the network releases an additional PCI of a serving cell, the network also explicitly releases the associated random access configuration in every UL BWP of the serving cell. This configuration may be different for different UEs.

***enableRA-PrioritizationForSlicing***

Indicates whether or not the *ra-PrioritizationForSlicing**/ra-PrioritizationForSlicingTwoStep* should override the *ra-PrioritizationForAccessIdentity*. The field is applicable only when the UE is configured by upper layers with both NSAG and Access Identity 1 or 2. If value *TRUE* is configured, the UE should only apply the *ra-PrioritizationForSlicing/ra-PrioritizationForSlicingTwoStep*. If value *FALSE *is configured, the UE should only apply *ra-PrioritizationForAccessIdentity*. If the field is absent, whether to use *ra-PrioritizationForSlicing/ra-PrioritizationForSlicingTwoStep* or *ra-PrioritizationForAccessIdentity* is up to UE implementation.

***mcs-Msg3-Repetitions***

Configuration of eight candidate MCS indexes for PUSCH transmission scheduled by RAR UL grant and DCI format 0_0 with CRC scrambled by TC-RNTI. Only the first 4 configured or default MCS indexes are used for PUSCH transmission scheduled by RAR UL grant. This field is only applicable when the UE selects Random Access resources indicating Msg3 repetition in this BWP. If this field is absent when the set(s) of Random Access resources with MSG3 repetition indication are configured in the *BWP-UplinkCommon*, the UE shall apply the values {0, 1, 2, 3, 4, 5, 6, 7} (see TS 38.214 [19], clause 6.1.4).

***msgA-ConfigCommon***

Configuration of the cell specific PRACH and PUSCH resource parameters for transmission of MsgA in 2-step random access type procedure. The NW can configure *msgA-ConfigCommon* only for UL BWPs if the linked DL BWPs (same bwp-Id as UL-BWP) are the initial DL BWPs or DL BWPs containing the SSB associated to the initial DL BWP or DL BWPs associated with *nonCellDefiningSSB* or, for (e)RedCap UEs, the RedCap-specific initial downlink BWP. The network configures *msgA-ConfigCommon *(without suffix) and/or *msgA-ConfigCommon-r17*, whenever it configures contention free 2-step random access, the UE then applies the corresponding configuration depending on the RACH resource set selected="selected" upon RACH initialization, as specified in TS 38.321 [3].

***numberOfMsg3-RepetitionsList***

The number of repetitions for PUSCH transmission scheduled by RAR UL grant and DCI format 0_0 with CRC scrambled by TC-RNTI. This field is only applicable when the UE selects Random Access resources indicating Msg3 repetition in this BWP. If this field is absent when the set(s) of Random Access resources with MSG3 repetition indication are configured in the *BWP-UplinkCommon*, the UE shall apply the values {n1, n2, n3, n4} (see TS 38.214 [19], clause 6.1.2.1).

***preambleTransMax-Msg1-Repetition***

Max number of transmissions of MSG1 repetitions number (2, 4 and 8) performed before switching to higher repetition number (see TS 38.321 [3], clauses 5.1.1). This field is only applicable when more than one repetition numbers are configured in shared RO. If the field is absent, switching from lower repetition number to higher repetition number is not allowed.

***pucch-ConfigCommon***

Cell specific parameters for the PUCCH of this BWP.

***pusch-ConfigCommon***

Cell specific parameters for the PUSCH of this BWP.

***rach-ConfigCommon***

Configuration of cell specific random access parameters which the UE uses for contention based and contention free random access as well as for contention based beam failure recovery in this BWP. The NW configures SSB-based RA (and hence *RACH-ConfigCommon*) only for UL BWPs if the linked DL BWPs (same *bwp-Id* as UL-BWP) are the initial DL BWPs or DL BWPs containing the SSB associated to the initial DL BWP or DL BWPs associated with *nonCellDefiningSSB* or, for (e)RedCap UEs, the RedCap-specific initial downlink BWP. The network configures *rach-ConfigCommon* (without suffix) and/or *rach-ConfigCommon-r17*, whenever it configures contention free 4-step random access (e.g. for reconfiguration with sync or for beam failure recovery or PDCCH order), the UE then applies the corresponding configuration depending on the RACH resource set selected="selected" upon RACH initialization, as specified in TS 38.321 [3]. For RedCap-specific initial uplink BWP, *rach-ConfigCommon* is always configured when *msgA-ConfigCommon* is configured in this BWP.

***rach-ConfigCommonIAB***

Configuration of cell specific random access parameters for the IAB-MT. The IAB specific IAB RACH configuration is used by IAB-MT, if configured.

***rsrp-ThresholdMsg1-RepetitionNum2, rsrp-ThresholdMsg1-RepetitionNum4, rsrp-ThresholdMsg1-RepetitionNum8***

Threshold used by the UE for determining whether to select resources indicating Msg1 repetition number 2, 4 or 8 in this BWP, as specified in TS 38.321 [3]. The value applies to all the BWPs and all RACH configurations. For a given MSG1 repetition number, this corresponding field is mandatory if both set(s) of Random Access resources with MSG1 repetition indication associated with this MSG1 repetition number and set(s) of Random Access resources without MSG1 repetition indication are configured in the BWP, or if the set(s) of Random Access resources with MSG1 repetition indication associated with this MSG1 repetition number and set(s) of Random Access resources with MSG1 repetition indication associated with a lower repetition number are configured in the BWP. It is absent otherwise.

***rsrp-ThresholdMsg3***

Threshold used by the UE for determining whether to select resources indicating Msg3 repetition in this BWP, as specified in TS 38.321 [3]. The field is mandatory if both set(s) of Random Access resources with MSG3 repetition indication and set(s) of Random Access resources without MSG3 repetition indication are configured in the BWP. It is absent otherwise.

***useInterlacePUCCH-PUSCH***

If the field is present, the UE uses uplink frequency domain resource allocation Type 2 for cell-specific PUSCH, e.g., PUSCH scheduled by RAR UL grant (see TS 38.213 [13] clause 8.3 and TS 38.214 [19], clause 6.1.2.2) and uses interlaced PUCCH Format 0 and 1 for cell-specific PUCCH (see TS 38.213 [13], clause 9.2.1).

 

Conditional Presence

Explanation

*Msg1Rep1*

This field is optionally present, Need R, if the set(s) of Random Access resources with MSG1 repetition indication are configured in the *BWP-UplinkCommon*. It is absent otherwise.

*Msg3Rep*

This field is optionally present, Need S, if the set(s) of Random Access resources with MSG3 repetition indication are configured in the *BWP-UplinkCommon*. It is absent otherwise.

*RA**-**PrioSliceAI*

The field is optionally present in *SIB1*, Need R, if both parameters *ra-PrioritizationForAccessIdentity* and the *ra-PrioritizationForSlicing/ra-PrioritizationForSlicingTwoStep* are present in *SIB1*. It is absent otherwise.

*SpCellOnly2*

The field is optionally present, Need M, in the *BWP-UplinkCommon* of an SpCell. It is absent otherwise.

*2TA-Only*

The field is optionally present, Need N in the *BWP-UplinkCommon* if *additionalPCI-ToAddModList* is present in *ServingCellConfig** *and if *tag2* is present in *ServingCellConfig*. It is absent otherwise.
