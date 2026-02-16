"""ClientIdDefinition AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)


class ClientIdDefinition(Identifiable):
    """AUTOSAR ClientIdDefinition."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("client_id", None, True, False, None),  # clientId
        ("client_server_instance_ref", None, False, False, ClientServerOperation),  # clientServerInstanceRef
    ]

    def __init__(self) -> None:
        """Initialize ClientIdDefinition."""
        super().__init__()
        self.client_id: Optional[Numerical] = None
        self.client_server_instance_ref: Optional[ClientServerOperation] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ClientIdDefinition to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ClientIdDefinition":
        """Create ClientIdDefinition from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ClientIdDefinition instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ClientIdDefinition since parent returns ARObject
        return cast("ClientIdDefinition", obj)


class ClientIdDefinitionBuilder:
    """Builder for ClientIdDefinition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ClientIdDefinition = ClientIdDefinition()

    def build(self) -> ClientIdDefinition:
        """Build and return ClientIdDefinition object.

        Returns:
            ClientIdDefinition instance
        """
        # TODO: Add validation
        return self._obj
