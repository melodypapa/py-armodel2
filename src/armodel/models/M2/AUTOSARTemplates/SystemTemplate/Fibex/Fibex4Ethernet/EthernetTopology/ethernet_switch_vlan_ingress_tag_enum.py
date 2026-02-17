"""AUTOSAR EthernetSwitchVlanIngressTagEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 111)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.enums.json"""

from enum import Enum


class EthernetSwitchVlanIngressTagEnum(Enum):
    """AUTOSAR EthernetSwitchVlanIngressTagEnum enumeration."""

    DROPUNTAGGED = "dropUntagged"
    FORWARDASIS = "forwardAsIs"
