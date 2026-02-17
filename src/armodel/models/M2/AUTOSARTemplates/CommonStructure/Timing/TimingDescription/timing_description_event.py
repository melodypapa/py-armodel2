"""TimingDescriptionEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 253)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description import (
    TimingDescription,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingClock.timing_clock import (
    TimingClock,
)


class TimingDescriptionEvent(TimingDescription):
    """AUTOSAR TimingDescriptionEvent."""
    """Abstract base class - do not instantiate directly."""

    clock_reference: Optional[TimingClock]
    occurrence: Optional[Any]
    def __init__(self) -> None:
        """Initialize TimingDescriptionEvent."""
        super().__init__()
        self.clock_reference: Optional[TimingClock] = None
        self.occurrence: Optional[Any] = None


class TimingDescriptionEventBuilder:
    """Builder for TimingDescriptionEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TimingDescriptionEvent = TimingDescriptionEvent()

    def build(self) -> TimingDescriptionEvent:
        """Build and return TimingDescriptionEvent object.

        Returns:
            TimingDescriptionEvent instance
        """
        # TODO: Add validation
        return self._obj
