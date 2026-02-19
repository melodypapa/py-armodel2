"""CouplingElementSwitchDetails AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 133)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_element_abstract_details import (
    CouplingElementAbstractDetails,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    flow_meterings: list[SwitchFlowMeteringEntry]
    stream_filters: list[SwitchStreamFilterEntry]
    stream_gates: list[SwitchStreamGateEntry]
    switch_streams: list[Any]
    traffic_shapers: list[SwitchAsynchronousTrafficShaperGroupEntry]
    def __init__(self) -> None:
        """Initialize CouplingElementSwitchDetails."""
        super().__init__()
        self.flow_meterings: list[SwitchFlowMeteringEntry] = []
        self.stream_filters: list[SwitchStreamFilterEntry] = []
        self.stream_gates: list[SwitchStreamGateEntry] = []
        self.switch_streams: list[Any] = []
        self.traffic_shapers: list[SwitchAsynchronousTrafficShaperGroupEntry] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "CouplingElementSwitchDetails":
        """Deserialize XML element to CouplingElementSwitchDetails object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CouplingElementSwitchDetails object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse flow_meterings (list)
        obj.flow_meterings = []
        for child in ARObject._find_all_child_elements(element, "FLOW-METERINGS"):
            flow_meterings_value = ARObject._deserialize_by_tag(child, "SwitchFlowMeteringEntry")
            obj.flow_meterings.append(flow_meterings_value)

        # Parse stream_filters (list)
        obj.stream_filters = []
        for child in ARObject._find_all_child_elements(element, "STREAM-FILTERS"):
            stream_filters_value = ARObject._deserialize_by_tag(child, "SwitchStreamFilterEntry")
            obj.stream_filters.append(stream_filters_value)

        # Parse stream_gates (list)
        obj.stream_gates = []
        for child in ARObject._find_all_child_elements(element, "STREAM-GATES"):
            stream_gates_value = ARObject._deserialize_by_tag(child, "SwitchStreamGateEntry")
            obj.stream_gates.append(stream_gates_value)

        # Parse switch_streams (list)
        obj.switch_streams = []
        for child in ARObject._find_all_child_elements(element, "SWITCH-STREAMS"):
            switch_streams_value = child.text
            obj.switch_streams.append(switch_streams_value)

        # Parse traffic_shapers (list)
        obj.traffic_shapers = []
        for child in ARObject._find_all_child_elements(element, "TRAFFIC-SHAPERS"):
            traffic_shapers_value = ARObject._deserialize_by_tag(child, "SwitchAsynchronousTrafficShaperGroupEntry")
            obj.traffic_shapers.append(traffic_shapers_value)

        return obj



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
