"""CommunicationController AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class CommunicationController(ARObject):
    """AUTOSAR CommunicationController."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("wake_up_by", None, True, False, None),  # wakeUpBy
    ]

    def __init__(self) -> None:
        """Initialize CommunicationController."""
        super().__init__()
        self.wake_up_by: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CommunicationController to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CommunicationController":
        """Create CommunicationController from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CommunicationController instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CommunicationController since parent returns ARObject
        return cast("CommunicationController", obj)


class CommunicationControllerBuilder:
    """Builder for CommunicationController."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CommunicationController = CommunicationController()

    def build(self) -> CommunicationController:
        """Build and return CommunicationController object.

        Returns:
            CommunicationController instance
        """
        # TODO: Add validation
        return self._obj
