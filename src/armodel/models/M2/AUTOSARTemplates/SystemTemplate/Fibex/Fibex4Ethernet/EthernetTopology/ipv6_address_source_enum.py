"""AUTOSAR Ipv6AddressSourceEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 467)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.enums.json"""

from enum import Enum


class Ipv6AddressSourceEnum(Enum):
    """AUTOSAR Ipv6AddressSourceEnum enumeration."""

    DHCPV6 = "dhcpv6"
    FIXED = "fixed"
    LINKLOCAL = "linkLocal"
    LINKLOCAL_DOIP = "linkLocal_doip"
    ROUTERADVERTISEMENT = "routerAdvertisement"
