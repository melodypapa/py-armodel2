"""OffsetTimingConstraint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 114)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_OffsetConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.timing_constraint import (
    TimingConstraint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)


class OffsetTimingConstraint(TimingConstraint):
    """AUTOSAR OffsetTimingConstraint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    maximum: Optional[MultidimensionalTime]
    minimum: Optional[MultidimensionalTime]
    source: Optional[TimingDescriptionEvent]
    target: Optional[TimingDescriptionEvent]
    def __init__(self) -> None:
        """Initialize OffsetTimingConstraint."""
        super().__init__()
        self.maximum: Optional[MultidimensionalTime] = None
        self.minimum: Optional[MultidimensionalTime] = None
        self.source: Optional[TimingDescriptionEvent] = None
        self.target: Optional[TimingDescriptionEvent] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "OffsetTimingConstraint":
        """Deserialize XML element to OffsetTimingConstraint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized OffsetTimingConstraint object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

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

        # Parse source
        child = ARObject._find_child_element(element, "SOURCE")
        if child is not None:
            source_value = ARObject._deserialize_by_tag(child, "TimingDescriptionEvent")
            obj.source = source_value

        # Parse target
        child = ARObject._find_child_element(element, "TARGET")
        if child is not None:
            target_value = ARObject._deserialize_by_tag(child, "TimingDescriptionEvent")
            obj.target = target_value

        return obj



class OffsetTimingConstraintBuilder:
    """Builder for OffsetTimingConstraint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: OffsetTimingConstraint = OffsetTimingConstraint()

    def build(self) -> OffsetTimingConstraint:
        """Build and return OffsetTimingConstraint object.

        Returns:
            OffsetTimingConstraint instance
        """
        # TODO: Add validation
        return self._obj
