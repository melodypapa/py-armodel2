"""ClientServerAnnotation AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.GeneralAnnotation.general_annotation import (
    GeneralAnnotation,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)


class ClientServerAnnotation(GeneralAnnotation):
    """AUTOSAR ClientServerAnnotation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("operation", None, False, False, ClientServerOperation),  # operation
    ]

    def __init__(self) -> None:
        """Initialize ClientServerAnnotation."""
        super().__init__()
        self.operation: Optional[ClientServerOperation] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ClientServerAnnotation to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ClientServerAnnotation":
        """Create ClientServerAnnotation from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ClientServerAnnotation instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ClientServerAnnotation since parent returns ARObject
        return cast("ClientServerAnnotation", obj)


class ClientServerAnnotationBuilder:
    """Builder for ClientServerAnnotation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ClientServerAnnotation = ClientServerAnnotation()

    def build(self) -> ClientServerAnnotation:
        """Build and return ClientServerAnnotation object.

        Returns:
            ClientServerAnnotation instance
        """
        # TODO: Add validation
        return self._obj
