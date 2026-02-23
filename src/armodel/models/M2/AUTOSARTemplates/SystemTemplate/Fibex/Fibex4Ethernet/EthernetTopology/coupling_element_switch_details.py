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
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_element_abstract_details import CouplingElementAbstractDetailsBuilder
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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


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



    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Get type hints for the class
        try:
            type_hints_dict = get_type_hints(type(self._obj))
        except Exception:
            # Cannot resolve type hints (e.g., forward references), skip validation
            return

        for attr_name, attr_type in type_hints_dict.items():
            if attr_name.startswith("_"):
                continue

            value = getattr(self._obj, attr_name)

            # Check required fields (not Optional)
            if value is None and not self._is_optional_type(attr_type):
                if mode == BuilderValidationMode.STRICT:
                    raise ValueError(
                        f"Required attribute '{attr_name}' is None"
                    )
                elif mode == BuilderValidationMode.LENIENT:
                    import warnings
                    warnings.warn(
                        f"Required attribute '{attr_name}' is None",
                        UserWarning
                    )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type is Optional, False otherwise
        """
        origin = getattr(type_hint, "__origin__", None)
        return origin is Union

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract expected type from type hint.

        Args:
            type_hint: Type hint to extract from

        Returns:
            Expected type
        """
        if isinstance(type_hint, str):
            return object
        origin = getattr(type_hint, "__origin__", None)
        if origin is Union:
            args = getattr(type_hint, "__args__", [])
            for arg in args:
                if arg is not type(None):
                    return arg
        elif origin is list:
            args = getattr(type_hint, "__args__", [object])
            return args[0] if args else object
        return type_hint if isinstance(type_hint, type) else object


    def build(self) -> CouplingElementSwitchDetails:
        """Build and return the CouplingElementSwitchDetails instance with validation."""
        self._validate_instance()
        pass
        return self._obj