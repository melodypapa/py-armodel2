"""AUTOSAR EventGroupControlTypeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 489)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.enums.json"""

from enum import Enum


class EventGroupControlTypeEnum(Enum):
    """AUTOSAR EventGroupControlTypeEnum enumeration."""

    ACTIVATIONAND = "activationAnd"
    ACTIVATIONMULTICAST = "activationMulticast"
    ACTIVATIONUNICAST = "activationUnicast"
    TRIGGERUNICAST = "triggerUnicast"
