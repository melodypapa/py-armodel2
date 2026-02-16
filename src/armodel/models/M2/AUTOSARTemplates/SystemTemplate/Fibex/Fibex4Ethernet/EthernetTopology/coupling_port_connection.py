"""CouplingPortConnection AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port import (
    CouplingPort,
)


class CouplingPortConnection(ARObject):
    """AUTOSAR CouplingPortConnection."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("first_port", None, False, False, CouplingPort),  # firstPort
        ("node_ports", None, False, True, CouplingPort),  # nodePorts
        ("plca_local_node", None, True, False, None),  # plcaLocalNode
        ("plca_transmit", None, True, False, None),  # plcaTransmit
        ("second_port", None, False, False, CouplingPort),  # secondPort
    ]

    def __init__(self) -> None:
        """Initialize CouplingPortConnection."""
        super().__init__()
        self.first_port: Optional[CouplingPort] = None
        self.node_ports: list[CouplingPort] = []
        self.plca_local_node: Optional[PositiveInteger] = None
        self.plca_transmit: Optional[PositiveInteger] = None
        self.second_port: Optional[CouplingPort] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CouplingPortConnection to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CouplingPortConnection":
        """Create CouplingPortConnection from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CouplingPortConnection instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CouplingPortConnection since parent returns ARObject
        return cast("CouplingPortConnection", obj)


class CouplingPortConnectionBuilder:
    """Builder for CouplingPortConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CouplingPortConnection = CouplingPortConnection()

    def build(self) -> CouplingPortConnection:
        """Build and return CouplingPortConnection object.

        Returns:
            CouplingPortConnection instance
        """
        # TODO: Add validation
        return self._obj
