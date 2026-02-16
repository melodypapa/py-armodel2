"""StreamFilterRuleDataLinkLayer AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.stream_filter_mac_address import (
    StreamFilterMACAddress,
)


class StreamFilterRuleDataLinkLayer(ARObject):
    """AUTOSAR StreamFilterRuleDataLinkLayer."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("destination_mac", None, False, False, StreamFilterMACAddress),  # destinationMac
        ("ether_type", None, True, False, None),  # etherType
        ("source_mac", None, False, False, StreamFilterMACAddress),  # sourceMac
        ("vlan_id", None, True, False, None),  # vlanId
        ("vlan_priority", None, True, False, None),  # vlanPriority
    ]

    def __init__(self) -> None:
        """Initialize StreamFilterRuleDataLinkLayer."""
        super().__init__()
        self.destination_mac: Optional[StreamFilterMACAddress] = None
        self.ether_type: Optional[PositiveInteger] = None
        self.source_mac: Optional[StreamFilterMACAddress] = None
        self.vlan_id: Optional[PositiveInteger] = None
        self.vlan_priority: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert StreamFilterRuleDataLinkLayer to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "StreamFilterRuleDataLinkLayer":
        """Create StreamFilterRuleDataLinkLayer from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            StreamFilterRuleDataLinkLayer instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to StreamFilterRuleDataLinkLayer since parent returns ARObject
        return cast("StreamFilterRuleDataLinkLayer", obj)


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
