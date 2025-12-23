### 6.1.5 a    MAC PDU (MSGB) [#](#6-1-5-a-mac-pdu-msgb)

A MAC PDU consists of one or more MAC subPDUs and optionally padding. Each MAC subPDU consists one of the following:

-    a MAC subheader with Backoff Indicator only;

-    a MAC subheader and fallbackRAR;

-    a MAC subheader and successRAR;

-    a MAC subheader and MAC SDU for CCCH, DCCH or DTCH;

-    a MAC subheader and padding.

A MAC subheader with Backoff Indicator consists of five header fields E/T1/T2/R/BI as described in Figure 6.1.5a-1. A MAC subPDU with Backoff Indicator only is placed at the beginning of the MAC PDU, if included.

A MAC subheader for fallbackRAR consists of three header fields E/T1/RAPID as described in Figure 6.1.5a-2. A MAC subheader for successRAR consists of eight header fields E/T1/T2/S/R/R/R/R as described in Figure 6.1.5a-3. A MAC subheader for MAC SDU consists of the four header fields R/F/LCID/L as described in Figure 6.1.2-1 and Figure 6.1.2-2.

At most one 'MAC subPDU for successRAR' indicating presence of 'MAC subPDU(s) for MAC SDU' is included in a MAC PDU. MAC subPDU(s) for MAC SDU are placed immediately after the 'MAC subPDU for successRAR' indicating presence of 'MAC subPDU(s) for MAC SDU'.

If MAC PDU includes MAC subPDU(s) for MAC SDU, the last MAC subPDU for MAC SDU is placed before MAC subPDU with padding as depicted in Figure 6.1.5a-4. Otherwise, the last MAC subPDU in MAC PDU is placed before padding as depicted in Figure 6.1.5a-5. The MAC subPDU with padding includes R/R/LCID MAC subheader as described in Figure 6.1.2-3 and padding. The size of padding in the MAC subPDU with padding can be zero. The length of padding is implicit based on TB size, size of MAC subPDU(s).

A-IoT device           gNB                  A-IoT CN node
      |                 |                          |
      |-----------------|--------------------------|
      | 1. Inventory procedure as specified in     |
      |    16.x.6 step 1~6                         |
      |                 |<-------------------------|
      |                 | 2. Command Request       |
      |----------------------------------------------------|
      | 3. Allocate / coordinate A-IoT radio resources and |
      |    perform command procedure over A-IoT radio      |
      |    interface                                       |
      |                 |------------------------->|
      |                 | 4. Command Response      |
      |-----------------|--------------------------|
      | 5. A-IoT Session Release as defined in clause 16.x.8|
      |                 |                          |

Description: A sequence diagram showing message flow among three entities: "A-IoT device", "gNB", and "A-IoT CN node". Steps include an inventory procedure, a command request and response, allocation/coordination of A-IoT radio resources and command execution, and an A-IoT session release.

Figure 6.1.5a-1: BI MAC subheader

gNB                               A-IoT CN node
|                                   |
|<----------- 1. AIoT Session Release Command -----------|
|                                   |
|--- 2. Release A-IoT context and radio resources ------>|
|                                   |
|----------- 3. AIoT Session Release Complete --------->|
|                                   |

Description:
A sequence diagram showing message exchange between "gNB" and "A-IoT CN node" for releasing an AIoT session, including a release command, context and radio resource release, and session release completion.

Figure 6.1.5a-2: FallbackRAR MAC subheader

gNB                         A-IoT CN node
 |                               |
 |-- 1. A-IoT Session Release Request -->|
 |                               |
 |<-- 2. agrees to release the A-IoT session --|
 |                               |
 |=========== 3. A-IoT Session Release procedure ===========|
 |                               |

Description: Sequence diagram showing message flow between "gNB" and "A-IoT CN node" for A-IoT session release: (1) release request from gNB, (2) agreement response from A-IoT CN node, and (3) session release procedure.

Figure 6.1.5a-3: SuccessRAR MAC subheader

UE              Receiving gNB         Last Serving gNB        AMF              UPF(s)
|                   |                      |                   |                 |
|  UE in RRC_INACTIVE CM-CONNECTED         |                   |                 |
|-----------------------------------------------------------------------------------
| 1. RRCResumeRequest + UL SDT data and/or UL SDT signalling  ->                  |
|                   |                      |                   |                 |
|                   | 2. RETRIEVE UE CONTEXT REQUEST (SDT Indicator, assistance) ->
|                   |                      |                   |                 |
|                   | <- 3. RETRIEVE UE CONTEXT RESPONSE                          |
|                   |                      |                   |                 |
|          4. Decides to continue small data transmission in RRC_INACTIVE        |
|                   |                      |                   |                 |
|------------------ UL small data ----------------------------------------------->|
|                   |                      |                   |                 |
|------------------ Xn-U ADDRESS INDICATION ----------------->|                  |
|                   |                      |                   |                 |
|<----------------- DL small data ------------------------------------------------|
|                   |                      |                   |                 |
|------------------ Subsequent UL Small data ------------------------------------>|
|                   |                      |                   |                 |
|                   | 5. PATH SWITCH REQUEST ----------------->|                 |
|                   |                      |                   |                 |
|                   | <- 6. PATH SWITCH REQUEST ACKNOWLEDGE                      |
|                   |                      |                   |                 |
|------------------ UPLINK NAS TRANSPORT (NAS PDU) ------------->|               |
|                   |                      |                   |                 |
|<----------------- Subsequent SDT signalling -----------------------------------|
|<----------------- Subsequent SDT data -----------------------------------------|
|                   |                      |                   |                 |
|          Decides to Terminate small data transmission in RRC_INACTIVE          |
|                   |                      |                   |                 |
| 7. RRCRelease (Suspend Config.) ->                                           |
|                   |                      |                   |                 |
|                   |                      | 8. UE CONTEXT RELEASE ->            |
|                   |                      |                   |                 |
|  UE in RRC_INACTIVE CM-CONNECTED again                                       |

Description:
Sequence diagram showing message flow for small data transmission in RRC_INACTIVE state between UE, Receiving gNB, Last Serving gNB, AMF, and UPF(s), including context retrieval, path switch, SDT data/signalling, and release procedures.

Figure 6.1.5a-4: Example of a MSGB MAC PDU with MAC SDU(s)

+-----------------+        +----------------+        +-------------------+        +---------+        +--------+
|       UE        |        |  Receiving gNB |        |  Last Serving gNB |        |   AMF   |        | UPF(s) |
+-----------------+        +----------------+        +-------------------+        +---------+        +--------+
        |                           |                          |                      |                 |
        | 0. UE in RRC_INACTIVE     |                          |                      |                 |
        |    CM-CONNECTED           |                          |                      |                 |
        |-------------------------->|                          |                      |                 |
        |1. RRCResumeRequest        |                          |                      |                 |
        |   + UL SDT data and/or    |                          |                      |                 |
        |   UL SDT signaling        |                          |                      |                 |
        |                           |------------------------->|                      |                 |
        |                           |2. RETRIEVE UE CONTEXT    |                      |                 |
        |                           |   REQUEST (SDT indicator,|                      |                 |
        |                           |   assistance info)       |                      |                 |
        |                           |                          |3. Decides to keep    |                 |
        |                           |                          |   UE context         |                 |
        |                           |<-------------------------|                      |                 |
        |                           |4. PARTIAL UE CONTEXT     |                      |                 |
        |                           |   TRANSFER               |                      |                 |
        |                           |------------------------->|                      |                 |
        |                           |5. PARTIAL UE CONTEXT     |                      |                 |
        |                           |   TRANSFER ACKNOWLEDGE   |                      |                 |
        |                           |                          |                      |                 |
        |                           | Establish SDT RLC entity |                      |                 |
        |                           |                          | Keep PDCP entity     |                 |
        |                           |--------------------------------------------------------------->   |
        |                           |        UL SDT data / RRC TRANSFER (UL SDT signaling)           | |
        |                           |---------------------------------------------------------------->| |
        |                           |                 UPLINK NAS TRANSPORT (UL NAS PDU)              | |
        |<------------------------------------------------------------------------------------------------|
        |      Subsequent UL/DL SDT data (dotted green arrows via gNBs/AMF/UPF)                       |
        |<--------------------------->--------------------------->------------------------->---------->|
        |      Subsequent UL/DL SDT signaling (dotted gray arrows)                                    |
        |                           |                          |                      |                 |
        |                           | Detects end SDT          |                      |                 |
        |                           |------------------------->|                      |                 |
        |                           |6. RETRIEVE UE CONTEXT    |                      |                 |
        |                           |   CONFIRM (end SDT)      |                      |                 |
        |                           |------------------------->|                      |                 |
        |                           |7. RETRIEVE UE CONTEXT    |                      |                 |
        |                           |   FAILURE (RRCRelease msg)|                     |                 |
        |<--------------------------|                          |                      |                 |
        |8. RRCRelease (Suspend Config.)                       |                      |                 |
        |-------------------------->|                          |                      |                 |
        |9. UE in RRC_INACTIVE CM-CONNECTED                    |                      |                 |
        |                           |                          |                      |                 |

Description:
Sequence diagram illustrating UE-initiated SDT (Small Data Transmission) in 5G NR. It shows message exchanges among UE, Receiving gNB, Last Serving gNB, AMF, and UPF(s), including context retrieval/transfer, establishment of SDT RLC entity, UL/DL SDT data and signaling flows, detection of SDT end, and RRC release leading the UE back to RRC_INACTIVE CM-CONNECTED state.

Figure 6.1.5a-5: Example of a MSGB MAC PDU without MAC SDU(s)
