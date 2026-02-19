"""LatencyTimingConstraint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 95)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_LatencyTimingConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.timing_constraint import (
    TimingConstraint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.LatencyTimingConstraint import (
    LatencyConstraintTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)


class LatencyTimingConstraint(TimingConstraint):
    """AUTOSAR LatencyTimingConstraint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    latency: Optional[LatencyConstraintTypeEnum]
    maximum: Optional[MultidimensionalTime]
    minimum: Optional[MultidimensionalTime]
    nominal: Optional[MultidimensionalTime]
    scope: Optional[TimingDescriptionEvent]
    def __init__(self) -> None:
        """Initialize LatencyTimingConstraint."""
        super().__init__()
        self.latency: Optional[LatencyConstraintTypeEnum] = None
        self.maximum: Optional[MultidimensionalTime] = None
        self.minimum: Optional[MultidimensionalTime] = None
        self.nominal: Optional[MultidimensionalTime] = None
        self.scope: Optional[TimingDescriptionEvent] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "LatencyTimingConstraint":
        """Deserialize XML element to LatencyTimingConstraint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LatencyTimingConstraint object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse latency
        child = ARObject._find_child_element(element, "LATENCY")
        if child is not None:
            latency_value = child.text
            obj.latency = latency_value

        # Parse maximum
        child = ARObject._find_child_element(element, "MAXIMUM")
        if child is not None:
            maximum_value = ARObject._deserialize_by_tag(child, "MultidimensionalTime")
            obj.maximum = maximum_value

        # Parse minimum
        child = ARObject._find_child_element(element, "MINIMUM")
        if child is not None:
            minimum_value = ARObject._deserialize_by_tag(child, "MultidimensionalTime")
            obj.minimum = minimum_value

        # Parse nominal
        child = ARObject._find_child_element(element, "NOMINAL")
        if child is not None:
            nominal_value = ARObject._deserialize_by_tag(child, "MultidimensionalTime")
            obj.nominal = nominal_value

        # Parse scope
        child = ARObject._find_child_element(element, "SCOPE")
        if child is not None:
            scope_value = ARObject._deserialize_by_tag(child, "TimingDescriptionEvent")
            obj.scope = scope_value

        return obj



class LatencyTimingConstraintBuilder:
    """Builder for LatencyTimingConstraint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LatencyTimingConstraint = LatencyTimingConstraint()

    def build(self) -> LatencyTimingConstraint:
        """Build and return LatencyTimingConstraint object.

        Returns:
            LatencyTimingConstraint instance
        """
        # TODO: Add validation
        return self._obj
