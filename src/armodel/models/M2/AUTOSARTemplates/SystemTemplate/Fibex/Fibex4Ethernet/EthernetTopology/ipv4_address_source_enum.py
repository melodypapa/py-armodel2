"""Ipv4AddressSourceEnum enumeration."""

from enum import Enum


class Ipv4AddressSourceEnum(Enum):
    """AUTOSAR Ipv4AddressSourceEnum enumeration."""

    AUTOIP = "autoIp"
    AUTOIP_DOIP = "autoIp_doip"
    DHCPV4 = "dhcpv4"
    FIXED = "fixed"
