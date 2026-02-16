"""DefaultValueElement AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class DefaultValueElement(ARObject):
    """AUTOSAR DefaultValueElement."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("element_byte_value", None, True, False, None),  # elementByteValue
        ("element_position", None, True, False, None),  # elementPosition
    ]

    def __init__(self) -> None:
        """Initialize DefaultValueElement."""
        super().__init__()
        self.element_byte_value: Optional[Integer] = None
        self.element_position: Optional[Integer] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DefaultValueElement to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DefaultValueElement":
        """Create DefaultValueElement from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DefaultValueElement instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DefaultValueElement since parent returns ARObject
        return cast("DefaultValueElement", obj)


class DefaultValueElementBuilder:
    """Builder for DefaultValueElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DefaultValueElement = DefaultValueElement()

    def build(self) -> DefaultValueElement:
        """Build and return DefaultValueElement object.

        Returns:
            DefaultValueElement instance
        """
        # TODO: Add validation
        return self._obj
