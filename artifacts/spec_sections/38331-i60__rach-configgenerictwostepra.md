#### –     *RACH-ConfigGenericTwoStepRA* [#](#rach-configgenerictwostepra)

The IE *RACH-ConfigGenericTwoStepRA* is used to specify the 2-step random access type parameters.

*RACH-ConfigGenericTwoStepRA* information element

ASN.1📋

```
`-- TAG-RACH-CONFIGGENERICTWOSTEPRA-START
 RACH-ConfigGenericTwoStepRA-r16 ::=     SEQUENCE {    msgA-PRACH-ConfigurationIndex-r16       INTEGER (0..262)                                                OPTIONAL,
-- Cond 2StepOnly    msgA-RO-FDM-r16                         ENUMERATED {one, two, four, eight}                              OPTIONAL,
-- Cond 2StepOnly    msgA-RO-FrequencyStart-r16              INTEGER (0..maxNrofPhysicalResourceBlocks-1)                    OPTIONAL,
-- Cond 2StepOnly    msgA-ZeroCorrelationZoneConfig-r16      INTEGER (0..15)                                                 OPTIONAL,
-- Cond 2StepOnly    msgA-PreamblePowerRampingStep-r16       ENUMERATED {dB0, dB2, dB4, dB6}                                 OPTIONAL,
-- Cond 2StepOnlyNoCFRA    msgA-PreambleReceivedTargetPower-r16    INTEGER (-202..-60)                                             OPTIONAL,
-- Cond 2StepOnlyNoCFRA    msgB-ResponseWindow-r16                 ENUMERATED {sl1, sl2, sl4, sl8, sl10, sl20, sl40, sl80, sl160, sl320}                                                                                                            OPTIONAL,
-- Cond NoCFRA    preambleTransMax-r16                    ENUMERATED {n3, n4, n5, n6, n7, n8, n10, n20, n50, n100, n200}  OPTIONAL,
-- Cond 2StepOnlyNoCFRA    ...,
[[    msgB-ResponseWindow-v1700               ENUMERATED {sl240, sl640, sl960, sl1280, sl1920, sl2560}        OPTIONAL  -- Cond NoCFRA2    ]]} -- TAG-RACH-CONFIGGENERICTWOSTEPRA-STOP`
```

 

*RACH-ConfigGenericTwoStepRA *field descriptions

***msgA-PreamblePowerRampingStep***

Power ramping steps for msgA PRACH. If the field is absent in *RACH-ConfigCommonTwoStepRA* in *AdditionalRACH-Config*, the UE shall apply the corresponding value in *RACH-ConfigCommon* in the same *AdditionalRACH-Config*. If the field is absent in other cases, UE shall use the value of *powerRampingStep* in *RACH-ConfigGeneric* in the configured BWP (see TS 38.321 [3], 5.1.3). This field may only be present if no 4-step type RA is configured in the BWP or in the case of separate ROs with 4-step type RA. The field is absent if *RACH-ConfigGenericTwoStepRA* is included in *CFRA-TwoStep* in *RACH-ConfigDedicated *and then* *the UE uses the value of *msgA-PreamblePowerRampingStep* in *RACH-ConfigGenericTwoStepRA *configured for* *CBRA.

***msgA-PreambleReceivedTargetPower***

The target power level at the network receiver side (see TS 38.213 [13], clause 7.1.1 and TS 38.321 [3], clause 5.1.1). Only multiples of 2 dBm may be chosen (e.g -202, -200, -198, …). If the field is absent, UE shall use the value of *preambleReceivedTargetPower* in *RACH-ConfigGeneric* in the configured BWP. This field may only be present if no 4-step type RA is configured in the BWP. The field is absent if *RACH-ConfigGenericTwoStepRA* is included in *CFRA-TwoStep* in *RACH-ConfigDedicated *and then* *the UE uses the value of *msgA-PreambleReceivedTargetPower**** ***in *RACH-ConfigGenericTwoStepRA *configured for* *CBRA*.*

***msgA-PRACH-ConfigurationIndex***

Cell-specific PRACH configuration index for 2-step RA type. If the field is absent in *RACH-ConfigCommonTwoStepRA *which is configured directly within a BWP (i.e. not within *AdditionalRACH-Config*), the UE shall use the value of corresponding 4-step random access parameter in the configured BWP. If the field is absent in *RACH-ConfigCommonTwoStepRA* in *AdditionalRACH-Config*, the UE shall apply the corresponding value in *RACH-ConfigCommon* in the same *AdditionalRACH-Config*. If the value is in the range of 256 to 262, the field *prach-ConfigurationIndex-v1610 *should be considered configured (see TS 38.211 [16], clause 6.3.3.2). This field may only be present if no 4-step type RA is configured in the BWP or in the case of separate ROs with 4-step type RA.

***msgA-RO-FDM***

The number of msgA PRACH transmission occasions Frequency-Division Multiplexed in one time instance. If the field is absent in *RACH-ConfigCommonTwoStepRA *which is configured directly within a BWP (i.e. not within *AdditionalRACH-Config*), UE shall use value of *msg1-FDM* in *RACH-ConfigGeneric* in the configured BWP. If the field is absent in *RACH-ConfigCommonTwoStepRA* in *AdditionalRACH-Config*, the UE shall apply the value of *msg1-FDM* in *RACH-ConfigCommon* in the same *AdditionalRACH-Config* (see TS 38.211 [16], clause 6.3.3.2). This field may only be present if no 4-step type RA is configured in the BWP or in the case of separate ROs with 4-step type RA.

***msgA-RO-FrequencyStart***

Offset of lowest PRACH transmissions occasion in frequency domain with respect to PRB 0. If the field is absent in* RACH-ConfigCommonTwoStepRA *which is configured directly within a BWP (i.e. not within *AdditionalRACH-Config*), UE shall use value of *msg1-FrequencyStart* in *RACH-ConfigGeneric* in the configured BWP. If the field is absent in *RACH-ConfigCommonTwoStepRA* in *AdditionalRACH-Config*, the UE shall apply the value of *msg1-FrequencyStart* in *RACH-ConfigCommon* in the same *AdditionalRACH-Config* (see TS 38.211 [16], clauses 5.3.2 and 6.3.3.2). This field may only be present if no 4-step type RA is configured in the BWP or in the case of separate ROs with 4-step type RA.

***msgA-ZeroCorrelationZoneConfig***

N-CS configuration for msgA preamble, see Table 6.3.3.1-5 in TS 38.211 [16]. If the field is absent in *RACH-ConfigCommonTwoStepRA* in *AdditionalRACH-Config*, the UE shall apply the corresponding value in *RACH-ConfigCommon* in the same *AdditionalRACH-Config*. If the field is absent in other cases, UE shall use value *zeroCorrelationZoneConfig* in *RACH-ConfigGeneric* in the configured BWP. This field may only be present if no 4-step type RA is configured in the BWP or in the case of separate ROs with 4-step type RA.

***msgB-ResponseWindow***

MsgB monitoring window length in number of slots. The network configures a value lower than or equal to 40ms (see TS 38.321 [3], clause 5.1.1). The network does not configure *msgB-ResponseWindow-r16 *simultaneously with *msgB-ResponseWindow-v17**00*, and if both fields are absent,* *the UE uses the value of *msgB-ResponseWindow* in *RACH-ConfigGenericTwoStepRA *configured for CBRA.

***preambleTransMax***

Max number of RA preamble transmission performed before declaring a failure (see TS 38.321 [3], clauses 5.1.4, 5.1.5). If the field is absent in *RACH-ConfigCommonTwoStepRA* in *AdditionalRACH-Config*, the UE shall apply the corresponding value in *RACH-ConfigCommon* in the same *AdditionalRACH-Config*. If the field is absent in other cases, UE shall use the value of *preambleTransMax* in *RACH-ConfigGeneric* in the configured BWP. The field is absent if *RACH-ConfigGenericTwoStepRA* is included in *CFRA-TwoStep* in *RACH-ConfigDedicated *and then* *the UE uses the value of *preambleTransMax**** ***in *RACH-ConfigGenericTwoStepRA *configured for* *CBRA*.*

 

Conditional Presence

Explanation

*2StepOnly*

The field is mandatory present in *msgA-ConfigCommon *field* *in *BWP-UplinkCommon *if *rach-ConfigCommon *field is absent in this *BWP-UplinkCommon*, otherwise the field is optionally present in *msgA-ConfigCommon *field* *in *BWP-UplinkCommon*, Need S.

The field is mandatory present in *msgA-ConfigCommon *in *AdditionalRACH-Config *if *rach-ConfigCommon *field is absent in this *AdditionalRACH-Config,* otherwise the field is optionally present in *msgA-ConfigCommon *field* *in *AdditionalRACH-Config*, Need S.

*2StepOnlyNoCFRA*

The field is mandatory present if *RACH-ConfigGenericTwoStepRA* is included in the *RACH-ConfigCommonTwoStepRA* and there are no 4-step random access configurations configured in the BWP (i.e only 2-step random access type configured in the BWP), otherwise (i.e. 4-step random access configuration also exists in the BWP) the field is optionally present, Need S. When *RACH-ConfigGenericTwoStepRA* is included in the *RACH-ConfigDedicated*, this field is absent.

*NoCFRA*

The field is mandatory present if *msgB-ResponseWindow-r17* is absent and *RACH-ConfigGenericTwoStepRA *is not included in *CFRA-TwoStep* in *RACH-ConfigDedicated, *otherwise the field is absent, Need S.

*NoCFRA2*

The field is mandatory present if *msgB-ResponseWindow-r16* is absent and *RACH-ConfigGenericTwoStepRA* is not included in *CFRA-TwoStep* in *RACH-ConfigDedicated*, otherwise the field is absent, Need S.
