"""DoIpInterface AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 551)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DoIP.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DoIP.do_ip_routing_activation import (
    DoIpRoutingActivation,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.do_ip_tp_config import (
    DoIpTpConfig,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ObsoleteModel.socket_connection import (
    SocketConnection,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.static_socket_connection import (
    StaticSocketConnection,
)


class DoIpInterface(Identifiable):
    """AUTOSAR DoIpInterface."""

    alive_check: Optional[TimeValue]
    doip_channel: Optional[DoIpTpConfig]
    doip_connections: list[SocketConnection]
    do_ip_routings: list[DoIpRoutingActivation]
    general_inactivity: Optional[TimeValue]
    initial_inactivity: Optional[TimeValue]
    initial_vehicle: Optional[TimeValue]
    is_activation_line: Optional[Boolean]
    max_tester: Optional[PositiveInteger]
    sockets: list[StaticSocketConnection]
    use_mac_address: Optional[Boolean]
    use_vehicle: Optional[Boolean]
    vehicle: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize DoIpInterface."""
        super().__init__()
        self.alive_check: Optional[TimeValue] = None
        self.doip_channel: Optional[DoIpTpConfig] = None
        self.doip_connections: list[SocketConnection] = []
        self.do_ip_routings: list[DoIpRoutingActivation] = []
        self.general_inactivity: Optional[TimeValue] = None
        self.initial_inactivity: Optional[TimeValue] = None
        self.initial_vehicle: Optional[TimeValue] = None
        self.is_activation_line: Optional[Boolean] = None
        self.max_tester: Optional[PositiveInteger] = None
        self.sockets: list[StaticSocketConnection] = []
        self.use_mac_address: Optional[Boolean] = None
        self.use_vehicle: Optional[Boolean] = None
        self.vehicle: Optional[TimeValue] = None


class DoIpInterfaceBuilder:
    """Builder for DoIpInterface."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DoIpInterface = DoIpInterface()

    def build(self) -> DoIpInterface:
        """Build and return DoIpInterface object.

        Returns:
            DoIpInterface instance
        """
        # TODO: Add validation
        return self._obj
