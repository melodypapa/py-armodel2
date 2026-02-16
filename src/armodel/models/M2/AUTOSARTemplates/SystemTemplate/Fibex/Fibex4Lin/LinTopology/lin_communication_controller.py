"""LinCommunicationController AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class LinCommunicationController(ARObject):
    """AUTOSAR LinCommunicationController."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("protocol_version", None, True, False, None),  # protocolVersion
    ]

    def __init__(self) -> None:
        """Initialize LinCommunicationController."""
        super().__init__()
        self.protocol_version: Optional[String] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert LinCommunicationController to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinCommunicationController":
        """Create LinCommunicationController from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            LinCommunicationController instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to LinCommunicationController since parent returns ARObject
        return cast("LinCommunicationController", obj)


class LinCommunicationControllerBuilder:
    """Builder for LinCommunicationController."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinCommunicationController = LinCommunicationController()

    def build(self) -> LinCommunicationController:
        """Build and return LinCommunicationController object.

        Returns:
            LinCommunicationController instance
        """
        # TODO: Add validation
        return self._obj
