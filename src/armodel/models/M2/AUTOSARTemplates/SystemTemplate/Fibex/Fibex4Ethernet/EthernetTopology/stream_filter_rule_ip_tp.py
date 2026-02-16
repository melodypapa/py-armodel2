"""StreamFilterRuleIpTp AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.stream_filter_ipv6_address import (
    StreamFilterIpv6Address,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.stream_filter_port_range import (
    StreamFilterPortRange,
)


class StreamFilterRuleIpTp(ARObject):
    """AUTOSAR StreamFilterRuleIpTp."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("destination", None, False, False, StreamFilterIpv6Address),  # destination
        ("destination_ports", None, False, True, StreamFilterPortRange),  # destinationPorts
        ("source", None, False, False, StreamFilterIpv6Address),  # source
        ("source_ports", None, False, True, StreamFilterPortRange),  # sourcePorts
    ]

    def __init__(self) -> None:
        """Initialize StreamFilterRuleIpTp."""
        super().__init__()
        self.destination: Optional[StreamFilterIpv6Address] = None
        self.destination_ports: list[StreamFilterPortRange] = []
        self.source: Optional[StreamFilterIpv6Address] = None
        self.source_ports: list[StreamFilterPortRange] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert StreamFilterRuleIpTp to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "StreamFilterRuleIpTp":
        """Create StreamFilterRuleIpTp from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            StreamFilterRuleIpTp instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to StreamFilterRuleIpTp since parent returns ARObject
        return cast("StreamFilterRuleIpTp", obj)


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
