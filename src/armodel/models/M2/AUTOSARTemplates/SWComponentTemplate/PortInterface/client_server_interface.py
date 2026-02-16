"""ClientServerInterface AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface import (
    PortInterface,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.application_error import (
    ApplicationError,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)


class ClientServerInterface(PortInterface):
    """AUTOSAR ClientServerInterface."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("operations", None, False, True, ClientServerOperation),  # operations
        ("possible_errors", None, False, True, ApplicationError),  # possibleErrors
    ]

    def __init__(self) -> None:
        """Initialize ClientServerInterface."""
        super().__init__()
        self.operations: list[ClientServerOperation] = []
        self.possible_errors: list[ApplicationError] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ClientServerInterface to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ClientServerInterface":
        """Create ClientServerInterface from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ClientServerInterface instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ClientServerInterface since parent returns ARObject
        return cast("ClientServerInterface", obj)


class ClientServerInterfaceBuilder:
    """Builder for ClientServerInterface."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ClientServerInterface = ClientServerInterface()

    def build(self) -> ClientServerInterface:
        """Build and return ClientServerInterface object.

        Returns:
            ClientServerInterface instance
        """
        # TODO: Add validation
        return self._obj
