"""ClientServerInterfaceToBswModuleEntryBlueprintMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_interface import (
    ClientServerInterface,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions.port_defined_argument_value import (
    PortDefinedArgumentValue,
)


class ClientServerInterfaceToBswModuleEntryBlueprintMapping(ARElement):
    """AUTOSAR ClientServerInterfaceToBswModuleEntryBlueprintMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("client_server", None, False, False, ClientServerInterface),  # clientServer
        ("operation", None, False, False, ClientServerOperation),  # operation
        ("port_defined_arguments", None, False, True, PortDefinedArgumentValue),  # portDefinedArguments
    ]

    def __init__(self) -> None:
        """Initialize ClientServerInterfaceToBswModuleEntryBlueprintMapping."""
        super().__init__()
        self.client_server: ClientServerInterface = None
        self.operation: ClientServerOperation = None
        self.port_defined_arguments: list[PortDefinedArgumentValue] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ClientServerInterfaceToBswModuleEntryBlueprintMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ClientServerInterfaceToBswModuleEntryBlueprintMapping":
        """Create ClientServerInterfaceToBswModuleEntryBlueprintMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ClientServerInterfaceToBswModuleEntryBlueprintMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ClientServerInterfaceToBswModuleEntryBlueprintMapping since parent returns ARObject
        return cast("ClientServerInterfaceToBswModuleEntryBlueprintMapping", obj)


class ClientServerInterfaceToBswModuleEntryBlueprintMappingBuilder:
    """Builder for ClientServerInterfaceToBswModuleEntryBlueprintMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ClientServerInterfaceToBswModuleEntryBlueprintMapping = ClientServerInterfaceToBswModuleEntryBlueprintMapping()

    def build(self) -> ClientServerInterfaceToBswModuleEntryBlueprintMapping:
        """Build and return ClientServerInterfaceToBswModuleEntryBlueprintMapping object.

        Returns:
            ClientServerInterfaceToBswModuleEntryBlueprintMapping instance
        """
        # TODO: Add validation
        return self._obj
