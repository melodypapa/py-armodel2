"""StreamFilterRuleIpTp AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "destination": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=StreamFilterIpv6Address,
        ),  # destination
        "destination_ports": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=StreamFilterPortRange,
        ),  # destinationPorts
        "source": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=StreamFilterIpv6Address,
        ),  # source
        "source_ports": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=StreamFilterPortRange,
        ),  # sourcePorts
    }

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
