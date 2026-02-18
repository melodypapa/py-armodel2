"""TimingExtension AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 254)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingExtensions.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingClock.timing_clock import (
    TimingClock,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingClock.timing_clock_sync_accuracy import (
    TimingClockSyncAccuracy,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.timing_condition import (
    TimingCondition,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.timing_constraint import (
    TimingConstraint,
)
from abc import ABC, abstractmethod


class TimingExtension(ARElement, ABC):
    """AUTOSAR TimingExtension."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    timing_clocks: list[TimingClock]
    timing_clock_syncs: list[TimingClockSyncAccuracy]
    timing_conditions: list[TimingCondition]
    timings: list[TimingConstraint]
    timing_resource: Optional[TimingExtension]
    def __init__(self) -> None:
        """Initialize TimingExtension."""
        super().__init__()
        self.timing_clocks: list[TimingClock] = []
        self.timing_clock_syncs: list[TimingClockSyncAccuracy] = []
        self.timing_conditions: list[TimingCondition] = []
        self.timings: list[TimingConstraint] = []
        self.timing_resource: Optional[TimingExtension] = None


class TimingExtensionBuilder:
    """Builder for TimingExtension."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TimingExtension = TimingExtension()

    def build(self) -> TimingExtension:
        """Build and return TimingExtension object.

        Returns:
            TimingExtension instance
        """
        # TODO: Add validation
        return self._obj
