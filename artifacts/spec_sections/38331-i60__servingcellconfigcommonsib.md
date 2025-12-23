#### –     *ServingCellConfigCommonSIB* [#](#servingcellconfigcommonsib)

The IE *ServingCellConfigCommonSIB *is used to configure cell specific parameters of a UE's serving cell in SIB1.

*ServingCellConfigCommonSIB *information element

ASN.1📋

```
`-- TAG-SERVINGCELLCONFIGCOMMONSIB-START
 ServingCellConfigCommonSIB ::=      SEQUENCE {    downlinkConfigCommon                DownlinkConfigCommonSIB,
uplinkConfigCommon                  UplinkConfigCommonSIB                                       OPTIONAL,
-- Need R    supplementaryUplink                 UplinkConfigCommonSIB                                       OPTIONAL,
-- Need R    n-TimingAdvanceOffset               ENUMERATED { n0, n25600, n39936 }                           OPTIONAL,
-- Need S    ssb-PositionsInBurst                SEQUENCE {        inOneGroup                          BIT STRING (SIZE (8)),        groupPresence                       BIT STRING (SIZE (8))                                   OPTIONAL  -- Cond FR2-Only    },
ssb-PeriodicityServingCell          ENUMERATED {ms5, ms10, ms20, ms40, ms80, ms160},
tdd-UL-DL-ConfigurationCommon       TDD-UL-DL-ConfigCommon                                      OPTIONAL,
-- Cond TDD    ss-PBCH-BlockPower                  INTEGER (-60..50),
...,
[[    channelAccessMode-r16               CHOICE {        dynamic                             NULL,        semiStatic                          SemiStaticChannelAccessConfig-r16    }                                                                                               OPTIONAL,
-- Cond SharedSpectrum    discoveryBurstWindowLength-r16      ENUMERATED {ms0dot5, ms1, ms2, ms3, ms4, ms5}               OPTIONAL,
-- Need R    highSpeedConfig-r16                 HighSpeedConfig-r16                                         OPTIONAL  -- Need R    ]],
[[    channelAccessMode2-r17              ENUMERATED {enabled}                                        OPTIONAL,
-- Cond SharedSpectrum2    discoveryBurstWindowLength-v1700    ENUMERATED {ms0dot125, ms0dot25, ms0dot5, ms0dot75, ms1, ms1dot25} OPTIONAL,
-- Need R    highSpeedConfigFR2-r17              HighSpeedConfigFR2-r17                                      OPTIONAL,
-- Need R    uplinkConfigCommon-v1700            UplinkConfigCommonSIB-v1700                                 OPTIONAL  -- Need R    ]],
[[    enhancedMeasurementNGSO-r17         ENUMERATED {true}                                           OPTIONAL  -- Need R    ]],
[[    ra-ChannelAccess-r17                ENUMERATED {enabled}                                        OPTIONAL  -- Cond SharedSpectrum2    ]],    [[    downlinkConfigCommon-v1760          DownlinkConfigCommonSIB-v1760                               OPTIONAL, -- Need R    uplinkConfigCommon-v1760            UplinkConfigCommonSIB-v1760                                 OPTIONAL  -- Need R    ]]} -- TAG-SERVINGCELLCONFIGCOMMONSIB-STOP`
```

 

*ServingCellConfigCommonSIB *field descriptions

***channelAccessMode***

If present, this field indicates which channel access procedures to apply for operation with shared spectrum channel access as defined in TS 37.213 [48]. If the field is configured as "semiStatic", the UE shall apply the channel access procedures for semi-static channel occupancy as described in clause 4.3 in TS 37.213. If the field is configured as "dynamic", the UE shall apply the channel access procedures as defined in TS 37.213, clause 4.1 and 4.2.

***channelAccessMode2***

If present, this field indicates that the UE shall apply channel access procedures for operation with shared spectrum channel access in accordance with TS 37.213 [48], clause 4.4 for FR2-2. If absent, the UE shall not apply any channel access procedure. The network always configures this field if channel access procedures are required for the serving cell within this region by regulations.

***discoveryBurstWindowLength***

Indicates the window length of the discovery burst in ms (see TS 37.213 [48]). The field *discoveryBurstWindowLength-v1700* is applicable to SCS 480 kHz and SCS 960 kHz.

***enhancedMeasurement******NGSO***

If the field is present and UE supports the enhanced cell reselection requirements for NTN NGSO in RRC_IDLE/RRC_INACTIVE, the UE shall apply the enhanced cell reselection requirements for NTN NGSO as specified in TS 38.133 [14], clauses 4.2C.2.3 and 4.2C.2.4.

***groupPresence***

This field is present when maximum number of SS/PBCH blocks per half frame equals to 64 as defined in TS 38.213 [13], clause 4.1. The first/leftmost bit corresponds to the SS/PBCH index 0-7, the second bit corresponds to SS/PBCH block 8-15, and so on. Value 0 in the bitmap indicates that the SSBs according to *inOneGroup* are absent. Value 1 indicates that the SS/PBCH blocks are transmitted in accordance with *inOneGroup*.

***inOneGroup***

When maximum number of SS/PBCH blocks per half frame equals to 4 as defined in TS 38.213 [13], clause 4.1, only the 4 leftmost bits are valid; the UE ignores the 4 rightmost bits. When maximum number of SS/PBCH blocks per half frame equals to 8 as defined in TS 38.213 [13], clause 4.1, all 8 bits are valid. The first/ leftmost bit corresponds to SS/PBCH block index 0, the second bit corresponds to SS/PBCH block index 1, and so on. When maximum number of SS/PBCH blocks per half frame equals to 64 as defined in TS 38.213 [13], clause 4.1, all 8 bit are valid; The first/ leftmost bit corresponds to the first SS/PBCH block index in the group (i.e., to SSB index 0, 8, and so on); the second bit corresponds to the second SS/PBCH block index in the group (i.e., to SSB index 1, 9, and so on), and so on. Value 0 in the bitmap indicates that the corresponding SS/PBCH block is not transmitted while value 1 indicates that the corresponding SS/PBCH block is transmitted.

***n-TimingAdvanceOffset***

The N_TA-Offset to be applied for random access on this serving cell. If the field is absent, the UE applies the value defined for the duplex mode and frequency range of this serving cell. See TS 38.133 [14], table 7.1.2-2/table 7.1C.2-4.

***ra-ChannelAccess***

If present, this field indicates that the UE shall apply channel access procedures before msg1/msgA transmission for operation with shared spectrum channel access in accordance with TS 37.213 [48], clause 4.4.5 for FR2-2.

***ssb-PositionsInBurst***

Time domain positions of the transmitted SS-blocks in an SS-burst as defined in TS 38.213 [13], clause 4.1.

For operation with shared spectrum channel access in FR1, only *inOneGroup* is used and the UE interprets this field same as *mediumBitmap* in *ServingCellConfigCommon*. The UE assumes that a bit in *inOneGroup* at position k > \(N_{SSB}^{QCL}\) is 0, where \(N_{SSB}^{QCL}\) is obtained from *MIB* as specified in TS 38.213 [13], clause 4.1. For operation with shared spectrum channel access in FR2-2, the m-th bit in *groupPresence* is set to 0 for m > \(N_{SSB}^{QCL}\)/8, where \(N_{SSB}^{QCL}\) is obtained from *MIB* as specified in TS 38.213 [13], clause 4.1.

***ss-PBCH-BlockPower***

Average EPRE of the resources elements that carry secondary synchronization signals in dBm that the NW used for SSB transmission, see TS 38.213 [13], clause 7.

 

Conditional Presence

Explanation

*FR2-Only*

This field is mandatory present for an FR2 carrier frequency. It is absent otherwise and UE releases any configured value.

*SharedSpectrum*

This field is mandatory present if this cell operates with shared spectrum channel access in FR1. Otherwise, it is absent, Need R.

*SharedSpectrum2*

This field is optionally present if this cell operates with shared spectrum channel access in FR2-2, Need R. Otherwise, it is absent, Need R.

*TDD*

The field is optionally present, Need R, for TDD cells; otherwise it is absent.
