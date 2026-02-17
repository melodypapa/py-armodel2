"""FlexrayTpConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 592)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_config import (
    TpConfig,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.flexray_tp_connection import (
    FlexrayTpConnection,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.flexray_tp_ecu import (
    FlexrayTpEcu,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.flexray_tp_node import (
    FlexrayTpNode,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.flexray_tp_pdu_pool import (
    FlexrayTpPduPool,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_address import (
    TpAddress,
)


class FlexrayTpConfig(TpConfig):
    """AUTOSAR FlexrayTpConfig."""

    def __init__(self) -> None:
        """Initialize FlexrayTpConfig."""
        super().__init__()
        self.pdu_pools: list[FlexrayTpPduPool] = []
        self.tp_addresses: list[TpAddress] = []
        self.tp_connections: list[FlexrayTpConnection] = []
        self.tp_ecus: list[FlexrayTpEcu] = []
        self.tp_nodes: list[FlexrayTpNode] = []


class FlexrayTpConfigBuilder:
    """Builder for FlexrayTpConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayTpConfig = FlexrayTpConfig()

    def build(self) -> FlexrayTpConfig:
        """Build and return FlexrayTpConfig object.

        Returns:
            FlexrayTpConfig instance
        """
        # TODO: Add validation
        return self._obj
