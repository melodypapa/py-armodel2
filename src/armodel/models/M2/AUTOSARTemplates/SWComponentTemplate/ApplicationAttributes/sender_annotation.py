"""SenderAnnotation AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.sender_receiver_annotation import (
    SenderReceiverAnnotation,
)


class SenderAnnotation(SenderReceiverAnnotation):
    """AUTOSAR SenderAnnotation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize SenderAnnotation."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SenderAnnotation to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SenderAnnotation":
        """Create SenderAnnotation from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SenderAnnotation instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SenderAnnotation since parent returns ARObject
        return cast("SenderAnnotation", obj)


class SenderAnnotationBuilder:
    """Builder for SenderAnnotation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SenderAnnotation = SenderAnnotation()

    def build(self) -> SenderAnnotation:
        """Build and return SenderAnnotation object.

        Returns:
            SenderAnnotation instance
        """
        # TODO: Add validation
        return self._obj
