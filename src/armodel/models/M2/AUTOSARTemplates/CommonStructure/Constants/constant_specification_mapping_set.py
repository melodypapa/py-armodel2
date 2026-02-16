"""ConstantSpecificationMappingSet AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.constant_specification import (
    ConstantSpecification,
)


class ConstantSpecificationMappingSet(ARElement):
    """AUTOSAR ConstantSpecificationMappingSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("mappings", None, False, True, ConstantSpecification),  # mappings
    ]

    def __init__(self) -> None:
        """Initialize ConstantSpecificationMappingSet."""
        super().__init__()
        self.mappings: list[ConstantSpecification] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ConstantSpecificationMappingSet to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ConstantSpecificationMappingSet":
        """Create ConstantSpecificationMappingSet from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ConstantSpecificationMappingSet instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ConstantSpecificationMappingSet since parent returns ARObject
        return cast("ConstantSpecificationMappingSet", obj)


class ConstantSpecificationMappingSetBuilder:
    """Builder for ConstantSpecificationMappingSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ConstantSpecificationMappingSet = ConstantSpecificationMappingSet()

    def build(self) -> ConstantSpecificationMappingSet:
        """Build and return ConstantSpecificationMappingSet object.

        Returns:
            ConstantSpecificationMappingSet instance
        """
        # TODO: Add validation
        return self._obj
