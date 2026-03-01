"""StreamFilterRuleDataLinkLayer AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 137)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.stream_filter_mac_address import (
    StreamFilterMACAddress,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class StreamFilterRuleDataLinkLayer(ARObject):
    """AUTOSAR StreamFilterRuleDataLinkLayer."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "STREAM-FILTER-RULE-DATA-LINK-LAYER"


    destination_mac: Optional[StreamFilterMACAddress]
    ether_type: Optional[PositiveInteger]
    source_mac: Optional[StreamFilterMACAddress]
    vlan_id: Optional[PositiveInteger]
    vlan_priority: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "DESTINATION-MAC": lambda obj, elem: setattr(obj, "destination_mac", SerializationHelper.deserialize_by_tag(elem, "StreamFilterMACAddress")),
        "ETHER-TYPE": lambda obj, elem: setattr(obj, "ether_type", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "SOURCE-MAC": lambda obj, elem: setattr(obj, "source_mac", SerializationHelper.deserialize_by_tag(elem, "StreamFilterMACAddress")),
        "VLAN-ID": lambda obj, elem: setattr(obj, "vlan_id", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "VLAN-PRIORITY": lambda obj, elem: setattr(obj, "vlan_priority", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize StreamFilterRuleDataLinkLayer."""
        super().__init__()
        self.destination_mac: Optional[StreamFilterMACAddress] = None
        self.ether_type: Optional[PositiveInteger] = None
        self.source_mac: Optional[StreamFilterMACAddress] = None
        self.vlan_id: Optional[PositiveInteger] = None
        self.vlan_priority: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize StreamFilterRuleDataLinkLayer to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(StreamFilterRuleDataLinkLayer, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize destination_mac
        if self.destination_mac is not None:
            serialized = SerializationHelper.serialize_item(self.destination_mac, "StreamFilterMACAddress")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DESTINATION-MAC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ether_type
        if self.ether_type is not None:
            serialized = SerializationHelper.serialize_item(self.ether_type, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ETHER-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize source_mac
        if self.source_mac is not None:
            serialized = SerializationHelper.serialize_item(self.source_mac, "StreamFilterMACAddress")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SOURCE-MAC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize vlan_id
        if self.vlan_id is not None:
            serialized = SerializationHelper.serialize_item(self.vlan_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VLAN-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize vlan_priority
        if self.vlan_priority is not None:
            serialized = SerializationHelper.serialize_item(self.vlan_priority, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VLAN-PRIORITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "StreamFilterRuleDataLinkLayer":
        """Deserialize XML element to StreamFilterRuleDataLinkLayer object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized StreamFilterRuleDataLinkLayer object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(StreamFilterRuleDataLinkLayer, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "DESTINATION-MAC":
                setattr(obj, "destination_mac", SerializationHelper.deserialize_by_tag(child, "StreamFilterMACAddress"))
            elif tag == "ETHER-TYPE":
                setattr(obj, "ether_type", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "SOURCE-MAC":
                setattr(obj, "source_mac", SerializationHelper.deserialize_by_tag(child, "StreamFilterMACAddress"))
            elif tag == "VLAN-ID":
                setattr(obj, "vlan_id", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "VLAN-PRIORITY":
                setattr(obj, "vlan_priority", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class StreamFilterRuleDataLinkLayerBuilder(BuilderBase):
    """Builder for StreamFilterRuleDataLinkLayer with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: StreamFilterRuleDataLinkLayer = StreamFilterRuleDataLinkLayer()


    def with_destination_mac(self, value: Optional[StreamFilterMACAddress]) -> "StreamFilterRuleDataLinkLayerBuilder":
        """Set destination_mac attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.destination_mac = value
        return self

    def with_ether_type(self, value: Optional[PositiveInteger]) -> "StreamFilterRuleDataLinkLayerBuilder":
        """Set ether_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ether_type = value
        return self

    def with_source_mac(self, value: Optional[StreamFilterMACAddress]) -> "StreamFilterRuleDataLinkLayerBuilder":
        """Set source_mac attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.source_mac = value
        return self

    def with_vlan_id(self, value: Optional[PositiveInteger]) -> "StreamFilterRuleDataLinkLayerBuilder":
        """Set vlan_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.vlan_id = value
        return self

    def with_vlan_priority(self, value: Optional[PositiveInteger]) -> "StreamFilterRuleDataLinkLayerBuilder":
        """Set vlan_priority attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.vlan_priority = value
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


    def build(self) -> StreamFilterRuleDataLinkLayer:
        """Build and return the StreamFilterRuleDataLinkLayer instance with validation."""
        self._validate_instance()
        pass
        return self._obj