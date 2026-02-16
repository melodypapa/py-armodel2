"""ClientServerInterfaceMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface_mapping import (
    PortInterfaceMapping,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_application_error_mapping import (
    ClientServerApplicationErrorMapping,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)


class ClientServerInterfaceMapping(PortInterfaceMapping):
    """AUTOSAR ClientServerInterfaceMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("error_mappings", None, False, True, ClientServerApplicationErrorMapping),  # errorMappings
        ("operations", None, False, True, ClientServerOperation),  # operations
    ]

    def __init__(self) -> None:
        """Initialize ClientServerInterfaceMapping."""
        super().__init__()
        self.error_mappings: list[ClientServerApplicationErrorMapping] = []
        self.operations: list[ClientServerOperation] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ClientServerInterfaceMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ClientServerInterfaceMapping":
        """Create ClientServerInterfaceMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ClientServerInterfaceMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ClientServerInterfaceMapping since parent returns ARObject
        return cast("ClientServerInterfaceMapping", obj)


class ClientServerInterfaceMappingBuilder:
    """Builder for ClientServerInterfaceMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ClientServerInterfaceMapping = ClientServerInterfaceMapping()

    def build(self) -> ClientServerInterfaceMapping:
        """Build and return ClientServerInterfaceMapping object.

        Returns:
            ClientServerInterfaceMapping instance
        """
        # TODO: Add validation
        return self._obj
