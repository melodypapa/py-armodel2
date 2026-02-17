"""AUTOSAR PduCollectionTriggerEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 357)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.enums.json"""

from enum import Enum


class PduCollectionTriggerEnum(Enum):
    """AUTOSAR PduCollectionTriggerEnum enumeration."""

    ALWAYS = "always"
    NEVER = "never"
