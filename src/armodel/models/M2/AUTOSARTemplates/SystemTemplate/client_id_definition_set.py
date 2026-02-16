"""ClientIdDefinitionSet AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.client_id_definition import (
    ClientIdDefinition,
)


class ClientIdDefinitionSet(ARElement):
    """AUTOSAR ClientIdDefinitionSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("client_ids", None, False, True, ClientIdDefinition),  # clientIds
    ]

    def __init__(self) -> None:
        """Initialize ClientIdDefinitionSet."""
        super().__init__()
        self.client_ids: list[ClientIdDefinition] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ClientIdDefinitionSet to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ClientIdDefinitionSet":
        """Create ClientIdDefinitionSet from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ClientIdDefinitionSet instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ClientIdDefinitionSet since parent returns ARObject
        return cast("ClientIdDefinitionSet", obj)


class ClientIdDefinitionSetBuilder:
    """Builder for ClientIdDefinitionSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ClientIdDefinitionSet = ClientIdDefinitionSet()

    def build(self) -> ClientIdDefinitionSet:
        """Build and return ClientIdDefinitionSet object.

        Returns:
            ClientIdDefinitionSet instance
        """
        # TODO: Add validation
        return self._obj
