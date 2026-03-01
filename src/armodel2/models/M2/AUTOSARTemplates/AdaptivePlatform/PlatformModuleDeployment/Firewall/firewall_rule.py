"""FirewallRule AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 584)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_AdaptivePlatform_PlatformModuleDeployment_Firewall.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class FirewallRule(ARElement):
    """AUTOSAR FirewallRule."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "FIREWALL-RULE"


    bucket_size: Optional[PositiveInteger]
    data_link_layer_rule: Optional[Any]
    dds_rule: Optional[Any]
    do_ip_rule: Optional[Any]
    network_layer_rule: Optional[Any]
    payload_byte_patterns: list[Any]
    refill_amount: Optional[PositiveInteger]
    someip_rule: Optional[Any]
    someip_sd_rule: Optional[Any]
    transport_layer_rule: Optional[Any]
    _DESERIALIZE_DISPATCH = {
        "BUCKET-SIZE": lambda obj, elem: setattr(obj, "bucket_size", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "DATA-LINK-LAYER-RULE": lambda obj, elem: setattr(obj, "data_link_layer_rule", SerializationHelper.deserialize_by_tag(elem, "any (DataLinkLayerRule)")),
        "DDS-RULE": lambda obj, elem: setattr(obj, "dds_rule", SerializationHelper.deserialize_by_tag(elem, "any (DdsRule)")),
        "DO-IP-RULE": lambda obj, elem: setattr(obj, "do_ip_rule", SerializationHelper.deserialize_by_tag(elem, "any (DoIpRule)")),
        "NETWORK-LAYER-RULE": lambda obj, elem: setattr(obj, "network_layer_rule", SerializationHelper.deserialize_by_tag(elem, "any (NetworkLayerRule)")),
        "PAYLOAD-BYTE-PATTERNS": lambda obj, elem: obj.payload_byte_patterns.append(SerializationHelper.deserialize_by_tag(elem, "any (PayloadBytePattern)")),
        "REFILL-AMOUNT": lambda obj, elem: setattr(obj, "refill_amount", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "SOMEIP-RULE": lambda obj, elem: setattr(obj, "someip_rule", SerializationHelper.deserialize_by_tag(elem, "any (SomeipProtocolRule)")),
        "SOMEIP-SD-RULE": lambda obj, elem: setattr(obj, "someip_sd_rule", SerializationHelper.deserialize_by_tag(elem, "any (SomeipSdRule)")),
        "TRANSPORT-LAYER-RULE": lambda obj, elem: setattr(obj, "transport_layer_rule", SerializationHelper.deserialize_by_tag(elem, "any (TransportLayerRule)")),
    }


    def __init__(self) -> None:
        """Initialize FirewallRule."""
        super().__init__()
        self.bucket_size: Optional[PositiveInteger] = None
        self.data_link_layer_rule: Optional[Any] = None
        self.dds_rule: Optional[Any] = None
        self.do_ip_rule: Optional[Any] = None
        self.network_layer_rule: Optional[Any] = None
        self.payload_byte_patterns: list[Any] = []
        self.refill_amount: Optional[PositiveInteger] = None
        self.someip_rule: Optional[Any] = None
        self.someip_sd_rule: Optional[Any] = None
        self.transport_layer_rule: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize FirewallRule to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FirewallRule, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize bucket_size
        if self.bucket_size is not None:
            serialized = SerializationHelper.serialize_item(self.bucket_size, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BUCKET-SIZE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize data_link_layer_rule
        if self.data_link_layer_rule is not None:
            serialized = SerializationHelper.serialize_item(self.data_link_layer_rule, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-LINK-LAYER-RULE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize dds_rule
        if self.dds_rule is not None:
            serialized = SerializationHelper.serialize_item(self.dds_rule, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DDS-RULE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize do_ip_rule
        if self.do_ip_rule is not None:
            serialized = SerializationHelper.serialize_item(self.do_ip_rule, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DO-IP-RULE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize network_layer_rule
        if self.network_layer_rule is not None:
            serialized = SerializationHelper.serialize_item(self.network_layer_rule, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NETWORK-LAYER-RULE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize payload_byte_patterns (list to container "PAYLOAD-BYTE-PATTERNS")
        if self.payload_byte_patterns:
            wrapper = ET.Element("PAYLOAD-BYTE-PATTERNS")
            for item in self.payload_byte_patterns:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize refill_amount
        if self.refill_amount is not None:
            serialized = SerializationHelper.serialize_item(self.refill_amount, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REFILL-AMOUNT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize someip_rule
        if self.someip_rule is not None:
            serialized = SerializationHelper.serialize_item(self.someip_rule, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SOMEIP-RULE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize someip_sd_rule
        if self.someip_sd_rule is not None:
            serialized = SerializationHelper.serialize_item(self.someip_sd_rule, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SOMEIP-SD-RULE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize transport_layer_rule
        if self.transport_layer_rule is not None:
            serialized = SerializationHelper.serialize_item(self.transport_layer_rule, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRANSPORT-LAYER-RULE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FirewallRule":
        """Deserialize XML element to FirewallRule object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FirewallRule object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FirewallRule, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "BUCKET-SIZE":
                setattr(obj, "bucket_size", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "DATA-LINK-LAYER-RULE":
                setattr(obj, "data_link_layer_rule", SerializationHelper.deserialize_by_tag(child, "any (DataLinkLayerRule)"))
            elif tag == "DDS-RULE":
                setattr(obj, "dds_rule", SerializationHelper.deserialize_by_tag(child, "any (DdsRule)"))
            elif tag == "DO-IP-RULE":
                setattr(obj, "do_ip_rule", SerializationHelper.deserialize_by_tag(child, "any (DoIpRule)"))
            elif tag == "NETWORK-LAYER-RULE":
                setattr(obj, "network_layer_rule", SerializationHelper.deserialize_by_tag(child, "any (NetworkLayerRule)"))
            elif tag == "PAYLOAD-BYTE-PATTERNS":
                obj.payload_byte_patterns.append(SerializationHelper.deserialize_by_tag(child, "any (PayloadBytePattern)"))
            elif tag == "REFILL-AMOUNT":
                setattr(obj, "refill_amount", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "SOMEIP-RULE":
                setattr(obj, "someip_rule", SerializationHelper.deserialize_by_tag(child, "any (SomeipProtocolRule)"))
            elif tag == "SOMEIP-SD-RULE":
                setattr(obj, "someip_sd_rule", SerializationHelper.deserialize_by_tag(child, "any (SomeipSdRule)"))
            elif tag == "TRANSPORT-LAYER-RULE":
                setattr(obj, "transport_layer_rule", SerializationHelper.deserialize_by_tag(child, "any (TransportLayerRule)"))

        return obj



class FirewallRuleBuilder(ARElementBuilder):
    """Builder for FirewallRule with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: FirewallRule = FirewallRule()


    def with_bucket_size(self, value: Optional[PositiveInteger]) -> "FirewallRuleBuilder":
        """Set bucket_size attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.bucket_size = value
        return self

    def with_data_link_layer_rule(self, value: Optional[any (DataLinkLayerRule)]) -> "FirewallRuleBuilder":
        """Set data_link_layer_rule attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.data_link_layer_rule = value
        return self

    def with_dds_rule(self, value: Optional[any (DdsRule)]) -> "FirewallRuleBuilder":
        """Set dds_rule attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.dds_rule = value
        return self

    def with_do_ip_rule(self, value: Optional[any (DoIpRule)]) -> "FirewallRuleBuilder":
        """Set do_ip_rule attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.do_ip_rule = value
        return self

    def with_network_layer_rule(self, value: Optional[any (NetworkLayerRule)]) -> "FirewallRuleBuilder":
        """Set network_layer_rule attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.network_layer_rule = value
        return self

    def with_payload_byte_patterns(self, items: list[any (PayloadBytePattern)]) -> "FirewallRuleBuilder":
        """Set payload_byte_patterns list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.payload_byte_patterns = list(items) if items else []
        return self

    def with_refill_amount(self, value: Optional[PositiveInteger]) -> "FirewallRuleBuilder":
        """Set refill_amount attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.refill_amount = value
        return self

    def with_someip_rule(self, value: Optional[any (SomeipProtocolRule)]) -> "FirewallRuleBuilder":
        """Set someip_rule attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.someip_rule = value
        return self

    def with_someip_sd_rule(self, value: Optional[any (SomeipSdRule)]) -> "FirewallRuleBuilder":
        """Set someip_sd_rule attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.someip_sd_rule = value
        return self

    def with_transport_layer_rule(self, value: Optional[any (TransportLayerRule)]) -> "FirewallRuleBuilder":
        """Set transport_layer_rule attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.transport_layer_rule = value
        return self


    def add_payload_byte_pattern(self, item: any (PayloadBytePattern)) -> "FirewallRuleBuilder":
        """Add a single item to payload_byte_patterns list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.payload_byte_patterns.append(item)
        return self

    def clear_payload_byte_patterns(self) -> "FirewallRuleBuilder":
        """Clear all items from payload_byte_patterns list.

        Returns:
            self for method chaining
        """
        self._obj.payload_byte_patterns = []
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


    def build(self) -> FirewallRule:
        """Build and return the FirewallRule instance with validation."""
        self._validate_instance()
        pass
        return self._obj