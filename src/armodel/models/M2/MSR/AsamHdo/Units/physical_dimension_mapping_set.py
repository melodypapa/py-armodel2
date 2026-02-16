"""PhysicalDimensionMappingSet AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.MSR.AsamHdo.Units.physical_dimension import (
    PhysicalDimension,
)


class PhysicalDimensionMappingSet(ARElement):
    """AUTOSAR PhysicalDimensionMappingSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("physicals", None, False, True, PhysicalDimension),  # physicals
    ]

    def __init__(self) -> None:
        """Initialize PhysicalDimensionMappingSet."""
        super().__init__()
        self.physicals: list[PhysicalDimension] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert PhysicalDimensionMappingSet to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PhysicalDimensionMappingSet":
        """Create PhysicalDimensionMappingSet from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            PhysicalDimensionMappingSet instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to PhysicalDimensionMappingSet since parent returns ARObject
        return cast("PhysicalDimensionMappingSet", obj)


class PhysicalDimensionMappingSetBuilder:
    """Builder for PhysicalDimensionMappingSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PhysicalDimensionMappingSet = PhysicalDimensionMappingSet()

    def build(self) -> PhysicalDimensionMappingSet:
        """Build and return PhysicalDimensionMappingSet object.

        Returns:
            PhysicalDimensionMappingSet instance
        """
        # TODO: Add validation
        return self._obj
