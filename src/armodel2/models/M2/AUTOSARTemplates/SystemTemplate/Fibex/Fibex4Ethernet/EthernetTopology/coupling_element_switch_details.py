"""CouplingElementSwitchDetails AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 133)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_element_abstract_details import (
    CouplingElementAbstractDetails,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_element_abstract_details import CouplingElementAbstractDetailsBuilder
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.switch_asynchronous_traffic_shaper_group_entry import (
    SwitchAsynchronousTrafficShaperGroupEntry,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.switch_flow_metering_entry import (
    SwitchFlowMeteringEntry,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.switch_stream_filter_entry import (
    SwitchStreamFilterEntry,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.switch_stream_gate_entry import (
    SwitchStreamGateEntry,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class CouplingElementSwitchDetails(CouplingElementAbstractDetails):
    """AUTOSAR CouplingElementSwitchDetails."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "COUPLING-ELEMENT-SWITCH-DETAILS"


    flow_meterings: list[SwitchFlowMeteringEntry]
    stream_filters: list[SwitchStreamFilterEntry]
    stream_gates: list[SwitchStreamGateEntry]
    switch_streams: list[Any]
    traffic_shapers: list[SwitchAsynchronousTrafficShaperGroupEntry]
    _DESERIALIZE_DISPATCH = {
        "FLOW-METERINGS": lambda obj, elem: obj.flow_meterings.append(SerializationHelper.deserialize_by_tag(elem, "SwitchFlowMeteringEntry")),
        "STREAM-FILTERS": lambda obj, elem: obj.stream_filters.append(SerializationHelper.deserialize_by_tag(elem, "SwitchStreamFilterEntry")),
        "STREAM-GATES": lambda obj, elem: obj.stream_gates.append(SerializationHelper.deserialize_by_tag(elem, "SwitchStreamGateEntry")),
        "SWITCH-STREAMS": lambda obj, elem: obj.switch_streams.append(SerializationHelper.deserialize_by_tag(elem, "any (SwitchStream)")),
        "TRAFFIC-SHAPERS": lambda obj, elem: obj.traffic_shapers.append(SerializationHelper.deserialize_by_tag(elem, "SwitchAsynchronousTrafficShaperGroupEntry")),
    }


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
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "FLOW-METERINGS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.flow_meterings.append(SerializationHelper.deserialize_by_tag(item_elem, "SwitchFlowMeteringEntry"))
            elif tag == "STREAM-FILTERS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.stream_filters.append(SerializationHelper.deserialize_by_tag(item_elem, "SwitchStreamFilterEntry"))
            elif tag == "STREAM-GATES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.stream_gates.append(SerializationHelper.deserialize_by_tag(item_elem, "SwitchStreamGateEntry"))
            elif tag == "SWITCH-STREAMS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.switch_streams.append(SerializationHelper.deserialize_by_tag(item_elem, "any (SwitchStream)"))
            elif tag == "TRAFFIC-SHAPERS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.traffic_shapers.append(SerializationHelper.deserialize_by_tag(item_elem, "SwitchAsynchronousTrafficShaperGroupEntry"))

        return obj



class CouplingElementSwitchDetailsBuilder(CouplingElementAbstractDetailsBuilder):
    """Builder for CouplingElementSwitchDetails with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CouplingElementSwitchDetails = CouplingElementSwitchDetails()


    def with_flow_meterings(self, items: list[SwitchFlowMeteringEntry]) -> "CouplingElementSwitchDetailsBuilder":
        """Set flow_meterings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.flow_meterings = list(items) if items else []
        return self

    def with_stream_filters(self, items: list[SwitchStreamFilterEntry]) -> "CouplingElementSwitchDetailsBuilder":
        """Set stream_filters list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.stream_filters = list(items) if items else []
        return self

    def with_stream_gates(self, items: list[SwitchStreamGateEntry]) -> "CouplingElementSwitchDetailsBuilder":
        """Set stream_gates list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.stream_gates = list(items) if items else []
        return self

    def with_switch_streams(self, items: list[any (SwitchStream)]) -> "CouplingElementSwitchDetailsBuilder":
        """Set switch_streams list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.switch_streams = list(items) if items else []
        return self

    def with_traffic_shapers(self, items: list[SwitchAsynchronousTrafficShaperGroupEntry]) -> "CouplingElementSwitchDetailsBuilder":
        """Set traffic_shapers list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.traffic_shapers = list(items) if items else []
        return self


    def add_flow_metering(self, item: SwitchFlowMeteringEntry) -> "CouplingElementSwitchDetailsBuilder":
        """Add a single item to flow_meterings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.flow_meterings.append(item)
        return self

    def clear_flow_meterings(self) -> "CouplingElementSwitchDetailsBuilder":
        """Clear all items from flow_meterings list.

        Returns:
            self for method chaining
        """
        self._obj.flow_meterings = []
        return self

    def add_stream_filter(self, item: SwitchStreamFilterEntry) -> "CouplingElementSwitchDetailsBuilder":
        """Add a single item to stream_filters list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.stream_filters.append(item)
        return self

    def clear_stream_filters(self) -> "CouplingElementSwitchDetailsBuilder":
        """Clear all items from stream_filters list.

        Returns:
            self for method chaining
        """
        self._obj.stream_filters = []
        return self

    def add_stream_gate(self, item: SwitchStreamGateEntry) -> "CouplingElementSwitchDetailsBuilder":
        """Add a single item to stream_gates list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.stream_gates.append(item)
        return self

    def clear_stream_gates(self) -> "CouplingElementSwitchDetailsBuilder":
        """Clear all items from stream_gates list.

        Returns:
            self for method chaining
        """
        self._obj.stream_gates = []
        return self

    def add_switch_stream(self, item: any (SwitchStream)) -> "CouplingElementSwitchDetailsBuilder":
        """Add a single item to switch_streams list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.switch_streams.append(item)
        return self

    def clear_switch_streams(self) -> "CouplingElementSwitchDetailsBuilder":
        """Clear all items from switch_streams list.

        Returns:
            self for method chaining
        """
        self._obj.switch_streams = []
        return self

    def add_traffic_shaper(self, item: SwitchAsynchronousTrafficShaperGroupEntry) -> "CouplingElementSwitchDetailsBuilder":
        """Add a single item to traffic_shapers list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.traffic_shapers.append(item)
        return self

    def clear_traffic_shapers(self) -> "CouplingElementSwitchDetailsBuilder":
        """Clear all items from traffic_shapers list.

        Returns:
            self for method chaining
        """
        self._obj.traffic_shapers = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "flowMetering",
        "streamFilter",
        "streamGate",
        "switchStream",
        "trafficShaper",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> CouplingElementSwitchDetails:
        """Build and return the CouplingElementSwitchDetails instance with validation."""
        self._validate_instance()
        return self._obj