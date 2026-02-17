"""AUTOSAR IpAddressKeepEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 465)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.enums.json"""

from enum import Enum


class IpAddressKeepEnum(Enum):
    """AUTOSAR IpAddressKeepEnum enumeration."""

    FORGET = "forget"
    STOREPERSISTENTLY = "storePersistently"
