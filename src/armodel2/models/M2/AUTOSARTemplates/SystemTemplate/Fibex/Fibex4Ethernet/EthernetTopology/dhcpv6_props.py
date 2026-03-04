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

    _XML_TAG = "DHCPV6-PROPS"


    tcp_ip_dhcp: Optional[TimeValue]
    tcp_ip_dhcp_v6_inf: Optional[TimeValue]
    tcp_ip_dhcp_v6_sol: Optional[TimeValue]
    _DESERIALIZE_DISPATCH = {
        "TCP-IP-DHCP": lambda obj, elem: setattr(obj, "tcp_ip_dhcp", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "TCP-IP-DHCP-V6-INF": lambda obj, elem: setattr(obj, "tcp_ip_dhcp_v6_inf", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "TCP-IP-DHCP-V6-SOL": lambda obj, elem: setattr(obj, "tcp_ip_dhcp_v6_sol", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
    }


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
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "TCP-IP-DHCP":
                setattr(obj, "tcp_ip_dhcp", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "TCP-IP-DHCP-V6-INF":
                setattr(obj, "tcp_ip_dhcp_v6_inf", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "TCP-IP-DHCP-V6-SOL":
                setattr(obj, "tcp_ip_dhcp_v6_sol", SerializationHelper.deserialize_by_tag(child, "TimeValue"))

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



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "tcpIpDhcp",
        "tcpIpDhcpV6Inf",
        "tcpIpDhcpV6Sol",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> Dhcpv6Props:
        """Build and return the Dhcpv6Props instance with validation."""
        self._validate_instance()
        return self._obj