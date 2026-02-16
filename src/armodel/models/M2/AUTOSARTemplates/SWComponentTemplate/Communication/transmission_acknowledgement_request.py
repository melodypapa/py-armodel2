"""TransmissionAcknowledgementRequest AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class TransmissionAcknowledgementRequest(ARObject):
    """AUTOSAR TransmissionAcknowledgementRequest."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("timeout", None, True, False, None),  # timeout
    ]

    def __init__(self) -> None:
        """Initialize TransmissionAcknowledgementRequest."""
        super().__init__()
        self.timeout: Optional[TimeValue] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TransmissionAcknowledgementRequest to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TransmissionAcknowledgementRequest":
        """Create TransmissionAcknowledgementRequest from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TransmissionAcknowledgementRequest instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TransmissionAcknowledgementRequest since parent returns ARObject
        return cast("TransmissionAcknowledgementRequest", obj)


class TransmissionAcknowledgementRequestBuilder:
    """Builder for TransmissionAcknowledgementRequest."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TransmissionAcknowledgementRequest = TransmissionAcknowledgementRequest()

    def build(self) -> TransmissionAcknowledgementRequest:
        """Build and return TransmissionAcknowledgementRequest object.

        Returns:
            TransmissionAcknowledgementRequest instance
        """
        # TODO: Add validation
        return self._obj
