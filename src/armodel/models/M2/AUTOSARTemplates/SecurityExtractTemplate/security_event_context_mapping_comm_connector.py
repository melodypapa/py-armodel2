"""SecurityEventContextMappingCommConnector AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.security_event_context_mapping import (
    SecurityEventContextMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_connector import (
    CommunicationConnector,
)


class SecurityEventContextMappingCommConnector(SecurityEventContextMapping):
    """AUTOSAR SecurityEventContextMappingCommConnector."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("comm_connectors", None, False, True, CommunicationConnector),  # commConnectors
    ]

    def __init__(self) -> None:
        """Initialize SecurityEventContextMappingCommConnector."""
        super().__init__()
        self.comm_connectors: list[CommunicationConnector] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SecurityEventContextMappingCommConnector to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SecurityEventContextMappingCommConnector":
        """Create SecurityEventContextMappingCommConnector from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SecurityEventContextMappingCommConnector instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SecurityEventContextMappingCommConnector since parent returns ARObject
        return cast("SecurityEventContextMappingCommConnector", obj)


class SecurityEventContextMappingCommConnectorBuilder:
    """Builder for SecurityEventContextMappingCommConnector."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecurityEventContextMappingCommConnector = SecurityEventContextMappingCommConnector()

    def build(self) -> SecurityEventContextMappingCommConnector:
        """Build and return SecurityEventContextMappingCommConnector object.

        Returns:
            SecurityEventContextMappingCommConnector instance
        """
        # TODO: Add validation
        return self._obj
