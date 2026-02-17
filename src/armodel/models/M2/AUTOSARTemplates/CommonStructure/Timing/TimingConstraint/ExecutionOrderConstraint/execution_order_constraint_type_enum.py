"""AUTOSAR ExecutionOrderConstraintTypeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 119)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_ExecutionOrderConstraint.enums.json"""

from enum import Enum


class ExecutionOrderConstraintTypeEnum(Enum):
    """AUTOSAR ExecutionOrderConstraintTypeEnum enumeration."""

    HIERARCHICALEOC = "hierarchicalEOC"
    ORDINARYEOC = "ordinaryEOC"
    REPETITIVEEOC = "repetitiveEOC"
