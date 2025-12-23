# TS 38.300 excerpts with proposed insertions (marked draft)

Source excerpt: `random_access_38300.txt`.

Markers:
- `[[ADD]]` new text to be inserted
- `[[MOD]]` change to baseline text
- `[[TBD]]` open item

## Random Access overview excerpt + insert

```
Two types of random access procedure are supported: 4-step RA type with MSG1 and 2-step RA type with MSGA. Both types of RA procedure support contention-based random access (CBRA) and contention-free random access (CFRA) as shown on Figure 9.2.6-1 below.

...

The MSG1 of the 4-step RA type consists of a preamble on PRACH. After MSG1 transmission, the UE monitors for a response from the network within a configured window.

[[ADD]] For the 4-step RA type, the network may support a PRACH refinement enhancement (proposal), where:
[[ADD]] - after MSG1 transmission, the UE may receive a Type-2 Random Access Response (Type-2 RAR) containing time and frequency pre-compensation information; and
[[ADD]] - upon reception of a Type-2 RAR, the UE transmits another PRACH preamble (Msg1-2) using a different PRACH preamble format/configuration (e.g. short PRACH), applying the time/frequency pre-compensation; and
[[ADD]] - the network then provides a (regular) Random Access Response to schedule MSG3 and proceed with contention resolution as in the baseline 4-step RA type.
[[ADD]] This enhancement does not change the definition of the 2-step RA type (MSGA/MSGB).

For CFRA, dedicated preamble for MSG1 transmission is assigned by the network and upon receiving random access response from the network, the UE ends the random access procedure as shown in Figure 9.2.6-1(c). For CBRA, upon reception of the random access response, the UE sends MSG3 using the UL grant scheduled in the response and monitors contention resolution as shown in Figure 9.2.6-1(a). If contention resolution is not successful after MSG3 (re)transmission(s), the UE goes back to MSG1 transmission.

The MSGA of the 2-step RA type includes a preamble on PRACH and a payload on PUSCH. ...
```

[[TBD]] Figure updates (38.300):
- extend the 4-step CBRA figure to show the optional Type-2 RAR → Msg1-2 insertion before the regular RAR/MSG3, or
- add a new figure for “4-step RA with PRACH refinement”.

