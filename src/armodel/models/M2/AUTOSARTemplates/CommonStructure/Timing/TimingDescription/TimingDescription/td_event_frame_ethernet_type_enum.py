"""AUTOSAR TDEventFrameEthernetTypeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 70)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.enums.json"""

from enum import Enum


class TDEventFrameEthernetTypeEnum(Enum):
    """AUTOSAR TDEventFrameEthernetTypeEnum enumeration."""

    FRAMEETHERNETTRANSMISSION = "frameEthernetTransmission"
    FRAMEETHERNET = "frameEthernet"
    FRAMEETHERNET = "frameEthernet"
    FRAMEETHERNETSENTONBUS = "frameEthernetSentOnBus"
