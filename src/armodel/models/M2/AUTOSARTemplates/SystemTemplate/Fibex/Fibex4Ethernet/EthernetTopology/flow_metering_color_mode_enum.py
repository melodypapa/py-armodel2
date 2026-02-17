"""AUTOSAR FlowMeteringColorModeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 143)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.enums.json"""

from enum import Enum


class FlowMeteringColorModeEnum(Enum):
    """AUTOSAR FlowMeteringColorModeEnum enumeration."""

    COLORAWARE = "colorAware"
    SYSTEM = "System"
    AUTOSAR = "AUTOSAR"
    COLORBLIND = "colorBlind"
