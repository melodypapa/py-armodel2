"""MacMulticastConfiguration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 467)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.network_endpoint_address import (
    NetworkEndpointAddress,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.mac_multicast_group import (
    MacMulticastGroup,
)


class MacMulticastConfiguration(NetworkEndpointAddress):
    """AUTOSAR MacMulticastConfiguration."""

    def __init__(self) -> None:
        """Initialize MacMulticastConfiguration."""
        super().__init__()
        self.mac_multicast_group_group: Optional[MacMulticastGroup] = None


class MacMulticastConfigurationBuilder:
    """Builder for MacMulticastConfiguration."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MacMulticastConfiguration = MacMulticastConfiguration()

    def build(self) -> MacMulticastConfiguration:
        """Build and return MacMulticastConfiguration object.

        Returns:
            MacMulticastConfiguration instance
        """
        # TODO: Add validation
        return self._obj
