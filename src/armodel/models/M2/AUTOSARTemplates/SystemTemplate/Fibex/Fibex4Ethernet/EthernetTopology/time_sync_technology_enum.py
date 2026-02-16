"""TimeSyncTechnologyEnum enumeration."""

from enum import Enum


class TimeSyncTechnologyEnum(Enum):
    """AUTOSAR TimeSyncTechnologyEnum enumeration."""

    AVB_IEEE802_1AS = "avb_ieee802_1AS"
    NTP_RFC958 = "ntp_rfc958"
    PTP_IEEE1588_2002 = "ptp_ieee1588_2002"
    PTP_IEEE1588_2008 = "ptp_ieee1588_2008"
