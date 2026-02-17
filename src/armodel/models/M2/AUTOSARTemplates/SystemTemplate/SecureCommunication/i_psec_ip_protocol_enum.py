"""AUTOSAR IPsecIpProtocolEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 573)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.enums.json"""

from enum import Enum


class IPsecIpProtocolEnum(Enum):
    """AUTOSAR IPsecIpProtocolEnum enumeration."""

    ANY = "any"
    ICMP = "icmp"
    TCP = "tcp"
    UDP = "udp"
