"""ReceiverAnnotation AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.sender_receiver_annotation import (
    SenderReceiverAnnotation,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)


class ReceiverAnnotation(SenderReceiverAnnotation):
    """AUTOSAR ReceiverAnnotation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("signal_age", None, False, False, MultidimensionalTime),  # signalAge
    ]

    def __init__(self) -> None:
        """Initialize ReceiverAnnotation."""
        super().__init__()
        self.signal_age: Optional[MultidimensionalTime] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ReceiverAnnotation to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ReceiverAnnotation":
        """Create ReceiverAnnotation from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ReceiverAnnotation instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ReceiverAnnotation since parent returns ARObject
        return cast("ReceiverAnnotation", obj)


class ReceiverAnnotationBuilder:
    """Builder for ReceiverAnnotation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ReceiverAnnotation = ReceiverAnnotation()

    def build(self) -> ReceiverAnnotation:
        """Build and return ReceiverAnnotation object.

        Returns:
            ReceiverAnnotation instance
        """
        # TODO: Add validation
        return self._obj
