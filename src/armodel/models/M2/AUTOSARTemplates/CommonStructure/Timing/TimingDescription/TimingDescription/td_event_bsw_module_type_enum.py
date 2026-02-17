"""AUTOSAR TDEventBswModuleTypeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 76)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.enums.json"""

from enum import Enum


class TDEventBswModuleTypeEnum(Enum):
    """AUTOSAR TDEventBswModuleTypeEnum enumeration."""

    BSWMENTRYCALLED = "bswMEntryCalled"
    BSWMENTRYCALLRETURNED = "bswMEntryCallReturned"
