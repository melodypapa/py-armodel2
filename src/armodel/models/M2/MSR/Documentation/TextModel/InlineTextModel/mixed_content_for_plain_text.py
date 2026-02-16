"""MixedContentForPlainText AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject


class MixedContentForPlainText(ARObject):
    """AUTOSAR MixedContentForPlainText."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize MixedContentForPlainText."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert MixedContentForPlainText to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MixedContentForPlainText":
        """Create MixedContentForPlainText from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            MixedContentForPlainText instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to MixedContentForPlainText since parent returns ARObject
        return cast("MixedContentForPlainText", obj)


class MixedContentForPlainTextBuilder:
    """Builder for MixedContentForPlainText."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MixedContentForPlainText = MixedContentForPlainText()

    def build(self) -> MixedContentForPlainText:
        """Build and return MixedContentForPlainText object.

        Returns:
            MixedContentForPlainText instance
        """
        # TODO: Add validation
        return self._obj
