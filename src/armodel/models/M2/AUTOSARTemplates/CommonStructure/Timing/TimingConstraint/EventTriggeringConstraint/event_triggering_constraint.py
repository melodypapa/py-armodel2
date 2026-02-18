"""EventTriggeringConstraint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 100)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_EventTriggeringConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.timing_constraint import (
    TimingConstraint,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)
from abc import ABC, abstractmethod


class EventTriggeringConstraint(TimingConstraint, ABC):
    """AUTOSAR EventTriggeringConstraint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    event: Optional[TimingDescriptionEvent]
    def __init__(self) -> None:
        """Initialize EventTriggeringConstraint."""
        super().__init__()
        self.event: Optional[TimingDescriptionEvent] = None


class EventTriggeringConstraintBuilder:
    """Builder for EventTriggeringConstraint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EventTriggeringConstraint = EventTriggeringConstraint()

    def build(self) -> EventTriggeringConstraint:
        """Build and return EventTriggeringConstraint object.

        Returns:
            EventTriggeringConstraint instance
        """
        # TODO: Add validation
        return self._obj
