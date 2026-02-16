"""LLongName AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class LLongName(ARObject):
    """AUTOSAR LLongName."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("blueprint_value", None, True, False, None),  # blueprintValue
    ]

    def __init__(self) -> None:
        """Initialize LLongName."""
        super().__init__()
        self.blueprint_value: Optional[String] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert LLongName to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LLongName":
        """Create LLongName from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            LLongName instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to LLongName since parent returns ARObject
        return cast("LLongName", obj)


class LLongNameBuilder:
    """Builder for LLongName."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LLongName = LLongName()

    def build(self) -> LLongName:
        """Build and return LLongName object.

        Returns:
            LLongName instance
        """
        # TODO: Add validation
        return self._obj
