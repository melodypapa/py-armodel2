"""CanTpConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 608)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.tp_connection import (
    TpConnection,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import (
    CanTpAddressingFormatType,
    NetworkTargetAddressType,
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    addressing: Optional[CanTpAddressingFormatType]
    cancellation: Optional[Boolean]
    can_tp_channel: Optional[CanTpChannel]
    data_pdu: Optional[NPdu]
    flow_control_pdu: Optional[NPdu]
    max_block_size: Optional[Integer]
    multicast: Optional[CanTpAddress]
    padding: Optional[Boolean]
    receivers: list[CanTpNode]
    ta_type_type: Optional[NetworkTargetAddressType]
    timeout_br: Optional[TimeValue]
    timeout_bs: Optional[TimeValue]
    timeout_cr: Optional[TimeValue]
    timeout_cs: Optional[TimeValue]
    tp_sdu: Optional[IPdu]
    transmitter: Optional[CanTpNode]
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanTpConnection":
        """Deserialize XML element to CanTpConnection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CanTpConnection object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse addressing
        child = ARObject._find_child_element(element, "ADDRESSING")
        if child is not None:
            addressing_value = child.text
            obj.addressing = addressing_value

        # Parse cancellation
        child = ARObject._find_child_element(element, "CANCELLATION")
        if child is not None:
            cancellation_value = child.text
            obj.cancellation = cancellation_value

        # Parse can_tp_channel
        child = ARObject._find_child_element(element, "CAN-TP-CHANNEL")
        if child is not None:
            can_tp_channel_value = ARObject._deserialize_by_tag(child, "CanTpChannel")
            obj.can_tp_channel = can_tp_channel_value

        # Parse data_pdu
        child = ARObject._find_child_element(element, "DATA-PDU")
        if child is not None:
            data_pdu_value = ARObject._deserialize_by_tag(child, "NPdu")
            obj.data_pdu = data_pdu_value

        # Parse flow_control_pdu
        child = ARObject._find_child_element(element, "FLOW-CONTROL-PDU")
        if child is not None:
            flow_control_pdu_value = ARObject._deserialize_by_tag(child, "NPdu")
            obj.flow_control_pdu = flow_control_pdu_value

        # Parse max_block_size
        child = ARObject._find_child_element(element, "MAX-BLOCK-SIZE")
        if child is not None:
            max_block_size_value = child.text
            obj.max_block_size = max_block_size_value

        # Parse multicast
        child = ARObject._find_child_element(element, "MULTICAST")
        if child is not None:
            multicast_value = ARObject._deserialize_by_tag(child, "CanTpAddress")
            obj.multicast = multicast_value

        # Parse padding
        child = ARObject._find_child_element(element, "PADDING")
        if child is not None:
            padding_value = child.text
            obj.padding = padding_value

        # Parse receivers (list)
        obj.receivers = []
        for child in ARObject._find_all_child_elements(element, "RECEIVERS"):
            receivers_value = ARObject._deserialize_by_tag(child, "CanTpNode")
            obj.receivers.append(receivers_value)

        # Parse ta_type_type
        child = ARObject._find_child_element(element, "TA-TYPE-TYPE")
        if child is not None:
            ta_type_type_value = child.text
            obj.ta_type_type = ta_type_type_value

        # Parse timeout_br
        child = ARObject._find_child_element(element, "TIMEOUT-BR")
        if child is not None:
            timeout_br_value = child.text
            obj.timeout_br = timeout_br_value

        # Parse timeout_bs
        child = ARObject._find_child_element(element, "TIMEOUT-BS")
        if child is not None:
            timeout_bs_value = child.text
            obj.timeout_bs = timeout_bs_value

        # Parse timeout_cr
        child = ARObject._find_child_element(element, "TIMEOUT-CR")
        if child is not None:
            timeout_cr_value = child.text
            obj.timeout_cr = timeout_cr_value

        # Parse timeout_cs
        child = ARObject._find_child_element(element, "TIMEOUT-CS")
        if child is not None:
            timeout_cs_value = child.text
            obj.timeout_cs = timeout_cs_value

        # Parse tp_sdu
        child = ARObject._find_child_element(element, "TP-SDU")
        if child is not None:
            tp_sdu_value = ARObject._deserialize_by_tag(child, "IPdu")
            obj.tp_sdu = tp_sdu_value

        # Parse transmitter
        child = ARObject._find_child_element(element, "TRANSMITTER")
        if child is not None:
            transmitter_value = ARObject._deserialize_by_tag(child, "CanTpNode")
            obj.transmitter = transmitter_value

        return obj



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
