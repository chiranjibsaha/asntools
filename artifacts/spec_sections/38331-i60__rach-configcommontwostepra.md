#### –     *RACH-ConfigCommonTwoStepRA* [#](#rach-configcommontwostepra)

The IE *RACH-ConfigCommonTwoStepRA* is used to specify cell specific 2-step random-access type parameters.

*RACH-ConfigCommonTwoStepRA* information element

ASN.1📋

```
`-- TAG-RACH-CONFIGCOMMONTWOSTEPRA-START
 RACH-ConfigCommonTwoStepRA-r16 ::=                   SEQUENCE {    rach-ConfigGenericTwoStepRA-r16                      RACH-ConfigGenericTwoStepRA-r16,
msgA-TotalNumberOfRA-Preambles-r16                   INTEGER (1..63)                                    OPTIONAL,
-- Need S    msgA-SSB-PerRACH-OccasionAndCB-PreamblesPerSSB-r16   CHOICE {        oneEighth                                            ENUMERATED {n4,n8,n12,n16,n20,n24,n28,n32,n36,n40,n44,n48,n52,n56,n60,n64},
oneFourth                                            ENUMERATED {n4,n8,n12,n16,n20,n24,n28,n32,n36,n40,n44,n48,n52,n56,n60,n64},
oneHalf                                              ENUMERATED {n4,n8,n12,n16,n20,n24,n28,n32,n36,n40,n44,n48,n52,n56,n60,n64},
one                                                  ENUMERATED {n4,n8,n12,n16,n20,n24,n28,n32,n36,n40,n44,n48,n52,n56,n60,n64},
two                                                  ENUMERATED {n4,n8,n12,n16,n20,n24,n28,n32},        four                                                 INTEGER (1..16),        eight                                                INTEGER (1..8),        sixteen                                              INTEGER (1..4)    }                                                                                                                   OPTIONAL,
-- Cond 2StepOnly    msgA-CB-PreamblesPerSSB-PerSharedRO-r16              INTEGER (1..60)                                                OPTIONAL,
-- Cond SharedRO    msgA-SSB-SharedRO-MaskIndex-r16                      INTEGER (1..15)                                                OPTIONAL,
-- Need S    groupB-ConfiguredTwoStepRA-r16                       GroupB-ConfiguredTwoStepRA-r16                                 OPTIONAL,
-- Need S    msgA-PRACH-RootSequenceIndex-r16                     CHOICE {        l839                                                 INTEGER (0..837),        l139                                                 INTEGER (0..137),        l571                                                 INTEGER (0..569),        l1151                                                INTEGER (0..1149)    }                                                                                                                   OPTIONAL,
-- Cond 2StepOnly    msgA-TransMax-r16                                    ENUMERATED {n1, n2, n4, n6, n8, n10, n20, n50, n100, n200}     OPTIONAL,
-- Need R    msgA-RSRP-Threshold-r16                              RSRP-Range                                                     OPTIONAL,
-- Cond 2Step4Step    msgA-RSRP-ThresholdSSB-r16                           RSRP-Range                                                     OPTIONAL,
-- Need R    msgA-SubcarrierSpacing-r16                           SubcarrierSpacing                                              OPTIONAL,
-- Cond 2StepOnlyL139    msgA-RestrictedSetConfig-r16                         ENUMERATED {unrestrictedSet, restrictedSetTypeA,                                                                     restrictedSetTypeB}                                OPTIONAL,
-- Cond 2StepOnly    ra-PrioritizationForAccessIdentityTwoStep-r16        SEQUENCE {        ra-Prioritization-r16                                RA-Prioritization,        ra-PrioritizationForAI-r16                           BIT STRING (SIZE (2))    }                                                                                                                   OPTIONAL,
-- Cond InitialBWP-Only    ra-ContentionResolutionTimer-r16                     ENUMERATED {sf8, sf16, sf24, sf32, sf40, sf48, sf56, sf64}     OPTIONAL, -- Cond 2StepOnly    ...,    [[    ra-PrioritizationForSlicingTwoStep-r17               RA-PrioritizationForSlicing-r17              OPTIONAL, -- Cond InitialBWP-Only    featureCombinationPreamblesList-r17 SEQUENCE (SIZE(1..maxFeatureCombPreamblesPerRACHResource-r17)) OF FeatureCombinationPreambles-r17 OPTIONAL  -- Cond AdditionalRACH    ]]} GroupB-ConfiguredTwoStepRA-r16 ::=                       SEQUENCE {    ra-MsgA-SizeGroupA-r16                               ENUMERATED {b56, b144, b208, b256, b282, b480, b640, b800,                                                                     b1000, b72, spare6, spare5, spare4, spare3, spare2, spare1},
messagePowerOffsetGroupB-r16                         ENUMERATED {minusinfinity, dB0, dB5, dB8, dB10, dB12, dB15, dB18},    numberOfRA-PreamblesGroupA-r16                       INTEGER (1..64)} -- TAG-RACH-CONFIGCOMMONTWOSTEPRA-STOP`
```

 

*RACH-ConfigCommonTwoStepRA *field descriptions

***featureCombinationPreambles******List***

Specifies a series of preamble partitions each associated to a combination of features and 2-step RA. The network does not configure this list to have more than 16 entries.

***groupB-ConfiguredTwoStepRA***

Preamble grouping for 2-step random access type. If the field is absent then there is only one preamble group configured and only one msgA PUSCH configuration.

***msgA-CB-PreamblesPerSSB-PerSharedRO***

Number of contention-based preambles used for 2-step RA type from the non-CBRA 4-step type preambles associated with each SSB for RO shared with 4-step type RA. The number of preambles for 2-step RA type shall not exceed the number of preambles per SSB minus the number of contention-based preambles per SSB for 4-step type RA. The possible value range for this parameter needs to be aligned with value range for the configured SSBs per RACH occasion in *ssb**-perRACH-OccasionAndCB-PreamblesPerSSB* in *RACH-ConfigCommon*. The field is only applicable for the case of shared ROs with 4-step type random access.

***msgA-PRACH-RootSequenceIndex***

PRACH root sequence index. If the field is not configured in *RACH-ConfigCommonTwoStepRA *which is configured directly within a BWP (i.e., not within *AdditionalRACH-Config*), the UE applies the value in field *prach-RootSequenceIndex* in *RACH-ConfigCommon* in the configured BWP. If the field is absent in *RACH-ConfigCommonTwoStepRA* in *AdditionalRACH-Config*, the UE applies the corresponding value of *prach-RootSequenceIndex* in *RACH-ConfigCommon* in the same *AdditionalRACH-Config*. When both 2-step and 4-step type random access is configured, this field is only configured for the case of separate ROs between 2-step and 4-step type random access.

For FR2-2, only the following values are applicable depending on the used subcarrier spacing:

120 kHz:  L=139, L=571, and L=1151

480 kHz:  L=139, and L=571

960 kHz:  L=139

***msgA-RestrictedSetConfig***

Configuration of an unrestricted set or one of two types of restricted sets for 2-step random access type preamble. If the field is not configured in *RACH-ConfigCommonTwoStepRA *which is configured directly within a BWP (i.e. not within *AdditionalRACH-Config*), the UE applies the value in field *restrictedSetConfig* in *RACH-ConfigCommon* in the configured BWP. If the field is absent in *RACH-ConfigCommonTwoStepRA* in *AdditionalRACH-Config*, the UE applies the value of *restrictedSetConfig* in *RACH-ConfigCommon* in the same *AdditionalRACH-Config*. When both 2-step and 4-step type random access is configured, this field is only configured for the case of separate ROs between 2-step and 4-step type random access.

***msgA-RSRP-Threshold***

The UE selects 2-step random access type to perform random access based on this threshold (see TS 38.321 [3], clause 5.1.1). This field is only present if both 2-step and 4-step RA type are configured for the BWP.

***msgA-RSRP-ThresholdSSB***

UE may select the SS block and corresponding PRACH resource for path-loss estimation and (re)transmission based on SS blocks that satisfy the threshold (see TS 38.213 [13]).

***msgA-SSB-PerRACH-OccasionAndCB-PreamblesPerSSB***

The meaning of this field is twofold: the CHOICE conveys the information about the number of SSBs per RACH occasion. Value *oneEight* corresponds to one SSB associated with 8 RACH occasions, value *oneFourth* corresponds to one SSB associated with 4 RACH occasions, and so on. The ENUMERATED part indicates the number of Contention Based preambles per SSB. Value *n4* corresponds to 4 Contention Based preambles per SSB, value *n8* corresponds to 8 Contention Based preambles per SSB, and so on. The total number of CB preambles in a RACH occasion is given by *CB-preambles-per-SSB* * max(1, *SSB-per-rach-occasion*). If the field is not configured in *RACH-ConfigCommonTwoStepRA *which is configured directly within a BWP (i.e. not within *AdditionalRACH-Config*) and both 2-step and 4-step are configured for the BWP, the UE applies the value in the field *ssb-perRACH-OccasionAndCB-PreamblesPerSSB* in *RACH-ConfigCommon**.* If the field is not configured in *AdditionalRACH-Config* and both 2-step and 4-step are configured in *AdditionalRACH-Config*, the UE applies the value in the field *ssb-perRACH-OccasionAndCB-PreamblesPerSSB* in *RACH-ConfigCommon *in the same *AdditionalRACH-Config*. The field is not present when RACH occasions are shared between 2-step and 4-step type random access in the BWP.

***msgA-SSB-SharedRO-MaskIndex***

Indicates the subset of 4-step type ROs shared with 2-step random access type for each SSB. This field is configured when there is more than one RO per SSB. If the field is absent, and 4-step and 2-step has shared ROs, then all ROs are shared.

***msgA-SubcarrierSpacing***

Subcarrier spacing of PRACH (see TS 38.211 [16], clause 5.3.2).

Only the following values are applicable depending on the used frequency:

FR1:    15 or 30 kHz

FR2-1/FR2-NTN:  60 or 120 kHz

FR2-2:  120, 480, or 960 kHz.

If the field is absent, the UE applies the SCS as derived from the *msgA-**PRACH-ConfigurationIndex* in *RACH-ConfigGeneric**TwoStepRA* (see tables Table 6.3.3.1-1, Table 6.3.3.1-2, Table 6.3.3.2-2 and Table 6.3.3.2-3, TS 38.211 [16]) in case of 2-step only BWP, otherwise the UE applies the same SCS as Msg1 derived from *RACH-ConfigCommon*. The value also applies to contention free 2-step random access type (*RACH-ConfigDedicated*).

***msgA-TotalNumberOfRA-Preambles***

Indicates the total number of preambles used for contention-based and contention-free 2-step random access type when ROs for 2-step are not shared with 4-step. If the field is absent, and 2-step and 4-step does not have shared ROs, all 64 preambles are available for 2-step random access type.

***msgA-TransMax***

Max number of MsgA preamble transmissions performed before switching to 4-step random access (see TS 38.321 [3], clauses 5.1.1). This field is only applicable when 2-step and 4-step RA type are configured and switching to 4-step type RA is supported. If the field is absent, switching from 2-step RA type to 4-step RA type is not allowed.

***ra-ContentionResolutionTimer***

The initial value for the contention resolution timer for fallback RAR in case no 4-step random access type is configured (see TS 38.321 [3], clause 5.1.5). Value *sf8* corresponds to 8 subframes, value *sf16* corresponds to 16 subframes, and so on. If both 2-step and 4-step random access type resources are configured on the BWP, then this field is absent. If the field is absent in *RACH-ConfigCommonTwoStepRA* in *AdditionalRACH-Config*, the UE shall apply the corresponding value in *RACH-ConfigCommon* in the same *AdditionalRACH-Config.*

***ra-Prioritization***

Parameters which apply for prioritized random access procedure on any UL BWP of SpCell for specific Access Identities (see TS 38.321 [3], clause 5.1.1a).

***ra-PrioritizationForAI***

Indicates whether the field *ra-Prioritization-r16* applies for Access Identities. The first/leftmost bit corresponds to Access Identity 1, the next bit corresponds to Access Identity 2. Value *1* for an Access Identity indicates that the field *ra-Prioritization-r16* applies, otherwise the field does not apply.

***ra-PrioritizationForSlicingTwoStep***

Parameters which apply to configure prioritized CBRA 2-step random access type for slicing.

***rach-ConfigGenericTwoStepRA***

2-step random access type parameters for both regular random access and beam failure recovery.

 

*GroupB-ConfiguredTwoStepRA *field descriptions

***messagePowerOffsetGroupB***

Threshold for preamble selection. Value is in dB. Value *minusinfinity* corresponds to –infinity. Value *dB0* corresponds to 0 dB, *dB5* corresponds to 5 dB and so on. (see TS 38.321 [3], clause 5.1.1).

***number******O******fRA-PreamblesGroupA***

The number of CB preambles per SSB in group A for idle/inactive or connected mode. The setting of the number of preambles for each group should be consistent with *msgA-SSB-PerRACH-OccasionAndCB-PreamblesPerSSB* or *msgA-CB-PreamblesPerSSB**-PerSharedRO* if configured.

***ra-MsgA-SizeGroupA***

Transport block size threshold in bits below which the UE shall use a contention-based RA preamble of group A. (see TS 38.321 [3], clause 5.1.1).

 

Conditional Presence

Explanation

*2Step4Step*

The field is mandatory present if both 2-step random access type and 4-step random access type are configured in the BWP, otherwise the field is not present.

The field is mandatory present in *msgA-ConfigCommon* field in *AdditionalRACH-Config *if both 2-step random access type and 4-step random access type are configured for the same feature combination in the BWP.

*2StepOnlyL139*

The field is mandatory present if *msgA-**PRACH**-RootSequenceIndex* L=139 and no 4-step random access type is configured, or if L=571 for FR2-2 and no 4-step random access type is configured, otherwise the field is absent, Need S.

*2StepOnly*

The field is mandatory present in *msgA-ConfigCommon* field in B*WP-UplinkCommon* if *rach-ConfigCommon* field is absent in this *BWP-UplinkCommon*, otherwise the field is optionally present in *msgA-ConfigCommon* field in *BWP-UplinkCommon*, Need S.

The field is mandatory present in *msgA-ConfigCommon* field in *AdditionalRACH-Config* if *rach-ConfigCommon* field is absent in this *AdditionalRACH-Config*, otherwise the field is optionally present in *msgA-ConfigCommon* field in *AdditionalRACH-Config*, Need S.

*AdditionalRACH*

The field is mandatory present if the *msgA-ConfigCommon* is included in an *AdditionalRACH-Config*. When included in *initialUplinkBWP-RedCap* to indicate other feature(s) than *redcap, *this field is mandatory present with at least two *FeatureCombinationPreambles *list entries: one list entry indicating only *redcap* and the other(s) indicating both *redcap* and one or multiple="multiple" other feature(s) (e.g. *smallData, nsag* or *msg3-Repetitions*).

Otherwise, it is optional, Need R.

*InitialBWP-Only*

This field is optionally present, Need R, if this BWP is the initial BWP of SpCell. Otherwise, the field is absent.

*SharedRO*

The field is mandatory present if the 2-step random access type occasions are shared with 4-step random access type, otherwise the field is not present.
