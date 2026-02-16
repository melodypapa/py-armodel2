"""CommunicationBufferLocking AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions.swc_supported_feature import (
    SwcSupportedFeature,
)


class CommunicationBufferLocking(SwcSupportedFeature):
    """AUTOSAR CommunicationBufferLocking."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("support_buffer_locking", None, False, False, SupportBufferLockingEnum),  # supportBufferLocking
    ]

    def __init__(self) -> None:
        """Initialize CommunicationBufferLocking."""
        super().__init__()
        self.support_buffer_locking: Optional[SupportBufferLockingEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CommunicationBufferLocking to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CommunicationBufferLocking":
        """Create CommunicationBufferLocking from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CommunicationBufferLocking instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CommunicationBufferLocking since parent returns ARObject
        return cast("CommunicationBufferLocking", obj)


class CommunicationBufferLockingBuilder:
    """Builder for CommunicationBufferLocking."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CommunicationBufferLocking = CommunicationBufferLocking()

    def build(self) -> CommunicationBufferLocking:
        """Build and return CommunicationBufferLocking object.

        Returns:
            CommunicationBufferLocking instance
        """
        # TODO: Add validation
        return self._obj
