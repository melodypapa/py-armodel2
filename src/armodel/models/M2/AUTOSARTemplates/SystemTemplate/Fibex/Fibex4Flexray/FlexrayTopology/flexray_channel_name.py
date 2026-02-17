"""AUTOSAR FlexrayChannelName enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 89)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Flexray_FlexrayTopology.enums.json"""

from enum import Enum


class FlexrayChannelName(Enum):
    """AUTOSAR FlexrayChannelName enumeration."""

    CHANNELA = "channelA"
    CHANNELB = "channelB"
