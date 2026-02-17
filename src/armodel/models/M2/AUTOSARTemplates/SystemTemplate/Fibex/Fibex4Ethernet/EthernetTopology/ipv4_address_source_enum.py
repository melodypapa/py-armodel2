"""AUTOSAR Ipv4AddressSourceEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 465)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.enums.json"""

from enum import Enum


class Ipv4AddressSourceEnum(Enum):
    """AUTOSAR Ipv4AddressSourceEnum enumeration."""

    AUTOIP = "autoIp"
    AUTOIP_DOIP = "autoIp_doip"
    DHCPV4 = "dhcpv4"
    FIXED = "fixed"
