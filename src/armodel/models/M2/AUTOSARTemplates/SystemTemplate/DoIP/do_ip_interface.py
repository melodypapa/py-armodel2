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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DoIpInterface":
        """Deserialize XML element to DoIpInterface object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DoIpInterface object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DoIpInterface, cls).deserialize(element)

        # Parse alive_check
        child = ARObject._find_child_element(element, "ALIVE-CHECK")
        if child is not None:
            alive_check_value = child.text
            obj.alive_check = alive_check_value

        # Parse doip_channel
        child = ARObject._find_child_element(element, "DOIP-CHANNEL")
        if child is not None:
            doip_channel_value = ARObject._deserialize_by_tag(child, "DoIpTpConfig")
            obj.doip_channel = doip_channel_value

        # Parse doip_connections (list from container "DOIP-CONNECTIONS")
        obj.doip_connections = []
        container = ARObject._find_child_element(element, "DOIP-CONNECTIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.doip_connections.append(child_value)

        # Parse do_ip_routings (list from container "DO-IP-ROUTINGS")
        obj.do_ip_routings = []
        container = ARObject._find_child_element(element, "DO-IP-ROUTINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.do_ip_routings.append(child_value)

        # Parse general_inactivity
        child = ARObject._find_child_element(element, "GENERAL-INACTIVITY")
        if child is not None:
            general_inactivity_value = child.text
            obj.general_inactivity = general_inactivity_value

        # Parse initial_inactivity
        child = ARObject._find_child_element(element, "INITIAL-INACTIVITY")
        if child is not None:
            initial_inactivity_value = child.text
            obj.initial_inactivity = initial_inactivity_value

        # Parse initial_vehicle
        child = ARObject._find_child_element(element, "INITIAL-VEHICLE")
        if child is not None:
            initial_vehicle_value = child.text
            obj.initial_vehicle = initial_vehicle_value

        # Parse is_activation_line
        child = ARObject._find_child_element(element, "IS-ACTIVATION-LINE")
        if child is not None:
            is_activation_line_value = child.text
            obj.is_activation_line = is_activation_line_value

        # Parse max_tester
        child = ARObject._find_child_element(element, "MAX-TESTER")
        if child is not None:
            max_tester_value = child.text
            obj.max_tester = max_tester_value

        # Parse sockets (list from container "SOCKETS")
        obj.sockets = []
        container = ARObject._find_child_element(element, "SOCKETS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sockets.append(child_value)

        # Parse use_mac_address
        child = ARObject._find_child_element(element, "USE-MAC-ADDRESS")
        if child is not None:
            use_mac_address_value = child.text
            obj.use_mac_address = use_mac_address_value

        # Parse use_vehicle
        child = ARObject._find_child_element(element, "USE-VEHICLE")
        if child is not None:
            use_vehicle_value = child.text
            obj.use_vehicle = use_vehicle_value

        # Parse vehicle
        child = ARObject._find_child_element(element, "VEHICLE")
        if child is not None:
            vehicle_value = child.text
            obj.vehicle = vehicle_value

        return obj



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
