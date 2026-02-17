"""FlexrayTpConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 594)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.tp_connection import (
    TpConnection,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.flexray_tp_node import (
    FlexrayTpNode,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.flexray_tp_pdu_pool import (
    FlexrayTpPduPool,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_address import (
    TpAddress,
)


class FlexrayTpConnection(TpConnection):
    """AUTOSAR FlexrayTpConnection."""

    def __init__(self) -> None:
        """Initialize FlexrayTpConnection."""
        super().__init__()
        self.bandwidth: Optional[Boolean] = None
        self.direct_tp_sdu: Optional[IPdu] = None
        self.multicast: Optional[TpAddress] = None
        self.receivers: list[FlexrayTpNode] = []
        self.reversed_tp_sdu: Optional[IPdu] = None
        self.rx_pdu_pool: Optional[FlexrayTpPduPool] = None
        self.tp_connection: Optional[FlexrayTpConnection] = None
        self.transmitter: Optional[FlexrayTpNode] = None
        self.tx_pdu_pool: Optional[FlexrayTpPduPool] = None


class FlexrayTpConnectionBuilder:
    """Builder for FlexrayTpConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayTpConnection = FlexrayTpConnection()

    def build(self) -> FlexrayTpConnection:
        """Build and return FlexrayTpConnection object.

        Returns:
            FlexrayTpConnection instance
        """
        # TODO: Add validation
        return self._obj
