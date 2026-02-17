"""AUTOSAR TcpRoleEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2074)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.enums.json"""

from enum import Enum


class TcpRoleEnum(Enum):
    """AUTOSAR TcpRoleEnum enumeration."""

    CONNECT = "connect"
    LISTEN = "listen"
