"""Ipv6Configuration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 466)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.network_endpoint_address import (
    NetworkEndpointAddress,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.network_endpoint_address import NetworkEndpointAddressBuilder
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    IpAddressKeepEnum,
    Ipv6AddressSourceEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Ip6AddressString,
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class Ipv6Configuration(NetworkEndpointAddress):
    """AUTOSAR Ipv6Configuration."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "IPV6-CONFIGURATION"


    assignment: Optional[PositiveInteger]
    default_router: Optional[Ip6AddressString]
    dns_servers: list[Ip6AddressString]
    enable_anycast: Optional[Boolean]
    hop_count: Optional[PositiveInteger]
    ip_address_keep_enum: Optional[IpAddressKeepEnum]
    ip_address_prefix: Optional[PositiveInteger]
    ipv6_address: Optional[Ip6AddressString]
    ipv6_address_source: Optional[Ipv6AddressSourceEnum]
    _DESERIALIZE_DISPATCH = {
        "ASSIGNMENT": lambda obj, elem: setattr(obj, "assignment", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "DEFAULT-ROUTER": lambda obj, elem: setattr(obj, "default_router", SerializationHelper.deserialize_by_tag(elem, "Ip6AddressString")),
        "DNS-SERVERS": lambda obj, elem: obj.dns_servers.append(SerializationHelper.deserialize_by_tag(elem, "Ip6AddressString")),
        "ENABLE-ANYCAST": lambda obj, elem: setattr(obj, "enable_anycast", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "HOP-COUNT": lambda obj, elem: setattr(obj, "hop_count", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "IP-ADDRESS-KEEP-ENUM": lambda obj, elem: setattr(obj, "ip_address_keep_enum", IpAddressKeepEnum.deserialize(elem)),
        "IP-ADDRESS-PREFIX": lambda obj, elem: setattr(obj, "ip_address_prefix", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "IPV6-ADDRESS": lambda obj, elem: setattr(obj, "ipv6_address", SerializationHelper.deserialize_by_tag(elem, "Ip6AddressString")),
        "IPV6-ADDRESS-SOURCE": lambda obj, elem: setattr(obj, "ipv6_address_source", Ipv6AddressSourceEnum.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize Ipv6Configuration."""
        super().__init__()
        self.assignment: Optional[PositiveInteger] = None
        self.default_router: Optional[Ip6AddressString] = None
        self.dns_servers: list[Ip6AddressString] = []
        self.enable_anycast: Optional[Boolean] = None
        self.hop_count: Optional[PositiveInteger] = None
        self.ip_address_keep_enum: Optional[IpAddressKeepEnum] = None
        self.ip_address_prefix: Optional[PositiveInteger] = None
        self.ipv6_address: Optional[Ip6AddressString] = None
        self.ipv6_address_source: Optional[Ipv6AddressSourceEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize Ipv6Configuration to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Ipv6Configuration, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize assignment
        if self.assignment is not None:
            serialized = SerializationHelper.serialize_item(self.assignment, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ASSIGNMENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize default_router
        if self.default_router is not None:
            serialized = SerializationHelper.serialize_item(self.default_router, "Ip6AddressString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEFAULT-ROUTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize dns_servers (list to container "DNS-SERVERS")
        if self.dns_servers:
            wrapper = ET.Element("DNS-SERVERS")
            for item in self.dns_servers:
                serialized = SerializationHelper.serialize_item(item, "Ip6AddressString")
                if serialized is not None:
                    child_elem = ET.Element("DNS-SERVER")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize enable_anycast
        if self.enable_anycast is not None:
            serialized = SerializationHelper.serialize_item(self.enable_anycast, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ENABLE-ANYCAST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize hop_count
        if self.hop_count is not None:
            serialized = SerializationHelper.serialize_item(self.hop_count, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HOP-COUNT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ip_address_keep_enum
        if self.ip_address_keep_enum is not None:
            serialized = SerializationHelper.serialize_item(self.ip_address_keep_enum, "IpAddressKeepEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IP-ADDRESS-KEEP-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ip_address_prefix
        if self.ip_address_prefix is not None:
            serialized = SerializationHelper.serialize_item(self.ip_address_prefix, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IP-ADDRESS-PREFIX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ipv6_address
        if self.ipv6_address is not None:
            serialized = SerializationHelper.serialize_item(self.ipv6_address, "Ip6AddressString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IPV6-ADDRESS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ipv6_address_source
        if self.ipv6_address_source is not None:
            serialized = SerializationHelper.serialize_item(self.ipv6_address_source, "Ipv6AddressSourceEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IPV6-ADDRESS-SOURCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Ipv6Configuration":
        """Deserialize XML element to Ipv6Configuration object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Ipv6Configuration object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Ipv6Configuration, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ASSIGNMENT":
                setattr(obj, "assignment", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "DEFAULT-ROUTER":
                setattr(obj, "default_router", SerializationHelper.deserialize_by_tag(child, "Ip6AddressString"))
            elif tag == "DNS-SERVERS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.dns_servers.append(SerializationHelper.deserialize_by_tag(item_elem, "Ip6AddressString"))
            elif tag == "ENABLE-ANYCAST":
                setattr(obj, "enable_anycast", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "HOP-COUNT":
                setattr(obj, "hop_count", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "IP-ADDRESS-KEEP-ENUM":
                setattr(obj, "ip_address_keep_enum", IpAddressKeepEnum.deserialize(child))
            elif tag == "IP-ADDRESS-PREFIX":
                setattr(obj, "ip_address_prefix", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "IPV6-ADDRESS":
                setattr(obj, "ipv6_address", SerializationHelper.deserialize_by_tag(child, "Ip6AddressString"))
            elif tag == "IPV6-ADDRESS-SOURCE":
                setattr(obj, "ipv6_address_source", Ipv6AddressSourceEnum.deserialize(child))

        return obj



class Ipv6ConfigurationBuilder(NetworkEndpointAddressBuilder):
    """Builder for Ipv6Configuration with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: Ipv6Configuration = Ipv6Configuration()


    def with_assignment(self, value: Optional[PositiveInteger]) -> "Ipv6ConfigurationBuilder":
        """Set assignment attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.assignment = value
        return self

    def with_default_router(self, value: Optional[Ip6AddressString]) -> "Ipv6ConfigurationBuilder":
        """Set default_router attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.default_router = value
        return self

    def with_dns_servers(self, items: list[Ip6AddressString]) -> "Ipv6ConfigurationBuilder":
        """Set dns_servers list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.dns_servers = list(items) if items else []
        return self

    def with_enable_anycast(self, value: Optional[Boolean]) -> "Ipv6ConfigurationBuilder":
        """Set enable_anycast attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.enable_anycast = value
        return self

    def with_hop_count(self, value: Optional[PositiveInteger]) -> "Ipv6ConfigurationBuilder":
        """Set hop_count attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.hop_count = value
        return self

    def with_ip_address_keep_enum(self, value: Optional[IpAddressKeepEnum]) -> "Ipv6ConfigurationBuilder":
        """Set ip_address_keep_enum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ip_address_keep_enum = value
        return self

    def with_ip_address_prefix(self, value: Optional[PositiveInteger]) -> "Ipv6ConfigurationBuilder":
        """Set ip_address_prefix attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ip_address_prefix = value
        return self

    def with_ipv6_address(self, value: Optional[Ip6AddressString]) -> "Ipv6ConfigurationBuilder":
        """Set ipv6_address attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ipv6_address = value
        return self

    def with_ipv6_address_source(self, value: Optional[Ipv6AddressSourceEnum]) -> "Ipv6ConfigurationBuilder":
        """Set ipv6_address_source attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ipv6_address_source = value
        return self


    def add_dns_server(self, item: Ip6AddressString) -> "Ipv6ConfigurationBuilder":
        """Add a single item to dns_servers list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.dns_servers.append(item)
        return self

    def clear_dns_servers(self) -> "Ipv6ConfigurationBuilder":
        """Clear all items from dns_servers list.

        Returns:
            self for method chaining
        """
        self._obj.dns_servers = []
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


    def build(self) -> Ipv6Configuration:
        """Build and return the Ipv6Configuration instance with validation."""
        self._validate_instance()
        pass
        return self._obj