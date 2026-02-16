"""TextTableValuePair AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
)


class TextTableValuePair(ARObject):
    """AUTOSAR TextTableValuePair."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("first_value", None, True, False, None),  # firstValue
        ("second_value", None, True, False, None),  # secondValue
    ]

    def __init__(self) -> None:
        """Initialize TextTableValuePair."""
        super().__init__()
        self.first_value: Optional[Numerical] = None
        self.second_value: Optional[Numerical] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TextTableValuePair to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TextTableValuePair":
        """Create TextTableValuePair from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TextTableValuePair instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TextTableValuePair since parent returns ARObject
        return cast("TextTableValuePair", obj)


class TextTableValuePairBuilder:
    """Builder for TextTableValuePair."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TextTableValuePair = TextTableValuePair()

    def build(self) -> TextTableValuePair:
        """Build and return TextTableValuePair object.

        Returns:
            TextTableValuePair instance
        """
        # TODO: Add validation
        return self._obj
