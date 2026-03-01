"""StreamFilterRuleIpTp AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 137)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.stream_filter_ipv6_address import (
    StreamFilterIpv6Address,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.stream_filter_port_range import (
    StreamFilterPortRange,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class StreamFilterRuleIpTp(ARObject):
    """AUTOSAR StreamFilterRuleIpTp."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "STREAM-FILTER-RULE-IP-TP"


    destination: Optional[StreamFilterIpv6Address]
    destination_ports: list[StreamFilterPortRange]
    source: Optional[StreamFilterIpv6Address]
    source_ports: list[StreamFilterPortRange]
    _DESERIALIZE_DISPATCH = {
        "DESTINATION": lambda obj, elem: setattr(obj, "destination", SerializationHelper.deserialize_by_tag(elem, "StreamFilterIpv6Address")),
        "DESTINATION-PORTS": lambda obj, elem: obj.destination_ports.append(SerializationHelper.deserialize_by_tag(elem, "StreamFilterPortRange")),
        "SOURCE": lambda obj, elem: setattr(obj, "source", SerializationHelper.deserialize_by_tag(elem, "StreamFilterIpv6Address")),
        "SOURCE-PORTS": lambda obj, elem: obj.source_ports.append(SerializationHelper.deserialize_by_tag(elem, "StreamFilterPortRange")),
    }


    def __init__(self) -> None:
        """Initialize StreamFilterRuleIpTp."""
        super().__init__()
        self.destination: Optional[StreamFilterIpv6Address] = None
        self.destination_ports: list[StreamFilterPortRange] = []
        self.source: Optional[StreamFilterIpv6Address] = None
        self.source_ports: list[StreamFilterPortRange] = []

    def serialize(self) -> ET.Element:
        """Serialize StreamFilterRuleIpTp to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(StreamFilterRuleIpTp, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize destination
        if self.destination is not None:
            serialized = SerializationHelper.serialize_item(self.destination, "StreamFilterIpv6Address")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DESTINATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize destination_ports (list to container "DESTINATION-PORTS")
        if self.destination_ports:
            wrapper = ET.Element("DESTINATION-PORTS")
            for item in self.destination_ports:
                serialized = SerializationHelper.serialize_item(item, "StreamFilterPortRange")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize source
        if self.source is not None:
            serialized = SerializationHelper.serialize_item(self.source, "StreamFilterIpv6Address")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SOURCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize source_ports (list to container "SOURCE-PORTS")
        if self.source_ports:
            wrapper = ET.Element("SOURCE-PORTS")
            for item in self.source_ports:
                serialized = SerializationHelper.serialize_item(item, "StreamFilterPortRange")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "StreamFilterRuleIpTp":
        """Deserialize XML element to StreamFilterRuleIpTp object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized StreamFilterRuleIpTp object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(StreamFilterRuleIpTp, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "DESTINATION":
                setattr(obj, "destination", SerializationHelper.deserialize_by_tag(child, "StreamFilterIpv6Address"))
            elif tag == "DESTINATION-PORTS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.destination_ports.append(SerializationHelper.deserialize_by_tag(item_elem, "StreamFilterPortRange"))
            elif tag == "SOURCE":
                setattr(obj, "source", SerializationHelper.deserialize_by_tag(child, "StreamFilterIpv6Address"))
            elif tag == "SOURCE-PORTS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.source_ports.append(SerializationHelper.deserialize_by_tag(item_elem, "StreamFilterPortRange"))

        return obj



class StreamFilterRuleIpTpBuilder(BuilderBase):
    """Builder for StreamFilterRuleIpTp with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: StreamFilterRuleIpTp = StreamFilterRuleIpTp()


    def with_destination(self, value: Optional[StreamFilterIpv6Address]) -> "StreamFilterRuleIpTpBuilder":
        """Set destination attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.destination = value
        return self

    def with_destination_ports(self, items: list[StreamFilterPortRange]) -> "StreamFilterRuleIpTpBuilder":
        """Set destination_ports list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.destination_ports = list(items) if items else []
        return self

    def with_source(self, value: Optional[StreamFilterIpv6Address]) -> "StreamFilterRuleIpTpBuilder":
        """Set source attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.source = value
        return self

    def with_source_ports(self, items: list[StreamFilterPortRange]) -> "StreamFilterRuleIpTpBuilder":
        """Set source_ports list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.source_ports = list(items) if items else []
        return self


    def add_destination_port(self, item: StreamFilterPortRange) -> "StreamFilterRuleIpTpBuilder":
        """Add a single item to destination_ports list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.destination_ports.append(item)
        return self

    def clear_destination_ports(self) -> "StreamFilterRuleIpTpBuilder":
        """Clear all items from destination_ports list.

        Returns:
            self for method chaining
        """
        self._obj.destination_ports = []
        return self

    def add_source_port(self, item: StreamFilterPortRange) -> "StreamFilterRuleIpTpBuilder":
        """Add a single item to source_ports list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.source_ports.append(item)
        return self

    def clear_source_ports(self) -> "StreamFilterRuleIpTpBuilder":
        """Clear all items from source_ports list.

        Returns:
            self for method chaining
        """
        self._obj.source_ports = []
        return self



    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

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


    def build(self) -> StreamFilterRuleIpTp:
        """Build and return the StreamFilterRuleIpTp instance with validation."""
        self._validate_instance()
        pass
        return self._obj