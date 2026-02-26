"""EventTriggeringConstraint module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint.event_triggering_constraint import (
        EventTriggeringConstraint,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint.periodic_event_triggering import (
        PeriodicEventTriggering,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint.sporadic_event_triggering import (
        SporadicEventTriggering,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint.concrete_pattern_event_triggering import (
        ConcretePatternEventTriggering,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint.burst_pattern_event_triggering import (
        BurstPatternEventTriggering,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint.arbitrary_event_triggering import (
        ArbitraryEventTriggering,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint.confidence_interval import (
        ConfidenceInterval,
    )

__all__ = [
    "ArbitraryEventTriggering",
    "BurstPatternEventTriggering",
    "ConcretePatternEventTriggering",
    "ConfidenceInterval",
    "EventTriggeringConstraint",
    "PeriodicEventTriggering",
    "SporadicEventTriggering",
]
