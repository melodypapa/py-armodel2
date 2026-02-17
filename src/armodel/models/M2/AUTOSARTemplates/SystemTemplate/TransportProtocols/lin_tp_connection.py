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
