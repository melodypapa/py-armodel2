"""Ipv4Configuration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 465)

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
    Ipv4AddressSourceEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Ip4AddressString,
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class Ipv4Configuration(NetworkEndpointAddress):
    """AUTOSAR Ipv4Configuration."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "IPV4-CONFIGURATION"


    assignment: Optional[PositiveInteger]
    default_gateway: Optional[Ip4AddressString]
    dns_servers: list[Ip4AddressString]
    ip_address_keep_enum: Optional[IpAddressKeepEnum]
    ipv4_address: Optional[Ip4AddressString]
    ipv4_address_source: Optional[Ipv4AddressSourceEnum]
    network_mask: Optional[Ip4AddressString]
    ttl: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "ASSIGNMENT": lambda obj, elem: setattr(obj, "assignment", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "DEFAULT-GATEWAY": lambda obj, elem: setattr(obj, "default_gateway", SerializationHelper.deserialize_by_tag(elem, "Ip4AddressString")),
        "DNS-SERVERS": lambda obj, elem: obj.dns_servers.append(SerializationHelper.deserialize_by_tag(elem, "Ip4AddressString")),
        "IP-ADDRESS-KEEP-ENUM": lambda obj, elem: setattr(obj, "ip_address_keep_enum", IpAddressKeepEnum.deserialize(elem)),
        "IPV4-ADDRESS": lambda obj, elem: setattr(obj, "ipv4_address", SerializationHelper.deserialize_by_tag(elem, "Ip4AddressString")),
        "IPV4-ADDRESS-SOURCE": lambda obj, elem: setattr(obj, "ipv4_address_source", Ipv4AddressSourceEnum.deserialize(elem)),
        "NETWORK-MASK": lambda obj, elem: setattr(obj, "network_mask", SerializationHelper.deserialize_by_tag(elem, "Ip4AddressString")),
        "TTL": lambda obj, elem: setattr(obj, "ttl", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize Ipv4Configuration."""
        super().__init__()
        self.assignment: Optional[PositiveInteger] = None
        self.default_gateway: Optional[Ip4AddressString] = None
        self.dns_servers: list[Ip4AddressString] = []
        self.ip_address_keep_enum: Optional[IpAddressKeepEnum] = None
        self.ipv4_address: Optional[Ip4AddressString] = None
        self.ipv4_address_source: Optional[Ipv4AddressSourceEnum] = None
        self.network_mask: Optional[Ip4AddressString] = None
        self.ttl: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize Ipv4Configuration to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Ipv4Configuration, self).serialize()

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

        # Serialize default_gateway
        if self.default_gateway is not None:
            serialized = SerializationHelper.serialize_item(self.default_gateway, "Ip4AddressString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEFAULT-GATEWAY")
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
                serialized = SerializationHelper.serialize_item(item, "Ip4AddressString")
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

        # Serialize ipv4_address
        if self.ipv4_address is not None:
            serialized = SerializationHelper.serialize_item(self.ipv4_address, "Ip4AddressString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IPV4-ADDRESS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ipv4_address_source
        if self.ipv4_address_source is not None:
            serialized = SerializationHelper.serialize_item(self.ipv4_address_source, "Ipv4AddressSourceEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IPV4-ADDRESS-SOURCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize network_mask
        if self.network_mask is not None:
            serialized = SerializationHelper.serialize_item(self.network_mask, "Ip4AddressString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NETWORK-MASK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ttl
        if self.ttl is not None:
            serialized = SerializationHelper.serialize_item(self.ttl, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TTL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Ipv4Configuration":
        """Deserialize XML element to Ipv4Configuration object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Ipv4Configuration object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Ipv4Configuration, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ASSIGNMENT":
                setattr(obj, "assignment", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "DEFAULT-GATEWAY":
                setattr(obj, "default_gateway", SerializationHelper.deserialize_by_tag(child, "Ip4AddressString"))
            elif tag == "DNS-SERVERS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.dns_servers.append(SerializationHelper.deserialize_by_tag(item_elem, "Ip4AddressString"))
            elif tag == "IP-ADDRESS-KEEP-ENUM":
                setattr(obj, "ip_address_keep_enum", IpAddressKeepEnum.deserialize(child))
            elif tag == "IPV4-ADDRESS":
                setattr(obj, "ipv4_address", SerializationHelper.deserialize_by_tag(child, "Ip4AddressString"))
            elif tag == "IPV4-ADDRESS-SOURCE":
                setattr(obj, "ipv4_address_source", Ipv4AddressSourceEnum.deserialize(child))
            elif tag == "NETWORK-MASK":
                setattr(obj, "network_mask", SerializationHelper.deserialize_by_tag(child, "Ip4AddressString"))
            elif tag == "TTL":
                setattr(obj, "ttl", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class Ipv4ConfigurationBuilder(NetworkEndpointAddressBuilder):
    """Builder for Ipv4Configuration with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: Ipv4Configuration = Ipv4Configuration()


    def with_assignment(self, value: Optional[PositiveInteger]) -> "Ipv4ConfigurationBuilder":
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

    def with_default_gateway(self, value: Optional[Ip4AddressString]) -> "Ipv4ConfigurationBuilder":
        """Set default_gateway attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.default_gateway = value
        return self

    def with_dns_servers(self, items: list[Ip4AddressString]) -> "Ipv4ConfigurationBuilder":
        """Set dns_servers list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.dns_servers = list(items) if items else []
        return self

    def with_ip_address_keep_enum(self, value: Optional[IpAddressKeepEnum]) -> "Ipv4ConfigurationBuilder":
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

    def with_ipv4_address(self, value: Optional[Ip4AddressString]) -> "Ipv4ConfigurationBuilder":
        """Set ipv4_address attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ipv4_address = value
        return self

    def with_ipv4_address_source(self, value: Optional[Ipv4AddressSourceEnum]) -> "Ipv4ConfigurationBuilder":
        """Set ipv4_address_source attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ipv4_address_source = value
        return self

    def with_network_mask(self, value: Optional[Ip4AddressString]) -> "Ipv4ConfigurationBuilder":
        """Set network_mask attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.network_mask = value
        return self

    def with_ttl(self, value: Optional[PositiveInteger]) -> "Ipv4ConfigurationBuilder":
        """Set ttl attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ttl = value
        return self


    def add_dns_server(self, item: Ip4AddressString) -> "Ipv4ConfigurationBuilder":
        """Add a single item to dns_servers list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.dns_servers.append(item)
        return self

    def clear_dns_servers(self) -> "Ipv4ConfigurationBuilder":
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


    def build(self) -> Ipv4Configuration:
        """Build and return the Ipv4Configuration instance with validation."""
        self._validate_instance()
        pass
        return self._obj