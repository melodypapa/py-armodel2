"""AUTOSAR CouplingPortRatePolicyActionEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 125)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.enums.json"""

from enum import Enum


class CouplingPortRatePolicyActionEnum(Enum):
    """AUTOSAR CouplingPortRatePolicyActionEnum enumeration."""

    BLOCKSOURCE = "blockSource"
    DROPFRAME = "dropFrame"
