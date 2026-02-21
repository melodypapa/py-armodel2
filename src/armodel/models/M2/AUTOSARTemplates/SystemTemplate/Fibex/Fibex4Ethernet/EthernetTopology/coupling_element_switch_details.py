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
from armodel.serialization import SerializationHelper
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

    def serialize(self) -> ET.Element:
        """Serialize CouplingElementSwitchDetails to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CouplingElementSwitchDetails, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize flow_meterings (list to container "FLOW-METERINGS")
        if self.flow_meterings:
            wrapper = ET.Element("FLOW-METERINGS")
            for item in self.flow_meterings:
                serialized = SerializationHelper.serialize_item(item, "SwitchFlowMeteringEntry")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize stream_filters (list to container "STREAM-FILTERS")
        if self.stream_filters:
            wrapper = ET.Element("STREAM-FILTERS")
            for item in self.stream_filters:
                serialized = SerializationHelper.serialize_item(item, "SwitchStreamFilterEntry")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize stream_gates (list to container "STREAM-GATES")
        if self.stream_gates:
            wrapper = ET.Element("STREAM-GATES")
            for item in self.stream_gates:
                serialized = SerializationHelper.serialize_item(item, "SwitchStreamGateEntry")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize switch_streams (list to container "SWITCH-STREAMS")
        if self.switch_streams:
            wrapper = ET.Element("SWITCH-STREAMS")
            for item in self.switch_streams:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize traffic_shapers (list to container "TRAFFIC-SHAPERS")
        if self.traffic_shapers:
            wrapper = ET.Element("TRAFFIC-SHAPERS")
            for item in self.traffic_shapers:
                serialized = SerializationHelper.serialize_item(item, "SwitchAsynchronousTrafficShaperGroupEntry")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CouplingElementSwitchDetails":
        """Deserialize XML element to CouplingElementSwitchDetails object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CouplingElementSwitchDetails object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CouplingElementSwitchDetails, cls).deserialize(element)

        # Parse flow_meterings (list from container "FLOW-METERINGS")
        obj.flow_meterings = []
        container = SerializationHelper.find_child_element(element, "FLOW-METERINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.flow_meterings.append(child_value)

        # Parse stream_filters (list from container "STREAM-FILTERS")
        obj.stream_filters = []
        container = SerializationHelper.find_child_element(element, "STREAM-FILTERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.stream_filters.append(child_value)

        # Parse stream_gates (list from container "STREAM-GATES")
        obj.stream_gates = []
        container = SerializationHelper.find_child_element(element, "STREAM-GATES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.stream_gates.append(child_value)

        # Parse switch_streams (list from container "SWITCH-STREAMS")
        obj.switch_streams = []
        container = SerializationHelper.find_child_element(element, "SWITCH-STREAMS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.switch_streams.append(child_value)

        # Parse traffic_shapers (list from container "TRAFFIC-SHAPERS")
        obj.traffic_shapers = []
        container = SerializationHelper.find_child_element(element, "TRAFFIC-SHAPERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.traffic_shapers.append(child_value)

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
