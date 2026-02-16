"""SlParagraph AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject


class SlParagraph(ARObject):
    """AUTOSAR SlParagraph."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize SlParagraph."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SlParagraph to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SlParagraph":
        """Create SlParagraph from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SlParagraph instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SlParagraph since parent returns ARObject
        return cast("SlParagraph", obj)


class SlParagraphBuilder:
    """Builder for SlParagraph."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SlParagraph = SlParagraph()

    def build(self) -> SlParagraph:
        """Build and return SlParagraph object.

        Returns:
            SlParagraph instance
        """
        # TODO: Add validation
        return self._obj
