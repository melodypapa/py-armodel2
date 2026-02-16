"""ConstantSpecification AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
    ValueSpecification,
)


class ConstantSpecification(ARElement):
    """AUTOSAR ConstantSpecification."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("value_spec", None, False, False, ValueSpecification),  # valueSpec
    ]

    def __init__(self) -> None:
        """Initialize ConstantSpecification."""
        super().__init__()
        self.value_spec: Optional[ValueSpecification] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ConstantSpecification to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ConstantSpecification":
        """Create ConstantSpecification from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ConstantSpecification instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ConstantSpecification since parent returns ARObject
        return cast("ConstantSpecification", obj)


class ConstantSpecificationBuilder:
    """Builder for ConstantSpecification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ConstantSpecification = ConstantSpecification()

    def build(self) -> ConstantSpecification:
        """Build and return ConstantSpecification object.

        Returns:
            ConstantSpecification instance
        """
        # TODO: Add validation
        return self._obj
