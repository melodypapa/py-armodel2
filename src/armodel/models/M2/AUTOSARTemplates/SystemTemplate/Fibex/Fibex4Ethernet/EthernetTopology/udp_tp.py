"""UdpTp AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 459)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.tcp_udp_config import (
    TcpUdpConfig,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.tp_port import (
    TpPort,
)


class UdpTp(TcpUdpConfig):
    """AUTOSAR UdpTp."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    udp_tp_port: Optional[TpPort]
    def __init__(self) -> None:
        """Initialize UdpTp."""
        super().__init__()
        self.udp_tp_port: Optional[TpPort] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "UdpTp":
        """Deserialize XML element to UdpTp object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized UdpTp object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse udp_tp_port
        child = ARObject._find_child_element(element, "UDP-TP-PORT")
        if child is not None:
            udp_tp_port_value = ARObject._deserialize_by_tag(child, "TpPort")
            obj.udp_tp_port = udp_tp_port_value

        return obj



class UdpTpBuilder:
    """Builder for UdpTp."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UdpTp = UdpTp()

    def build(self) -> UdpTp:
        """Build and return UdpTp object.

        Returns:
            UdpTp instance
        """
        # TODO: Add validation
        return self._obj
