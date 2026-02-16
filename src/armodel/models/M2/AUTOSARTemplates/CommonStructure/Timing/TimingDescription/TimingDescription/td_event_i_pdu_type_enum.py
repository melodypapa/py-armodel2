"""TDEventIPduTypeEnum enumeration."""

from enum import Enum


class TDEventIPduTypeEnum(Enum):
    """AUTOSAR TDEventIPduTypeEnum enumeration."""

    IPDURECEIVEDBY = "iPduReceivedBy"
    COM = "COM"
    IPDUSENTTOIFSPECIFIC = "iPduSentToIfspecific"
