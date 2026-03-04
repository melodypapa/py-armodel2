"""TcpIpIcmpv4Props AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 156)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class TcpIpIcmpv4Props(ARObject):
    """AUTOSAR TcpIpIcmpv4Props."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "TCP-IP-ICMPV4-PROPS"


    tcp_ip_icmp: Optional[Boolean]
    tcp_ip_icmp_v4_ttl: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "TCP-IP-ICMP": lambda obj, elem: setattr(obj, "tcp_ip_icmp", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "TCP-IP-ICMP-V4-TTL": lambda obj, elem: setattr(obj, "tcp_ip_icmp_v4_ttl", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize TcpIpIcmpv4Props."""
        super().__init__()
        self.tcp_ip_icmp: Optional[Boolean] = None
        self.tcp_ip_icmp_v4_ttl: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize TcpIpIcmpv4Props to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TcpIpIcmpv4Props, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize tcp_ip_icmp
        if self.tcp_ip_icmp is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_ip_icmp, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-IP-ICMP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_ip_icmp_v4_ttl
        if self.tcp_ip_icmp_v4_ttl is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_ip_icmp_v4_ttl, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-IP-ICMP-V4-TTL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TcpIpIcmpv4Props":
        """Deserialize XML element to TcpIpIcmpv4Props object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TcpIpIcmpv4Props object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TcpIpIcmpv4Props, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "TCP-IP-ICMP":
                setattr(obj, "tcp_ip_icmp", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "TCP-IP-ICMP-V4-TTL":
                setattr(obj, "tcp_ip_icmp_v4_ttl", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class TcpIpIcmpv4PropsBuilder(BuilderBase):
    """Builder for TcpIpIcmpv4Props with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TcpIpIcmpv4Props = TcpIpIcmpv4Props()


    def with_tcp_ip_icmp(self, value: Optional[Boolean]) -> "TcpIpIcmpv4PropsBuilder":
        """Set tcp_ip_icmp attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tcp_ip_icmp = value
        return self

    def with_tcp_ip_icmp_v4_ttl(self, value: Optional[PositiveInteger]) -> "TcpIpIcmpv4PropsBuilder":
        """Set tcp_ip_icmp_v4_ttl attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tcp_ip_icmp_v4_ttl = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "tcpIpIcmp",
        "tcpIpIcmpV4Ttl",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> TcpIpIcmpv4Props:
        """Build and return the TcpIpIcmpv4Props instance with validation."""
        self._validate_instance()
        return self._obj