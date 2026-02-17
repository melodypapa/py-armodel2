"""AUTOSAR TDEventFrameEthernetTypeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 70)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.enums.json"""

from enum import Enum


class TDEventFrameEthernetTypeEnum(Enum):
    """AUTOSAR TDEventFrameEthernetTypeEnum enumeration."""

    # Note: 1 duplicate literal(s) found and removed: frameEthernet
    FRAMEETHERNETTRANSMISSION = "frameEthernetTransmission"
    FRAMEETHERNET = "frameEthernet"
    FRAMEETHERNETSENTONBUS = "frameEthernetSentOnBus"
