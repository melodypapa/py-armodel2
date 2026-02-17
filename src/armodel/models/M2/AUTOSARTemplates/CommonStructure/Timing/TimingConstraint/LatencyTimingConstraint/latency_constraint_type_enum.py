"""AUTOSAR LatencyConstraintTypeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 96)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_LatencyTimingConstraint.enums.json"""

from enum import Enum


class LatencyConstraintTypeEnum(Enum):
    """AUTOSAR LatencyConstraintTypeEnum enumeration."""

    AGE = "age"
    REACTION = "reaction"
