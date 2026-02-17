"""AUTOSAR CouplingElementEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 108)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.enums.json"""

from enum import Enum


class CouplingElementEnum(Enum):
    """AUTOSAR CouplingElementEnum enumeration."""

    HUB = "hub"
    ROUTER = "router"
    SWITCH = "switch"
