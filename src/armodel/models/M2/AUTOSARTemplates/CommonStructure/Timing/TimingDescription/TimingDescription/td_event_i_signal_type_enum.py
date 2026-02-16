"""TDEventISignalTypeEnum enumeration."""

from enum import Enum


class TDEventISignalTypeEnum(Enum):
    """AUTOSAR TDEventISignalTypeEnum enumeration."""

    ISIGNALAVAILABLEFOR = "iSignalAvailableFor"
    RTE = "RTE"
    ISIGNALSENTTOCOM = "iSignalSentToCOM"
