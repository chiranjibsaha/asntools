### 6.1.5     MAC PDU (Random Access Response) [#](#6-1-5-mac-pdu-random-access-response)

A MAC PDU consists of one or more MAC subPDUs and optionally padding. Each MAC subPDU consists one of the following:

-    a MAC subheader with Backoff Indicator only;

-    a MAC subheader with RAPID only (i.e. acknowledgment for SI request or SIB1 request);

-    a MAC subheader with RAPID and MAC RAR.

A MAC subheader with Backoff Indicator consists of five header fields E/T/R/R/BI as described in Figure 6.1.5-1. A MAC subPDU with Backoff Indicator only is placed at the beginning of the MAC PDU, if included. 'MAC subPDU(s) with RAPID only' and 'MAC subPDU(s) with RAPID and MAC RAR' can be placed anywhere between MAC subPDU with Backoff Indicator only (if any) and padding (if any).

A MAC subheader with RAPID consists of three header fields E/T/RAPID as described in Figure 6.1.5-2.

Padding is placed at the end of the MAC PDU if present. Presence and length of padding is implicit based on TB size, size of MAC subPDU(s).

A-IoT device                                      A-IoT reader
     |                                                  |
     |<---------------- A-IoT paging message -----------|  (0)
     |        with CBRA indication or                   |
     |        Access Trigger message                    |
 (1) |---------------- Access Random ID message ------->|
     |<-------------- Random ID Response message -------|  (2)
 (3) |----------- D2R Upper Layer Data Transfer message ->|
     |                                                  |

Description: Sequence diagram showing message exchange between an A-IoT device and an A-IoT reader. Four numbered steps: (0) reader sends paging or access trigger message to device; (1) device sends Access Random ID message to reader; (2) reader sends Random ID Response message back; (3) device sends D2R upper layer data transfer message to reader.

Figure 6.1.5-1: E/T/R/R/BI MAC subheader

A-IoT device                                 A-IoT reader
     |                                              |
     |<-------- A-IoT paging message with ---------|
     |          CFA indication                      |
 (1) |                                              | (0)
     |-------- D2R Upper Layer Data Transfer ----->|
     |                 message                      |

Description: A sequence diagram showing communication between an A-IoT device and an A-IoT reader. The reader sends an "A-IoT paging message with CFA indication" to the device, and the device responds with a "D2R Upper Layer Data Transfer message." The device side is labeled with a green circle "1" and the reader side with a green circle "0".

Figure 6.1.5-2: E/T/RAPID MAC subheader

A-IoT device          gNB                     A-IoT CN node
     |                 |                            |
     |<----------------| 1. Inventory Request       |
     |                 |                            |
     |                 | 2. Allocate / coordinate   |
     |                 |    A-IoT radio resources   |
     |                 |                            |
     |                 |-------------> 3. Inventory Response ---->|
     |                 |                            |
4. Inventory procedure over A-IoT radio interface   |
     |--------------------------------------------->|
     |                 |                            |
     |                 |-------------> 5. Inventory Report ------>|
     |                 |                            |
     |                 |--------- - - > 6. Inventory Report - - ->|
     |                 |                            |
     |                 | 7. A-IoT Session Release as defined      |
     |                 |    in clause 16.x.8                      |
     |                 |                            |
     v                 v                            v

Description:
A sequence diagram showing message exchanges between three entities: "A-IoT device", "gNB", and "A-IoT CN node". The steps include an Inventory Request, allocation/coordination of A-IoT radio resources, Inventory Response, an inventory procedure over the A-IoT radio interface, Inventory Reports, and finally an A-IoT Session Release as defined in clause 16.x.8.

Figure 6.1.5-3: Example of MAC PDU consisting of MAC RARs
