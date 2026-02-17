"""AUTOSAR TimeSyncTechnologyEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 470)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.enums.json"""

from enum import Enum


class TimeSyncTechnologyEnum(Enum):
    """AUTOSAR TimeSyncTechnologyEnum enumeration."""

    AVB_IEEE802_1AS = "avb_ieee802_1AS"
    NTP_RFC958 = "ntp_rfc958"
    PTP_IEEE1588_2002 = "ptp_ieee1588_2002"
    PTP_IEEE1588_2008 = "ptp_ieee1588_2008"
