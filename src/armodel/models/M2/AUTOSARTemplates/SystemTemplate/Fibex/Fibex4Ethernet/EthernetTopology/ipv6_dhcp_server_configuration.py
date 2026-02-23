"""Ipv6DhcpServerConfiguration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 132)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.describable import (
    Describable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.describable import DescribableBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Ip6AddressString,
    TimeValue,
)


class Ipv6DhcpServerConfiguration(Describable):
    """AUTOSAR Ipv6DhcpServerConfiguration."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    address_range: Optional[Ip6AddressString]
    default_gateway: Optional[Ip6AddressString]
    default_lease: Optional[TimeValue]
    dns_servers: list[Ip6AddressString]
    network_mask: Optional[Ip6AddressString]
    def __init__(self) -> None:
        """Initialize Ipv6DhcpServerConfiguration."""
        super().__init__()
        self.address_range: Optional[Ip6AddressString] = None
        self.default_gateway: Optional[Ip6AddressString] = None
        self.default_lease: Optional[TimeValue] = None
        self.dns_servers: list[Ip6AddressString] = []
        self.network_mask: Optional[Ip6AddressString] = None

    def serialize(self) -> ET.Element:
        """Serialize Ipv6DhcpServerConfiguration to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Ipv6DhcpServerConfiguration, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize address_range
        if self.address_range is not None:
            serialized = SerializationHelper.serialize_item(self.address_range, "Ip6AddressString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ADDRESS-RANGE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize default_gateway
        if self.default_gateway is not None:
            serialized = SerializationHelper.serialize_item(self.default_gateway, "Ip6AddressString")
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

        # Serialize default_lease
        if self.default_lease is not None:
            serialized = SerializationHelper.serialize_item(self.default_lease, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEFAULT-LEASE")
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

        # Serialize network_mask
        if self.network_mask is not None:
            serialized = SerializationHelper.serialize_item(self.network_mask, "Ip6AddressString")
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

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Ipv6DhcpServerConfiguration":
        """Deserialize XML element to Ipv6DhcpServerConfiguration object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Ipv6DhcpServerConfiguration object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Ipv6DhcpServerConfiguration, cls).deserialize(element)

        # Parse address_range
        child = SerializationHelper.find_child_element(element, "ADDRESS-RANGE")
        if child is not None:
            address_range_value = child.text
            obj.address_range = address_range_value

        # Parse default_gateway
        child = SerializationHelper.find_child_element(element, "DEFAULT-GATEWAY")
        if child is not None:
            default_gateway_value = child.text
            obj.default_gateway = default_gateway_value

        # Parse default_lease
        child = SerializationHelper.find_child_element(element, "DEFAULT-LEASE")
        if child is not None:
            default_lease_value = child.text
            obj.default_lease = default_lease_value

        # Parse dns_servers (list from container "DNS-SERVERS")
        obj.dns_servers = []
        container = SerializationHelper.find_child_element(element, "DNS-SERVERS")
        if container is not None:
            for child in container:
                # Extract primitive value (Ip6AddressString) as text
                child_value = child.text
                if child_value is not None:
                    obj.dns_servers.append(child_value)

        # Parse network_mask
        child = SerializationHelper.find_child_element(element, "NETWORK-MASK")
        if child is not None:
            network_mask_value = child.text
            obj.network_mask = network_mask_value

        return obj



class Ipv6DhcpServerConfigurationBuilder(DescribableBuilder):
    """Builder for Ipv6DhcpServerConfiguration with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: Ipv6DhcpServerConfiguration = Ipv6DhcpServerConfiguration()


    def with_address_range(self, value: Optional[Ip6AddressString]) -> "Ipv6DhcpServerConfigurationBuilder":
        """Set address_range attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.address_range = value
        return self

    def with_default_gateway(self, value: Optional[Ip6AddressString]) -> "Ipv6DhcpServerConfigurationBuilder":
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

    def with_default_lease(self, value: Optional[TimeValue]) -> "Ipv6DhcpServerConfigurationBuilder":
        """Set default_lease attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.default_lease = value
        return self

    def with_dns_servers(self, items: list[Ip6AddressString]) -> "Ipv6DhcpServerConfigurationBuilder":
        """Set dns_servers list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.dns_servers = list(items) if items else []
        return self

    def with_network_mask(self, value: Optional[Ip6AddressString]) -> "Ipv6DhcpServerConfigurationBuilder":
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


    def add_dns_server(self, item: Ip6AddressString) -> "Ipv6DhcpServerConfigurationBuilder":
        """Add a single item to dns_servers list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.dns_servers.append(item)
        return self

    def clear_dns_servers(self) -> "Ipv6DhcpServerConfigurationBuilder":
        """Clear all items from dns_servers list.

        Returns:
            self for method chaining
        """
        self._obj.dns_servers = []
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


    def build(self) -> Ipv6DhcpServerConfiguration:
        """Build and return the Ipv6DhcpServerConfiguration instance with validation."""
        self._validate_instance()
        pass
        return self._obj