### 4.7.1     Architecture [#](#4-7-1-architecture)

Integrated access and backhaul (IAB) enables wireless relaying in NG-RAN. The relaying node, referred to as *IAB-node*, supports access and backhauling via NR. The terminating node of NR backhauling on network side is referred to as the *IAB-donor*, which represents a gNB with additional functionality to support IAB. Backhauling can occur via a single or via multiple="multiple" hops. The IAB architecture is shown in Figure 4.7.1-1.

The IAB-node supports the gNB-DU functionality, as defined in TS 38.401 [4], to terminate the NR access interface to UEs and next-hop IAB-nodes, and to terminate the F1 protocol to the gNB-CU functionality, as defined in TS 38.401 [4], on the IAB-donor. The gNB-DU functionality on the IAB-node is also referred to as *IAB-DU*.

In addition to the gNB-DU functionality, the IAB-node also supports a subset of the UE functionality referred to as *IAB-MT*, which includes, e.g., physical layer, layer-2, RRC and NAS functionality to connect to the gNB-DU of another IAB-node or the IAB-donor, to connect to the gNB-CU on the IAB-donor, and to the core network.

The IAB-node can access the network using either SA mode or EN-DC. In EN-DC, the IAB-node connects via E-UTRA to a MeNB, and the IAB-donor terminates X2-C as SgNB (TS 37.340 [21]).

a)
 AMF/UPF           AMF/UPF
   |  \ NG       NG /  |
   |   \           /   |
   |    \   NG-C  /    |
  gNB----\-------/--IAB-donor (gNB)
            Xn          |
                        | NR Uu
                     IAB-node
                        | NR Uu
                     IAB-node

b)
 MME/S-PGW          MME/S-PGW
   |  \ S1       S1 /  |
   |   \         /   |
   |    \  S1-U /    |
  eNB----\-----/----MeNB----------IAB-donor (SgNB)
            X2           \           |
                         X2-C        | NR Uu
                           \      IAB-node
                            \ LTE Uu  |
                             \        | NR Uu
                              \    IAB-node

Description:
Two subfigures labeled a) and b) showing network architectures for integrated access and backhaul (IAB). They depict connections between core network entities (AMF/UPF or MME/S-PGW), base stations (gNB, eNB, MeNB, IAB-donor), and multiple IAB-nodes using various interfaces (NG, Xn, S1, X2, X2-C, F1, NR Uu, LTE Uu).

Figure 4.7.1-1: IAB architecture; a) IAB-node using SA mode with 5GC; b) IAB-node using EN-DC

All IAB-nodes that are connected to an IAB-donor via one or multiple="multiple" backhaul hops and controlled by this IAB-donor via F1AP and/or RRC form an IAB topology with the IAB-donor as its root (Fig. 4.7.1-2). In this IAB topology, the neighbour node of the IAB-DU or the IAB-donor-DU is referred to as the *child* node and the neighbour node of the IAB-MT is referred to as the *parent* node. The direction toward the child node is referred to as *downstream* while the direction toward the parent node is referred to as *upstream*. The IAB-donor performs centralized resource, topology and route management for its IAB topology.

Diagram: IAB-node with parent and child nodes connected via NR Uu links

ASCII diagram:

          Parent nodes
             ↑  (upstream)

         +---------+      +---------+
         | +-----+ |      | +-----+ |
         | |IAB- | |      | |IAB- | |
         | | DU  | |      | | DU  | |
         | +-----+ |      | +-----+ |
         +---------+      +---------+
              \               /
               \   NR Uu     /
                \           /
                 \         /
                  \       /
                 +-----------+
                 | +-------+ |
                 | | IAB-  | |
                 | |  MT   | |
                 | +-------+ |
                 | +-------+ |
                 | | IAB-  | |
                 | |  DU   | |
                 | +-------+ |
                 +-----------+
                         |
                         |  NR Uu
        -----------------------------------------
        |                  |                    |
   +-----------+     +-----------+        +-----------+
   | +-------+ |     | +-------+ |        | +-------+ |
   | | IAB-  | |     | | IAB-  | |        | | IAB-  | |
   | |  MT   | |     | |  MT   | |        | |  MT   | |
   | +-------+ |     | +-------+ |        | +-------+ |
   |           |     |           |        |           |
   +-----------+     +-----------+        +-----------+
        .                  .                    .
        .                  .                    .

                 ↓  (downstream)
                 Child nodes

Figure 4.7.1-2: Parent- and child-node relationship for IAB-node
