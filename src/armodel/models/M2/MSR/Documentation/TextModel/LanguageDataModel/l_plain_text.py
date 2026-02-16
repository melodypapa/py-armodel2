"""LPlainText AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject


class LPlainText(ARObject):
    """AUTOSAR LPlainText."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize LPlainText."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert LPlainText to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LPlainText":
        """Create LPlainText from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            LPlainText instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to LPlainText since parent returns ARObject
        return cast("LPlainText", obj)


class LPlainTextBuilder:
    """Builder for LPlainText."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LPlainText = LPlainText()

    def build(self) -> LPlainText:
        """Build and return LPlainText object.

        Returns:
            LPlainText instance
        """
        # TODO: Add validation
        return self._obj
