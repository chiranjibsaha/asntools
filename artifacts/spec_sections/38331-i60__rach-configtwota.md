#### –     *RACH-ConfigTwoTA* [#](#rach-configtwota)

The IE *RACH-ConfigTwoTA* is used to specify random access parameters for each additional PCI configured for the serving cell.

*RACH-ConfigTwoTA* information element

ASN.1📋

```
`-- TAG-RACH-CONFIGTWOTA-START
 RACH-ConfigTwoTA-r18 ::=     SEQUENCE {    additionalPCI-andRACH-Index-r18  AdditionalPCIIndex-r17,
rach-ConfigGeneric-r18       RACH-ConfigGeneric,
ssb-perRACH-Occasion-r18     ENUMERATED {oneEighth, oneFourth, oneHalf, one, two, four, eight, sixteen}   OPTIONAL,
-- Need M    prach-RootSequenceIndex-r18  CHOICE {        l839                         INTEGER (0..837),        l139                         INTEGER (0..137),        l571                         INTEGER (0..569),        l1151                        INTEGER (0..1149)    },
msg1-SubcarrierSpacing-r18   SubcarrierSpacing                                                            OPTIONAL,
-- Cond L139    ...,
[[    twoTA-restrictedSetConfig-r18    ENUMERATED {unrestrictedSet, restrictedSetTypeA, restrictedSetTypeB}     OPTIONAL  -- Need R    ]]} -- TAG-RACH-CONFIGTWOTA-STOP`
```

 

*RACH-ConfigTwoTA *field descriptions

***additionalPCI-andRACH-Index***

Indicates the associated PCI to this random access configuration.

***msg1-SubcarrierSpacing***

Subcarrier spacing of PRACH when prach-RootSequenceIndex has value set to l139 (see TS 38.211 [16], clause 5.3.2). Only the following values are applicable depending on the used frequency: FR1: 15 or 30 kHz FR2-1: 60 or 120 kHz FR2-2: 120, 480, or 960 kHz. If absent, the UE applies the SCS as derived from the *prach-ConfigurationIndex* in *RACH-ConfigGeneric* (see tables Table 6.3.3.1-1, Table 6.3.3.1-2, Table 6.3.3.2-2 and Table 6.3.3.2-3, TS 38.211 [16]).

***prach-RootSequenceIndex***

PRACH root sequence index (see TS 38.211 [16], clause 6.3.3.1). The value range depends on whether L=839, L=139, L=571 or L=1151.

For FR2-2, only the following values are applicable depending on the used subcarrier spacing:

120 kHz:  L=139, L=571, and L=1151

480 kHz:  L=139, and L=571

960 kHz:  L=139

***rach-ConfigGeneric***

RACH parameters for contention free random access occasions for CFRA.

***ssb-perRACH-Occasion***

Number of SSBs per RACH occasion.

***twoTA-restrictedSetConfig***

Configuration of an unrestricted set or one of two types of restricted sets associated with additional PCI, see TS 38.211 [16], clause 6.3.3.1.

 

Conditional Presence

Explanation

*L139*

The field is mandatory present if *prach-RootSequenceIndex* L=139, or if L=571 for FR2-2, otherwise the field is absent, Need S.
