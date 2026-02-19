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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "TimingExtension":
        """Deserialize XML element to TimingExtension object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TimingExtension object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse timing_clocks (list)
        obj.timing_clocks = []
        for child in ARObject._find_all_child_elements(element, "TIMING-CLOCKS"):
            timing_clocks_value = ARObject._deserialize_by_tag(child, "TimingClock")
            obj.timing_clocks.append(timing_clocks_value)

        # Parse timing_clock_syncs (list)
        obj.timing_clock_syncs = []
        for child in ARObject._find_all_child_elements(element, "TIMING-CLOCK-SYNCS"):
            timing_clock_syncs_value = ARObject._deserialize_by_tag(child, "TimingClockSyncAccuracy")
            obj.timing_clock_syncs.append(timing_clock_syncs_value)

        # Parse timing_conditions (list)
        obj.timing_conditions = []
        for child in ARObject._find_all_child_elements(element, "TIMING-CONDITIONS"):
            timing_conditions_value = ARObject._deserialize_by_tag(child, "TimingCondition")
            obj.timing_conditions.append(timing_conditions_value)

        # Parse timings (list)
        obj.timings = []
        for child in ARObject._find_all_child_elements(element, "TIMINGS"):
            timings_value = ARObject._deserialize_by_tag(child, "TimingConstraint")
            obj.timings.append(timings_value)

        # Parse timing_resource
        child = ARObject._find_child_element(element, "TIMING-RESOURCE")
        if child is not None:
            timing_resource_value = ARObject._deserialize_by_tag(child, "TimingExtension")
            obj.timing_resource = timing_resource_value

        return obj



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
