"""LinTpConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 615)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.tp_connection import (
    TpConnection,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_pdu: Optional[NPdu]
    flow_control: Optional[NPdu]
    lin_tp_n_sdu: Optional[IPdu]
    multicast: Optional[TpAddress]
    receivers: list[LinTpNode]
    timeout_as: Optional[TimeValue]
    timeout_cr: Optional[TimeValue]
    timeout_cs: Optional[TimeValue]
    transmitter: Optional[LinTpNode]
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinTpConnection":
        """Deserialize XML element to LinTpConnection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LinTpConnection object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse data_pdu
        child = ARObject._find_child_element(element, "DATA-PDU")
        if child is not None:
            data_pdu_value = ARObject._deserialize_by_tag(child, "NPdu")
            obj.data_pdu = data_pdu_value

        # Parse flow_control
        child = ARObject._find_child_element(element, "FLOW-CONTROL")
        if child is not None:
            flow_control_value = ARObject._deserialize_by_tag(child, "NPdu")
            obj.flow_control = flow_control_value

        # Parse lin_tp_n_sdu
        child = ARObject._find_child_element(element, "LIN-TP-N-SDU")
        if child is not None:
            lin_tp_n_sdu_value = ARObject._deserialize_by_tag(child, "IPdu")
            obj.lin_tp_n_sdu = lin_tp_n_sdu_value

        # Parse multicast
        child = ARObject._find_child_element(element, "MULTICAST")
        if child is not None:
            multicast_value = ARObject._deserialize_by_tag(child, "TpAddress")
            obj.multicast = multicast_value

        # Parse receivers (list)
        obj.receivers = []
        for child in ARObject._find_all_child_elements(element, "RECEIVERS"):
            receivers_value = ARObject._deserialize_by_tag(child, "LinTpNode")
            obj.receivers.append(receivers_value)

        # Parse timeout_as
        child = ARObject._find_child_element(element, "TIMEOUT-AS")
        if child is not None:
            timeout_as_value = child.text
            obj.timeout_as = timeout_as_value

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

        # Parse transmitter
        child = ARObject._find_child_element(element, "TRANSMITTER")
        if child is not None:
            transmitter_value = ARObject._deserialize_by_tag(child, "LinTpNode")
            obj.transmitter = transmitter_value

        return obj



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
