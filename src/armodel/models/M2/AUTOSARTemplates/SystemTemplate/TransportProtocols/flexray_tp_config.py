"""FlexrayTpConfig AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "pdu_pools": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=FlexrayTpPduPool,
        ),  # pduPools
        "tp_addresses": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=TpAddress,
        ),  # tpAddresses
        "tp_connections": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=FlexrayTpConnection,
        ),  # tpConnections
        "tp_ecus": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=FlexrayTpEcu,
        ),  # tpEcus
        "tp_nodes": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=FlexrayTpNode,
        ),  # tpNodes
    }

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
