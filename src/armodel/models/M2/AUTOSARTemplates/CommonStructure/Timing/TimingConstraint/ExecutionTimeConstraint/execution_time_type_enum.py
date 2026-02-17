"""AUTOSAR ExecutionTimeTypeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 130)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_ExecutionTimeConstraint.enums.json"""

from enum import Enum


class ExecutionTimeTypeEnum(Enum):
    """AUTOSAR ExecutionTimeTypeEnum enumeration."""

    GROSSINTERRUPTIONNETINTERRUPTION = "grossinterruptionnetinterruption"
