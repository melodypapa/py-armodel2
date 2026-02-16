"""CouplingElementSwitchDetails AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_element_abstract_details import (
    CouplingElementAbstractDetails,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.switch_asynchronous_traffic_shaper_group_entry import (
    SwitchAsynchronousTrafficShaperGroupEntry,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.switch_flow_metering_entry import (
    SwitchFlowMeteringEntry,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.switch_stream_filter_entry import (
    SwitchStreamFilterEntry,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.switch_stream_gate_entry import (
    SwitchStreamGateEntry,
)


class CouplingElementSwitchDetails(CouplingElementAbstractDetails):
    """AUTOSAR CouplingElementSwitchDetails."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("flow_meterings", None, False, True, SwitchFlowMeteringEntry),  # flowMeterings
        ("stream_filters", None, False, True, SwitchStreamFilterEntry),  # streamFilters
        ("stream_gates", None, False, True, SwitchStreamGateEntry),  # streamGates
        ("switch_streams", None, False, True, any (SwitchStream)),  # switchStreams
        ("traffic_shapers", None, False, True, SwitchAsynchronousTrafficShaperGroupEntry),  # trafficShapers
    ]

    def __init__(self) -> None:
        """Initialize CouplingElementSwitchDetails."""
        super().__init__()
        self.flow_meterings: list[SwitchFlowMeteringEntry] = []
        self.stream_filters: list[SwitchStreamFilterEntry] = []
        self.stream_gates: list[SwitchStreamGateEntry] = []
        self.switch_streams: list[Any] = []
        self.traffic_shapers: list[SwitchAsynchronousTrafficShaperGroupEntry] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CouplingElementSwitchDetails to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CouplingElementSwitchDetails":
        """Create CouplingElementSwitchDetails from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CouplingElementSwitchDetails instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CouplingElementSwitchDetails since parent returns ARObject
        return cast("CouplingElementSwitchDetails", obj)


class CouplingElementSwitchDetailsBuilder:
    """Builder for CouplingElementSwitchDetails."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CouplingElementSwitchDetails = CouplingElementSwitchDetails()

    def build(self) -> CouplingElementSwitchDetails:
        """Build and return CouplingElementSwitchDetails object.

        Returns:
            CouplingElementSwitchDetails instance
        """
        # TODO: Add validation
        return self._obj
