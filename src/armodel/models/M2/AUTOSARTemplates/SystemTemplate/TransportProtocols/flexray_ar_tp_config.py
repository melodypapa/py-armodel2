"""FlexrayArTpConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 599)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_config import (
    TpConfig,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.flexray_ar_tp_channel import (
    FlexrayArTpChannel,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.flexray_ar_tp_node import (
    FlexrayArTpNode,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_address import (
    TpAddress,
)


class FlexrayArTpConfig(TpConfig):
    """AUTOSAR FlexrayArTpConfig."""

    tp_addresses: list[TpAddress]
    tp_channels: list[FlexrayArTpChannel]
    tp_nodes: list[FlexrayArTpNode]
    def __init__(self) -> None:
        """Initialize FlexrayArTpConfig."""
        super().__init__()
        self.tp_addresses: list[TpAddress] = []
        self.tp_channels: list[FlexrayArTpChannel] = []
        self.tp_nodes: list[FlexrayArTpNode] = []


class FlexrayArTpConfigBuilder:
    """Builder for FlexrayArTpConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayArTpConfig = FlexrayArTpConfig()

    def build(self) -> FlexrayArTpConfig:
        """Build and return FlexrayArTpConfig object.

        Returns:
            FlexrayArTpConfig instance
        """
        # TODO: Add validation
        return self._obj
