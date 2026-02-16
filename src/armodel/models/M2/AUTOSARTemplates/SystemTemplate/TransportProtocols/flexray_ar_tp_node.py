"""FlexrayArTpNode AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_address import (
    TpAddress,
)


class FlexrayArTpNode(Identifiable):
    """AUTOSAR FlexrayArTpNode."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("connectors", None, False, True, any (FlexrayCommunication)),  # connectors
        ("tp_address", None, False, False, TpAddress),  # tpAddress
    ]

    def __init__(self) -> None:
        """Initialize FlexrayArTpNode."""
        super().__init__()
        self.connectors: list[Any] = []
        self.tp_address: Optional[TpAddress] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert FlexrayArTpNode to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayArTpNode":
        """Create FlexrayArTpNode from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            FlexrayArTpNode instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to FlexrayArTpNode since parent returns ARObject
        return cast("FlexrayArTpNode", obj)


class FlexrayArTpNodeBuilder:
    """Builder for FlexrayArTpNode."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayArTpNode = FlexrayArTpNode()

    def build(self) -> FlexrayArTpNode:
        """Build and return FlexrayArTpNode object.

        Returns:
            FlexrayArTpNode instance
        """
        # TODO: Add validation
        return self._obj
