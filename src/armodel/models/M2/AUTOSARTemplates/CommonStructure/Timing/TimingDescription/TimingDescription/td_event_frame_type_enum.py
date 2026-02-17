"""AUTOSAR TDEventFrameTypeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 68)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.enums.json"""

from enum import Enum


class TDEventFrameTypeEnum(Enum):
    """AUTOSAR TDEventFrameTypeEnum enumeration."""

    FRAMEQUEUEDFOR = "frameQueuedFor"
    FRAMERECEIVEDBYIFCORRESPONDING = "frameReceivedByIfcorresponding"
    FRAMETRANSMITTEDONBUS = "frameTransmittedOnBus"
