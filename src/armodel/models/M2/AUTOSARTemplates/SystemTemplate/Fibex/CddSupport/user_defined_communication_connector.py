"""UserDefinedCommunicationConnector AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_connector import (
    CommunicationConnector,
)


class UserDefinedCommunicationConnector(CommunicationConnector):
    """AUTOSAR UserDefinedCommunicationConnector."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize UserDefinedCommunicationConnector."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert UserDefinedCommunicationConnector to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "UserDefinedCommunicationConnector":
        """Create UserDefinedCommunicationConnector from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            UserDefinedCommunicationConnector instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to UserDefinedCommunicationConnector since parent returns ARObject
        return cast("UserDefinedCommunicationConnector", obj)


class UserDefinedCommunicationConnectorBuilder:
    """Builder for UserDefinedCommunicationConnector."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UserDefinedCommunicationConnector = UserDefinedCommunicationConnector()

    def build(self) -> UserDefinedCommunicationConnector:
        """Build and return UserDefinedCommunicationConnector object.

        Returns:
            UserDefinedCommunicationConnector instance
        """
        # TODO: Add validation
        return self._obj
