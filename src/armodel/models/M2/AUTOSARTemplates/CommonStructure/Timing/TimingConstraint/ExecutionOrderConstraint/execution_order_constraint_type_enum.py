"""ExecutionOrderConstraintTypeEnum enumeration."""

from enum import Enum


class ExecutionOrderConstraintTypeEnum(Enum):
    """AUTOSAR ExecutionOrderConstraintTypeEnum enumeration."""

    HIERARCHICALEOC = "hierarchicalEOC"
    ORDINARYEOC = "ordinaryEOC"
    REPETITIVEEOC = "repetitiveEOC"
