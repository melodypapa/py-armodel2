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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "StreamFilterRuleIpTp":
        """Deserialize XML element to StreamFilterRuleIpTp object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized StreamFilterRuleIpTp object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse destination
        child = ARObject._find_child_element(element, "DESTINATION")
        if child is not None:
            destination_value = ARObject._deserialize_by_tag(child, "StreamFilterIpv6Address")
            obj.destination = destination_value

        # Parse destination_ports (list)
        obj.destination_ports = []
        for child in ARObject._find_all_child_elements(element, "DESTINATION-PORTS"):
            destination_ports_value = ARObject._deserialize_by_tag(child, "StreamFilterPortRange")
            obj.destination_ports.append(destination_ports_value)

        # Parse source
        child = ARObject._find_child_element(element, "SOURCE")
        if child is not None:
            source_value = ARObject._deserialize_by_tag(child, "StreamFilterIpv6Address")
            obj.source = source_value

        # Parse source_ports (list)
        obj.source_ports = []
        for child in ARObject._find_all_child_elements(element, "SOURCE-PORTS"):
            source_ports_value = ARObject._deserialize_by_tag(child, "StreamFilterPortRange")
            obj.source_ports.append(source_ports_value)

        return obj



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
