"""AUTOSAR TDEventBswInternalBehaviorTypeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 74)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.enums.json"""

from enum import Enum


class TDEventBswInternalBehaviorTypeEnum(Enum):
    """AUTOSAR TDEventBswInternalBehaviorTypeEnum enumeration."""

    # Note: 1 duplicate literal(s) found and removed: bswModuleEntity
    BSWMODULEENTITY = "bswModuleEntity"
    BSWMODULEENTITYTERMINATED = "bswModuleEntityTerminated"
