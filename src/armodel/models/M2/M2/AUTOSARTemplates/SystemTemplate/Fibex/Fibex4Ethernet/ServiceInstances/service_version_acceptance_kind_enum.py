"""AUTOSAR ServiceVersionAcceptanceKindEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2056)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.enums.json"""

from enum import Enum


class ServiceVersionAcceptanceKindEnum(Enum):
    """AUTOSAR ServiceVersionAcceptanceKindEnum enumeration."""

    EXACTORANYMINOR = "exactOrAnyMinor"
    SYSTEM = "System"
    AUTOSAR = "AUTOSAR"
    MINIMUMMINOR = "minimumMinor"
