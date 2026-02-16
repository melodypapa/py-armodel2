"""ClientServerOperationMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.data_prototype_mapping import (
    DataPrototypeMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.data_transformation import (
    DataTransformation,
)


class ClientServerOperationMapping(ARObject):
    """AUTOSAR ClientServerOperationMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("arguments", None, False, True, DataPrototypeMapping),  # arguments
        ("first_operation", None, False, False, ClientServerOperation),  # firstOperation
        ("first_to_second", None, False, False, DataTransformation),  # firstToSecond
        ("second", None, False, False, ClientServerOperation),  # second
    ]

    def __init__(self) -> None:
        """Initialize ClientServerOperationMapping."""
        super().__init__()
        self.arguments: list[DataPrototypeMapping] = []
        self.first_operation: Optional[ClientServerOperation] = None
        self.first_to_second: Optional[DataTransformation] = None
        self.second: Optional[ClientServerOperation] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ClientServerOperationMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ClientServerOperationMapping":
        """Create ClientServerOperationMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ClientServerOperationMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ClientServerOperationMapping since parent returns ARObject
        return cast("ClientServerOperationMapping", obj)


class ClientServerOperationMappingBuilder:
    """Builder for ClientServerOperationMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ClientServerOperationMapping = ClientServerOperationMapping()

    def build(self) -> ClientServerOperationMapping:
        """Build and return ClientServerOperationMapping object.

        Returns:
            ClientServerOperationMapping instance
        """
        # TODO: Add validation
        return self._obj
