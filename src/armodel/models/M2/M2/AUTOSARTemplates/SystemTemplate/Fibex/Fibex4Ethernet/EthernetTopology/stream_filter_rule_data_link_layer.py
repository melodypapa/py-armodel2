"""StreamFilterRuleDataLinkLayer AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 137)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.stream_filter_mac_address import (
    StreamFilterMACAddress,
)


class StreamFilterRuleDataLinkLayer(ARObject):
    """AUTOSAR StreamFilterRuleDataLinkLayer."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "destination_mac": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=StreamFilterMACAddress,
        ),  # destinationMac
        "ether_type": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # etherType
        "source_mac": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=StreamFilterMACAddress,
        ),  # sourceMac
        "vlan_id": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # vlanId
        "vlan_priority": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # vlanPriority
    }

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
