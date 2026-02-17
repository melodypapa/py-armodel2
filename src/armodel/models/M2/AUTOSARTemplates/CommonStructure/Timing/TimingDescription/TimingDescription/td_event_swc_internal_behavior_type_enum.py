"""AUTOSAR TDEventSwcInternalBehaviorTypeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 62)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.enums.json"""

from enum import Enum


class TDEventSwcInternalBehaviorTypeEnum(Enum):
    """AUTOSAR TDEventSwcInternalBehaviorTypeEnum enumeration."""

    # Note: 1 duplicate literal(s) found and removed: runnableEntity
    RUNNABLEENTITY = "runnableEntity"
    RUNNABLEENTITYTERMINATED = "runnableEntityTerminated"
    RUNNABLEENTITYVARIABLEACCESS = "runnableEntityVariableAccess"
