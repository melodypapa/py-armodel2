"""SynchronizationTiming module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.SynchronizationTiming.synchronization_timing_constraint import (
        SynchronizationTimingConstraint,
    )

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.SynchronizationTiming.synchronization_type_enum import (
    SynchronizationTypeEnum,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.SynchronizationTiming.event_occurrence_kind_enum import (
    EventOccurrenceKindEnum,
)

__all__ = [
    "EventOccurrenceKindEnum",
    "SynchronizationTimingConstraint",
    "SynchronizationTypeEnum",
]
