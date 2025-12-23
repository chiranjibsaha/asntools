### 4.7.2     Protocol Stacks [#](#4-7-2-protocol-stacks)

Fig. 4.7.2-1 shows the protocol stack for F1-U and Fig. 4.7.2-2 shows the protocol stack for F1-C between IAB-DU and IAB-donor-CU. In these figures, F1-U and F1-C are carried over two backhaul hops.

F1-U and F1-C use an IP transport layer between IAB-DU and IAB-donor-CU as defined in TS 38.470 [32]. F1-U and F1-C need to be security-protected as described in TS 33.501 [5] (the security layer is not shown in the Figures 4.7.2-1/2).

On the wireless backhaul, the IP layer is carried over the Backhaul Adaptation Protocol (BAP) sublayer, which enables routing over multiple="multiple" hops. The IP layer can also be used for *non*-F1 traffic, such as OAM traffic as defined in TS 38.401 [4].

On each backhaul link, the BAP PDUs are carried by BH RLC channels. Multiple BH RLC channels can be configured on each BH link to allow traffic prioritization and QoS enforcement. The BH-RLC-channel mapping for BAP PDUs is performed by the BAP entities on each IAB-node and the IAB-donor-DU.

Protocol stacks for an IAB-donor with split gNB architecture are specified in TS 38.401 [4].

IAB-node 2                                  IAB-node 1                                  IAB-donor
+---------------------------+               +---------------------------+               +---------------------------+
| IAB-DU        | IAB-MT   |               | IAB-DU        | IAB-MT   |               | DU             | CU        |
|               |          |               |               |          |               |                |           |
| [GTP-U]-------------------------------[GTP-U]                                               |
| [UDP ]-------------------------------[UDP ]                                               |
| [IP  ]-------------------------------[IP  ]-----------------------------[IP ]             |
|                           |               |                           |               |                |           |
| [BAP ]------------------------\      /------------------------[BAP ]   | [BAP]         |
| [RLC ]-------------------------\    /-------------------------[RLC ]---| [RLC]         |
| [MAC ]--------------------------\  /--------------------------[MAC ]---| [MAC]         |
| [PHY ]---------------------------\/---------------------------[PHY ]---| [PHY]         |
+---------------------------+   BH RLC channel      BH RLC channel      +---------------------------+

Description:
Layered protocol/architecture diagram for an Integrated Access and Backhaul (IAB) network. It shows three entities (IAB-node 2, IAB-node 1, and IAB-donor) with functional splits into IAB-DU/IAB-MT or DU/CU. Protocol layers (GTP-U, UDP, IP, BAP, RLC, MAC, PHY) are depicted as stacked boxes, with horizontal lines indicating connections across nodes and labeled backhaul RLC channels between the nodes.

Fig. 4.7.2-1: Protocol stack for the support of F1-U protocol

+--------------------------------------------------------------------------------------+
|                                   IAB-node 2     IAB-node 1              IAB-donor   |
|                                +------------+  +------------+         +------------+ |
|                                | IAB-DU IAB-MT| | IAB-DU IAB-MT|      |   DU   CU  | |
|                                +------------+  +------------+         +------------+ |
|                                                                                      |
| F1AP  [box]---------------------------horizontal line------------------------[box]F1AP|
| SCTP  [box]---------------------------horizontal line------------------------[box]SCTP|
| IP    [box]---------------------------horizontal line------------------------[box] IP |
|                                                                                      |
|            BAP [box]------\         +-----+  +-----+            BAP [box]            |
|            RLC [box]-------\--------|BAP  |  |BAP  |------------RLC [box]            |
|            MAC [box]--------\-------|RLC  |  |RLC  |------------MAC [box]            |
|            PHY [box]---------\------|MAC  |  |MAC  |------------PHY [box]            |
|                               \-----|PHY  |  |PHY  |                               |
|                                      +-----+  +-----+                              |
|                                                                                      |
|                        BH RLC channel                BH RLC channel                  |
+--------------------------------------------------------------------------------------+

Description:
Layered protocol/architecture diagram showing three entities: "IAB-node 2", "IAB-node 1", and "IAB-donor". Each has sub-blocks (IAB-DU/IAB-MT or DU/CU) with protocol layers such as F1AP, SCTP, IP, BAP, RLC, MAC, and PHY. Horizontal lines indicate connections between corresponding layers, and "BH RLC channel" labels the backhaul RLC channels between nodes.

Fig. 4.7.2-2: Protocol stack for the support of F1-C protocol

The IAB-MT further establishes SRBs (carrying RRC and NAS) with the IAB-donor-CU. For IAB-nodes operating in EN-DC, the IAB-MT establishes one or more DRBs with the eNB and one or more DRBs with the IAB-donor-CU, which can be used, e.g., to carry OAM traffic. For SA mode, the establishment of DRBs is optional. These SRBs and DRBs are transported between the IAB-MT and its parent node over Uu access channel(s). The protocol stacks for the SRB is shown in Fig. 4.7.2-3.

IAB-node 2                     IAB-node 1                 IAB-donor                 AMF
+----------------+            +----------------+         +----------------+       +----------+
|    IAB-MT      |            |    IAB-DU      |         |       CU       |       |   NAS    |
|                |            |                |         |                |       |          |
| +-----+        |            |                |         |                |       |          |
| | NAS |--------+------------+----------------+---------+----------------+-------+          |
| +-----+        |            |                |         |   +-----+      |       |          |
| +-----+        |            |                |         |   | RRC |------/       |          |
| | RRC |--------+------------+----------------+---------+---+-----+              |          |
| +-----+        |            |                |         |   +------+             |          |
| +------+       |            |                |         |   | PDCP |-------------/          |
| | PDCP |-------+------------+----------------+---------+---+------+                        |
| +------+       |            |   +-----+      |         |                                    |
| +-----+        |            |   | RLC |------+         |                                    |
| | RLC |--------+------------+---+-----+                |                                    |
| +-----+        |            |   +-----+                |                                    |
| +-----+        |            |   | MAC |----------------+                                    |
| | MAC |--------+------------+---+-----+                |                                    |
| +-----+        |            |   +-----+                |                                    |
| +-----+        |            |   | PHY |----------------+                                    |
| | PHY |--------+------------+---+-----+                |                                    |
| +-----+        |            |                |         |                                    |
+----------------+            +----------------+         +----------------+       +----------+

             <-------------------------- NR Uu --------------------------------->

Description:
ASCII representation of a 5G IAB (Integrated Access and Backhaul) protocol stack diagram. It shows IAB-node 2 (IAB-MT) connected via NR Uu to IAB-node 1 (IAB-DU), which connects to an IAB-donor CU and then to the AMF. Protocol layers (NAS, RRC, PDCP, RLC, MAC, PHY) are illustrated with horizontal connections between the corresponding functional blocks.

Figure 4.7.2-3: Protocol stack for the support of IAB-MT's RRC and NAS connections
