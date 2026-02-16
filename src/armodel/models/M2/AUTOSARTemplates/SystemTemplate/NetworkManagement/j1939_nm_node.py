"""J1939NmNode AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_node import (
    NmNode,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.j1939_node_name import (
    J1939NodeName,
)


class J1939NmNode(NmNode):
    """AUTOSAR J1939NmNode."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("address", None, False, False, J1939NmAddressConfigurationCapabilityEnum),  # address
        ("node_name", None, False, False, J1939NodeName),  # nodeName
    ]

    def __init__(self) -> None:
        """Initialize J1939NmNode."""
        super().__init__()
        self.address: Optional[J1939NmAddressConfigurationCapabilityEnum] = None
        self.node_name: Optional[J1939NodeName] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert J1939NmNode to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "J1939NmNode":
        """Create J1939NmNode from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            J1939NmNode instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to J1939NmNode since parent returns ARObject
        return cast("J1939NmNode", obj)


class J1939NmNodeBuilder:
    """Builder for J1939NmNode."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: J1939NmNode = J1939NmNode()

    def build(self) -> J1939NmNode:
        """Build and return J1939NmNode object.

        Returns:
            J1939NmNode instance
        """
        # TODO: Add validation
        return self._obj
