"""J1939ControllerApplicationToJ1939NmNodeMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.j1939_nm_node import (
    J1939NmNode,
)


class J1939ControllerApplicationToJ1939NmNodeMapping(ARObject):
    """AUTOSAR J1939ControllerApplicationToJ1939NmNodeMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("j1939_controller", None, False, False, any (J1939Controller)),  # j1939Controller
        ("j1939_nm_node", None, False, False, J1939NmNode),  # j1939NmNode
    ]

    def __init__(self) -> None:
        """Initialize J1939ControllerApplicationToJ1939NmNodeMapping."""
        super().__init__()
        self.j1939_controller: Optional[Any] = None
        self.j1939_nm_node: Optional[J1939NmNode] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert J1939ControllerApplicationToJ1939NmNodeMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "J1939ControllerApplicationToJ1939NmNodeMapping":
        """Create J1939ControllerApplicationToJ1939NmNodeMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            J1939ControllerApplicationToJ1939NmNodeMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to J1939ControllerApplicationToJ1939NmNodeMapping since parent returns ARObject
        return cast("J1939ControllerApplicationToJ1939NmNodeMapping", obj)


class J1939ControllerApplicationToJ1939NmNodeMappingBuilder:
    """Builder for J1939ControllerApplicationToJ1939NmNodeMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: J1939ControllerApplicationToJ1939NmNodeMapping = J1939ControllerApplicationToJ1939NmNodeMapping()

    def build(self) -> J1939ControllerApplicationToJ1939NmNodeMapping:
        """Build and return J1939ControllerApplicationToJ1939NmNodeMapping object.

        Returns:
            J1939ControllerApplicationToJ1939NmNodeMapping instance
        """
        # TODO: Add validation
        return self._obj
