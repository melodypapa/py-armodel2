"""CommunicationControllerMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_controller import (
    CommunicationController,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_element import (
    HwElement,
)


class CommunicationControllerMapping(ARObject):
    """AUTOSAR CommunicationControllerMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("communication_controller", None, False, False, CommunicationController),  # communicationController
        ("hw", None, False, False, HwElement),  # hw
    ]

    def __init__(self) -> None:
        """Initialize CommunicationControllerMapping."""
        super().__init__()
        self.communication_controller: Optional[CommunicationController] = None
        self.hw: Optional[HwElement] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CommunicationControllerMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CommunicationControllerMapping":
        """Create CommunicationControllerMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CommunicationControllerMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CommunicationControllerMapping since parent returns ARObject
        return cast("CommunicationControllerMapping", obj)


class CommunicationControllerMappingBuilder:
    """Builder for CommunicationControllerMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CommunicationControllerMapping = CommunicationControllerMapping()

    def build(self) -> CommunicationControllerMapping:
        """Build and return CommunicationControllerMapping object.

        Returns:
            CommunicationControllerMapping instance
        """
        # TODO: Add validation
        return self._obj
