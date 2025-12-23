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
