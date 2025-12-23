### 6.2.2     MAC subheader for Random Access Response [#](#6-2-2-mac-subheader-for-random-access-response)

The MAC subheader consists of the following fields:

-    E: The Extension field is a flag indicating if the MAC subPDU including this MAC subheader is the last MAC subPDU or not in the MAC PDU. The E field is set to 1 to indicate at least another MAC subPDU follows. The E field is set to 0 to indicate that the MAC subPDU including this MAC subheader is the last MAC subPDU in the MAC PDU;

-    T: The Type field is a flag indicating whether the MAC subheader contains a Random Access Preamble ID or a Backoff Indicator. The T field is set to 0 to indicate the presence of a Backoff Indicator field in the subheader (BI). The T field is set to 1 to indicate the presence of a Random Access Preamble ID field in the subheader (RAPID);

-    R: Reserved bit, set to 0;

-    BI: The Backoff Indicator field identifies the overload condition in the cell. The size of the BI field is 4 bits;

-    RAPID: The Random Access Preamble IDentifier field identifies the transmitted Random Access Preamble (see clause 5.1.3). The size of the RAPID field is 6 bits. If the RAPID in the MAC subheader of a MAC subPDU corresponds to one of the Random Access Preambles configured for SI request or SIB1 request, MAC RAR is not included in the MAC subPDU.

The MAC subheader is octet aligned.
