"""TransportProtocolConfiguration AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject


class TransportProtocolConfiguration(ARObject):
    """AUTOSAR TransportProtocolConfiguration."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize TransportProtocolConfiguration."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TransportProtocolConfiguration to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TransportProtocolConfiguration":
        """Create TransportProtocolConfiguration from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TransportProtocolConfiguration instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TransportProtocolConfiguration since parent returns ARObject
        return cast("TransportProtocolConfiguration", obj)


class TransportProtocolConfigurationBuilder:
    """Builder for TransportProtocolConfiguration."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TransportProtocolConfiguration = TransportProtocolConfiguration()

    def build(self) -> TransportProtocolConfiguration:
        """Build and return TransportProtocolConfiguration object.

        Returns:
            TransportProtocolConfiguration instance
        """
        # TODO: Add validation
        return self._obj
