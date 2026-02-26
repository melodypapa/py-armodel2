"""ExecutionTimeConstraint module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionTimeConstraint.execution_time_constraint import (
        ExecutionTimeConstraint,
    )

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionTimeConstraint.execution_time_type_enum import (
    ExecutionTimeTypeEnum,
)

__all__ = [
    "ExecutionTimeConstraint",
    "ExecutionTimeTypeEnum",
]
