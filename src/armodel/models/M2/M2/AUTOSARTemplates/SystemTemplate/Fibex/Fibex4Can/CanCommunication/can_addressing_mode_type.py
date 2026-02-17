"""AUTOSAR CanAddressingModeType enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 443)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanCommunication.enums.json"""

from enum import Enum


class CanAddressingModeType(Enum):
    """AUTOSAR CanAddressingModeType enumeration."""

    EXTENDED = "extended"
    STANDARD = "standard"
