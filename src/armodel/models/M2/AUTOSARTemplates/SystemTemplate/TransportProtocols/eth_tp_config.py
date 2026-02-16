"""EthTpConfig AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_config import (
    TpConfig,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.eth_tp_connection import (
    EthTpConnection,
)


class EthTpConfig(TpConfig):
    """AUTOSAR EthTpConfig."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "tp_connections": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=EthTpConnection,
        ),  # tpConnections
    }

    def __init__(self) -> None:
        """Initialize EthTpConfig."""
        super().__init__()
        self.tp_connections: list[EthTpConnection] = []


class EthTpConfigBuilder:
    """Builder for EthTpConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EthTpConfig = EthTpConfig()

    def build(self) -> EthTpConfig:
        """Build and return EthTpConfig object.

        Returns:
            EthTpConfig instance
        """
        # TODO: Add validation
        return self._obj
