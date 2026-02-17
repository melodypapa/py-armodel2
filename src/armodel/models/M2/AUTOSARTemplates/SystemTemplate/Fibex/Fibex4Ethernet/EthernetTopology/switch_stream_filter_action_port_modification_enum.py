"""AUTOSAR SwitchStreamFilterActionPortModificationEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 140)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.enums.json"""

from enum import Enum


class SwitchStreamFilterActionPortModificationEnum(Enum):
    """AUTOSAR SwitchStreamFilterActionPortModificationEnum enumeration."""

    EXTEND = "extend"
    OVERWRITE = "overwrite"
