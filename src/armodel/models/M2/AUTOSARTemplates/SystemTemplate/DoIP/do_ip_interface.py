"""DoIpInterface AUTOSAR element."""

from typing import Optional, cast
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("alive_check", None, True, False, None),  # aliveCheck
        ("doip_channel", None, False, False, DoIpTpConfig),  # doipChannel
        ("doip_connections", None, False, True, SocketConnection),  # doipConnections
        ("do_ip_routings", None, False, True, DoIpRoutingActivation),  # doIpRoutings
        ("general_inactivity", None, True, False, None),  # generalInactivity
        ("initial_inactivity", None, True, False, None),  # initialInactivity
        ("initial_vehicle", None, True, False, None),  # initialVehicle
        ("is_activation_line", None, True, False, None),  # isActivationLine
        ("max_tester", None, True, False, None),  # maxTester
        ("sockets", None, False, True, StaticSocketConnection),  # sockets
        ("use_mac_address", None, True, False, None),  # useMacAddress
        ("use_vehicle", None, True, False, None),  # useVehicle
        ("vehicle", None, True, False, None),  # vehicle
    ]

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

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DoIpInterface to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DoIpInterface":
        """Create DoIpInterface from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DoIpInterface instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DoIpInterface since parent returns ARObject
        return cast("DoIpInterface", obj)


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
