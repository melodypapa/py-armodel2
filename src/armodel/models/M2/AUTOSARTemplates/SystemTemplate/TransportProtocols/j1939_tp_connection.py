"""J1939TpConnection AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.tp_connection import (
    TpConnection,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.j1939_tp_node import (
    J1939TpNode,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.j1939_tp_pg import (
    J1939TpPg,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.n_pdu import (
    NPdu,
)


class J1939TpConnection(TpConnection):
    """AUTOSAR J1939TpConnection."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("broadcast", None, True, False, None),  # broadcast
        ("buffer_ratio", None, True, False, None),  # bufferRatio
        ("cancellation", None, True, False, None),  # cancellation
        ("data_pdu", None, False, False, NPdu),  # dataPdu
        ("dynamic_bs", None, True, False, None),  # dynamicBs
        ("flow_control_pdu", None, False, False, NPdu),  # flowControlPdu
        ("max_bs", None, True, False, None),  # maxBs
        ("max_exp_bs", None, True, False, None),  # maxExpBs
        ("receivers", None, False, True, J1939TpNode),  # receivers
        ("retry", None, True, False, None),  # retry
        ("tp_pgs", None, False, True, J1939TpPg),  # tpPgs
        ("transmitter", None, False, False, J1939TpNode),  # transmitter
    ]

    def __init__(self) -> None:
        """Initialize J1939TpConnection."""
        super().__init__()
        self.broadcast: Optional[Boolean] = None
        self.buffer_ratio: Optional[PositiveInteger] = None
        self.cancellation: Optional[Boolean] = None
        self.data_pdu: Optional[NPdu] = None
        self.dynamic_bs: Optional[Boolean] = None
        self.flow_control_pdu: NPdu = None
        self.max_bs: Optional[PositiveInteger] = None
        self.max_exp_bs: Optional[PositiveInteger] = None
        self.receivers: list[J1939TpNode] = []
        self.retry: Optional[Boolean] = None
        self.tp_pgs: list[J1939TpPg] = []
        self.transmitter: Optional[J1939TpNode] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert J1939TpConnection to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "J1939TpConnection":
        """Create J1939TpConnection from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            J1939TpConnection instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to J1939TpConnection since parent returns ARObject
        return cast("J1939TpConnection", obj)


class J1939TpConnectionBuilder:
    """Builder for J1939TpConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: J1939TpConnection = J1939TpConnection()

    def build(self) -> J1939TpConnection:
        """Build and return J1939TpConnection object.

        Returns:
            J1939TpConnection instance
        """
        # TODO: Add validation
        return self._obj
