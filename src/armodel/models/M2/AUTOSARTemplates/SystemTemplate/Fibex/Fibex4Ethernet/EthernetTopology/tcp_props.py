"""TcpProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 154)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    TimeValue,
)


class TcpProps(ARObject):
    """AUTOSAR TcpProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    tcp_congestion: Optional[Boolean]
    tcp_delayed_ack: Optional[TimeValue]
    tcp_fast_recovery: Optional[Any]
    tcp_fast: Optional[Boolean]
    tcp_fin: Optional[TimeValue]
    tcp_keep_alive: Optional[TimeValue]
    tcp_max_rtx: Optional[PositiveInteger]
    tcp_msl: Optional[TimeValue]
    tcp_nagle: Optional[Boolean]
    tcp_receive_window_max: Optional[PositiveInteger]
    tcp: Optional[TimeValue]
    tcp_slow_start: Optional[Boolean]
    tcp_syn_max_rtx: Optional[PositiveInteger]
    tcp_syn_received: Optional[TimeValue]
    tcp_ttl: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize TcpProps."""
        super().__init__()
        self.tcp_congestion: Optional[Boolean] = None
        self.tcp_delayed_ack: Optional[TimeValue] = None
        self.tcp_fast_recovery: Optional[Any] = None
        self.tcp_fast: Optional[Boolean] = None
        self.tcp_fin: Optional[TimeValue] = None
        self.tcp_keep_alive: Optional[TimeValue] = None
        self.tcp_max_rtx: Optional[PositiveInteger] = None
        self.tcp_msl: Optional[TimeValue] = None
        self.tcp_nagle: Optional[Boolean] = None
        self.tcp_receive_window_max: Optional[PositiveInteger] = None
        self.tcp: Optional[TimeValue] = None
        self.tcp_slow_start: Optional[Boolean] = None
        self.tcp_syn_max_rtx: Optional[PositiveInteger] = None
        self.tcp_syn_received: Optional[TimeValue] = None
        self.tcp_ttl: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "TcpProps":
        """Deserialize XML element to TcpProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TcpProps object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse tcp_congestion
        child = ARObject._find_child_element(element, "TCP-CONGESTION")
        if child is not None:
            tcp_congestion_value = child.text
            obj.tcp_congestion = tcp_congestion_value

        # Parse tcp_delayed_ack
        child = ARObject._find_child_element(element, "TCP-DELAYED-ACK")
        if child is not None:
            tcp_delayed_ack_value = child.text
            obj.tcp_delayed_ack = tcp_delayed_ack_value

        # Parse tcp_fast_recovery
        child = ARObject._find_child_element(element, "TCP-FAST-RECOVERY")
        if child is not None:
            tcp_fast_recovery_value = child.text
            obj.tcp_fast_recovery = tcp_fast_recovery_value

        # Parse tcp_fast
        child = ARObject._find_child_element(element, "TCP-FAST")
        if child is not None:
            tcp_fast_value = child.text
            obj.tcp_fast = tcp_fast_value

        # Parse tcp_fin
        child = ARObject._find_child_element(element, "TCP-FIN")
        if child is not None:
            tcp_fin_value = child.text
            obj.tcp_fin = tcp_fin_value

        # Parse tcp_keep_alive
        child = ARObject._find_child_element(element, "TCP-KEEP-ALIVE")
        if child is not None:
            tcp_keep_alive_value = child.text
            obj.tcp_keep_alive = tcp_keep_alive_value

        # Parse tcp_max_rtx
        child = ARObject._find_child_element(element, "TCP-MAX-RTX")
        if child is not None:
            tcp_max_rtx_value = child.text
            obj.tcp_max_rtx = tcp_max_rtx_value

        # Parse tcp_msl
        child = ARObject._find_child_element(element, "TCP-MSL")
        if child is not None:
            tcp_msl_value = child.text
            obj.tcp_msl = tcp_msl_value

        # Parse tcp_nagle
        child = ARObject._find_child_element(element, "TCP-NAGLE")
        if child is not None:
            tcp_nagle_value = child.text
            obj.tcp_nagle = tcp_nagle_value

        # Parse tcp_receive_window_max
        child = ARObject._find_child_element(element, "TCP-RECEIVE-WINDOW-MAX")
        if child is not None:
            tcp_receive_window_max_value = child.text
            obj.tcp_receive_window_max = tcp_receive_window_max_value

        # Parse tcp
        child = ARObject._find_child_element(element, "TCP")
        if child is not None:
            tcp_value = child.text
            obj.tcp = tcp_value

        # Parse tcp_slow_start
        child = ARObject._find_child_element(element, "TCP-SLOW-START")
        if child is not None:
            tcp_slow_start_value = child.text
            obj.tcp_slow_start = tcp_slow_start_value

        # Parse tcp_syn_max_rtx
        child = ARObject._find_child_element(element, "TCP-SYN-MAX-RTX")
        if child is not None:
            tcp_syn_max_rtx_value = child.text
            obj.tcp_syn_max_rtx = tcp_syn_max_rtx_value

        # Parse tcp_syn_received
        child = ARObject._find_child_element(element, "TCP-SYN-RECEIVED")
        if child is not None:
            tcp_syn_received_value = child.text
            obj.tcp_syn_received = tcp_syn_received_value

        # Parse tcp_ttl
        child = ARObject._find_child_element(element, "TCP-TTL")
        if child is not None:
            tcp_ttl_value = child.text
            obj.tcp_ttl = tcp_ttl_value

        return obj



class TcpPropsBuilder:
    """Builder for TcpProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TcpProps = TcpProps()

    def build(self) -> TcpProps:
        """Build and return TcpProps object.

        Returns:
            TcpProps instance
        """
        # TODO: Add validation
        return self._obj
