"""J1939TpNode AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_address import (
    TpAddress,
)


class J1939TpNode(Identifiable):
    """AUTOSAR J1939TpNode."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("connector", None, False, False, any (Communication)),  # connector
        ("tp_address", None, False, False, TpAddress),  # tpAddress
    ]

    def __init__(self) -> None:
        """Initialize J1939TpNode."""
        super().__init__()
        self.connector: Optional[Any] = None
        self.tp_address: Optional[TpAddress] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert J1939TpNode to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "J1939TpNode":
        """Create J1939TpNode from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            J1939TpNode instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to J1939TpNode since parent returns ARObject
        return cast("J1939TpNode", obj)


class J1939TpNodeBuilder:
    """Builder for J1939TpNode."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: J1939TpNode = J1939TpNode()

    def build(self) -> J1939TpNode:
        """Build and return J1939TpNode object.

        Returns:
            J1939TpNode instance
        """
        # TODO: Add validation
        return self._obj
