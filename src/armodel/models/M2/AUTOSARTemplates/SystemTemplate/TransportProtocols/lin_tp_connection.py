"""LinTpConnection AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.tp_connection import (
    TpConnection,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.lin_tp_node import (
    LinTpNode,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.n_pdu import (
    NPdu,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_address import (
    TpAddress,
)


class LinTpConnection(TpConnection):
    """AUTOSAR LinTpConnection."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("data_pdu", None, False, False, NPdu),  # dataPdu
        ("flow_control", None, False, False, NPdu),  # flowControl
        ("lin_tp_n_sdu", None, False, False, IPdu),  # linTpNSdu
        ("multicast", None, False, False, TpAddress),  # multicast
        ("receivers", None, False, True, LinTpNode),  # receivers
        ("timeout_as", None, True, False, None),  # timeoutAs
        ("timeout_cr", None, True, False, None),  # timeoutCr
        ("timeout_cs", None, True, False, None),  # timeoutCs
        ("transmitter", None, False, False, LinTpNode),  # transmitter
    ]

    def __init__(self) -> None:
        """Initialize LinTpConnection."""
        super().__init__()
        self.data_pdu: Optional[NPdu] = None
        self.flow_control: Optional[NPdu] = None
        self.lin_tp_n_sdu: Optional[IPdu] = None
        self.multicast: Optional[TpAddress] = None
        self.receivers: list[LinTpNode] = []
        self.timeout_as: Optional[TimeValue] = None
        self.timeout_cr: Optional[TimeValue] = None
        self.timeout_cs: Optional[TimeValue] = None
        self.transmitter: Optional[LinTpNode] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert LinTpConnection to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinTpConnection":
        """Create LinTpConnection from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            LinTpConnection instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to LinTpConnection since parent returns ARObject
        return cast("LinTpConnection", obj)


class LinTpConnectionBuilder:
    """Builder for LinTpConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinTpConnection = LinTpConnection()

    def build(self) -> LinTpConnection:
        """Build and return LinTpConnection object.

        Returns:
            LinTpConnection instance
        """
        # TODO: Add validation
        return self._obj
