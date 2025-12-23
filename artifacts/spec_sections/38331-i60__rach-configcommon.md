#### –     *RACH-ConfigCommon* [#](#rach-configcommon)

The IE *RACH-ConfigCommon* is used to specify the cell specific random-access parameters.

*RACH-ConfigCommon* information element

ASN.1📋

```
`-- TAG-RACH-CONFIGCOMMON-START
 RACH-ConfigCommon ::=               SEQUENCE {    rach-ConfigGeneric                  RACH-ConfigGeneric,
totalNumberOfRA-Preambles           INTEGER (1..63)                                                     OPTIONAL,
-- Need S    ssb-perRACH-OccasionAndCB-PreamblesPerSSB   CHOICE {        oneEighth                                   ENUMERATED {n4,n8,n12,n16,n20,n24,n28,n32,n36,n40,n44,n48,n52,n56,n60,n64},
oneFourth                                   ENUMERATED {n4,n8,n12,n16,n20,n24,n28,n32,n36,n40,n44,n48,n52,n56,n60,n64},
oneHalf                                     ENUMERATED {n4,n8,n12,n16,n20,n24,n28,n32,n36,n40,n44,n48,n52,n56,n60,n64},
one                                         ENUMERATED {n4,n8,n12,n16,n20,n24,n28,n32,n36,n40,n44,n48,n52,n56,n60,n64},
two                                         ENUMERATED {n4,n8,n12,n16,n20,n24,n28,n32},        four                                        INTEGER (1..16),        eight                                       INTEGER (1..8),        sixteen                                     INTEGER (1..4)    }                                                                                                       OPTIONAL,
-- Need M     groupBconfigured                    SEQUENCE {        ra-Msg3SizeGroupA                   ENUMERATED {b56, b144, b208, b256, b282, b480, b640,                                                        b800, b1000, b72, spare6, spare5,spare4, spare3, spare2, spare1},
messagePowerOffsetGroupB            ENUMERATED { minusinfinity, dB0, dB5, dB8, dB10, dB12, dB15, dB18},        numberOfRA-PreamblesGroupA          INTEGER (1..64)    }                                                                                                       OPTIONAL,
-- Need R    ra-ContentionResolutionTimer            ENUMERATED { sf8, sf16, sf24, sf32, sf40, sf48, sf56, sf64},
rsrp-ThresholdSSB                       RSRP-Range                                                      OPTIONAL,
-- Need R    rsrp-ThresholdSSB-SUL                   RSRP-Range                                                      OPTIONAL,
-- Cond SUL    prach-RootSequenceIndex                 CHOICE {        l839                                    INTEGER (0..837),        l139                                    INTEGER (0..137)    },
msg1-SubcarrierSpacing                  SubcarrierSpacing                                               OPTIONAL,
-- Cond L139    restrictedSetConfig                     ENUMERATED {unrestrictedSet, restrictedSetTypeA, restrictedSetTypeB},
msg3-transformPrecoder                  ENUMERATED {enabled}                                            OPTIONAL,
-- Need R    ...,
[[    ra-PrioritizationForAccessIdentity-r16  SEQUENCE {        ra-Prioritization-r16                   RA-Prioritization,        ra-PrioritizationForAI-r16              BIT STRING (SIZE (2))    }                                                                                                       OPTIONAL,
-- Cond InitialBWP-Only    prach-RootSequenceIndex-r16             CHOICE {        l571                                    INTEGER (0..569),        l1151                                   INTEGER (0..1149)    }   OPTIONAL   -- Need R    ]],    [[    ra-PrioritizationForSlicing-r17         RA-PrioritizationForSlicing-r17                          OPTIONAL,   -- Cond InitialBWP-Only    featureCombinationPreamblesList-r17     SEQUENCE (SIZE(1..maxFeatureCombPreamblesPerRACHResource-r17)) OF FeatureCombinationPreambles-r17 OPTIONAL -- Cond AdditionalRACH    ]]} -- TAG-RACH-CONFIGCOMMON-STOP`
```

 

*RACH-ConfigCommon *field descriptions

***featureCombinationPreambles******List***

Specifies a series of preamble partitions each associated to a combination of features and 4-step RA. The network does not configure this list to have more than 16 entries.

***messagePowerOffsetGroupB***

Threshold for preamble selection. Value is in dB. Value *minusinfinity* corresponds to –infinity. Value *dB0* corresponds to 0 dB, *dB5* corresponds to 5 dB and so on (see TS 38.321 [3], clause 5.1.2). This field is set to the same value for different repetition numbers associated with a specific *FeatureCombination*.

***msg1-SubcarrierSpacing***

Subcarrier spacing of PRACH (see TS 38.211 [16], clause 5.3.2).

Only the following values are applicable depending on the used frequency:

FR1:    15 or 30 kHz

FR2-1/FR2-NTN:  60 or 120 kHz

FR2-2:  120, 480, or 960 kHz

If absent, the UE applies the SCS as derived from the *prach-ConfigurationIndex* in *RACH-ConfigGeneric* (see tables Table 6.3.3.1-1, Table 6.3.3.1-2, Table 6.3.3.2-2 and Table 6.3.3.2-3, TS 38.211 [16]). The value also applies to contention free random access (*RACH-ConfigDedicated*), to SI-request and to contention-based beam failure recovery (CB-BFR). But it does not apply for contention free beam failure recovery (CF-BFR) (see *BeamFailureRecoveryConfig*).

***msg3-transformPrecoder***

Enables the transform precoder for Msg3 transmission according to clause 6.1.3 of TS 38.214 [19]. If the field is absent, the UE disables the transformer precoder (see TS 38.213 [13], clause 8.3).

***numberOfRA-PreamblesGroupA***

The number of CB preambles per SSB in group A. This determines implicitly the number of CB preambles per SSB available in group B. (see TS 38.321 [3], clause 5.1.1). The setting should be consistent with the setting of *ssb-perRACH-OccasionAndCB-PreamblesPerSSB*.

***prach-RootSequenceIndex***

PRACH root sequence index (see TS 38.211 [16], clause 6.3.3.1). The value range depends on whether L=839 or L=139 or L=571 or L=1151. The length of the root sequence corresponding with the index indicated in this IE should be consistent with the one indicated in *prach-ConfigurationIndex* in the *RACH-ConfigDedicated* (if configured). If *prach-RootSequenceIndex-r16* is signalled, UE shall ignore the *prach-RootSequenceIndex *(without suffix).

For FR2-2, only the following values are applicable depending on the used subcarrier spacing:

120 kHz:  L=139, L=571, and L=1151

480 kHz:  L=139, and L=571

960 kHz:  L=139

***ra-ContentionResolutionTimer***

The initial value for the contention resolution timer (see TS 38.321 [3], clause 5.1.5). Value *sf8* corresponds to 8 subframes, value *sf16* corresponds to 16 subframes, and so on.

***ra-Msg3SizeGroupA***

Transport Blocks size threshold in bits below which the UE shall use a contention-based RA preamble of group A (see TS 38.321 [3], clause 5.1.2). This field is set to the same value for different repetition numbers associated with a specific *FeatureCombination*.

***ra-Prioritization***

Parameters which apply for prioritized random access procedure on any UL BWP of SpCell for specific Access Identities (see TS 38.321 [3], clause 5.1.1a).

***ra-PrioritizationForAI***

Indicates whether the field *ra-Prioritization-r16 *applies for Access Identities. The first/leftmost bit corresponds to Access Identity 1, the next bit corresponds to Access Identity 2. Value 1 indicates that the field *ra-Prioritization-r16* applies otherwise the field does not apply (see TS 23.501 [32]).

***ra-PrioritizationForSlicing***

Parameters which apply to configure prioritized CBRA 4-step random access type for slicing.

***rach-ConfigGeneric***

RACH parameters for both regular random access and beam failure recovery.

***restrictedSetConfig***

Configuration of an unrestricted set or one of two types of restricted sets, see TS 38.211 [16], clause 6.3.3.1.

***rsrp-ThresholdSSB***

UE may select the SS block and corresponding PRACH resource for path-loss estimation and (re)transmission based on SS blocks that satisfy the threshold (see TS 38.213 [13]).

***rsrp-ThresholdSSB-SUL***

The UE selects SUL carrier to perform random access based on this threshold (see TS 38.321 [3], clause 5.1.1). The value applies to all the BWPs and all RACH configurations.

***ssb-perRACH-OccasionAndCB-PreamblesPerSSB***

The meaning of this field is twofold: the CHOICE conveys the information about the number of SSBs per RACH occasion. Value *oneEighth* corresponds to one SSB associated with 8 RACH occasions, value *oneFourth* corresponds to one SSB associated with 4 RACH occasions, and so on. The ENUMERATED part indicates the number of Contention Based preambles per SSB. Value *n4* corresponds to 4 Contention Based preambles per SSB, value *n8* corresponds to 8 Contention Based preambles per SSB, and so on. The total number of CB preambles in a RACH occasion is given by *CB-preambles-per-SSB* * max(1, *SSB-per-rach-occasion*). See TS 38.213 [13].

***totalNumberOfRA-Preambles***

Total number of preambles used for contention based and contention free 4-step or 2-step random access in the RACH resources defined in *RACH-ConfigCommon*, excluding preambles used for other purposes (e.g. for SI request). If the field is absent, all 64 preambles are available for RA. The setting should be consistent with the setting of *ssb-perRACH-OccasionAndCB-PreamblesPerSSB*, i.e. it should be a multiple="multiple" of the number of SSBs per RACH occasion.

 

Conditional Presence

Explanation

*AdditionalRACH*

The field is mandatory present if the *RACH-ConfigCommon* is included in an *AdditionalRACH-Config*. When included in *initialUplinkBWP-RedCap* to indicate other feature(s) than *redcap** and eRedCap**, *this field is mandatory present with at least *FeatureCombinationPreambles *list entries: the list entry/entries indicating only *redcap** *or* eRedCap* and the other(s) indicating both *redcap** *or *eRedCap* and one or multiple="multiple" other feature(s) (e.g., *smallData, nsag* or *msg3-Repetitions*). When included in *initialUplinkBWP-RedCap* to indicate eRedCap and RedCap separately, this field is mandatory present with at least two *FeatureCombinationPreambles* list entries: one list entry indicating only *redcap* and the other list entry indicating only *eRedCap*.

Otherwise, it is optional, Need R.

*InitialBWP-Only*

This field is optionally present, Need R, if this BWP is the initial BWP of SpCell. Otherwise, the field is absent.

*L139*

The field is mandatory present if *prach-RootSequenceIndex* L=139, or if L=571 for FR2-2, otherwise the field is absent, Need S.

*SUL*

The field is mandatory present in *rach-ConfigCommon* in *initialUplinkBWP* if *supplementaryUplink* is configured in *ServingCellConfigCommonSIB* or if *supplementaryUplinkConfig* is configured in *ServingCellConfigCommon*; otherwise, the field is absent. This field is not configured in *additionalRACH-Config*.
