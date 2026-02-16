"""TDEventFrameTypeEnum enumeration."""

from enum import Enum


class TDEventFrameTypeEnum(Enum):
    """AUTOSAR TDEventFrameTypeEnum enumeration."""

    FRAMEQUEUEDFOR = "frameQueuedFor"
    FRAMERECEIVEDBYIFCORRESPONDING = "frameReceivedByIfcorresponding"
    FRAMETRANSMITTEDONBUS = "frameTransmittedOnBus"
