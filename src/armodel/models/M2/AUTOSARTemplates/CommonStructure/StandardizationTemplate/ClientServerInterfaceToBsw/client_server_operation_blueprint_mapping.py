"""ClientServerOperationBlueprintMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_entry import (
    BswModuleEntry,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)


class ClientServerOperationBlueprintMapping(ARObject):
    """AUTOSAR ClientServerOperationBlueprintMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("blueprint", None, False, False, DocumentationBlock),  # blueprint
        ("bsw_module_entry", None, False, False, BswModuleEntry),  # bswModuleEntry
        ("client_server", None, False, False, ClientServerOperation),  # clientServer
    ]

    def __init__(self) -> None:
        """Initialize ClientServerOperationBlueprintMapping."""
        super().__init__()
        self.blueprint: Optional[DocumentationBlock] = None
        self.bsw_module_entry: BswModuleEntry = None
        self.client_server: ClientServerOperation = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ClientServerOperationBlueprintMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ClientServerOperationBlueprintMapping":
        """Create ClientServerOperationBlueprintMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ClientServerOperationBlueprintMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ClientServerOperationBlueprintMapping since parent returns ARObject
        return cast("ClientServerOperationBlueprintMapping", obj)


class ClientServerOperationBlueprintMappingBuilder:
    """Builder for ClientServerOperationBlueprintMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ClientServerOperationBlueprintMapping = ClientServerOperationBlueprintMapping()

    def build(self) -> ClientServerOperationBlueprintMapping:
        """Build and return ClientServerOperationBlueprintMapping object.

        Returns:
            ClientServerOperationBlueprintMapping instance
        """
        # TODO: Add validation
        return self._obj
