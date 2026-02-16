"""CouplingPortConnection AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "first_port": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CouplingPort,
        ),  # firstPort
        "node_ports": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=CouplingPort,
        ),  # nodePorts
        "plca_local_node": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # plcaLocalNode
        "plca_transmit": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # plcaTransmit
        "second_port": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CouplingPort,
        ),  # secondPort
    }

    def __init__(self) -> None:
        """Initialize CouplingPortConnection."""
        super().__init__()
        self.first_port: Optional[CouplingPort] = None
        self.node_ports: list[CouplingPort] = []
        self.plca_local_node: Optional[PositiveInteger] = None
        self.plca_transmit: Optional[PositiveInteger] = None
        self.second_port: Optional[CouplingPort] = None


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
