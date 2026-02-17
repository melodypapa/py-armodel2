"""TcpTp AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 460)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.tcp_udp_config import (
    TcpUdpConfig,
)
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "keep_alive": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # keepAlive
        "keep_alives": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # keepAlives
        "keep_alive_time": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # keepAliveTime
        "nagles_algorithm": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # naglesAlgorithm
        "receive_window_min": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # receiveWindowMin
        "tcp": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # tcp
        "tcp_tp_port": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TpPort,
        ),  # tcpTpPort
    }

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
