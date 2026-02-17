"""SocketConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2057)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ObsoleteModel.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.describable import (
    Describable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Identifier,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.socket_address import (
    SocketAddress,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.socket_connection_ipdu_identifier_set import (
    SocketConnectionIpduIdentifierSet,
)


class SocketConnection(Describable):
    """AUTOSAR SocketConnection."""

    client_ip_addr: Optional[Boolean]
    client_port: Optional[SocketAddress]
    client_port_from: Optional[Boolean]
    pdus: list[SocketConnectionIpduIdentifierSet]
    pdu_collection: Optional[TimeValue]
    runtime_ip: Optional[Any]
    runtime_port: Optional[Any]
    short_label: Optional[Identifier]
    def __init__(self) -> None:
        """Initialize SocketConnection."""
        super().__init__()
        self.client_ip_addr: Optional[Boolean] = None
        self.client_port: Optional[SocketAddress] = None
        self.client_port_from: Optional[Boolean] = None
        self.pdus: list[SocketConnectionIpduIdentifierSet] = []
        self.pdu_collection: Optional[TimeValue] = None
        self.runtime_ip: Optional[Any] = None
        self.runtime_port: Optional[Any] = None
        self.short_label: Optional[Identifier] = None


class SocketConnectionBuilder:
    """Builder for SocketConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SocketConnection = SocketConnection()

    def build(self) -> SocketConnection:
        """Build and return SocketConnection object.

        Returns:
            SocketConnection instance
        """
        # TODO: Add validation
        return self._obj
