# TS 38.331 (RRC) marked excerpts for “Type-2 RAR triggered Msg1 PRACH switch” (draft)

This file reproduces selected excerpts from the extracted TS 38.331 sections under `artifacts/spec_sections/38331-i60__*.md` and annotates proposed additions using `[[ADD]]` / `[[MOD]]` markers.

## 1) Where `RACH-ConfigCommon` is carried (SIB1 path)

From `artifacts/spec_sections/38331-i60__bwp-uplinkcommon.md`:

```
BWP-UplinkCommon ::= SEQUENCE {
    genericParameters                   BWP,
    rach-ConfigCommon                   SetupRelease { RACH-ConfigCommon } OPTIONAL,
    ...
}
```

[[ADD]] If `rach-ConfigCommon` is configured and includes `type2Rar-PrachSwitchConfig-rXX`, the UE may use it to derive a secondary PRACH configuration for transmission of an additional Random Access Preamble (Msg1-2) as triggered by MAC (TS 38.321 changes).

## 2) `RACH-ConfigCommon` (add a secondary PRACH config container)

From `artifacts/spec_sections/38331-i60__rach-configcommon.md`:

```
RACH-ConfigCommon ::= SEQUENCE {
    rach-ConfigGeneric                  RACH-ConfigGeneric,
    totalNumberOfRA-Preambles           INTEGER (1..63) OPTIONAL,
    ssb-perRACH-OccasionAndCB-PreamblesPerSSB   CHOICE { ... } OPTIONAL,
    groupBconfigured                    SEQUENCE { ... } OPTIONAL,
    ra-ContentionResolutionTimer        ENUMERATED { sf8, sf16, ... },
    rsrp-ThresholdSSB                   RSRP-Range OPTIONAL,
    rsrp-ThresholdSSB-SUL               RSRP-Range OPTIONAL,
    prach-RootSequenceIndex             CHOICE { l839 INTEGER (0..837), l139 INTEGER (0..137) },
    msg1-SubcarrierSpacing              SubcarrierSpacing OPTIONAL,
    restrictedSetConfig                 ENUMERATED {unrestrictedSet, restrictedSetTypeA, restrictedSetTypeB},
    msg3-transformPrecoder              ENUMERATED {enabled} OPTIONAL,
    ...,
    [[ ... r16 ... ]],
    [[ ... r17 ... ]]
}
```

[[ADD]] Add an optional extension field in `RACH-ConfigCommon`:

```
[[    type2Rar-PrachSwitchConfig-rXX   Type2Rar-PrachSwitchConfig-rXX OPTIONAL  -- Need R  ]]
```

### New field description (to be added under `RACH-ConfigCommon` field descriptions)

[[ADD]] ***type2Rar-PrachSwitchConfig***

[[ADD]] If present, this field provides a secondary PRACH configuration that the UE uses for transmission of an additional Random Access Preamble (Msg1-2) when the UE is instructed by MAC upon reception of a Type-2 Random Access Response (TS 38.321).

[[ADD]] If absent, the UE does not perform a PRACH configuration switch for Msg1-2 based on Type-2 Random Access Response.

## 3) New IE definition (secondary PRACH config for Msg1-2)

[[ADD]] Add a new IE definition (placeholder naming; exact release suffix TBD):

```
Type2Rar-PrachSwitchConfig-rXX ::= SEQUENCE {
    rach-ConfigGeneric-Msg1-2-rXX                    RACH-ConfigGeneric,
    totalNumberOfRA-Preambles-Msg1-2-rXX             INTEGER (1..63) OPTIONAL,
    ssb-perRACH-OccasionAndCB-PreamblesPerSSB-Msg1-2-rXX CHOICE { ... } OPTIONAL,
    rsrp-ThresholdSSB-Msg1-2-rXX                     RSRP-Range OPTIONAL,
    prach-RootSequenceIndex-Msg1-2-rXX               CHOICE { l839 INTEGER (0..837), l139 INTEGER (0..137), ... },
    msg1-SubcarrierSpacing-Msg1-2-rXX                SubcarrierSpacing OPTIONAL,
    restrictedSetConfig-Msg1-2-rXX                   ENUMERATED {unrestrictedSet, restrictedSetTypeA, restrictedSetTypeB}
}
```

[[ADD]] Semantics:

- [[ADD]] `rach-ConfigGeneric-Msg1-2-rXX` provides the PRACH occasion resources (e.g. via `prach-ConfigurationIndex`, `msg1-FDM`, `msg1-FrequencyStart`) and the Msg2 (RAR) monitoring window (`ra-ResponseWindow`) for the Msg1-2 transmission.
- [[ADD]] `prach-RootSequenceIndex-Msg1-2-rXX`, `restrictedSetConfig-Msg1-2-rXX`, and `msg1-SubcarrierSpacing-Msg1-2-rXX` (when applicable) provide the PRACH preamble generation context for Msg1-2.
- [[ADD]] Msg1-2 is contention-free in the sense that the UE reuses the `RAPID`/preamble index confirmed by the Type-2 MAC RAR for Msg1-1; the UE does not perform contention-based preamble selection for Msg1-2. The PRACH sequence transmitted for the same preamble index differs because the PRACH configuration differs.
- [[ADD]] Whether the UE uses the same SSB for Msg1-2 as used for Msg1-1, or re-selects an SSB, is specified in the corresponding MAC procedure text (TS 38.321 changes). RRC only provides the configuration.

[[ADD]] Note: No “must support” requirements are introduced; if the network does not configure `type2Rar-PrachSwitchConfig-rXX`, the feature is not applicable.
