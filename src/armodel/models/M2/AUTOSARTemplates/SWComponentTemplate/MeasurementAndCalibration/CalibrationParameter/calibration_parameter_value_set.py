"""CalibrationParameterValueSet AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)


class CalibrationParameterValueSet(ARElement):
    """AUTOSAR CalibrationParameterValueSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("calibrations", None, False, True, any (CalibrationParameter)),  # calibrations
    ]

    def __init__(self) -> None:
        """Initialize CalibrationParameterValueSet."""
        super().__init__()
        self.calibrations: list[Any] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CalibrationParameterValueSet to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CalibrationParameterValueSet":
        """Create CalibrationParameterValueSet from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CalibrationParameterValueSet instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CalibrationParameterValueSet since parent returns ARObject
        return cast("CalibrationParameterValueSet", obj)


class CalibrationParameterValueSetBuilder:
    """Builder for CalibrationParameterValueSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CalibrationParameterValueSet = CalibrationParameterValueSet()

    def build(self) -> CalibrationParameterValueSet:
        """Build and return CalibrationParameterValueSet object.

        Returns:
            CalibrationParameterValueSet instance
        """
        # TODO: Add validation
        return self._obj
