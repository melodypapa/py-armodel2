"""ClientServerApplicationErrorMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.application_error import (
    ApplicationError,
)


class ClientServerApplicationErrorMapping(ARObject):
    """AUTOSAR ClientServerApplicationErrorMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("first_application", None, False, False, ApplicationError),  # firstApplication
        ("second", None, False, False, ApplicationError),  # second
    ]

    def __init__(self) -> None:
        """Initialize ClientServerApplicationErrorMapping."""
        super().__init__()
        self.first_application: Optional[ApplicationError] = None
        self.second: Optional[ApplicationError] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ClientServerApplicationErrorMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ClientServerApplicationErrorMapping":
        """Create ClientServerApplicationErrorMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ClientServerApplicationErrorMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ClientServerApplicationErrorMapping since parent returns ARObject
        return cast("ClientServerApplicationErrorMapping", obj)


class ClientServerApplicationErrorMappingBuilder:
    """Builder for ClientServerApplicationErrorMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ClientServerApplicationErrorMapping = ClientServerApplicationErrorMapping()

    def build(self) -> ClientServerApplicationErrorMapping:
        """Build and return ClientServerApplicationErrorMapping object.

        Returns:
            ClientServerApplicationErrorMapping instance
        """
        # TODO: Add validation
        return self._obj
