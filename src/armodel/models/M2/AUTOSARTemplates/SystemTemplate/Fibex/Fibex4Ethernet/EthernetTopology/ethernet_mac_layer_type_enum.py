"""AUTOSAR EthernetMacLayerTypeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 110)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.enums.json"""

from enum import Enum


class EthernetMacLayerTypeEnum(Enum):
    """AUTOSAR EthernetMacLayerTypeEnum enumeration."""

    XGMII = "xGMII"
    XMII = "xMII"
    XXGMII = "xXGMII"
