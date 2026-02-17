"""StreamFilterRuleIpTp AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 137)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.stream_filter_ipv6_address import (
    StreamFilterIpv6Address,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.stream_filter_port_range import (
    StreamFilterPortRange,
)


class StreamFilterRuleIpTp(ARObject):
    """AUTOSAR StreamFilterRuleIpTp."""

    destination: Optional[StreamFilterIpv6Address]
    destination_ports: list[StreamFilterPortRange]
    source: Optional[StreamFilterIpv6Address]
    source_ports: list[StreamFilterPortRange]
    def __init__(self) -> None:
        """Initialize StreamFilterRuleIpTp."""
        super().__init__()
        self.destination: Optional[StreamFilterIpv6Address] = None
        self.destination_ports: list[StreamFilterPortRange] = []
        self.source: Optional[StreamFilterIpv6Address] = None
        self.source_ports: list[StreamFilterPortRange] = []


class StreamFilterRuleIpTpBuilder:
    """Builder for StreamFilterRuleIpTp."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: StreamFilterRuleIpTp = StreamFilterRuleIpTp()

    def build(self) -> StreamFilterRuleIpTp:
        """Build and return StreamFilterRuleIpTp object.

        Returns:
            StreamFilterRuleIpTp instance
        """
        # TODO: Add validation
        return self._obj
