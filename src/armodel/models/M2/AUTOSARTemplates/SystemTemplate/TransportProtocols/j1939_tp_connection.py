"""J1939TpConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 624)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.tp_connection import (
    TpConnection,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    broadcast: Optional[Boolean]
    buffer_ratio: Optional[PositiveInteger]
    cancellation: Optional[Boolean]
    data_pdu: Optional[NPdu]
    dynamic_bs: Optional[Boolean]
    flow_control_pdu: NPdu
    max_bs: Optional[PositiveInteger]
    max_exp_bs: Optional[PositiveInteger]
    receivers: list[J1939TpNode]
    retry: Optional[Boolean]
    tp_pgs: list[J1939TpPg]
    transmitter: Optional[J1939TpNode]
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "J1939TpConnection":
        """Deserialize XML element to J1939TpConnection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized J1939TpConnection object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse broadcast
        child = ARObject._find_child_element(element, "BROADCAST")
        if child is not None:
            broadcast_value = child.text
            obj.broadcast = broadcast_value

        # Parse buffer_ratio
        child = ARObject._find_child_element(element, "BUFFER-RATIO")
        if child is not None:
            buffer_ratio_value = child.text
            obj.buffer_ratio = buffer_ratio_value

        # Parse cancellation
        child = ARObject._find_child_element(element, "CANCELLATION")
        if child is not None:
            cancellation_value = child.text
            obj.cancellation = cancellation_value

        # Parse data_pdu
        child = ARObject._find_child_element(element, "DATA-PDU")
        if child is not None:
            data_pdu_value = ARObject._deserialize_by_tag(child, "NPdu")
            obj.data_pdu = data_pdu_value

        # Parse dynamic_bs
        child = ARObject._find_child_element(element, "DYNAMIC-BS")
        if child is not None:
            dynamic_bs_value = child.text
            obj.dynamic_bs = dynamic_bs_value

        # Parse flow_control_pdu
        child = ARObject._find_child_element(element, "FLOW-CONTROL-PDU")
        if child is not None:
            flow_control_pdu_value = ARObject._deserialize_by_tag(child, "NPdu")
            obj.flow_control_pdu = flow_control_pdu_value

        # Parse max_bs
        child = ARObject._find_child_element(element, "MAX-BS")
        if child is not None:
            max_bs_value = child.text
            obj.max_bs = max_bs_value

        # Parse max_exp_bs
        child = ARObject._find_child_element(element, "MAX-EXP-BS")
        if child is not None:
            max_exp_bs_value = child.text
            obj.max_exp_bs = max_exp_bs_value

        # Parse receivers (list)
        obj.receivers = []
        for child in ARObject._find_all_child_elements(element, "RECEIVERS"):
            receivers_value = ARObject._deserialize_by_tag(child, "J1939TpNode")
            obj.receivers.append(receivers_value)

        # Parse retry
        child = ARObject._find_child_element(element, "RETRY")
        if child is not None:
            retry_value = child.text
            obj.retry = retry_value

        # Parse tp_pgs (list)
        obj.tp_pgs = []
        for child in ARObject._find_all_child_elements(element, "TP-PGS"):
            tp_pgs_value = ARObject._deserialize_by_tag(child, "J1939TpPg")
            obj.tp_pgs.append(tp_pgs_value)

        # Parse transmitter
        child = ARObject._find_child_element(element, "TRANSMITTER")
        if child is not None:
            transmitter_value = ARObject._deserialize_by_tag(child, "J1939TpNode")
            obj.transmitter = transmitter_value

        return obj



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
