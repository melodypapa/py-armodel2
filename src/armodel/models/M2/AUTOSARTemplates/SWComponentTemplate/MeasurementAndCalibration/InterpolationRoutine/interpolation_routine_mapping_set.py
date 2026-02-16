"""InterpolationRoutineMappingSet AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.MeasurementAndCalibration.InterpolationRoutine.interpolation_routine import (
    InterpolationRoutine,
)


class InterpolationRoutineMappingSet(ARElement):
    """AUTOSAR InterpolationRoutineMappingSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("interpolation_routines", None, False, True, InterpolationRoutine),  # interpolationRoutines
    ]

    def __init__(self) -> None:
        """Initialize InterpolationRoutineMappingSet."""
        super().__init__()
        self.interpolation_routines: list[InterpolationRoutine] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert InterpolationRoutineMappingSet to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "InterpolationRoutineMappingSet":
        """Create InterpolationRoutineMappingSet from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            InterpolationRoutineMappingSet instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to InterpolationRoutineMappingSet since parent returns ARObject
        return cast("InterpolationRoutineMappingSet", obj)


class InterpolationRoutineMappingSetBuilder:
    """Builder for InterpolationRoutineMappingSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InterpolationRoutineMappingSet = InterpolationRoutineMappingSet()

    def build(self) -> InterpolationRoutineMappingSet:
        """Build and return InterpolationRoutineMappingSet object.

        Returns:
            InterpolationRoutineMappingSet instance
        """
        # TODO: Add validation
        return self._obj
