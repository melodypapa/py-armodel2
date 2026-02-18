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
