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
