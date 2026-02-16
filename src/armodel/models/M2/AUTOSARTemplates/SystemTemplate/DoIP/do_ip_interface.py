"""DoIpInterface AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "alive_check": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # aliveCheck
        "doip_channel": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DoIpTpConfig,
        ),  # doipChannel
        "doip_connections": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=SocketConnection,
        ),  # doipConnections
        "do_ip_routings": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DoIpRoutingActivation,
        ),  # doIpRoutings
        "general_inactivity": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # generalInactivity
        "initial_inactivity": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # initialInactivity
        "initial_vehicle": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # initialVehicle
        "is_activation_line": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # isActivationLine
        "max_tester": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maxTester
        "sockets": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=StaticSocketConnection,
        ),  # sockets
        "use_mac_address": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # useMacAddress
        "use_vehicle": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # useVehicle
        "vehicle": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # vehicle
    }

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
