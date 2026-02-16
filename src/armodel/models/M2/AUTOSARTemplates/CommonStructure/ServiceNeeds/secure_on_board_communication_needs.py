"""SecureOnBoardCommunicationNeeds AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)


class SecureOnBoardCommunicationNeeds(ServiceNeeds):
    """AUTOSAR SecureOnBoardCommunicationNeeds."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("verification", None, False, False, VerificationStatusIndicationModeEnum),  # verification
    ]

    def __init__(self) -> None:
        """Initialize SecureOnBoardCommunicationNeeds."""
        super().__init__()
        self.verification: Optional[VerificationStatusIndicationModeEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SecureOnBoardCommunicationNeeds to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SecureOnBoardCommunicationNeeds":
        """Create SecureOnBoardCommunicationNeeds from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SecureOnBoardCommunicationNeeds instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SecureOnBoardCommunicationNeeds since parent returns ARObject
        return cast("SecureOnBoardCommunicationNeeds", obj)


class SecureOnBoardCommunicationNeedsBuilder:
    """Builder for SecureOnBoardCommunicationNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecureOnBoardCommunicationNeeds = SecureOnBoardCommunicationNeeds()

    def build(self) -> SecureOnBoardCommunicationNeeds:
        """Build and return SecureOnBoardCommunicationNeeds object.

        Returns:
            SecureOnBoardCommunicationNeeds instance
        """
        # TODO: Add validation
        return self._obj
