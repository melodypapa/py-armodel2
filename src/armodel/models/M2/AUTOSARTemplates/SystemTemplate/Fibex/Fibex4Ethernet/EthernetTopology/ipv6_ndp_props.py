"""Ipv6NdpProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 150)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    TimeValue,
)


class Ipv6NdpProps(ARObject):
    """AUTOSAR Ipv6NdpProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    tcp_ip_ndp_default: Optional[TimeValue]
    tcp_ip_ndp_default_router_list_size: Optional[PositiveInteger]
    tcp_ip_ndp: Optional[Boolean]
    tcp_ip_ndp_delay_first_probe_time_value: Optional[TimeValue]
    tcp_ip_ndp_max_random_factor: Optional[PositiveInteger]
    tcp_ip_ndp_max_rtr: Optional[PositiveInteger]
    tcp_ip_ndp_min_random_factor: Optional[PositiveInteger]
    tcp_ip_ndp_num: Optional[PositiveInteger]
    tcp_ip_ndp_packet: Optional[Boolean]
    tcp_ip_ndp_prefix: Optional[PositiveInteger]
    tcp_ip_ndp_rnd_rtr: Optional[Boolean]
    tcp_ip_ndp_rtr: Optional[TimeValue]
    tcp_ip_ndp_slaac: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize Ipv6NdpProps."""
        super().__init__()
        self.tcp_ip_ndp_default: Optional[TimeValue] = None
        self.tcp_ip_ndp_default_router_list_size: Optional[PositiveInteger] = None
        self.tcp_ip_ndp: Optional[Boolean] = None
        self.tcp_ip_ndp_delay_first_probe_time_value: Optional[TimeValue] = None
        self.tcp_ip_ndp_max_random_factor: Optional[PositiveInteger] = None
        self.tcp_ip_ndp_max_rtr: Optional[PositiveInteger] = None
        self.tcp_ip_ndp_min_random_factor: Optional[PositiveInteger] = None
        self.tcp_ip_ndp_num: Optional[PositiveInteger] = None
        self.tcp_ip_ndp_packet: Optional[Boolean] = None
        self.tcp_ip_ndp_prefix: Optional[PositiveInteger] = None
        self.tcp_ip_ndp_rnd_rtr: Optional[Boolean] = None
        self.tcp_ip_ndp_rtr: Optional[TimeValue] = None
        self.tcp_ip_ndp_slaac: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize Ipv6NdpProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Ipv6NdpProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize tcp_ip_ndp_default
        if self.tcp_ip_ndp_default is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_ip_ndp_default, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-IP-NDP-DEFAULT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_ip_ndp_default_router_list_size
        if self.tcp_ip_ndp_default_router_list_size is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_ip_ndp_default_router_list_size, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-IP-NDP-DEFAULT-ROUTER-LIST-SIZE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_ip_ndp
        if self.tcp_ip_ndp is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_ip_ndp, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-IP-NDP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_ip_ndp_delay_first_probe_time_value
        if self.tcp_ip_ndp_delay_first_probe_time_value is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_ip_ndp_delay_first_probe_time_value, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-IP-NDP-DELAY-FIRST-PROBE-TIME-VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_ip_ndp_max_random_factor
        if self.tcp_ip_ndp_max_random_factor is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_ip_ndp_max_random_factor, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-IP-NDP-MAX-RANDOM-FACTOR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_ip_ndp_max_rtr
        if self.tcp_ip_ndp_max_rtr is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_ip_ndp_max_rtr, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-IP-NDP-MAX-RTR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_ip_ndp_min_random_factor
        if self.tcp_ip_ndp_min_random_factor is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_ip_ndp_min_random_factor, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-IP-NDP-MIN-RANDOM-FACTOR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_ip_ndp_num
        if self.tcp_ip_ndp_num is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_ip_ndp_num, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-IP-NDP-NUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_ip_ndp_packet
        if self.tcp_ip_ndp_packet is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_ip_ndp_packet, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-IP-NDP-PACKET")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_ip_ndp_prefix
        if self.tcp_ip_ndp_prefix is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_ip_ndp_prefix, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-IP-NDP-PREFIX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_ip_ndp_rnd_rtr
        if self.tcp_ip_ndp_rnd_rtr is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_ip_ndp_rnd_rtr, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-IP-NDP-RND-RTR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_ip_ndp_rtr
        if self.tcp_ip_ndp_rtr is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_ip_ndp_rtr, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-IP-NDP-RTR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_ip_ndp_slaac
        if self.tcp_ip_ndp_slaac is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_ip_ndp_slaac, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-IP-NDP-SLAAC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Ipv6NdpProps":
        """Deserialize XML element to Ipv6NdpProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Ipv6NdpProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Ipv6NdpProps, cls).deserialize(element)

        # Parse tcp_ip_ndp_default
        child = SerializationHelper.find_child_element(element, "TCP-IP-NDP-DEFAULT")
        if child is not None:
            tcp_ip_ndp_default_value = child.text
            obj.tcp_ip_ndp_default = tcp_ip_ndp_default_value

        # Parse tcp_ip_ndp_default_router_list_size
        child = SerializationHelper.find_child_element(element, "TCP-IP-NDP-DEFAULT-ROUTER-LIST-SIZE")
        if child is not None:
            tcp_ip_ndp_default_router_list_size_value = child.text
            obj.tcp_ip_ndp_default_router_list_size = tcp_ip_ndp_default_router_list_size_value

        # Parse tcp_ip_ndp
        child = SerializationHelper.find_child_element(element, "TCP-IP-NDP")
        if child is not None:
            tcp_ip_ndp_value = child.text
            obj.tcp_ip_ndp = tcp_ip_ndp_value

        # Parse tcp_ip_ndp_delay_first_probe_time_value
        child = SerializationHelper.find_child_element(element, "TCP-IP-NDP-DELAY-FIRST-PROBE-TIME-VALUE")
        if child is not None:
            tcp_ip_ndp_delay_first_probe_time_value_value = child.text
            obj.tcp_ip_ndp_delay_first_probe_time_value = tcp_ip_ndp_delay_first_probe_time_value_value

        # Parse tcp_ip_ndp_max_random_factor
        child = SerializationHelper.find_child_element(element, "TCP-IP-NDP-MAX-RANDOM-FACTOR")
        if child is not None:
            tcp_ip_ndp_max_random_factor_value = child.text
            obj.tcp_ip_ndp_max_random_factor = tcp_ip_ndp_max_random_factor_value

        # Parse tcp_ip_ndp_max_rtr
        child = SerializationHelper.find_child_element(element, "TCP-IP-NDP-MAX-RTR")
        if child is not None:
            tcp_ip_ndp_max_rtr_value = child.text
            obj.tcp_ip_ndp_max_rtr = tcp_ip_ndp_max_rtr_value

        # Parse tcp_ip_ndp_min_random_factor
        child = SerializationHelper.find_child_element(element, "TCP-IP-NDP-MIN-RANDOM-FACTOR")
        if child is not None:
            tcp_ip_ndp_min_random_factor_value = child.text
            obj.tcp_ip_ndp_min_random_factor = tcp_ip_ndp_min_random_factor_value

        # Parse tcp_ip_ndp_num
        child = SerializationHelper.find_child_element(element, "TCP-IP-NDP-NUM")
        if child is not None:
            tcp_ip_ndp_num_value = child.text
            obj.tcp_ip_ndp_num = tcp_ip_ndp_num_value

        # Parse tcp_ip_ndp_packet
        child = SerializationHelper.find_child_element(element, "TCP-IP-NDP-PACKET")
        if child is not None:
            tcp_ip_ndp_packet_value = child.text
            obj.tcp_ip_ndp_packet = tcp_ip_ndp_packet_value

        # Parse tcp_ip_ndp_prefix
        child = SerializationHelper.find_child_element(element, "TCP-IP-NDP-PREFIX")
        if child is not None:
            tcp_ip_ndp_prefix_value = child.text
            obj.tcp_ip_ndp_prefix = tcp_ip_ndp_prefix_value

        # Parse tcp_ip_ndp_rnd_rtr
        child = SerializationHelper.find_child_element(element, "TCP-IP-NDP-RND-RTR")
        if child is not None:
            tcp_ip_ndp_rnd_rtr_value = child.text
            obj.tcp_ip_ndp_rnd_rtr = tcp_ip_ndp_rnd_rtr_value

        # Parse tcp_ip_ndp_rtr
        child = SerializationHelper.find_child_element(element, "TCP-IP-NDP-RTR")
        if child is not None:
            tcp_ip_ndp_rtr_value = child.text
            obj.tcp_ip_ndp_rtr = tcp_ip_ndp_rtr_value

        # Parse tcp_ip_ndp_slaac
        child = SerializationHelper.find_child_element(element, "TCP-IP-NDP-SLAAC")
        if child is not None:
            tcp_ip_ndp_slaac_value = child.text
            obj.tcp_ip_ndp_slaac = tcp_ip_ndp_slaac_value

        return obj



class Ipv6NdpPropsBuilder:
    """Builder for Ipv6NdpProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: Ipv6NdpProps = Ipv6NdpProps()


    def with_tcp_ip_ndp_default(self, value: Optional[TimeValue]) -> "Ipv6NdpPropsBuilder":
        """Set tcp_ip_ndp_default attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tcp_ip_ndp_default = value
        return self

    def with_tcp_ip_ndp_default_router_list_size(self, value: Optional[PositiveInteger]) -> "Ipv6NdpPropsBuilder":
        """Set tcp_ip_ndp_default_router_list_size attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tcp_ip_ndp_default_router_list_size = value
        return self

    def with_tcp_ip_ndp(self, value: Optional[Boolean]) -> "Ipv6NdpPropsBuilder":
        """Set tcp_ip_ndp attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tcp_ip_ndp = value
        return self

    def with_tcp_ip_ndp_delay_first_probe_time_value(self, value: Optional[TimeValue]) -> "Ipv6NdpPropsBuilder":
        """Set tcp_ip_ndp_delay_first_probe_time_value attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tcp_ip_ndp_delay_first_probe_time_value = value
        return self

    def with_tcp_ip_ndp_max_random_factor(self, value: Optional[PositiveInteger]) -> "Ipv6NdpPropsBuilder":
        """Set tcp_ip_ndp_max_random_factor attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tcp_ip_ndp_max_random_factor = value
        return self

    def with_tcp_ip_ndp_max_rtr(self, value: Optional[PositiveInteger]) -> "Ipv6NdpPropsBuilder":
        """Set tcp_ip_ndp_max_rtr attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tcp_ip_ndp_max_rtr = value
        return self

    def with_tcp_ip_ndp_min_random_factor(self, value: Optional[PositiveInteger]) -> "Ipv6NdpPropsBuilder":
        """Set tcp_ip_ndp_min_random_factor attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tcp_ip_ndp_min_random_factor = value
        return self

    def with_tcp_ip_ndp_num(self, value: Optional[PositiveInteger]) -> "Ipv6NdpPropsBuilder":
        """Set tcp_ip_ndp_num attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tcp_ip_ndp_num = value
        return self

    def with_tcp_ip_ndp_packet(self, value: Optional[Boolean]) -> "Ipv6NdpPropsBuilder":
        """Set tcp_ip_ndp_packet attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tcp_ip_ndp_packet = value
        return self

    def with_tcp_ip_ndp_prefix(self, value: Optional[PositiveInteger]) -> "Ipv6NdpPropsBuilder":
        """Set tcp_ip_ndp_prefix attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tcp_ip_ndp_prefix = value
        return self

    def with_tcp_ip_ndp_rnd_rtr(self, value: Optional[Boolean]) -> "Ipv6NdpPropsBuilder":
        """Set tcp_ip_ndp_rnd_rtr attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tcp_ip_ndp_rnd_rtr = value
        return self

    def with_tcp_ip_ndp_rtr(self, value: Optional[TimeValue]) -> "Ipv6NdpPropsBuilder":
        """Set tcp_ip_ndp_rtr attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tcp_ip_ndp_rtr = value
        return self

    def with_tcp_ip_ndp_slaac(self, value: Optional[Boolean]) -> "Ipv6NdpPropsBuilder":
        """Set tcp_ip_ndp_slaac attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tcp_ip_ndp_slaac = value
        return self



    @staticmethod
    def _coerce_to_int(value: Any) -> int:
        """Coerce value to int.

        Args:
            value: Value to coerce

        Returns:
            Integer value

        Raises:
            ValueError: If value cannot be coerced to int
        """
        if isinstance(value, int):
            return value
        if isinstance(value, str) and value.isdigit():
            return int(value)
        if isinstance(value, float):
            return int(value)
        if isinstance(value, bool):
            return int(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to int: {value}")

    @staticmethod
    def _coerce_to_float(value: Any) -> float:
        """Coerce value to float.

        Args:
            value: Value to coerce

        Returns:
            Float value

        Raises:
            ValueError: If value cannot be coerced to float
        """
        if isinstance(value, float):
            return value
        if isinstance(value, int):
            return float(value)
        if isinstance(value, str):
            try:
                return float(value)
            except ValueError:
                pass
        raise ValueError(f"Cannot coerce {type(value).__name__} to float: {value}")

    @staticmethod
    def _coerce_to_bool(value: Any) -> bool:
        """Coerce value to bool.

        Args:
            value: Value to coerce

        Returns:
            Boolean value

        Raises:
            ValueError: If value cannot be coerced to bool
        """
        if isinstance(value, bool):
            return value
        if isinstance(value, int):
            return bool(value)
        if isinstance(value, str):
            if value.lower() in ("true", "1", "yes"):
                return True
            if value.lower() in ("false", "0", "no"):
                return False
        raise ValueError(f"Cannot coerce {type(value).__name__} to bool: {value}")

    @staticmethod
    def _coerce_to_str(value: Any) -> str:
        """Coerce value to str.

        Args:
            value: Value to coerce

        Returns:
            String value
        """
        return str(value)


    @staticmethod
    def _coerce_to_list(value: Any, item_type: str) -> list:
        """Coerce value to list.

        Args:
            value: Value to coerce
            item_type: Expected item type (for error messages)

        Returns:
            List value

        Raises:
            ValueError: If value cannot be coerced to list
        """
        if isinstance(value, list):
            return value
        if isinstance(value, tuple):
            return list(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to list[{item_type}]: {value}")


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


    def build(self) -> Ipv6NdpProps:
        """Build and return the Ipv6NdpProps instance with validation."""
        self._validate_instance()
        pass
        return self._obj