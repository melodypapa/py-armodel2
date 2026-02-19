"""ArbitraryEventTriggering AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 111)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_EventTriggeringConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint.event_triggering_constraint import (
    EventTriggeringConstraint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint.confidence_interval import (
    ConfidenceInterval,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)


class ArbitraryEventTriggering(EventTriggeringConstraint):
    """AUTOSAR ArbitraryEventTriggering."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    confidence_intervals: list[ConfidenceInterval]
    maximums: list[MultidimensionalTime]
    minimums: list[MultidimensionalTime]
    def __init__(self) -> None:
        """Initialize ArbitraryEventTriggering."""
        super().__init__()
        self.confidence_intervals: list[ConfidenceInterval] = []
        self.maximums: list[MultidimensionalTime] = []
        self.minimums: list[MultidimensionalTime] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ArbitraryEventTriggering":
        """Deserialize XML element to ArbitraryEventTriggering object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ArbitraryEventTriggering object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse confidence_intervals (list)
        obj.confidence_intervals = []
        for child in ARObject._find_all_child_elements(element, "CONFIDENCE-INTERVALS"):
            confidence_intervals_value = ARObject._deserialize_by_tag(child, "ConfidenceInterval")
            obj.confidence_intervals.append(confidence_intervals_value)

        # Parse maximums (list)
        obj.maximums = []
        for child in ARObject._find_all_child_elements(element, "MAXIMUMS"):
            maximums_value = ARObject._deserialize_by_tag(child, "MultidimensionalTime")
            obj.maximums.append(maximums_value)

        # Parse minimums (list)
        obj.minimums = []
        for child in ARObject._find_all_child_elements(element, "MINIMUMS"):
            minimums_value = ARObject._deserialize_by_tag(child, "MultidimensionalTime")
            obj.minimums.append(minimums_value)

        return obj



class ArbitraryEventTriggeringBuilder:
    """Builder for ArbitraryEventTriggering."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ArbitraryEventTriggering = ArbitraryEventTriggering()

    def build(self) -> ArbitraryEventTriggering:
        """Build and return ArbitraryEventTriggering object.

        Returns:
            ArbitraryEventTriggering instance
        """
        # TODO: Add validation
        return self._obj
