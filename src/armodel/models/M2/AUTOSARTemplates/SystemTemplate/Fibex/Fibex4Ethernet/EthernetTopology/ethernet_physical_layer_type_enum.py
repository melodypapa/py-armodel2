"""AUTOSAR EthernetPhysicalLayerTypeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 111)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.enums.json"""

from enum import Enum


class EthernetPhysicalLayerTypeEnum(Enum):
    """AUTOSAR EthernetPhysicalLayerTypeEnum enumeration."""

    _1000BASE_T = "_1000BASE_T"
    _1000BASE_T1 = "_1000BASE_T1"
    _100BASE_T1 = "_100BASE_T1"
    _100BASE_TX = "_100BASE_TX"
    _10BASE_T1S = "_10BASE_T1S"
    IEEE802_11P = "iEEE802_11P"
