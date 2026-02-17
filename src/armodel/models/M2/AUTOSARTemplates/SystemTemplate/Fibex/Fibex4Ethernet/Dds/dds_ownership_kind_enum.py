"""AUTOSAR DdsOwnershipKindEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 533)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.enums.json"""

from enum import Enum


class DdsOwnershipKindEnum(Enum):
    """AUTOSAR DdsOwnershipKindEnum enumeration."""

    EXCLUSIVESHARED = "exclusiveshared"
