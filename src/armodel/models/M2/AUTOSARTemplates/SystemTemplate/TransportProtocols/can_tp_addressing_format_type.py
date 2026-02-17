"""AUTOSAR CanTpAddressingFormatType enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 609)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.enums.json"""

from enum import Enum


class CanTpAddressingFormatType(Enum):
    """AUTOSAR CanTpAddressingFormatType enumeration."""

    EXTENDED = "extended"
    SYSTEM = "System"
    AUTOSAR = "AUTOSAR"
    MIXED = "mixed"
    MIXED29BIT = "mixed29bit"
    NORMALFIXED = "normalfixed"
    STANDARD = "standard"
