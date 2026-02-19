"""TimingClockSyncAccuracy AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 252)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingClock.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingClock.timing_clock import (
    TimingClock,
)


class TimingClockSyncAccuracy(Identifiable):
    """AUTOSAR TimingClockSyncAccuracy."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    accuracy: Optional[MultidimensionalTime]
    lower: Optional[TimingClock]
    upper: Optional[TimingClock]
    def __init__(self) -> None:
        """Initialize TimingClockSyncAccuracy."""
        super().__init__()
        self.accuracy: Optional[MultidimensionalTime] = None
        self.lower: Optional[TimingClock] = None
        self.upper: Optional[TimingClock] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "TimingClockSyncAccuracy":
        """Deserialize XML element to TimingClockSyncAccuracy object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TimingClockSyncAccuracy object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TimingClockSyncAccuracy, cls).deserialize(element)

        # Parse accuracy
        child = ARObject._find_child_element(element, "ACCURACY")
        if child is not None:
            accuracy_value = ARObject._deserialize_by_tag(child, "MultidimensionalTime")
            obj.accuracy = accuracy_value

        # Parse lower
        child = ARObject._find_child_element(element, "LOWER")
        if child is not None:
            lower_value = ARObject._deserialize_by_tag(child, "TimingClock")
            obj.lower = lower_value

        # Parse upper
        child = ARObject._find_child_element(element, "UPPER")
        if child is not None:
            upper_value = ARObject._deserialize_by_tag(child, "TimingClock")
            obj.upper = upper_value

        return obj



class TimingClockSyncAccuracyBuilder:
    """Builder for TimingClockSyncAccuracy."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TimingClockSyncAccuracy = TimingClockSyncAccuracy()

    def build(self) -> TimingClockSyncAccuracy:
        """Build and return TimingClockSyncAccuracy object.

        Returns:
            TimingClockSyncAccuracy instance
        """
        # TODO: Add validation
        return self._obj
