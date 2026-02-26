"""Dhcpv6Props AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 149)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class Dhcpv6Props(ARObject):
    """AUTOSAR Dhcpv6Props."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    tcp_ip_dhcp: Optional[TimeValue]
    tcp_ip_dhcp_v6_inf: Optional[TimeValue]
    tcp_ip_dhcp_v6_sol: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize Dhcpv6Props."""
        super().__init__()
        self.tcp_ip_dhcp: Optional[TimeValue] = None
        self.tcp_ip_dhcp_v6_inf: Optional[TimeValue] = None
        self.tcp_ip_dhcp_v6_sol: Optional[TimeValue] = None

    def serialize(self) -> ET.Element:
        """Serialize Dhcpv6Props to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Dhcpv6Props, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize tcp_ip_dhcp
        if self.tcp_ip_dhcp is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_ip_dhcp, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-IP-DHCP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_ip_dhcp_v6_inf
        if self.tcp_ip_dhcp_v6_inf is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_ip_dhcp_v6_inf, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-IP-DHCP-V6-INF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_ip_dhcp_v6_sol
        if self.tcp_ip_dhcp_v6_sol is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_ip_dhcp_v6_sol, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-IP-DHCP-V6-SOL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Dhcpv6Props":
        """Deserialize XML element to Dhcpv6Props object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Dhcpv6Props object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Dhcpv6Props, cls).deserialize(element)

        # Parse tcp_ip_dhcp
        child = SerializationHelper.find_child_element(element, "TCP-IP-DHCP")
        if child is not None:
            tcp_ip_dhcp_value = child.text
            obj.tcp_ip_dhcp = tcp_ip_dhcp_value

        # Parse tcp_ip_dhcp_v6_inf
        child = SerializationHelper.find_child_element(element, "TCP-IP-DHCP-V6-INF")
        if child is not None:
            tcp_ip_dhcp_v6_inf_value = child.text
            obj.tcp_ip_dhcp_v6_inf = tcp_ip_dhcp_v6_inf_value

        # Parse tcp_ip_dhcp_v6_sol
        child = SerializationHelper.find_child_element(element, "TCP-IP-DHCP-V6-SOL")
        if child is not None:
            tcp_ip_dhcp_v6_sol_value = child.text
            obj.tcp_ip_dhcp_v6_sol = tcp_ip_dhcp_v6_sol_value

        return obj



class Dhcpv6PropsBuilder(BuilderBase):
    """Builder for Dhcpv6Props with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: Dhcpv6Props = Dhcpv6Props()


    def with_tcp_ip_dhcp(self, value: Optional[TimeValue]) -> "Dhcpv6PropsBuilder":
        """Set tcp_ip_dhcp attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tcp_ip_dhcp = value
        return self

    def with_tcp_ip_dhcp_v6_inf(self, value: Optional[TimeValue]) -> "Dhcpv6PropsBuilder":
        """Set tcp_ip_dhcp_v6_inf attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tcp_ip_dhcp_v6_inf = value
        return self

    def with_tcp_ip_dhcp_v6_sol(self, value: Optional[TimeValue]) -> "Dhcpv6PropsBuilder":
        """Set tcp_ip_dhcp_v6_sol attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tcp_ip_dhcp_v6_sol = value
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


    def build(self) -> Dhcpv6Props:
        """Build and return the Dhcpv6Props instance with validation."""
        self._validate_instance()
        pass
        return self._obj