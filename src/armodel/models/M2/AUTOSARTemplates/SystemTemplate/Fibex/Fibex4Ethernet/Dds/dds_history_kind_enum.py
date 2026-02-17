"""AUTOSAR DdsHistoryKindEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 537)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.enums.json"""

from enum import Enum


class DdsHistoryKindEnum(Enum):
    """AUTOSAR DdsHistoryKindEnum enumeration."""

    KEEPALLKEEPLAST = "keepAllkeepLast"
