"""ConstantSpecificationMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.constant_specification import (
    ConstantSpecification,
)


class ConstantSpecificationMapping(ARObject):
    """AUTOSAR ConstantSpecificationMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("appl_constant", None, False, False, ConstantSpecification),  # applConstant
        ("impl_constant", None, False, False, ConstantSpecification),  # implConstant
    ]

    def __init__(self) -> None:
        """Initialize ConstantSpecificationMapping."""
        super().__init__()
        self.appl_constant: Optional[ConstantSpecification] = None
        self.impl_constant: Optional[ConstantSpecification] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ConstantSpecificationMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ConstantSpecificationMapping":
        """Create ConstantSpecificationMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ConstantSpecificationMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ConstantSpecificationMapping since parent returns ARObject
        return cast("ConstantSpecificationMapping", obj)


class ConstantSpecificationMappingBuilder:
    """Builder for ConstantSpecificationMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ConstantSpecificationMapping = ConstantSpecificationMapping()

    def build(self) -> ConstantSpecificationMapping:
        """Build and return ConstantSpecificationMapping object.

        Returns:
            ConstantSpecificationMapping instance
        """
        # TODO: Add validation
        return self._obj
