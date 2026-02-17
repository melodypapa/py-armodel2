"""AUTOSAR TDEventIPduTypeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 67)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.enums.json"""

from enum import Enum


class TDEventIPduTypeEnum(Enum):
    """AUTOSAR TDEventIPduTypeEnum enumeration."""

    IPDURECEIVEDBY = "iPduReceivedBy"
    COM = "COM"
    IPDUSENTTOIFSPECIFIC = "iPduSentToIfspecific"
