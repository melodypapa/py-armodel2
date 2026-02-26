"""LatencyTimingConstraint module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.LatencyTimingConstraint.latency_timing_constraint import (
        LatencyTimingConstraint,
    )

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.LatencyTimingConstraint.latency_constraint_type_enum import (
    LatencyConstraintTypeEnum,
)

__all__ = [
    "LatencyConstraintTypeEnum",
    "LatencyTimingConstraint",
]
