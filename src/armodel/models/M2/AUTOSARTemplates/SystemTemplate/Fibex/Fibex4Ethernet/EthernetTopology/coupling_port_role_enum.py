"""AUTOSAR CouplingPortRoleEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2013)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.enums.json"""

from enum import Enum


class CouplingPortRoleEnum(Enum):
    """AUTOSAR CouplingPortRoleEnum enumeration."""

    HOSTPORTELEMENT = "hostPortElement"
    STANDARDPORTUPLINKPORT = "standardPortupLinkPort"
    ECU = "ECU"
