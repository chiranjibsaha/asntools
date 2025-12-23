```text
└─ RRCResume/RRCReconfiguration
   └─ criticalExtensions
      └─ rrcReconfiguration
         ├─ nonCriticalExtension
         │  ├─ dedicatedSIB1-Delivery
         │  │  └─ SIB1
         │  │     └─ servingCellConfigCommon
         │  │        ├─ supplementaryUplink
         │  │        │  └─ initialUplinkBWP
         │  │        │     ├─ additionalRACH-ConfigList-r17
         │  │        │     │  └─ setup
         │  │        │     │     └─ _item_
         │  │        │     │        ├─ msgA-ConfigCommon-r17
         │  │        │     │        │  └─ rach-ConfigCommonTwoStepRA-r16
         │  │        │     │        │     └─ featureCombinationPreamblesList-r17
         │  │        │     │        │        └─ _item_
         │  │        │     │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
         │  │        │     │        └─ rach-ConfigCommon-r17
         │  │        │     │           └─ featureCombinationPreamblesList-r17
         │  │        │     │              └─ _item_
         │  │        │     │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
         │  │        │     ├─ msgA-ConfigCommon-r16
         │  │        │     │  └─ setup
         │  │        │     │     └─ rach-ConfigCommonTwoStepRA-r16
         │  │        │     │        └─ featureCombinationPreamblesList-r17
         │  │        │     │           └─ _item_
         │  │        │     │              └─ msg1-RepetitionTimeOffsetROGroup-r18
         │  │        │     ├─ rach-ConfigCommon
         │  │        │     │  └─ setup
         │  │        │     │     └─ featureCombinationPreamblesList-r17
         │  │        │     │        └─ _item_
         │  │        │     │           └─ msg1-RepetitionTimeOffsetROGroup-r18
         │  │        │     └─ rach-ConfigCommonIAB-r16
         │  │        │        └─ setup
         │  │        │           └─ featureCombinationPreamblesList-r17
         │  │        │              └─ _item_
         │  │        │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
         │  │        ├─ uplinkConfigCommon
         │  │        │  └─ initialUplinkBWP
         │  │        │     ├─ additionalRACH-ConfigList-r17
         │  │        │     │  └─ setup
         │  │        │     │     └─ _item_
         │  │        │     │        ├─ msgA-ConfigCommon-r17
         │  │        │     │        │  └─ rach-ConfigCommonTwoStepRA-r16
         │  │        │     │        │     └─ featureCombinationPreamblesList-r17
         │  │        │     │        │        └─ _item_
         │  │        │     │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
         │  │        │     │        └─ rach-ConfigCommon-r17
         │  │        │     │           └─ featureCombinationPreamblesList-r17
         │  │        │     │              └─ _item_
         │  │        │     │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
         │  │        │     ├─ msgA-ConfigCommon-r16
         │  │        │     │  └─ setup
         │  │        │     │     └─ rach-ConfigCommonTwoStepRA-r16
         │  │        │     │        └─ featureCombinationPreamblesList-r17
         │  │        │     │           └─ _item_
         │  │        │     │              └─ msg1-RepetitionTimeOffsetROGroup-r18
         │  │        │     ├─ rach-ConfigCommon
         │  │        │     │  └─ setup
         │  │        │     │     └─ featureCombinationPreamblesList-r17
         │  │        │     │        └─ _item_
         │  │        │     │           └─ msg1-RepetitionTimeOffsetROGroup-r18
         │  │        │     └─ rach-ConfigCommonIAB-r16
         │  │        │        └─ setup
         │  │        │           └─ featureCombinationPreamblesList-r17
         │  │        │              └─ _item_
         │  │        │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
         │  │        └─ uplinkConfigCommon-v1700
         │  │           └─ initialUplinkBWP-RedCap-r17
         │  │              ├─ additionalRACH-ConfigList-r17
         │  │              │  └─ setup
         │  │              │     └─ _item_
         │  │              │        ├─ msgA-ConfigCommon-r17
         │  │              │        │  └─ rach-ConfigCommonTwoStepRA-r16
         │  │              │        │     └─ featureCombinationPreamblesList-r17
         │  │              │        │        └─ _item_
         │  │              │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
         │  │              │        └─ rach-ConfigCommon-r17
         │  │              │           └─ featureCombinationPreamblesList-r17
         │  │              │              └─ _item_
         │  │              │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
         │  │              ├─ msgA-ConfigCommon-r16
         │  │              │  └─ setup
         │  │              │     └─ rach-ConfigCommonTwoStepRA-r16
         │  │              │        └─ featureCombinationPreamblesList-r17
         │  │              │           └─ _item_
         │  │              │              └─ msg1-RepetitionTimeOffsetROGroup-r18
         │  │              ├─ rach-ConfigCommon
         │  │              │  └─ setup
         │  │              │     └─ featureCombinationPreamblesList-r17
         │  │              │        └─ _item_
         │  │              │           └─ msg1-RepetitionTimeOffsetROGroup-r18
         │  │              └─ rach-ConfigCommonIAB-r16
         │  │                 └─ setup
         │  │                    └─ featureCombinationPreamblesList-r17
         │  │                       └─ _item_
         │  │                          └─ msg1-RepetitionTimeOffsetROGroup-r18
         │  └─ masterCellGroup
         │     └─ CellGroupConfig
         │        ├─ sCellToAddModList
         │        │  └─ _item_
         │        │     ├─ sCellConfigCommon
         │        │     │  ├─ supplementaryUplinkConfig
         │        │     │  │  └─ initialUplinkBWP
         │        │     │  │     ├─ additionalRACH-ConfigList-r17
         │        │     │  │     │  └─ setup
         │        │     │  │     │     └─ _item_
         │        │     │  │     │        ├─ msgA-ConfigCommon-r17
         │        │     │  │     │        │  └─ rach-ConfigCommonTwoStepRA-r16
         │        │     │  │     │        │     └─ featureCombinationPreamblesList-r17
         │        │     │  │     │        │        └─ _item_
         │        │     │  │     │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
         │        │     │  │     │        └─ rach-ConfigCommon-r17
         │        │     │  │     │           └─ featureCombinationPreamblesList-r17
         │        │     │  │     │              └─ _item_
         │        │     │  │     │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
         │        │     │  │     ├─ msgA-ConfigCommon-r16
         │        │     │  │     │  └─ setup
         │        │     │  │     │     └─ rach-ConfigCommonTwoStepRA-r16
         │        │     │  │     │        └─ featureCombinationPreamblesList-r17
         │        │     │  │     │           └─ _item_
         │        │     │  │     │              └─ msg1-RepetitionTimeOffsetROGroup-r18
         │        │     │  │     ├─ rach-ConfigCommon
         │        │     │  │     │  └─ setup
         │        │     │  │     │     └─ featureCombinationPreamblesList-r17
         │        │     │  │     │        └─ _item_
         │        │     │  │     │           └─ msg1-RepetitionTimeOffsetROGroup-r18
         │        │     │  │     └─ rach-ConfigCommonIAB-r16
         │        │     │  │        └─ setup
         │        │     │  │           └─ featureCombinationPreamblesList-r17
         │        │     │  │              └─ _item_
         │        │     │  │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
         │        │     │  ├─ uplinkConfigCommon
         │        │     │  │  └─ initialUplinkBWP
         │        │     │  │     ├─ additionalRACH-ConfigList-r17
         │        │     │  │     │  └─ setup
         │        │     │  │     │     └─ _item_
         │        │     │  │     │        ├─ msgA-ConfigCommon-r17
         │        │     │  │     │        │  └─ rach-ConfigCommonTwoStepRA-r16
         │        │     │  │     │        │     └─ featureCombinationPreamblesList-r17
         │        │     │  │     │        │        └─ _item_
         │        │     │  │     │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
         │        │     │  │     │        └─ rach-ConfigCommon-r17
         │        │     │  │     │           └─ featureCombinationPreamblesList-r17
         │        │     │  │     │              └─ _item_
         │        │     │  │     │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
         │        │     │  │     ├─ msgA-ConfigCommon-r16
         │        │     │  │     │  └─ setup
         │        │     │  │     │     └─ rach-ConfigCommonTwoStepRA-r16
         │        │     │  │     │        └─ featureCombinationPreamblesList-r17
         │        │     │  │     │           └─ _item_
         │        │     │  │     │              └─ msg1-RepetitionTimeOffsetROGroup-r18
         │        │     │  │     ├─ rach-ConfigCommon
         │        │     │  │     │  └─ setup
         │        │     │  │     │     └─ featureCombinationPreamblesList-r17
         │        │     │  │     │        └─ _item_
         │        │     │  │     │           └─ msg1-RepetitionTimeOffsetROGroup-r18
         │        │     │  │     └─ rach-ConfigCommonIAB-r16
         │        │     │  │        └─ setup
         │        │     │  │           └─ featureCombinationPreamblesList-r17
         │        │     │  │              └─ _item_
         │        │     │  │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
         │        │     │  └─ uplinkConfigCommon-v1700
         │        │     │     └─ initialUplinkBWP-RedCap-r17
         │        │     │        ├─ additionalRACH-ConfigList-r17
         │        │     │        │  └─ setup
         │        │     │        │     └─ _item_
         │        │     │        │        ├─ msgA-ConfigCommon-r17
         │        │     │        │        │  └─ rach-ConfigCommonTwoStepRA-r16
         │        │     │        │        │     └─ featureCombinationPreamblesList-r17
         │        │     │        │        │        └─ _item_
         │        │     │        │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
         │        │     │        │        └─ rach-ConfigCommon-r17
         │        │     │        │           └─ featureCombinationPreamblesList-r17
         │        │     │        │              └─ _item_
         │        │     │        │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
         │        │     │        ├─ msgA-ConfigCommon-r16
         │        │     │        │  └─ setup
         │        │     │        │     └─ rach-ConfigCommonTwoStepRA-r16
         │        │     │        │        └─ featureCombinationPreamblesList-r17
         │        │     │        │           └─ _item_
         │        │     │        │              └─ msg1-RepetitionTimeOffsetROGroup-r18
         │        │     │        ├─ rach-ConfigCommon
         │        │     │        │  └─ setup
         │        │     │        │     └─ featureCombinationPreamblesList-r17
         │        │     │        │        └─ _item_
         │        │     │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
         │        │     │        └─ rach-ConfigCommonIAB-r16
         │        │     │           └─ setup
         │        │     │              └─ featureCombinationPreamblesList-r17
         │        │     │                 └─ _item_
         │        │     │                    └─ msg1-RepetitionTimeOffsetROGroup-r18
         │        │     └─ sCellConfigDedicated
         │        │        ├─ supplementaryUplink
         │        │        │  └─ uplinkBWP-ToAddModList
         │        │        │     └─ _item_
         │        │        │        └─ bwp-Common
         │        │        │           ├─ additionalRACH-ConfigList-r17
         │        │        │           │  └─ setup
         │        │        │           │     └─ _item_
         │        │        │           │        ├─ msgA-ConfigCommon-r17
         │        │        │           │        │  └─ rach-ConfigCommonTwoStepRA-r16
         │        │        │           │        │     └─ featureCombinationPreamblesList-r17
         │        │        │           │        │        └─ _item_
         │        │        │           │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
         │        │        │           │        └─ rach-ConfigCommon-r17
         │        │        │           │           └─ featureCombinationPreamblesList-r17
         │        │        │           │              └─ _item_
         │        │        │           │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
         │        │        │           ├─ msgA-ConfigCommon-r16
         │        │        │           │  └─ setup
         │        │        │           │     └─ rach-ConfigCommonTwoStepRA-r16
         │        │        │           │        └─ featureCombinationPreamblesList-r17
         │        │        │           │           └─ _item_
         │        │        │           │              └─ msg1-RepetitionTimeOffsetROGroup-r18
         │        │        │           ├─ rach-ConfigCommon
         │        │        │           │  └─ setup
         │        │        │           │     └─ featureCombinationPreamblesList-r17
         │        │        │           │        └─ _item_
         │        │        │           │           └─ msg1-RepetitionTimeOffsetROGroup-r18
         │        │        │           └─ rach-ConfigCommonIAB-r16
         │        │        │              └─ setup
         │        │        │                 └─ featureCombinationPreamblesList-r17
         │        │        │                    └─ _item_
         │        │        │                       └─ msg1-RepetitionTimeOffsetROGroup-r18
         │        │        └─ uplinkConfig
         │        │           └─ uplinkBWP-ToAddModList
         │        │              └─ _item_
         │        │                 └─ bwp-Common
         │        │                    ├─ additionalRACH-ConfigList-r17
         │        │                    │  └─ setup
         │        │                    │     └─ _item_
         │        │                    │        ├─ msgA-ConfigCommon-r17
         │        │                    │        │  └─ rach-ConfigCommonTwoStepRA-r16
         │        │                    │        │     └─ featureCombinationPreamblesList-r17
         │        │                    │        │        └─ _item_
         │        │                    │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
         │        │                    │        └─ rach-ConfigCommon-r17
         │        │                    │           └─ featureCombinationPreamblesList-r17
         │        │                    │              └─ _item_
         │        │                    │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
         │        │                    ├─ msgA-ConfigCommon-r16
         │        │                    │  └─ setup
         │        │                    │     └─ rach-ConfigCommonTwoStepRA-r16
         │        │                    │        └─ featureCombinationPreamblesList-r17
         │        │                    │           └─ _item_
         │        │                    │              └─ msg1-RepetitionTimeOffsetROGroup-r18
         │        │                    ├─ rach-ConfigCommon
         │        │                    │  └─ setup
         │        │                    │     └─ featureCombinationPreamblesList-r17
         │        │                    │        └─ _item_
         │        │                    │           └─ msg1-RepetitionTimeOffsetROGroup-r18
         │        │                    └─ rach-ConfigCommonIAB-r16
         │        │                       └─ setup
         │        │                          └─ featureCombinationPreamblesList-r17
         │        │                             └─ _item_
         │        │                                └─ msg1-RepetitionTimeOffsetROGroup-r18
         │        └─ spCellConfig
         │           ├─ reconfigurationWithSync
         │           │  └─ spCellConfigCommon
         │           │     ├─ supplementaryUplinkConfig
         │           │     │  └─ initialUplinkBWP
         │           │     │     ├─ additionalRACH-ConfigList-r17
         │           │     │     │  └─ setup
         │           │     │     │     └─ _item_
         │           │     │     │        ├─ msgA-ConfigCommon-r17
         │           │     │     │        │  └─ rach-ConfigCommonTwoStepRA-r16
         │           │     │     │        │     └─ featureCombinationPreamblesList-r17
         │           │     │     │        │        └─ _item_
         │           │     │     │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
         │           │     │     │        └─ rach-ConfigCommon-r17
         │           │     │     │           └─ featureCombinationPreamblesList-r17
         │           │     │     │              └─ _item_
         │           │     │     │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
         │           │     │     ├─ msgA-ConfigCommon-r16
         │           │     │     │  └─ setup
         │           │     │     │     └─ rach-ConfigCommonTwoStepRA-r16
         │           │     │     │        └─ featureCombinationPreamblesList-r17
         │           │     │     │           └─ _item_
         │           │     │     │              └─ msg1-RepetitionTimeOffsetROGroup-r18
         │           │     │     ├─ rach-ConfigCommon
         │           │     │     │  └─ setup
         │           │     │     │     └─ featureCombinationPreamblesList-r17
         │           │     │     │        └─ _item_
         │           │     │     │           └─ msg1-RepetitionTimeOffsetROGroup-r18
         │           │     │     └─ rach-ConfigCommonIAB-r16
         │           │     │        └─ setup
         │           │     │           └─ featureCombinationPreamblesList-r17
         │           │     │              └─ _item_
         │           │     │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
         │           │     ├─ uplinkConfigCommon
         │           │     │  └─ initialUplinkBWP
         │           │     │     ├─ additionalRACH-ConfigList-r17
         │           │     │     │  └─ setup
         │           │     │     │     └─ _item_
         │           │     │     │        ├─ msgA-ConfigCommon-r17
         │           │     │     │        │  └─ rach-ConfigCommonTwoStepRA-r16
         │           │     │     │        │     └─ featureCombinationPreamblesList-r17
         │           │     │     │        │        └─ _item_
         │           │     │     │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
         │           │     │     │        └─ rach-ConfigCommon-r17
         │           │     │     │           └─ featureCombinationPreamblesList-r17
         │           │     │     │              └─ _item_
         │           │     │     │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
         │           │     │     ├─ msgA-ConfigCommon-r16
         │           │     │     │  └─ setup
         │           │     │     │     └─ rach-ConfigCommonTwoStepRA-r16
         │           │     │     │        └─ featureCombinationPreamblesList-r17
         │           │     │     │           └─ _item_
         │           │     │     │              └─ msg1-RepetitionTimeOffsetROGroup-r18
         │           │     │     ├─ rach-ConfigCommon
         │           │     │     │  └─ setup
         │           │     │     │     └─ featureCombinationPreamblesList-r17
         │           │     │     │        └─ _item_
         │           │     │     │           └─ msg1-RepetitionTimeOffsetROGroup-r18
         │           │     │     └─ rach-ConfigCommonIAB-r16
         │           │     │        └─ setup
         │           │     │           └─ featureCombinationPreamblesList-r17
         │           │     │              └─ _item_
         │           │     │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
         │           │     └─ uplinkConfigCommon-v1700
         │           │        └─ initialUplinkBWP-RedCap-r17
         │           │           ├─ additionalRACH-ConfigList-r17
         │           │           │  └─ setup
         │           │           │     └─ _item_
         │           │           │        ├─ msgA-ConfigCommon-r17
         │           │           │        │  └─ rach-ConfigCommonTwoStepRA-r16
         │           │           │        │     └─ featureCombinationPreamblesList-r17
         │           │           │        │        └─ _item_
         │           │           │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
         │           │           │        └─ rach-ConfigCommon-r17
         │           │           │           └─ featureCombinationPreamblesList-r17
         │           │           │              └─ _item_
         │           │           │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
         │           │           ├─ msgA-ConfigCommon-r16
         │           │           │  └─ setup
         │           │           │     └─ rach-ConfigCommonTwoStepRA-r16
         │           │           │        └─ featureCombinationPreamblesList-r17
         │           │           │           └─ _item_
         │           │           │              └─ msg1-RepetitionTimeOffsetROGroup-r18
         │           │           ├─ rach-ConfigCommon
         │           │           │  └─ setup
         │           │           │     └─ featureCombinationPreamblesList-r17
         │           │           │        └─ _item_
         │           │           │           └─ msg1-RepetitionTimeOffsetROGroup-r18
         │           │           └─ rach-ConfigCommonIAB-r16
         │           │              └─ setup
         │           │                 └─ featureCombinationPreamblesList-r17
         │           │                    └─ _item_
         │           │                       └─ msg1-RepetitionTimeOffsetROGroup-r18
         │           └─ spCellConfigDedicated
         │              ├─ supplementaryUplink
         │              │  └─ uplinkBWP-ToAddModList
         │              │     └─ _item_
         │              │        └─ bwp-Common
         │              │           ├─ additionalRACH-ConfigList-r17
         │              │           │  └─ setup
         │              │           │     └─ _item_
         │              │           │        ├─ msgA-ConfigCommon-r17
         │              │           │        │  └─ rach-ConfigCommonTwoStepRA-r16
         │              │           │        │     └─ featureCombinationPreamblesList-r17
         │              │           │        │        └─ _item_
         │              │           │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
         │              │           │        └─ rach-ConfigCommon-r17
         │              │           │           └─ featureCombinationPreamblesList-r17
         │              │           │              └─ _item_
         │              │           │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
         │              │           ├─ msgA-ConfigCommon-r16
         │              │           │  └─ setup
         │              │           │     └─ rach-ConfigCommonTwoStepRA-r16
         │              │           │        └─ featureCombinationPreamblesList-r17
         │              │           │           └─ _item_
         │              │           │              └─ msg1-RepetitionTimeOffsetROGroup-r18
         │              │           ├─ rach-ConfigCommon
         │              │           │  └─ setup
         │              │           │     └─ featureCombinationPreamblesList-r17
         │              │           │        └─ _item_
         │              │           │           └─ msg1-RepetitionTimeOffsetROGroup-r18
         │              │           └─ rach-ConfigCommonIAB-r16
         │              │              └─ setup
         │              │                 └─ featureCombinationPreamblesList-r17
         │              │                    └─ _item_
         │              │                       └─ msg1-RepetitionTimeOffsetROGroup-r18
         │              └─ uplinkConfig
         │                 └─ uplinkBWP-ToAddModList
         │                    └─ _item_
         │                       └─ bwp-Common
         │                          ├─ additionalRACH-ConfigList-r17
         │                          │  └─ setup
         │                          │     └─ _item_
         │                          │        ├─ msgA-ConfigCommon-r17
         │                          │        │  └─ rach-ConfigCommonTwoStepRA-r16
         │                          │        │     └─ featureCombinationPreamblesList-r17
         │                          │        │        └─ _item_
         │                          │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
         │                          │        └─ rach-ConfigCommon-r17
         │                          │           └─ featureCombinationPreamblesList-r17
         │                          │              └─ _item_
         │                          │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
         │                          ├─ msgA-ConfigCommon-r16
         │                          │  └─ setup
         │                          │     └─ rach-ConfigCommonTwoStepRA-r16
         │                          │        └─ featureCombinationPreamblesList-r17
         │                          │           └─ _item_
         │                          │              └─ msg1-RepetitionTimeOffsetROGroup-r18
         │                          ├─ rach-ConfigCommon
         │                          │  └─ setup
         │                          │     └─ featureCombinationPreamblesList-r17
         │                          │        └─ _item_
         │                          │           └─ msg1-RepetitionTimeOffsetROGroup-r18
         │                          └─ rach-ConfigCommonIAB-r16
         │                             └─ setup
         │                                └─ featureCombinationPreamblesList-r17
         │                                   └─ _item_
         │                                      └─ msg1-RepetitionTimeOffsetROGroup-r18
         └─ secondaryCellGroup
            └─ CellGroupConfig
               ├─ sCellToAddModList
               │  └─ _item_
               │     ├─ sCellConfigCommon
               │     │  ├─ supplementaryUplinkConfig
               │     │  │  └─ initialUplinkBWP
               │     │  │     ├─ additionalRACH-ConfigList-r17
               │     │  │     │  └─ setup
               │     │  │     │     └─ _item_
               │     │  │     │        ├─ msgA-ConfigCommon-r17
               │     │  │     │        │  └─ rach-ConfigCommonTwoStepRA-r16
               │     │  │     │        │     └─ featureCombinationPreamblesList-r17
               │     │  │     │        │        └─ _item_
               │     │  │     │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
               │     │  │     │        └─ rach-ConfigCommon-r17
               │     │  │     │           └─ featureCombinationPreamblesList-r17
               │     │  │     │              └─ _item_
               │     │  │     │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
               │     │  │     ├─ msgA-ConfigCommon-r16
               │     │  │     │  └─ setup
               │     │  │     │     └─ rach-ConfigCommonTwoStepRA-r16
               │     │  │     │        └─ featureCombinationPreamblesList-r17
               │     │  │     │           └─ _item_
               │     │  │     │              └─ msg1-RepetitionTimeOffsetROGroup-r18
               │     │  │     ├─ rach-ConfigCommon
               │     │  │     │  └─ setup
               │     │  │     │     └─ featureCombinationPreamblesList-r17
               │     │  │     │        └─ _item_
               │     │  │     │           └─ msg1-RepetitionTimeOffsetROGroup-r18
               │     │  │     └─ rach-ConfigCommonIAB-r16
               │     │  │        └─ setup
               │     │  │           └─ featureCombinationPreamblesList-r17
               │     │  │              └─ _item_
               │     │  │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
               │     │  ├─ uplinkConfigCommon
               │     │  │  └─ initialUplinkBWP
               │     │  │     ├─ additionalRACH-ConfigList-r17
               │     │  │     │  └─ setup
               │     │  │     │     └─ _item_
               │     │  │     │        ├─ msgA-ConfigCommon-r17
               │     │  │     │        │  └─ rach-ConfigCommonTwoStepRA-r16
               │     │  │     │        │     └─ featureCombinationPreamblesList-r17
               │     │  │     │        │        └─ _item_
               │     │  │     │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
               │     │  │     │        └─ rach-ConfigCommon-r17
               │     │  │     │           └─ featureCombinationPreamblesList-r17
               │     │  │     │              └─ _item_
               │     │  │     │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
               │     │  │     ├─ msgA-ConfigCommon-r16
               │     │  │     │  └─ setup
               │     │  │     │     └─ rach-ConfigCommonTwoStepRA-r16
               │     │  │     │        └─ featureCombinationPreamblesList-r17
               │     │  │     │           └─ _item_
               │     │  │     │              └─ msg1-RepetitionTimeOffsetROGroup-r18
               │     │  │     ├─ rach-ConfigCommon
               │     │  │     │  └─ setup
               │     │  │     │     └─ featureCombinationPreamblesList-r17
               │     │  │     │        └─ _item_
               │     │  │     │           └─ msg1-RepetitionTimeOffsetROGroup-r18
               │     │  │     └─ rach-ConfigCommonIAB-r16
               │     │  │        └─ setup
               │     │  │           └─ featureCombinationPreamblesList-r17
               │     │  │              └─ _item_
               │     │  │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
               │     │  └─ uplinkConfigCommon-v1700
               │     │     └─ initialUplinkBWP-RedCap-r17
               │     │        ├─ additionalRACH-ConfigList-r17
               │     │        │  └─ setup
               │     │        │     └─ _item_
               │     │        │        ├─ msgA-ConfigCommon-r17
               │     │        │        │  └─ rach-ConfigCommonTwoStepRA-r16
               │     │        │        │     └─ featureCombinationPreamblesList-r17
               │     │        │        │        └─ _item_
               │     │        │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
               │     │        │        └─ rach-ConfigCommon-r17
               │     │        │           └─ featureCombinationPreamblesList-r17
               │     │        │              └─ _item_
               │     │        │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
               │     │        ├─ msgA-ConfigCommon-r16
               │     │        │  └─ setup
               │     │        │     └─ rach-ConfigCommonTwoStepRA-r16
               │     │        │        └─ featureCombinationPreamblesList-r17
               │     │        │           └─ _item_
               │     │        │              └─ msg1-RepetitionTimeOffsetROGroup-r18
               │     │        ├─ rach-ConfigCommon
               │     │        │  └─ setup
               │     │        │     └─ featureCombinationPreamblesList-r17
               │     │        │        └─ _item_
               │     │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
               │     │        └─ rach-ConfigCommonIAB-r16
               │     │           └─ setup
               │     │              └─ featureCombinationPreamblesList-r17
               │     │                 └─ _item_
               │     │                    └─ msg1-RepetitionTimeOffsetROGroup-r18
               │     └─ sCellConfigDedicated
               │        ├─ supplementaryUplink
               │        │  └─ uplinkBWP-ToAddModList
               │        │     └─ _item_
               │        │        └─ bwp-Common
               │        │           ├─ additionalRACH-ConfigList-r17
               │        │           │  └─ setup
               │        │           │     └─ _item_
               │        │           │        ├─ msgA-ConfigCommon-r17
               │        │           │        │  └─ rach-ConfigCommonTwoStepRA-r16
               │        │           │        │     └─ featureCombinationPreamblesList-r17
               │        │           │        │        └─ _item_
               │        │           │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
               │        │           │        └─ rach-ConfigCommon-r17
               │        │           │           └─ featureCombinationPreamblesList-r17
               │        │           │              └─ _item_
               │        │           │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
               │        │           ├─ msgA-ConfigCommon-r16
               │        │           │  └─ setup
               │        │           │     └─ rach-ConfigCommonTwoStepRA-r16
               │        │           │        └─ featureCombinationPreamblesList-r17
               │        │           │           └─ _item_
               │        │           │              └─ msg1-RepetitionTimeOffsetROGroup-r18
               │        │           ├─ rach-ConfigCommon
               │        │           │  └─ setup
               │        │           │     └─ featureCombinationPreamblesList-r17
               │        │           │        └─ _item_
               │        │           │           └─ msg1-RepetitionTimeOffsetROGroup-r18
               │        │           └─ rach-ConfigCommonIAB-r16
               │        │              └─ setup
               │        │                 └─ featureCombinationPreamblesList-r17
               │        │                    └─ _item_
               │        │                       └─ msg1-RepetitionTimeOffsetROGroup-r18
               │        └─ uplinkConfig
               │           └─ uplinkBWP-ToAddModList
               │              └─ _item_
               │                 └─ bwp-Common
               │                    ├─ additionalRACH-ConfigList-r17
               │                    │  └─ setup
               │                    │     └─ _item_
               │                    │        ├─ msgA-ConfigCommon-r17
               │                    │        │  └─ rach-ConfigCommonTwoStepRA-r16
               │                    │        │     └─ featureCombinationPreamblesList-r17
               │                    │        │        └─ _item_
               │                    │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
               │                    │        └─ rach-ConfigCommon-r17
               │                    │           └─ featureCombinationPreamblesList-r17
               │                    │              └─ _item_
               │                    │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
               │                    ├─ msgA-ConfigCommon-r16
               │                    │  └─ setup
               │                    │     └─ rach-ConfigCommonTwoStepRA-r16
               │                    │        └─ featureCombinationPreamblesList-r17
               │                    │           └─ _item_
               │                    │              └─ msg1-RepetitionTimeOffsetROGroup-r18
               │                    ├─ rach-ConfigCommon
               │                    │  └─ setup
               │                    │     └─ featureCombinationPreamblesList-r17
               │                    │        └─ _item_
               │                    │           └─ msg1-RepetitionTimeOffsetROGroup-r18
               │                    └─ rach-ConfigCommonIAB-r16
               │                       └─ setup
               │                          └─ featureCombinationPreamblesList-r17
               │                             └─ _item_
               │                                └─ msg1-RepetitionTimeOffsetROGroup-r18
               └─ spCellConfig
                  ├─ reconfigurationWithSync
                  │  └─ spCellConfigCommon
                  │     ├─ supplementaryUplinkConfig
                  │     │  └─ initialUplinkBWP
                  │     │     ├─ additionalRACH-ConfigList-r17
                  │     │     │  └─ setup
                  │     │     │     └─ _item_
                  │     │     │        ├─ msgA-ConfigCommon-r17
                  │     │     │        │  └─ rach-ConfigCommonTwoStepRA-r16
                  │     │     │        │     └─ featureCombinationPreamblesList-r17
                  │     │     │        │        └─ _item_
                  │     │     │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                  │     │     │        └─ rach-ConfigCommon-r17
                  │     │     │           └─ featureCombinationPreamblesList-r17
                  │     │     │              └─ _item_
                  │     │     │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
                  │     │     ├─ msgA-ConfigCommon-r16
                  │     │     │  └─ setup
                  │     │     │     └─ rach-ConfigCommonTwoStepRA-r16
                  │     │     │        └─ featureCombinationPreamblesList-r17
                  │     │     │           └─ _item_
                  │     │     │              └─ msg1-RepetitionTimeOffsetROGroup-r18
                  │     │     ├─ rach-ConfigCommon
                  │     │     │  └─ setup
                  │     │     │     └─ featureCombinationPreamblesList-r17
                  │     │     │        └─ _item_
                  │     │     │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                  │     │     └─ rach-ConfigCommonIAB-r16
                  │     │        └─ setup
                  │     │           └─ featureCombinationPreamblesList-r17
                  │     │              └─ _item_
                  │     │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
                  │     ├─ uplinkConfigCommon
                  │     │  └─ initialUplinkBWP
                  │     │     ├─ additionalRACH-ConfigList-r17
                  │     │     │  └─ setup
                  │     │     │     └─ _item_
                  │     │     │        ├─ msgA-ConfigCommon-r17
                  │     │     │        │  └─ rach-ConfigCommonTwoStepRA-r16
                  │     │     │        │     └─ featureCombinationPreamblesList-r17
                  │     │     │        │        └─ _item_
                  │     │     │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                  │     │     │        └─ rach-ConfigCommon-r17
                  │     │     │           └─ featureCombinationPreamblesList-r17
                  │     │     │              └─ _item_
                  │     │     │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
                  │     │     ├─ msgA-ConfigCommon-r16
                  │     │     │  └─ setup
                  │     │     │     └─ rach-ConfigCommonTwoStepRA-r16
                  │     │     │        └─ featureCombinationPreamblesList-r17
                  │     │     │           └─ _item_
                  │     │     │              └─ msg1-RepetitionTimeOffsetROGroup-r18
                  │     │     ├─ rach-ConfigCommon
                  │     │     │  └─ setup
                  │     │     │     └─ featureCombinationPreamblesList-r17
                  │     │     │        └─ _item_
                  │     │     │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                  │     │     └─ rach-ConfigCommonIAB-r16
                  │     │        └─ setup
                  │     │           └─ featureCombinationPreamblesList-r17
                  │     │              └─ _item_
                  │     │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
                  │     └─ uplinkConfigCommon-v1700
                  │        └─ initialUplinkBWP-RedCap-r17
                  │           ├─ additionalRACH-ConfigList-r17
                  │           │  └─ setup
                  │           │     └─ _item_
                  │           │        ├─ msgA-ConfigCommon-r17
                  │           │        │  └─ rach-ConfigCommonTwoStepRA-r16
                  │           │        │     └─ featureCombinationPreamblesList-r17
                  │           │        │        └─ _item_
                  │           │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                  │           │        └─ rach-ConfigCommon-r17
                  │           │           └─ featureCombinationPreamblesList-r17
                  │           │              └─ _item_
                  │           │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
                  │           ├─ msgA-ConfigCommon-r16
                  │           │  └─ setup
                  │           │     └─ rach-ConfigCommonTwoStepRA-r16
                  │           │        └─ featureCombinationPreamblesList-r17
                  │           │           └─ _item_
                  │           │              └─ msg1-RepetitionTimeOffsetROGroup-r18
                  │           ├─ rach-ConfigCommon
                  │           │  └─ setup
                  │           │     └─ featureCombinationPreamblesList-r17
                  │           │        └─ _item_
                  │           │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                  │           └─ rach-ConfigCommonIAB-r16
                  │              └─ setup
                  │                 └─ featureCombinationPreamblesList-r17
                  │                    └─ _item_
                  │                       └─ msg1-RepetitionTimeOffsetROGroup-r18
                  └─ spCellConfigDedicated
                     ├─ supplementaryUplink
                     │  └─ uplinkBWP-ToAddModList
                     │     └─ _item_
                     │        └─ bwp-Common
                     │           ├─ additionalRACH-ConfigList-r17
                     │           │  └─ setup
                     │           │     └─ _item_
                     │           │        ├─ msgA-ConfigCommon-r17
                     │           │        │  └─ rach-ConfigCommonTwoStepRA-r16
                     │           │        │     └─ featureCombinationPreamblesList-r17
                     │           │        │        └─ _item_
                     │           │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                     │           │        └─ rach-ConfigCommon-r17
                     │           │           └─ featureCombinationPreamblesList-r17
                     │           │              └─ _item_
                     │           │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
                     │           ├─ msgA-ConfigCommon-r16
                     │           │  └─ setup
                     │           │     └─ rach-ConfigCommonTwoStepRA-r16
                     │           │        └─ featureCombinationPreamblesList-r17
                     │           │           └─ _item_
                     │           │              └─ msg1-RepetitionTimeOffsetROGroup-r18
                     │           ├─ rach-ConfigCommon
                     │           │  └─ setup
                     │           │     └─ featureCombinationPreamblesList-r17
                     │           │        └─ _item_
                     │           │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                     │           └─ rach-ConfigCommonIAB-r16
                     │              └─ setup
                     │                 └─ featureCombinationPreamblesList-r17
                     │                    └─ _item_
                     │                       └─ msg1-RepetitionTimeOffsetROGroup-r18
                     └─ uplinkConfig
                        └─ uplinkBWP-ToAddModList
                           └─ _item_
                              └─ bwp-Common
                                 ├─ additionalRACH-ConfigList-r17
                                 │  └─ setup
                                 │     └─ _item_
                                 │        ├─ msgA-ConfigCommon-r17
                                 │        │  └─ rach-ConfigCommonTwoStepRA-r16
                                 │        │     └─ featureCombinationPreamblesList-r17
                                 │        │        └─ _item_
                                 │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                                 │        └─ rach-ConfigCommon-r17
                                 │           └─ featureCombinationPreamblesList-r17
                                 │              └─ _item_
                                 │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
                                 ├─ msgA-ConfigCommon-r16
                                 │  └─ setup
                                 │     └─ rach-ConfigCommonTwoStepRA-r16
                                 │        └─ featureCombinationPreamblesList-r17
                                 │           └─ _item_
                                 │              └─ msg1-RepetitionTimeOffsetROGroup-r18
                                 ├─ rach-ConfigCommon
                                 │  └─ setup
                                 │     └─ featureCombinationPreamblesList-r17
                                 │        └─ _item_
                                 │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                                 └─ rach-ConfigCommonIAB-r16
                                    └─ setup
                                       └─ featureCombinationPreamblesList-r17
                                          └─ _item_
                                             └─ msg1-RepetitionTimeOffsetROGroup-r18

└─ RRCResume/RRCReconfiguration
   └─ criticalExtensions
      └─ rrcResume
         ├─ masterCellGroup
         │  └─ CellGroupConfig
         │     ├─ sCellToAddModList
         │     │  └─ _item_
         │     │     ├─ sCellConfigCommon
         │     │     │  ├─ supplementaryUplinkConfig
         │     │     │  │  └─ initialUplinkBWP
         │     │     │  │     ├─ additionalRACH-ConfigList-r17
         │     │     │  │     │  └─ setup
         │     │     │  │     │     └─ _item_
         │     │     │  │     │        ├─ msgA-ConfigCommon-r17
         │     │     │  │     │        │  └─ rach-ConfigCommonTwoStepRA-r16
         │     │     │  │     │        │     └─ featureCombinationPreamblesList-r17
         │     │     │  │     │        │        └─ _item_
         │     │     │  │     │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
         │     │     │  │     │        └─ rach-ConfigCommon-r17
         │     │     │  │     │           └─ featureCombinationPreamblesList-r17
         │     │     │  │     │              └─ _item_
         │     │     │  │     │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
         │     │     │  │     ├─ msgA-ConfigCommon-r16
         │     │     │  │     │  └─ setup
         │     │     │  │     │     └─ rach-ConfigCommonTwoStepRA-r16
         │     │     │  │     │        └─ featureCombinationPreamblesList-r17
         │     │     │  │     │           └─ _item_
         │     │     │  │     │              └─ msg1-RepetitionTimeOffsetROGroup-r18
         │     │     │  │     ├─ rach-ConfigCommon
         │     │     │  │     │  └─ setup
         │     │     │  │     │     └─ featureCombinationPreamblesList-r17
         │     │     │  │     │        └─ _item_
         │     │     │  │     │           └─ msg1-RepetitionTimeOffsetROGroup-r18
         │     │     │  │     └─ rach-ConfigCommonIAB-r16
         │     │     │  │        └─ setup
         │     │     │  │           └─ featureCombinationPreamblesList-r17
         │     │     │  │              └─ _item_
         │     │     │  │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
         │     │     │  ├─ uplinkConfigCommon
         │     │     │  │  └─ initialUplinkBWP
         │     │     │  │     ├─ additionalRACH-ConfigList-r17
         │     │     │  │     │  └─ setup
         │     │     │  │     │     └─ _item_
         │     │     │  │     │        ├─ msgA-ConfigCommon-r17
         │     │     │  │     │        │  └─ rach-ConfigCommonTwoStepRA-r16
         │     │     │  │     │        │     └─ featureCombinationPreamblesList-r17
         │     │     │  │     │        │        └─ _item_
         │     │     │  │     │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
         │     │     │  │     │        └─ rach-ConfigCommon-r17
         │     │     │  │     │           └─ featureCombinationPreamblesList-r17
         │     │     │  │     │              └─ _item_
         │     │     │  │     │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
         │     │     │  │     ├─ msgA-ConfigCommon-r16
         │     │     │  │     │  └─ setup
         │     │     │  │     │     └─ rach-ConfigCommonTwoStepRA-r16
         │     │     │  │     │        └─ featureCombinationPreamblesList-r17
         │     │     │  │     │           └─ _item_
         │     │     │  │     │              └─ msg1-RepetitionTimeOffsetROGroup-r18
         │     │     │  │     ├─ rach-ConfigCommon
         │     │     │  │     │  └─ setup
         │     │     │  │     │     └─ featureCombinationPreamblesList-r17
         │     │     │  │     │        └─ _item_
         │     │     │  │     │           └─ msg1-RepetitionTimeOffsetROGroup-r18
         │     │     │  │     └─ rach-ConfigCommonIAB-r16
         │     │     │  │        └─ setup
         │     │     │  │           └─ featureCombinationPreamblesList-r17
         │     │     │  │              └─ _item_
         │     │     │  │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
         │     │     │  └─ uplinkConfigCommon-v1700
         │     │     │     └─ initialUplinkBWP-RedCap-r17
         │     │     │        ├─ additionalRACH-ConfigList-r17
         │     │     │        │  └─ setup
         │     │     │        │     └─ _item_
         │     │     │        │        ├─ msgA-ConfigCommon-r17
         │     │     │        │        │  └─ rach-ConfigCommonTwoStepRA-r16
         │     │     │        │        │     └─ featureCombinationPreamblesList-r17
         │     │     │        │        │        └─ _item_
         │     │     │        │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
         │     │     │        │        └─ rach-ConfigCommon-r17
         │     │     │        │           └─ featureCombinationPreamblesList-r17
         │     │     │        │              └─ _item_
         │     │     │        │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
         │     │     │        ├─ msgA-ConfigCommon-r16
         │     │     │        │  └─ setup
         │     │     │        │     └─ rach-ConfigCommonTwoStepRA-r16
         │     │     │        │        └─ featureCombinationPreamblesList-r17
         │     │     │        │           └─ _item_
         │     │     │        │              └─ msg1-RepetitionTimeOffsetROGroup-r18
         │     │     │        ├─ rach-ConfigCommon
         │     │     │        │  └─ setup
         │     │     │        │     └─ featureCombinationPreamblesList-r17
         │     │     │        │        └─ _item_
         │     │     │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
         │     │     │        └─ rach-ConfigCommonIAB-r16
         │     │     │           └─ setup
         │     │     │              └─ featureCombinationPreamblesList-r17
         │     │     │                 └─ _item_
         │     │     │                    └─ msg1-RepetitionTimeOffsetROGroup-r18
         │     │     └─ sCellConfigDedicated
         │     │        ├─ supplementaryUplink
         │     │        │  └─ uplinkBWP-ToAddModList
         │     │        │     └─ _item_
         │     │        │        └─ bwp-Common
         │     │        │           ├─ additionalRACH-ConfigList-r17
         │     │        │           │  └─ setup
         │     │        │           │     └─ _item_
         │     │        │           │        ├─ msgA-ConfigCommon-r17
         │     │        │           │        │  └─ rach-ConfigCommonTwoStepRA-r16
         │     │        │           │        │     └─ featureCombinationPreamblesList-r17
         │     │        │           │        │        └─ _item_
         │     │        │           │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
         │     │        │           │        └─ rach-ConfigCommon-r17
         │     │        │           │           └─ featureCombinationPreamblesList-r17
         │     │        │           │              └─ _item_
         │     │        │           │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
         │     │        │           ├─ msgA-ConfigCommon-r16
         │     │        │           │  └─ setup
         │     │        │           │     └─ rach-ConfigCommonTwoStepRA-r16
         │     │        │           │        └─ featureCombinationPreamblesList-r17
         │     │        │           │           └─ _item_
         │     │        │           │              └─ msg1-RepetitionTimeOffsetROGroup-r18
         │     │        │           ├─ rach-ConfigCommon
         │     │        │           │  └─ setup
         │     │        │           │     └─ featureCombinationPreamblesList-r17
         │     │        │           │        └─ _item_
         │     │        │           │           └─ msg1-RepetitionTimeOffsetROGroup-r18
         │     │        │           └─ rach-ConfigCommonIAB-r16
         │     │        │              └─ setup
         │     │        │                 └─ featureCombinationPreamblesList-r17
         │     │        │                    └─ _item_
         │     │        │                       └─ msg1-RepetitionTimeOffsetROGroup-r18
         │     │        └─ uplinkConfig
         │     │           └─ uplinkBWP-ToAddModList
         │     │              └─ _item_
         │     │                 └─ bwp-Common
         │     │                    ├─ additionalRACH-ConfigList-r17
         │     │                    │  └─ setup
         │     │                    │     └─ _item_
         │     │                    │        ├─ msgA-ConfigCommon-r17
         │     │                    │        │  └─ rach-ConfigCommonTwoStepRA-r16
         │     │                    │        │     └─ featureCombinationPreamblesList-r17
         │     │                    │        │        └─ _item_
         │     │                    │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
         │     │                    │        └─ rach-ConfigCommon-r17
         │     │                    │           └─ featureCombinationPreamblesList-r17
         │     │                    │              └─ _item_
         │     │                    │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
         │     │                    ├─ msgA-ConfigCommon-r16
         │     │                    │  └─ setup
         │     │                    │     └─ rach-ConfigCommonTwoStepRA-r16
         │     │                    │        └─ featureCombinationPreamblesList-r17
         │     │                    │           └─ _item_
         │     │                    │              └─ msg1-RepetitionTimeOffsetROGroup-r18
         │     │                    ├─ rach-ConfigCommon
         │     │                    │  └─ setup
         │     │                    │     └─ featureCombinationPreamblesList-r17
         │     │                    │        └─ _item_
         │     │                    │           └─ msg1-RepetitionTimeOffsetROGroup-r18
         │     │                    └─ rach-ConfigCommonIAB-r16
         │     │                       └─ setup
         │     │                          └─ featureCombinationPreamblesList-r17
         │     │                             └─ _item_
         │     │                                └─ msg1-RepetitionTimeOffsetROGroup-r18
         │     └─ spCellConfig
         │        ├─ reconfigurationWithSync
         │        │  └─ spCellConfigCommon
         │        │     ├─ supplementaryUplinkConfig
         │        │     │  └─ initialUplinkBWP
         │        │     │     ├─ additionalRACH-ConfigList-r17
         │        │     │     │  └─ setup
         │        │     │     │     └─ _item_
         │        │     │     │        ├─ msgA-ConfigCommon-r17
         │        │     │     │        │  └─ rach-ConfigCommonTwoStepRA-r16
         │        │     │     │        │     └─ featureCombinationPreamblesList-r17
         │        │     │     │        │        └─ _item_
         │        │     │     │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
         │        │     │     │        └─ rach-ConfigCommon-r17
         │        │     │     │           └─ featureCombinationPreamblesList-r17
         │        │     │     │              └─ _item_
         │        │     │     │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
         │        │     │     ├─ msgA-ConfigCommon-r16
         │        │     │     │  └─ setup
         │        │     │     │     └─ rach-ConfigCommonTwoStepRA-r16
         │        │     │     │        └─ featureCombinationPreamblesList-r17
         │        │     │     │           └─ _item_
         │        │     │     │              └─ msg1-RepetitionTimeOffsetROGroup-r18
         │        │     │     ├─ rach-ConfigCommon
         │        │     │     │  └─ setup
         │        │     │     │     └─ featureCombinationPreamblesList-r17
         │        │     │     │        └─ _item_
         │        │     │     │           └─ msg1-RepetitionTimeOffsetROGroup-r18
         │        │     │     └─ rach-ConfigCommonIAB-r16
         │        │     │        └─ setup
         │        │     │           └─ featureCombinationPreamblesList-r17
         │        │     │              └─ _item_
         │        │     │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
         │        │     ├─ uplinkConfigCommon
         │        │     │  └─ initialUplinkBWP
         │        │     │     ├─ additionalRACH-ConfigList-r17
         │        │     │     │  └─ setup
         │        │     │     │     └─ _item_
         │        │     │     │        ├─ msgA-ConfigCommon-r17
         │        │     │     │        │  └─ rach-ConfigCommonTwoStepRA-r16
         │        │     │     │        │     └─ featureCombinationPreamblesList-r17
         │        │     │     │        │        └─ _item_
         │        │     │     │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
         │        │     │     │        └─ rach-ConfigCommon-r17
         │        │     │     │           └─ featureCombinationPreamblesList-r17
         │        │     │     │              └─ _item_
         │        │     │     │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
         │        │     │     ├─ msgA-ConfigCommon-r16
         │        │     │     │  └─ setup
         │        │     │     │     └─ rach-ConfigCommonTwoStepRA-r16
         │        │     │     │        └─ featureCombinationPreamblesList-r17
         │        │     │     │           └─ _item_
         │        │     │     │              └─ msg1-RepetitionTimeOffsetROGroup-r18
         │        │     │     ├─ rach-ConfigCommon
         │        │     │     │  └─ setup
         │        │     │     │     └─ featureCombinationPreamblesList-r17
         │        │     │     │        └─ _item_
         │        │     │     │           └─ msg1-RepetitionTimeOffsetROGroup-r18
         │        │     │     └─ rach-ConfigCommonIAB-r16
         │        │     │        └─ setup
         │        │     │           └─ featureCombinationPreamblesList-r17
         │        │     │              └─ _item_
         │        │     │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
         │        │     └─ uplinkConfigCommon-v1700
         │        │        └─ initialUplinkBWP-RedCap-r17
         │        │           ├─ additionalRACH-ConfigList-r17
         │        │           │  └─ setup
         │        │           │     └─ _item_
         │        │           │        ├─ msgA-ConfigCommon-r17
         │        │           │        │  └─ rach-ConfigCommonTwoStepRA-r16
         │        │           │        │     └─ featureCombinationPreamblesList-r17
         │        │           │        │        └─ _item_
         │        │           │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
         │        │           │        └─ rach-ConfigCommon-r17
         │        │           │           └─ featureCombinationPreamblesList-r17
         │        │           │              └─ _item_
         │        │           │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
         │        │           ├─ msgA-ConfigCommon-r16
         │        │           │  └─ setup
         │        │           │     └─ rach-ConfigCommonTwoStepRA-r16
         │        │           │        └─ featureCombinationPreamblesList-r17
         │        │           │           └─ _item_
         │        │           │              └─ msg1-RepetitionTimeOffsetROGroup-r18
         │        │           ├─ rach-ConfigCommon
         │        │           │  └─ setup
         │        │           │     └─ featureCombinationPreamblesList-r17
         │        │           │        └─ _item_
         │        │           │           └─ msg1-RepetitionTimeOffsetROGroup-r18
         │        │           └─ rach-ConfigCommonIAB-r16
         │        │              └─ setup
         │        │                 └─ featureCombinationPreamblesList-r17
         │        │                    └─ _item_
         │        │                       └─ msg1-RepetitionTimeOffsetROGroup-r18
         │        └─ spCellConfigDedicated
         │           ├─ supplementaryUplink
         │           │  └─ uplinkBWP-ToAddModList
         │           │     └─ _item_
         │           │        └─ bwp-Common
         │           │           ├─ additionalRACH-ConfigList-r17
         │           │           │  └─ setup
         │           │           │     └─ _item_
         │           │           │        ├─ msgA-ConfigCommon-r17
         │           │           │        │  └─ rach-ConfigCommonTwoStepRA-r16
         │           │           │        │     └─ featureCombinationPreamblesList-r17
         │           │           │        │        └─ _item_
         │           │           │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
         │           │           │        └─ rach-ConfigCommon-r17
         │           │           │           └─ featureCombinationPreamblesList-r17
         │           │           │              └─ _item_
         │           │           │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
         │           │           ├─ msgA-ConfigCommon-r16
         │           │           │  └─ setup
         │           │           │     └─ rach-ConfigCommonTwoStepRA-r16
         │           │           │        └─ featureCombinationPreamblesList-r17
         │           │           │           └─ _item_
         │           │           │              └─ msg1-RepetitionTimeOffsetROGroup-r18
         │           │           ├─ rach-ConfigCommon
         │           │           │  └─ setup
         │           │           │     └─ featureCombinationPreamblesList-r17
         │           │           │        └─ _item_
         │           │           │           └─ msg1-RepetitionTimeOffsetROGroup-r18
         │           │           └─ rach-ConfigCommonIAB-r16
         │           │              └─ setup
         │           │                 └─ featureCombinationPreamblesList-r17
         │           │                    └─ _item_
         │           │                       └─ msg1-RepetitionTimeOffsetROGroup-r18
         │           └─ uplinkConfig
         │              └─ uplinkBWP-ToAddModList
         │                 └─ _item_
         │                    └─ bwp-Common
         │                       ├─ additionalRACH-ConfigList-r17
         │                       │  └─ setup
         │                       │     └─ _item_
         │                       │        ├─ msgA-ConfigCommon-r17
         │                       │        │  └─ rach-ConfigCommonTwoStepRA-r16
         │                       │        │     └─ featureCombinationPreamblesList-r17
         │                       │        │        └─ _item_
         │                       │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
         │                       │        └─ rach-ConfigCommon-r17
         │                       │           └─ featureCombinationPreamblesList-r17
         │                       │              └─ _item_
         │                       │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
         │                       ├─ msgA-ConfigCommon-r16
         │                       │  └─ setup
         │                       │     └─ rach-ConfigCommonTwoStepRA-r16
         │                       │        └─ featureCombinationPreamblesList-r17
         │                       │           └─ _item_
         │                       │              └─ msg1-RepetitionTimeOffsetROGroup-r18
         │                       ├─ rach-ConfigCommon
         │                       │  └─ setup
         │                       │     └─ featureCombinationPreamblesList-r17
         │                       │        └─ _item_
         │                       │           └─ msg1-RepetitionTimeOffsetROGroup-r18
         │                       └─ rach-ConfigCommonIAB-r16
         │                          └─ setup
         │                             └─ featureCombinationPreamblesList-r17
         │                                └─ _item_
         │                                   └─ msg1-RepetitionTimeOffsetROGroup-r18
         └─ nonCriticalExtension
            └─ nonCriticalExtension
               └─ mrdc-SecondaryCellGroup-r16
                  └─ nr-SCG-r16
                     └─ RRCReconfiguration
                        └─ criticalExtensions
                           └─ rrcReconfiguration
                              ├─ nonCriticalExtension
                              │  ├─ dedicatedSIB1-Delivery
                              │  │  └─ SIB1
                              │  │     └─ servingCellConfigCommon
                              │  │        ├─ supplementaryUplink
                              │  │        │  └─ initialUplinkBWP
                              │  │        │     ├─ additionalRACH-ConfigList-r17
                              │  │        │     │  └─ setup
                              │  │        │     │     └─ _item_
                              │  │        │     │        ├─ msgA-ConfigCommon-r17
                              │  │        │     │        │  └─ rach-ConfigCommonTwoStepRA-r16
                              │  │        │     │        │     └─ featureCombinationPreamblesList-r17
                              │  │        │     │        │        └─ _item_
                              │  │        │     │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │  │        │     │        └─ rach-ConfigCommon-r17
                              │  │        │     │           └─ featureCombinationPreamblesList-r17
                              │  │        │     │              └─ _item_
                              │  │        │     │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │  │        │     ├─ msgA-ConfigCommon-r16
                              │  │        │     │  └─ setup
                              │  │        │     │     └─ rach-ConfigCommonTwoStepRA-r16
                              │  │        │     │        └─ featureCombinationPreamblesList-r17
                              │  │        │     │           └─ _item_
                              │  │        │     │              └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │  │        │     ├─ rach-ConfigCommon
                              │  │        │     │  └─ setup
                              │  │        │     │     └─ featureCombinationPreamblesList-r17
                              │  │        │     │        └─ _item_
                              │  │        │     │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │  │        │     └─ rach-ConfigCommonIAB-r16
                              │  │        │        └─ setup
                              │  │        │           └─ featureCombinationPreamblesList-r17
                              │  │        │              └─ _item_
                              │  │        │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │  │        ├─ uplinkConfigCommon
                              │  │        │  └─ initialUplinkBWP
                              │  │        │     ├─ additionalRACH-ConfigList-r17
                              │  │        │     │  └─ setup
                              │  │        │     │     └─ _item_
                              │  │        │     │        ├─ msgA-ConfigCommon-r17
                              │  │        │     │        │  └─ rach-ConfigCommonTwoStepRA-r16
                              │  │        │     │        │     └─ featureCombinationPreamblesList-r17
                              │  │        │     │        │        └─ _item_
                              │  │        │     │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │  │        │     │        └─ rach-ConfigCommon-r17
                              │  │        │     │           └─ featureCombinationPreamblesList-r17
                              │  │        │     │              └─ _item_
                              │  │        │     │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │  │        │     ├─ msgA-ConfigCommon-r16
                              │  │        │     │  └─ setup
                              │  │        │     │     └─ rach-ConfigCommonTwoStepRA-r16
                              │  │        │     │        └─ featureCombinationPreamblesList-r17
                              │  │        │     │           └─ _item_
                              │  │        │     │              └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │  │        │     ├─ rach-ConfigCommon
                              │  │        │     │  └─ setup
                              │  │        │     │     └─ featureCombinationPreamblesList-r17
                              │  │        │     │        └─ _item_
                              │  │        │     │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │  │        │     └─ rach-ConfigCommonIAB-r16
                              │  │        │        └─ setup
                              │  │        │           └─ featureCombinationPreamblesList-r17
                              │  │        │              └─ _item_
                              │  │        │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │  │        └─ uplinkConfigCommon-v1700
                              │  │           └─ initialUplinkBWP-RedCap-r17
                              │  │              ├─ additionalRACH-ConfigList-r17
                              │  │              │  └─ setup
                              │  │              │     └─ _item_
                              │  │              │        ├─ msgA-ConfigCommon-r17
                              │  │              │        │  └─ rach-ConfigCommonTwoStepRA-r16
                              │  │              │        │     └─ featureCombinationPreamblesList-r17
                              │  │              │        │        └─ _item_
                              │  │              │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │  │              │        └─ rach-ConfigCommon-r17
                              │  │              │           └─ featureCombinationPreamblesList-r17
                              │  │              │              └─ _item_
                              │  │              │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │  │              ├─ msgA-ConfigCommon-r16
                              │  │              │  └─ setup
                              │  │              │     └─ rach-ConfigCommonTwoStepRA-r16
                              │  │              │        └─ featureCombinationPreamblesList-r17
                              │  │              │           └─ _item_
                              │  │              │              └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │  │              ├─ rach-ConfigCommon
                              │  │              │  └─ setup
                              │  │              │     └─ featureCombinationPreamblesList-r17
                              │  │              │        └─ _item_
                              │  │              │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │  │              └─ rach-ConfigCommonIAB-r16
                              │  │                 └─ setup
                              │  │                    └─ featureCombinationPreamblesList-r17
                              │  │                       └─ _item_
                              │  │                          └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │  └─ masterCellGroup
                              │     └─ CellGroupConfig
                              │        ├─ sCellToAddModList
                              │        │  └─ _item_
                              │        │     ├─ sCellConfigCommon
                              │        │     │  ├─ supplementaryUplinkConfig
                              │        │     │  │  └─ initialUplinkBWP
                              │        │     │  │     ├─ additionalRACH-ConfigList-r17
                              │        │     │  │     │  └─ setup
                              │        │     │  │     │     └─ _item_
                              │        │     │  │     │        ├─ msgA-ConfigCommon-r17
                              │        │     │  │     │        │  └─ rach-ConfigCommonTwoStepRA-r16
                              │        │     │  │     │        │     └─ featureCombinationPreamblesList-r17
                              │        │     │  │     │        │        └─ _item_
                              │        │     │  │     │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │        │     │  │     │        └─ rach-ConfigCommon-r17
                              │        │     │  │     │           └─ featureCombinationPreamblesList-r17
                              │        │     │  │     │              └─ _item_
                              │        │     │  │     │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │        │     │  │     ├─ msgA-ConfigCommon-r16
                              │        │     │  │     │  └─ setup
                              │        │     │  │     │     └─ rach-ConfigCommonTwoStepRA-r16
                              │        │     │  │     │        └─ featureCombinationPreamblesList-r17
                              │        │     │  │     │           └─ _item_
                              │        │     │  │     │              └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │        │     │  │     ├─ rach-ConfigCommon
                              │        │     │  │     │  └─ setup
                              │        │     │  │     │     └─ featureCombinationPreamblesList-r17
                              │        │     │  │     │        └─ _item_
                              │        │     │  │     │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │        │     │  │     └─ rach-ConfigCommonIAB-r16
                              │        │     │  │        └─ setup
                              │        │     │  │           └─ featureCombinationPreamblesList-r17
                              │        │     │  │              └─ _item_
                              │        │     │  │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │        │     │  ├─ uplinkConfigCommon
                              │        │     │  │  └─ initialUplinkBWP
                              │        │     │  │     ├─ additionalRACH-ConfigList-r17
                              │        │     │  │     │  └─ setup
                              │        │     │  │     │     └─ _item_
                              │        │     │  │     │        ├─ msgA-ConfigCommon-r17
                              │        │     │  │     │        │  └─ rach-ConfigCommonTwoStepRA-r16
                              │        │     │  │     │        │     └─ featureCombinationPreamblesList-r17
                              │        │     │  │     │        │        └─ _item_
                              │        │     │  │     │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │        │     │  │     │        └─ rach-ConfigCommon-r17
                              │        │     │  │     │           └─ featureCombinationPreamblesList-r17
                              │        │     │  │     │              └─ _item_
                              │        │     │  │     │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │        │     │  │     ├─ msgA-ConfigCommon-r16
                              │        │     │  │     │  └─ setup
                              │        │     │  │     │     └─ rach-ConfigCommonTwoStepRA-r16
                              │        │     │  │     │        └─ featureCombinationPreamblesList-r17
                              │        │     │  │     │           └─ _item_
                              │        │     │  │     │              └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │        │     │  │     ├─ rach-ConfigCommon
                              │        │     │  │     │  └─ setup
                              │        │     │  │     │     └─ featureCombinationPreamblesList-r17
                              │        │     │  │     │        └─ _item_
                              │        │     │  │     │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │        │     │  │     └─ rach-ConfigCommonIAB-r16
                              │        │     │  │        └─ setup
                              │        │     │  │           └─ featureCombinationPreamblesList-r17
                              │        │     │  │              └─ _item_
                              │        │     │  │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │        │     │  └─ uplinkConfigCommon-v1700
                              │        │     │     └─ initialUplinkBWP-RedCap-r17
                              │        │     │        ├─ additionalRACH-ConfigList-r17
                              │        │     │        │  └─ setup
                              │        │     │        │     └─ _item_
                              │        │     │        │        ├─ msgA-ConfigCommon-r17
                              │        │     │        │        │  └─ rach-ConfigCommonTwoStepRA-r16
                              │        │     │        │        │     └─ featureCombinationPreamblesList-r17
                              │        │     │        │        │        └─ _item_
                              │        │     │        │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │        │     │        │        └─ rach-ConfigCommon-r17
                              │        │     │        │           └─ featureCombinationPreamblesList-r17
                              │        │     │        │              └─ _item_
                              │        │     │        │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │        │     │        ├─ msgA-ConfigCommon-r16
                              │        │     │        │  └─ setup
                              │        │     │        │     └─ rach-ConfigCommonTwoStepRA-r16
                              │        │     │        │        └─ featureCombinationPreamblesList-r17
                              │        │     │        │           └─ _item_
                              │        │     │        │              └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │        │     │        ├─ rach-ConfigCommon
                              │        │     │        │  └─ setup
                              │        │     │        │     └─ featureCombinationPreamblesList-r17
                              │        │     │        │        └─ _item_
                              │        │     │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │        │     │        └─ rach-ConfigCommonIAB-r16
                              │        │     │           └─ setup
                              │        │     │              └─ featureCombinationPreamblesList-r17
                              │        │     │                 └─ _item_
                              │        │     │                    └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │        │     └─ sCellConfigDedicated
                              │        │        ├─ supplementaryUplink
                              │        │        │  └─ uplinkBWP-ToAddModList
                              │        │        │     └─ _item_
                              │        │        │        └─ bwp-Common
                              │        │        │           ├─ additionalRACH-ConfigList-r17
                              │        │        │           │  └─ setup
                              │        │        │           │     └─ _item_
                              │        │        │           │        ├─ msgA-ConfigCommon-r17
                              │        │        │           │        │  └─ rach-ConfigCommonTwoStepRA-r16
                              │        │        │           │        │     └─ featureCombinationPreamblesList-r17
                              │        │        │           │        │        └─ _item_
                              │        │        │           │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │        │        │           │        └─ rach-ConfigCommon-r17
                              │        │        │           │           └─ featureCombinationPreamblesList-r17
                              │        │        │           │              └─ _item_
                              │        │        │           │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │        │        │           ├─ msgA-ConfigCommon-r16
                              │        │        │           │  └─ setup
                              │        │        │           │     └─ rach-ConfigCommonTwoStepRA-r16
                              │        │        │           │        └─ featureCombinationPreamblesList-r17
                              │        │        │           │           └─ _item_
                              │        │        │           │              └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │        │        │           ├─ rach-ConfigCommon
                              │        │        │           │  └─ setup
                              │        │        │           │     └─ featureCombinationPreamblesList-r17
                              │        │        │           │        └─ _item_
                              │        │        │           │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │        │        │           └─ rach-ConfigCommonIAB-r16
                              │        │        │              └─ setup
                              │        │        │                 └─ featureCombinationPreamblesList-r17
                              │        │        │                    └─ _item_
                              │        │        │                       └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │        │        └─ uplinkConfig
                              │        │           └─ uplinkBWP-ToAddModList
                              │        │              └─ _item_
                              │        │                 └─ bwp-Common
                              │        │                    ├─ additionalRACH-ConfigList-r17
                              │        │                    │  └─ setup
                              │        │                    │     └─ _item_
                              │        │                    │        ├─ msgA-ConfigCommon-r17
                              │        │                    │        │  └─ rach-ConfigCommonTwoStepRA-r16
                              │        │                    │        │     └─ featureCombinationPreamblesList-r17
                              │        │                    │        │        └─ _item_
                              │        │                    │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │        │                    │        └─ rach-ConfigCommon-r17
                              │        │                    │           └─ featureCombinationPreamblesList-r17
                              │        │                    │              └─ _item_
                              │        │                    │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │        │                    ├─ msgA-ConfigCommon-r16
                              │        │                    │  └─ setup
                              │        │                    │     └─ rach-ConfigCommonTwoStepRA-r16
                              │        │                    │        └─ featureCombinationPreamblesList-r17
                              │        │                    │           └─ _item_
                              │        │                    │              └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │        │                    ├─ rach-ConfigCommon
                              │        │                    │  └─ setup
                              │        │                    │     └─ featureCombinationPreamblesList-r17
                              │        │                    │        └─ _item_
                              │        │                    │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │        │                    └─ rach-ConfigCommonIAB-r16
                              │        │                       └─ setup
                              │        │                          └─ featureCombinationPreamblesList-r17
                              │        │                             └─ _item_
                              │        │                                └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │        └─ spCellConfig
                              │           ├─ reconfigurationWithSync
                              │           │  └─ spCellConfigCommon
                              │           │     ├─ supplementaryUplinkConfig
                              │           │     │  └─ initialUplinkBWP
                              │           │     │     ├─ additionalRACH-ConfigList-r17
                              │           │     │     │  └─ setup
                              │           │     │     │     └─ _item_
                              │           │     │     │        ├─ msgA-ConfigCommon-r17
                              │           │     │     │        │  └─ rach-ConfigCommonTwoStepRA-r16
                              │           │     │     │        │     └─ featureCombinationPreamblesList-r17
                              │           │     │     │        │        └─ _item_
                              │           │     │     │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │           │     │     │        └─ rach-ConfigCommon-r17
                              │           │     │     │           └─ featureCombinationPreamblesList-r17
                              │           │     │     │              └─ _item_
                              │           │     │     │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │           │     │     ├─ msgA-ConfigCommon-r16
                              │           │     │     │  └─ setup
                              │           │     │     │     └─ rach-ConfigCommonTwoStepRA-r16
                              │           │     │     │        └─ featureCombinationPreamblesList-r17
                              │           │     │     │           └─ _item_
                              │           │     │     │              └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │           │     │     ├─ rach-ConfigCommon
                              │           │     │     │  └─ setup
                              │           │     │     │     └─ featureCombinationPreamblesList-r17
                              │           │     │     │        └─ _item_
                              │           │     │     │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │           │     │     └─ rach-ConfigCommonIAB-r16
                              │           │     │        └─ setup
                              │           │     │           └─ featureCombinationPreamblesList-r17
                              │           │     │              └─ _item_
                              │           │     │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │           │     ├─ uplinkConfigCommon
                              │           │     │  └─ initialUplinkBWP
                              │           │     │     ├─ additionalRACH-ConfigList-r17
                              │           │     │     │  └─ setup
                              │           │     │     │     └─ _item_
                              │           │     │     │        ├─ msgA-ConfigCommon-r17
                              │           │     │     │        │  └─ rach-ConfigCommonTwoStepRA-r16
                              │           │     │     │        │     └─ featureCombinationPreamblesList-r17
                              │           │     │     │        │        └─ _item_
                              │           │     │     │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │           │     │     │        └─ rach-ConfigCommon-r17
                              │           │     │     │           └─ featureCombinationPreamblesList-r17
                              │           │     │     │              └─ _item_
                              │           │     │     │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │           │     │     ├─ msgA-ConfigCommon-r16
                              │           │     │     │  └─ setup
                              │           │     │     │     └─ rach-ConfigCommonTwoStepRA-r16
                              │           │     │     │        └─ featureCombinationPreamblesList-r17
                              │           │     │     │           └─ _item_
                              │           │     │     │              └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │           │     │     ├─ rach-ConfigCommon
                              │           │     │     │  └─ setup
                              │           │     │     │     └─ featureCombinationPreamblesList-r17
                              │           │     │     │        └─ _item_
                              │           │     │     │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │           │     │     └─ rach-ConfigCommonIAB-r16
                              │           │     │        └─ setup
                              │           │     │           └─ featureCombinationPreamblesList-r17
                              │           │     │              └─ _item_
                              │           │     │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │           │     └─ uplinkConfigCommon-v1700
                              │           │        └─ initialUplinkBWP-RedCap-r17
                              │           │           ├─ additionalRACH-ConfigList-r17
                              │           │           │  └─ setup
                              │           │           │     └─ _item_
                              │           │           │        ├─ msgA-ConfigCommon-r17
                              │           │           │        │  └─ rach-ConfigCommonTwoStepRA-r16
                              │           │           │        │     └─ featureCombinationPreamblesList-r17
                              │           │           │        │        └─ _item_
                              │           │           │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │           │           │        └─ rach-ConfigCommon-r17
                              │           │           │           └─ featureCombinationPreamblesList-r17
                              │           │           │              └─ _item_
                              │           │           │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │           │           ├─ msgA-ConfigCommon-r16
                              │           │           │  └─ setup
                              │           │           │     └─ rach-ConfigCommonTwoStepRA-r16
                              │           │           │        └─ featureCombinationPreamblesList-r17
                              │           │           │           └─ _item_
                              │           │           │              └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │           │           ├─ rach-ConfigCommon
                              │           │           │  └─ setup
                              │           │           │     └─ featureCombinationPreamblesList-r17
                              │           │           │        └─ _item_
                              │           │           │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │           │           └─ rach-ConfigCommonIAB-r16
                              │           │              └─ setup
                              │           │                 └─ featureCombinationPreamblesList-r17
                              │           │                    └─ _item_
                              │           │                       └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │           └─ spCellConfigDedicated
                              │              ├─ supplementaryUplink
                              │              │  └─ uplinkBWP-ToAddModList
                              │              │     └─ _item_
                              │              │        └─ bwp-Common
                              │              │           ├─ additionalRACH-ConfigList-r17
                              │              │           │  └─ setup
                              │              │           │     └─ _item_
                              │              │           │        ├─ msgA-ConfigCommon-r17
                              │              │           │        │  └─ rach-ConfigCommonTwoStepRA-r16
                              │              │           │        │     └─ featureCombinationPreamblesList-r17
                              │              │           │        │        └─ _item_
                              │              │           │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │              │           │        └─ rach-ConfigCommon-r17
                              │              │           │           └─ featureCombinationPreamblesList-r17
                              │              │           │              └─ _item_
                              │              │           │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │              │           ├─ msgA-ConfigCommon-r16
                              │              │           │  └─ setup
                              │              │           │     └─ rach-ConfigCommonTwoStepRA-r16
                              │              │           │        └─ featureCombinationPreamblesList-r17
                              │              │           │           └─ _item_
                              │              │           │              └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │              │           ├─ rach-ConfigCommon
                              │              │           │  └─ setup
                              │              │           │     └─ featureCombinationPreamblesList-r17
                              │              │           │        └─ _item_
                              │              │           │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │              │           └─ rach-ConfigCommonIAB-r16
                              │              │              └─ setup
                              │              │                 └─ featureCombinationPreamblesList-r17
                              │              │                    └─ _item_
                              │              │                       └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │              └─ uplinkConfig
                              │                 └─ uplinkBWP-ToAddModList
                              │                    └─ _item_
                              │                       └─ bwp-Common
                              │                          ├─ additionalRACH-ConfigList-r17
                              │                          │  └─ setup
                              │                          │     └─ _item_
                              │                          │        ├─ msgA-ConfigCommon-r17
                              │                          │        │  └─ rach-ConfigCommonTwoStepRA-r16
                              │                          │        │     └─ featureCombinationPreamblesList-r17
                              │                          │        │        └─ _item_
                              │                          │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │                          │        └─ rach-ConfigCommon-r17
                              │                          │           └─ featureCombinationPreamblesList-r17
                              │                          │              └─ _item_
                              │                          │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │                          ├─ msgA-ConfigCommon-r16
                              │                          │  └─ setup
                              │                          │     └─ rach-ConfigCommonTwoStepRA-r16
                              │                          │        └─ featureCombinationPreamblesList-r17
                              │                          │           └─ _item_
                              │                          │              └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │                          ├─ rach-ConfigCommon
                              │                          │  └─ setup
                              │                          │     └─ featureCombinationPreamblesList-r17
                              │                          │        └─ _item_
                              │                          │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                              │                          └─ rach-ConfigCommonIAB-r16
                              │                             └─ setup
                              │                                └─ featureCombinationPreamblesList-r17
                              │                                   └─ _item_
                              │                                      └─ msg1-RepetitionTimeOffsetROGroup-r18
                              └─ secondaryCellGroup
                                 └─ CellGroupConfig
                                    ├─ sCellToAddModList
                                    │  └─ _item_
                                    │     ├─ sCellConfigCommon
                                    │     │  ├─ supplementaryUplinkConfig
                                    │     │  │  └─ initialUplinkBWP
                                    │     │  │     ├─ additionalRACH-ConfigList-r17
                                    │     │  │     │  └─ setup
                                    │     │  │     │     └─ _item_
                                    │     │  │     │        ├─ msgA-ConfigCommon-r17
                                    │     │  │     │        │  └─ rach-ConfigCommonTwoStepRA-r16
                                    │     │  │     │        │     └─ featureCombinationPreamblesList-r17
                                    │     │  │     │        │        └─ _item_
                                    │     │  │     │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                                    │     │  │     │        └─ rach-ConfigCommon-r17
                                    │     │  │     │           └─ featureCombinationPreamblesList-r17
                                    │     │  │     │              └─ _item_
                                    │     │  │     │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
                                    │     │  │     ├─ msgA-ConfigCommon-r16
                                    │     │  │     │  └─ setup
                                    │     │  │     │     └─ rach-ConfigCommonTwoStepRA-r16
                                    │     │  │     │        └─ featureCombinationPreamblesList-r17
                                    │     │  │     │           └─ _item_
                                    │     │  │     │              └─ msg1-RepetitionTimeOffsetROGroup-r18
                                    │     │  │     ├─ rach-ConfigCommon
                                    │     │  │     │  └─ setup
                                    │     │  │     │     └─ featureCombinationPreamblesList-r17
                                    │     │  │     │        └─ _item_
                                    │     │  │     │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                                    │     │  │     └─ rach-ConfigCommonIAB-r16
                                    │     │  │        └─ setup
                                    │     │  │           └─ featureCombinationPreamblesList-r17
                                    │     │  │              └─ _item_
                                    │     │  │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
                                    │     │  ├─ uplinkConfigCommon
                                    │     │  │  └─ initialUplinkBWP
                                    │     │  │     ├─ additionalRACH-ConfigList-r17
                                    │     │  │     │  └─ setup
                                    │     │  │     │     └─ _item_
                                    │     │  │     │        ├─ msgA-ConfigCommon-r17
                                    │     │  │     │        │  └─ rach-ConfigCommonTwoStepRA-r16
                                    │     │  │     │        │     └─ featureCombinationPreamblesList-r17
                                    │     │  │     │        │        └─ _item_
                                    │     │  │     │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                                    │     │  │     │        └─ rach-ConfigCommon-r17
                                    │     │  │     │           └─ featureCombinationPreamblesList-r17
                                    │     │  │     │              └─ _item_
                                    │     │  │     │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
                                    │     │  │     ├─ msgA-ConfigCommon-r16
                                    │     │  │     │  └─ setup
                                    │     │  │     │     └─ rach-ConfigCommonTwoStepRA-r16
                                    │     │  │     │        └─ featureCombinationPreamblesList-r17
                                    │     │  │     │           └─ _item_
                                    │     │  │     │              └─ msg1-RepetitionTimeOffsetROGroup-r18
                                    │     │  │     ├─ rach-ConfigCommon
                                    │     │  │     │  └─ setup
                                    │     │  │     │     └─ featureCombinationPreamblesList-r17
                                    │     │  │     │        └─ _item_
                                    │     │  │     │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                                    │     │  │     └─ rach-ConfigCommonIAB-r16
                                    │     │  │        └─ setup
                                    │     │  │           └─ featureCombinationPreamblesList-r17
                                    │     │  │              └─ _item_
                                    │     │  │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
                                    │     │  └─ uplinkConfigCommon-v1700
                                    │     │     └─ initialUplinkBWP-RedCap-r17
                                    │     │        ├─ additionalRACH-ConfigList-r17
                                    │     │        │  └─ setup
                                    │     │        │     └─ _item_
                                    │     │        │        ├─ msgA-ConfigCommon-r17
                                    │     │        │        │  └─ rach-ConfigCommonTwoStepRA-r16
                                    │     │        │        │     └─ featureCombinationPreamblesList-r17
                                    │     │        │        │        └─ _item_
                                    │     │        │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                                    │     │        │        └─ rach-ConfigCommon-r17
                                    │     │        │           └─ featureCombinationPreamblesList-r17
                                    │     │        │              └─ _item_
                                    │     │        │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
                                    │     │        ├─ msgA-ConfigCommon-r16
                                    │     │        │  └─ setup
                                    │     │        │     └─ rach-ConfigCommonTwoStepRA-r16
                                    │     │        │        └─ featureCombinationPreamblesList-r17
                                    │     │        │           └─ _item_
                                    │     │        │              └─ msg1-RepetitionTimeOffsetROGroup-r18
                                    │     │        ├─ rach-ConfigCommon
                                    │     │        │  └─ setup
                                    │     │        │     └─ featureCombinationPreamblesList-r17
                                    │     │        │        └─ _item_
                                    │     │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                                    │     │        └─ rach-ConfigCommonIAB-r16
                                    │     │           └─ setup
                                    │     │              └─ featureCombinationPreamblesList-r17
                                    │     │                 └─ _item_
                                    │     │                    └─ msg1-RepetitionTimeOffsetROGroup-r18
                                    │     └─ sCellConfigDedicated
                                    │        ├─ supplementaryUplink
                                    │        │  └─ uplinkBWP-ToAddModList
                                    │        │     └─ _item_
                                    │        │        └─ bwp-Common
                                    │        │           ├─ additionalRACH-ConfigList-r17
                                    │        │           │  └─ setup
                                    │        │           │     └─ _item_
                                    │        │           │        ├─ msgA-ConfigCommon-r17
                                    │        │           │        │  └─ rach-ConfigCommonTwoStepRA-r16
                                    │        │           │        │     └─ featureCombinationPreamblesList-r17
                                    │        │           │        │        └─ _item_
                                    │        │           │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                                    │        │           │        └─ rach-ConfigCommon-r17
                                    │        │           │           └─ featureCombinationPreamblesList-r17
                                    │        │           │              └─ _item_
                                    │        │           │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
                                    │        │           ├─ msgA-ConfigCommon-r16
                                    │        │           │  └─ setup
                                    │        │           │     └─ rach-ConfigCommonTwoStepRA-r16
                                    │        │           │        └─ featureCombinationPreamblesList-r17
                                    │        │           │           └─ _item_
                                    │        │           │              └─ msg1-RepetitionTimeOffsetROGroup-r18
                                    │        │           ├─ rach-ConfigCommon
                                    │        │           │  └─ setup
                                    │        │           │     └─ featureCombinationPreamblesList-r17
                                    │        │           │        └─ _item_
                                    │        │           │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                                    │        │           └─ rach-ConfigCommonIAB-r16
                                    │        │              └─ setup
                                    │        │                 └─ featureCombinationPreamblesList-r17
                                    │        │                    └─ _item_
                                    │        │                       └─ msg1-RepetitionTimeOffsetROGroup-r18
                                    │        └─ uplinkConfig
                                    │           └─ uplinkBWP-ToAddModList
                                    │              └─ _item_
                                    │                 └─ bwp-Common
                                    │                    ├─ additionalRACH-ConfigList-r17
                                    │                    │  └─ setup
                                    │                    │     └─ _item_
                                    │                    │        ├─ msgA-ConfigCommon-r17
                                    │                    │        │  └─ rach-ConfigCommonTwoStepRA-r16
                                    │                    │        │     └─ featureCombinationPreamblesList-r17
                                    │                    │        │        └─ _item_
                                    │                    │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                                    │                    │        └─ rach-ConfigCommon-r17
                                    │                    │           └─ featureCombinationPreamblesList-r17
                                    │                    │              └─ _item_
                                    │                    │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
                                    │                    ├─ msgA-ConfigCommon-r16
                                    │                    │  └─ setup
                                    │                    │     └─ rach-ConfigCommonTwoStepRA-r16
                                    │                    │        └─ featureCombinationPreamblesList-r17
                                    │                    │           └─ _item_
                                    │                    │              └─ msg1-RepetitionTimeOffsetROGroup-r18
                                    │                    ├─ rach-ConfigCommon
                                    │                    │  └─ setup
                                    │                    │     └─ featureCombinationPreamblesList-r17
                                    │                    │        └─ _item_
                                    │                    │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                                    │                    └─ rach-ConfigCommonIAB-r16
                                    │                       └─ setup
                                    │                          └─ featureCombinationPreamblesList-r17
                                    │                             └─ _item_
                                    │                                └─ msg1-RepetitionTimeOffsetROGroup-r18
                                    └─ spCellConfig
                                       ├─ reconfigurationWithSync
                                       │  └─ spCellConfigCommon
                                       │     ├─ supplementaryUplinkConfig
                                       │     │  └─ initialUplinkBWP
                                       │     │     ├─ additionalRACH-ConfigList-r17
                                       │     │     │  └─ setup
                                       │     │     │     └─ _item_
                                       │     │     │        ├─ msgA-ConfigCommon-r17
                                       │     │     │        │  └─ rach-ConfigCommonTwoStepRA-r16
                                       │     │     │        │     └─ featureCombinationPreamblesList-r17
                                       │     │     │        │        └─ _item_
                                       │     │     │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                                       │     │     │        └─ rach-ConfigCommon-r17
                                       │     │     │           └─ featureCombinationPreamblesList-r17
                                       │     │     │              └─ _item_
                                       │     │     │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
                                       │     │     ├─ msgA-ConfigCommon-r16
                                       │     │     │  └─ setup
                                       │     │     │     └─ rach-ConfigCommonTwoStepRA-r16
                                       │     │     │        └─ featureCombinationPreamblesList-r17
                                       │     │     │           └─ _item_
                                       │     │     │              └─ msg1-RepetitionTimeOffsetROGroup-r18
                                       │     │     ├─ rach-ConfigCommon
                                       │     │     │  └─ setup
                                       │     │     │     └─ featureCombinationPreamblesList-r17
                                       │     │     │        └─ _item_
                                       │     │     │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                                       │     │     └─ rach-ConfigCommonIAB-r16
                                       │     │        └─ setup
                                       │     │           └─ featureCombinationPreamblesList-r17
                                       │     │              └─ _item_
                                       │     │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
                                       │     ├─ uplinkConfigCommon
                                       │     │  └─ initialUplinkBWP
                                       │     │     ├─ additionalRACH-ConfigList-r17
                                       │     │     │  └─ setup
                                       │     │     │     └─ _item_
                                       │     │     │        ├─ msgA-ConfigCommon-r17
                                       │     │     │        │  └─ rach-ConfigCommonTwoStepRA-r16
                                       │     │     │        │     └─ featureCombinationPreamblesList-r17
                                       │     │     │        │        └─ _item_
                                       │     │     │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                                       │     │     │        └─ rach-ConfigCommon-r17
                                       │     │     │           └─ featureCombinationPreamblesList-r17
                                       │     │     │              └─ _item_
                                       │     │     │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
                                       │     │     ├─ msgA-ConfigCommon-r16
                                       │     │     │  └─ setup
                                       │     │     │     └─ rach-ConfigCommonTwoStepRA-r16
                                       │     │     │        └─ featureCombinationPreamblesList-r17
                                       │     │     │           └─ _item_
                                       │     │     │              └─ msg1-RepetitionTimeOffsetROGroup-r18
                                       │     │     ├─ rach-ConfigCommon
                                       │     │     │  └─ setup
                                       │     │     │     └─ featureCombinationPreamblesList-r17
                                       │     │     │        └─ _item_
                                       │     │     │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                                       │     │     └─ rach-ConfigCommonIAB-r16
                                       │     │        └─ setup
                                       │     │           └─ featureCombinationPreamblesList-r17
                                       │     │              └─ _item_
                                       │     │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
                                       │     └─ uplinkConfigCommon-v1700
                                       │        └─ initialUplinkBWP-RedCap-r17
                                       │           ├─ additionalRACH-ConfigList-r17
                                       │           │  └─ setup
                                       │           │     └─ _item_
                                       │           │        ├─ msgA-ConfigCommon-r17
                                       │           │        │  └─ rach-ConfigCommonTwoStepRA-r16
                                       │           │        │     └─ featureCombinationPreamblesList-r17
                                       │           │        │        └─ _item_
                                       │           │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                                       │           │        └─ rach-ConfigCommon-r17
                                       │           │           └─ featureCombinationPreamblesList-r17
                                       │           │              └─ _item_
                                       │           │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
                                       │           ├─ msgA-ConfigCommon-r16
                                       │           │  └─ setup
                                       │           │     └─ rach-ConfigCommonTwoStepRA-r16
                                       │           │        └─ featureCombinationPreamblesList-r17
                                       │           │           └─ _item_
                                       │           │              └─ msg1-RepetitionTimeOffsetROGroup-r18
                                       │           ├─ rach-ConfigCommon
                                       │           │  └─ setup
                                       │           │     └─ featureCombinationPreamblesList-r17
                                       │           │        └─ _item_
                                       │           │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                                       │           └─ rach-ConfigCommonIAB-r16
                                       │              └─ setup
                                       │                 └─ featureCombinationPreamblesList-r17
                                       │                    └─ _item_
                                       │                       └─ msg1-RepetitionTimeOffsetROGroup-r18
                                       └─ spCellConfigDedicated
                                          ├─ supplementaryUplink
                                          │  └─ uplinkBWP-ToAddModList
                                          │     └─ _item_
                                          │        └─ bwp-Common
                                          │           ├─ additionalRACH-ConfigList-r17
                                          │           │  └─ setup
                                          │           │     └─ _item_
                                          │           │        ├─ msgA-ConfigCommon-r17
                                          │           │        │  └─ rach-ConfigCommonTwoStepRA-r16
                                          │           │        │     └─ featureCombinationPreamblesList-r17
                                          │           │        │        └─ _item_
                                          │           │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                                          │           │        └─ rach-ConfigCommon-r17
                                          │           │           └─ featureCombinationPreamblesList-r17
                                          │           │              └─ _item_
                                          │           │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
                                          │           ├─ msgA-ConfigCommon-r16
                                          │           │  └─ setup
                                          │           │     └─ rach-ConfigCommonTwoStepRA-r16
                                          │           │        └─ featureCombinationPreamblesList-r17
                                          │           │           └─ _item_
                                          │           │              └─ msg1-RepetitionTimeOffsetROGroup-r18
                                          │           ├─ rach-ConfigCommon
                                          │           │  └─ setup
                                          │           │     └─ featureCombinationPreamblesList-r17
                                          │           │        └─ _item_
                                          │           │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                                          │           └─ rach-ConfigCommonIAB-r16
                                          │              └─ setup
                                          │                 └─ featureCombinationPreamblesList-r17
                                          │                    └─ _item_
                                          │                       └─ msg1-RepetitionTimeOffsetROGroup-r18
                                          └─ uplinkConfig
                                             └─ uplinkBWP-ToAddModList
                                                └─ _item_
                                                   └─ bwp-Common
                                                      ├─ additionalRACH-ConfigList-r17
                                                      │  └─ setup
                                                      │     └─ _item_
                                                      │        ├─ msgA-ConfigCommon-r17
                                                      │        │  └─ rach-ConfigCommonTwoStepRA-r16
                                                      │        │     └─ featureCombinationPreamblesList-r17
                                                      │        │        └─ _item_
                                                      │        │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                                                      │        └─ rach-ConfigCommon-r17
                                                      │           └─ featureCombinationPreamblesList-r17
                                                      │              └─ _item_
                                                      │                 └─ msg1-RepetitionTimeOffsetROGroup-r18
                                                      ├─ msgA-ConfigCommon-r16
                                                      │  └─ setup
                                                      │     └─ rach-ConfigCommonTwoStepRA-r16
                                                      │        └─ featureCombinationPreamblesList-r17
                                                      │           └─ _item_
                                                      │              └─ msg1-RepetitionTimeOffsetROGroup-r18
                                                      ├─ rach-ConfigCommon
                                                      │  └─ setup
                                                      │     └─ featureCombinationPreamblesList-r17
                                                      │        └─ _item_
                                                      │           └─ msg1-RepetitionTimeOffsetROGroup-r18
                                                      └─ rach-ConfigCommonIAB-r16
                                                         └─ setup
                                                            └─ featureCombinationPreamblesList-r17
                                                               └─ _item_
                                                                  └─ msg1-RepetitionTimeOffsetROGroup-r18
```
