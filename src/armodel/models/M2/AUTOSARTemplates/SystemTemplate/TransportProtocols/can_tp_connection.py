"""CanTpConnection AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.tp_connection import (
    TpConnection,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.can_tp_address import (
    CanTpAddress,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.can_tp_channel import (
    CanTpChannel,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.can_tp_node import (
    CanTpNode,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.n_pdu import (
    NPdu,
)


class CanTpConnection(TpConnection):
    """AUTOSAR CanTpConnection."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("addressing", None, False, False, CanTpAddressingFormatType),  # addressing
        ("cancellation", None, True, False, None),  # cancellation
        ("can_tp_channel", None, False, False, CanTpChannel),  # canTpChannel
        ("data_pdu", None, False, False, NPdu),  # dataPdu
        ("flow_control_pdu", None, False, False, NPdu),  # flowControlPdu
        ("max_block_size", None, True, False, None),  # maxBlockSize
        ("multicast", None, False, False, CanTpAddress),  # multicast
        ("padding", None, True, False, None),  # padding
        ("receivers", None, False, True, CanTpNode),  # receivers
        ("ta_type_type", None, False, False, NetworkTargetAddressType),  # taTypeType
        ("timeout_br", None, True, False, None),  # timeoutBr
        ("timeout_bs", None, True, False, None),  # timeoutBs
        ("timeout_cr", None, True, False, None),  # timeoutCr
        ("timeout_cs", None, True, False, None),  # timeoutCs
        ("tp_sdu", None, False, False, IPdu),  # tpSdu
        ("transmitter", None, False, False, CanTpNode),  # transmitter
    ]

    def __init__(self) -> None:
        """Initialize CanTpConnection."""
        super().__init__()
        self.addressing: Optional[CanTpAddressingFormatType] = None
        self.cancellation: Optional[Boolean] = None
        self.can_tp_channel: Optional[CanTpChannel] = None
        self.data_pdu: Optional[NPdu] = None
        self.flow_control_pdu: Optional[NPdu] = None
        self.max_block_size: Optional[Integer] = None
        self.multicast: Optional[CanTpAddress] = None
        self.padding: Optional[Boolean] = None
        self.receivers: list[CanTpNode] = []
        self.ta_type_type: Optional[NetworkTargetAddressType] = None
        self.timeout_br: Optional[TimeValue] = None
        self.timeout_bs: Optional[TimeValue] = None
        self.timeout_cr: Optional[TimeValue] = None
        self.timeout_cs: Optional[TimeValue] = None
        self.tp_sdu: Optional[IPdu] = None
        self.transmitter: Optional[CanTpNode] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CanTpConnection to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanTpConnection":
        """Create CanTpConnection from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CanTpConnection instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CanTpConnection since parent returns ARObject
        return cast("CanTpConnection", obj)


class CanTpConnectionBuilder:
    """Builder for CanTpConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanTpConnection = CanTpConnection()

    def build(self) -> CanTpConnection:
        """Build and return CanTpConnection object.

        Returns:
            CanTpConnection instance
        """
        # TODO: Add validation
        return self._obj
