"""IEEE1722TpCrfTypeEnum enumeration."""

from enum import Enum


class IEEE1722TpCrfTypeEnum(Enum):
    """AUTOSAR IEEE1722TpCrfTypeEnum enumeration."""

    AUDIOSAMPLE = "audioSample"
    MACHINECYCLE = "machineCycle"
    USER = "user"
    VIDEOFRAME = "videoFrame"
    VIDEOLINE = "videoLine"
