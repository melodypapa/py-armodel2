"""StreamFilterRuleDataLinkLayer AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 137)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.stream_filter_mac_address import (
    StreamFilterMACAddress,
)


class StreamFilterRuleDataLinkLayer(ARObject):
    """AUTOSAR StreamFilterRuleDataLinkLayer."""

    def __init__(self) -> None:
        """Initialize StreamFilterRuleDataLinkLayer."""
        super().__init__()
        self.destination_mac: Optional[StreamFilterMACAddress] = None
        self.ether_type: Optional[PositiveInteger] = None
        self.source_mac: Optional[StreamFilterMACAddress] = None
        self.vlan_id: Optional[PositiveInteger] = None
        self.vlan_priority: Optional[PositiveInteger] = None


class StreamFilterRuleDataLinkLayerBuilder:
    """Builder for StreamFilterRuleDataLinkLayer."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: StreamFilterRuleDataLinkLayer = StreamFilterRuleDataLinkLayer()

    def build(self) -> StreamFilterRuleDataLinkLayer:
        """Build and return StreamFilterRuleDataLinkLayer object.

        Returns:
            StreamFilterRuleDataLinkLayer instance
        """
        # TODO: Add validation
        return self._obj
