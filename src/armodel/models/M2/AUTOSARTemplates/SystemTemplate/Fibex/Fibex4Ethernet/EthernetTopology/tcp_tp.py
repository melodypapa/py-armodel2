"""TcpTp AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 460)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.tcp_udp_config import (
    TcpUdpConfig,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.tp_port import (
    TpPort,
)


class TcpTp(TcpUdpConfig):
    """AUTOSAR TcpTp."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    keep_alive: Optional[PositiveInteger]
    keep_alives: Optional[Boolean]
    keep_alive_time: Optional[TimeValue]
    nagles_algorithm: Optional[Boolean]
    receive_window_min: Optional[PositiveInteger]
    tcp: Optional[TimeValue]
    tcp_tp_port: Optional[TpPort]
    def __init__(self) -> None:
        """Initialize TcpTp."""
        super().__init__()
        self.keep_alive: Optional[PositiveInteger] = None
        self.keep_alives: Optional[Boolean] = None
        self.keep_alive_time: Optional[TimeValue] = None
        self.nagles_algorithm: Optional[Boolean] = None
        self.receive_window_min: Optional[PositiveInteger] = None
        self.tcp: Optional[TimeValue] = None
        self.tcp_tp_port: Optional[TpPort] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "TcpTp":
        """Deserialize XML element to TcpTp object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TcpTp object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TcpTp, cls).deserialize(element)

        # Parse keep_alive
        child = ARObject._find_child_element(element, "KEEP-ALIVE")
        if child is not None:
            keep_alive_value = child.text
            obj.keep_alive = keep_alive_value

        # Parse keep_alives
        child = ARObject._find_child_element(element, "KEEP-ALIVES")
        if child is not None:
            keep_alives_value = child.text
            obj.keep_alives = keep_alives_value

        # Parse keep_alive_time
        child = ARObject._find_child_element(element, "KEEP-ALIVE-TIME")
        if child is not None:
            keep_alive_time_value = child.text
            obj.keep_alive_time = keep_alive_time_value

        # Parse nagles_algorithm
        child = ARObject._find_child_element(element, "NAGLES-ALGORITHM")
        if child is not None:
            nagles_algorithm_value = child.text
            obj.nagles_algorithm = nagles_algorithm_value

        # Parse receive_window_min
        child = ARObject._find_child_element(element, "RECEIVE-WINDOW-MIN")
        if child is not None:
            receive_window_min_value = child.text
            obj.receive_window_min = receive_window_min_value

        # Parse tcp
        child = ARObject._find_child_element(element, "TCP")
        if child is not None:
            tcp_value = child.text
            obj.tcp = tcp_value

        # Parse tcp_tp_port
        child = ARObject._find_child_element(element, "TCP-TP-PORT")
        if child is not None:
            tcp_tp_port_value = ARObject._deserialize_by_tag(child, "TpPort")
            obj.tcp_tp_port = tcp_tp_port_value

        return obj



class TcpTpBuilder:
    """Builder for TcpTp."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TcpTp = TcpTp()

    def build(self) -> TcpTp:
        """Build and return TcpTp object.

        Returns:
            TcpTp instance
        """
        # TODO: Add validation
        return self._obj
