"""AgeConstraint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 115)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_AgeConstraint.classes.json"""

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


class AgeConstraint(TimingConstraint):
    """AUTOSAR AgeConstraint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    maximum: Optional[MultidimensionalTime]
    minimum: Optional[MultidimensionalTime]
    scope: Optional[TimingDescriptionEvent]
    def __init__(self) -> None:
        """Initialize AgeConstraint."""
        super().__init__()
        self.maximum: Optional[MultidimensionalTime] = None
        self.minimum: Optional[MultidimensionalTime] = None
        self.scope: Optional[TimingDescriptionEvent] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "AgeConstraint":
        """Deserialize XML element to AgeConstraint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AgeConstraint object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AgeConstraint, cls).deserialize(element)

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

        # Parse scope
        child = ARObject._find_child_element(element, "SCOPE")
        if child is not None:
            scope_value = ARObject._deserialize_by_tag(child, "TimingDescriptionEvent")
            obj.scope = scope_value

        return obj



class AgeConstraintBuilder:
    """Builder for AgeConstraint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AgeConstraint = AgeConstraint()

    def build(self) -> AgeConstraint:
        """Build and return AgeConstraint object.

        Returns:
            AgeConstraint instance
        """
        # TODO: Add validation
        return self._obj
