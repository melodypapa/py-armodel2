"""IPsecIpProtocolEnum enumeration."""

from enum import Enum


class IPsecIpProtocolEnum(Enum):
    """AUTOSAR IPsecIpProtocolEnum enumeration."""

    ANY = "any"
    ICMP = "icmp"
    TCP = "tcp"
    UDP = "udp"
