"""AbstractCanCommunicationConnector AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_connector import (
    CommunicationConnector,
)


class AbstractCanCommunicationConnector(CommunicationConnector):
    """AUTOSAR AbstractCanCommunicationConnector."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize AbstractCanCommunicationConnector."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert AbstractCanCommunicationConnector to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractCanCommunicationConnector":
        """Create AbstractCanCommunicationConnector from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            AbstractCanCommunicationConnector instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to AbstractCanCommunicationConnector since parent returns ARObject
        return cast("AbstractCanCommunicationConnector", obj)


class AbstractCanCommunicationConnectorBuilder:
    """Builder for AbstractCanCommunicationConnector."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractCanCommunicationConnector = AbstractCanCommunicationConnector()

    def build(self) -> AbstractCanCommunicationConnector:
        """Build and return AbstractCanCommunicationConnector object.

        Returns:
            AbstractCanCommunicationConnector instance
        """
        # TODO: Add validation
        return self._obj
