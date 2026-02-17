"""EthTpConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 618)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.tp_connection import (
    TpConnection,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class EthTpConnection(TpConnection):
    """AUTOSAR EthTpConnection."""

    def __init__(self) -> None:
        """Initialize EthTpConnection."""
        super().__init__()
        self.tp_sdus: list[PduTriggering] = []


class EthTpConnectionBuilder:
    """Builder for EthTpConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EthTpConnection = EthTpConnection()

    def build(self) -> EthTpConnection:
        """Build and return EthTpConnection object.

        Returns:
            EthTpConnection instance
        """
        # TODO: Add validation
        return self._obj
