"""AUTOSAR DoIpEntityRoleEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 471)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.enums.json"""

from enum import Enum


class DoIpEntityRoleEnum(Enum):
    """AUTOSAR DoIpEntityRoleEnum enumeration."""

    EDGENODE = "edgeNode"
    GATEWAY = "gateway"
    NODE = "node"
