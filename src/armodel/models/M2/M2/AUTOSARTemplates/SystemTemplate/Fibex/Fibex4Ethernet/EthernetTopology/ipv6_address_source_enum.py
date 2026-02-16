"""Ipv6AddressSourceEnum enumeration."""

from enum import Enum


class Ipv6AddressSourceEnum(Enum):
    """AUTOSAR Ipv6AddressSourceEnum enumeration."""

    DHCPV6 = "dhcpv6"
    FIXED = "fixed"
    LINKLOCAL = "linkLocal"
    LINKLOCAL_DOIP = "linkLocal_doip"
    ROUTERADVERTISEMENT = "routerAdvertisement"
