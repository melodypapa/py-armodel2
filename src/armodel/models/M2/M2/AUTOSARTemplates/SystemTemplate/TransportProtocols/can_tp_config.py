"""CanTpConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 606)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_config import (
    TpConfig,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.can_tp_address import (
    CanTpAddress,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.can_tp_channel import (
    CanTpChannel,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.can_tp_connection import (
    CanTpConnection,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.can_tp_ecu import (
    CanTpEcu,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.can_tp_node import (
    CanTpNode,
)


class CanTpConfig(TpConfig):
    """AUTOSAR CanTpConfig."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "tp_addresses": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=CanTpAddress,
        ),  # tpAddresses
        "tp_channels": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=CanTpChannel,
        ),  # tpChannels
        "tp_connections": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=CanTpConnection,
        ),  # tpConnections
        "tp_ecus": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=CanTpEcu,
        ),  # tpEcus
        "tp_nodes": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=CanTpNode,
        ),  # tpNodes
    }

    def __init__(self) -> None:
        """Initialize CanTpConfig."""
        super().__init__()
        self.tp_addresses: list[CanTpAddress] = []
        self.tp_channels: list[CanTpChannel] = []
        self.tp_connections: list[CanTpConnection] = []
        self.tp_ecus: list[CanTpEcu] = []
        self.tp_nodes: list[CanTpNode] = []


class CanTpConfigBuilder:
    """Builder for CanTpConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanTpConfig = CanTpConfig()

    def build(self) -> CanTpConfig:
        """Build and return CanTpConfig object.

        Returns:
            CanTpConfig instance
        """
        # TODO: Add validation
        return self._obj
