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
