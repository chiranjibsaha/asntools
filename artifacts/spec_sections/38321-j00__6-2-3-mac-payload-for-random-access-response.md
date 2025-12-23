### 6.2.3     MAC payload for Random Access Response [#](#6-2-3-mac-payload-for-random-access-response)

The MAC RAR is of fixed size as depicted in Figure 6.2.3-1, and consists of the following fields:

-    R: Reserved bit, set to 0;

-    TI: If two TAGs are configured for the Serving Cell in which the Random Access procedure is being performed, this field indicates one of the two TAGs to which the Timing Advance Command is applied. If *tag2-flag* is set to *true* by upper layers, the field set to 0 indicates the *tag2-Id* and the field set to 1 indicates the *tag-Id* of the Serving Cell, otherwise the field set to 0 indicates the *tag-Id* and the field set to 1 indicates the *tag2-Id* of the Serving Cell. If the Serving Cell in which the Random Access procedure is being performed is not configured with two TAGs, the R bit is present instead;

-    Timing Advance Command: The Timing Advance Command field indicates the index value *T**A* used to control the amount of timing adjustment that the MAC entity has to apply in TS 38.213 [6]. The size of the Timing Advance Command field is 12 bits;

-    UL Grant: The Uplink Grant field indicates the resources to be used on the uplink in TS 38.213 [6]. The size of the UL Grant field is 27 bits;

-    Temporary C-RNTI: The Temporary C-RNTI field indicates the temporary identity that is used by the MAC entity during Random Access. The size of the Temporary C-RNTI field is 16 bits.

The MAC RAR is octet aligned.

UE         gNB          UPF          AMF
|           |            |            |
|-----------|------------|----------->|
| 1. PDU Session Establishment Request |
|           |            |            |
|           |<------------------------|
|           | 2. PDU SESSION RESOURCE |
|           |    SETUP REQUEST        |
|           |            |            |
|<----------|            |            |
| 3. RRCReconfiguration  |            |
|           |            |            |
| [4. DRB(s) established]            |
|           |            |            |
|---------->|            |            |
| 5. RRCReconfigurationComplete       |
|           |            |            |
|           |------------------------>|
|           | 6. PDU SESSION RESOURCE |
|           |    SETUP RESPONSE       |
|           |            |            |
|<--------->|            |            |
| 7. UP Data (QFI)       |            |
|           |<---------->|            |
|           | 7. UP Data (QFI)        |
|           |            |            |

Description: Sequence diagram showing message flow among UE, gNB, UPF, and AMF for PDU session establishment, resource setup, RRC reconfiguration, DRB establishment, and user-plane data transfer.

Figure 6.2.3-1: MAC RAR
