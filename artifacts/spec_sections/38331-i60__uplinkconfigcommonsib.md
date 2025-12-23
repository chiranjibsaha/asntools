#### –     *UplinkConfigCommonSIB* [#](#uplinkconfigcommonsib)

The IE *UplinkConfigCommonSIB *provides common uplink parameters of a cell.

*UplinkConfigCommonSIB *information element

ASN.1📋

```
`-- TAG-UPLINKCONFIGCOMMONSIB-START
 UplinkConfigCommonSIB ::=               SEQUENCE {    frequencyInfoUL                         FrequencyInfoUL-SIB,    initialUplinkBWP                        BWP-UplinkCommon,    timeAlignmentTimerCommon                TimeAlignmentTimer} UplinkConfigCommonSIB-v1700 ::=         SEQUENCE {    initialUplinkBWP-RedCap-r17             BWP-UplinkCommon                                OPTIONAL   -- Need R} UplinkConfigCommonSIB-v1760 ::=         SEQUENCE {    frequencyInfoUL-v1760                   FrequencyInfoUL-SIB-v1760} -- TAG-UPLINKCONFIGCOMMONSIB-STOP`
```

 

*UplinkConfigCommonSIB* field descriptions

***frequencyInfoUL***

Absolute uplink frequency configuration and subcarrier specific virtual carriers.

***InitialUplinkBWP***

The initial uplink BWP configuration for a PCell (see TS 38.213 [13], clause 12).

***initialUplinkBWP-RedCap***

If present, (e)RedCap UEs use this UL BWP instead of *initialUplinkBWP*.

If absent, (e)RedCap UEs use *initialUplinkBWP* provided that it does not exceed the (e)RedCap UE maximum bandwidth (see also clause 5.2.2.4.2).
