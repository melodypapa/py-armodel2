"""DoIpTpConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 555)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_config import (
    TpConfig,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.do_ip_logic_address import (
    DoIpLogicAddress,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.do_ip_tp_connection import (
    DoIpTpConnection,
)


class DoIpTpConfig(TpConfig):
    """AUTOSAR DoIpTpConfig."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "do_ip_logic_address_addresses": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DoIpLogicAddress,
        ),  # doIpLogicAddressAddresses
        "tp_connections": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DoIpTpConnection,
        ),  # tpConnections
    }

    def __init__(self) -> None:
        """Initialize DoIpTpConfig."""
        super().__init__()
        self.do_ip_logic_address_addresses: list[DoIpLogicAddress] = []
        self.tp_connections: list[DoIpTpConnection] = []


class DoIpTpConfigBuilder:
    """Builder for DoIpTpConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DoIpTpConfig = DoIpTpConfig()

    def build(self) -> DoIpTpConfig:
        """Build and return DoIpTpConfig object.

        Returns:
            DoIpTpConfig instance
        """
        # TODO: Add validation
        return self._obj
