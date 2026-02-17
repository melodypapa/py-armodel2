"""AUTOSAR TDEventISignalTypeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 66)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.enums.json"""

from enum import Enum


class TDEventISignalTypeEnum(Enum):
    """AUTOSAR TDEventISignalTypeEnum enumeration."""

    ISIGNALAVAILABLEFOR = "iSignalAvailableFor"
    RTE = "RTE"
    ISIGNALSENTTOCOM = "iSignalSentToCOM"
