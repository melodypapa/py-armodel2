"""TcpUdpConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 459)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.transport_protocol_configuration import (
    TransportProtocolConfiguration,
)
from abc import ABC, abstractmethod


class TcpUdpConfig(TransportProtocolConfiguration, ABC):
    """AUTOSAR TcpUdpConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize TcpUdpConfig."""
        super().__init__()


class TcpUdpConfigBuilder:
    """Builder for TcpUdpConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TcpUdpConfig = TcpUdpConfig()

    def build(self) -> TcpUdpConfig:
        """Build and return TcpUdpConfig object.

        Returns:
            TcpUdpConfig instance
        """
        # TODO: Add validation
        return self._obj
