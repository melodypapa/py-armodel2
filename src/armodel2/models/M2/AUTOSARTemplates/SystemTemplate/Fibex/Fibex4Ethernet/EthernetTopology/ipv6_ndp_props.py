"""Ipv6NdpProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 150)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class Ipv6NdpProps(ARObject):
    """AUTOSAR Ipv6NdpProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "IPV6-NDP-PROPS"


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
    _DESERIALIZE_DISPATCH = {
        "TCP-IP-NDP-DEFAULT": lambda obj, elem: setattr(obj, "tcp_ip_ndp_default", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "TCP-IP-NDP-DEFAULT-ROUTER-LIST-SIZE": lambda obj, elem: setattr(obj, "tcp_ip_ndp_default_router_list_size", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "TCP-IP-NDP": lambda obj, elem: setattr(obj, "tcp_ip_ndp", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "TCP-IP-NDP-DELAY-FIRST-PROBE-TIME-VALUE": lambda obj, elem: setattr(obj, "tcp_ip_ndp_delay_first_probe_time_value", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "TCP-IP-NDP-MAX-RANDOM-FACTOR": lambda obj, elem: setattr(obj, "tcp_ip_ndp_max_random_factor", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "TCP-IP-NDP-MAX-RTR": lambda obj, elem: setattr(obj, "tcp_ip_ndp_max_rtr", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "TCP-IP-NDP-MIN-RANDOM-FACTOR": lambda obj, elem: setattr(obj, "tcp_ip_ndp_min_random_factor", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "TCP-IP-NDP-NUM": lambda obj, elem: setattr(obj, "tcp_ip_ndp_num", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "TCP-IP-NDP-PACKET": lambda obj, elem: setattr(obj, "tcp_ip_ndp_packet", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "TCP-IP-NDP-PREFIX": lambda obj, elem: setattr(obj, "tcp_ip_ndp_prefix", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "TCP-IP-NDP-RND-RTR": lambda obj, elem: setattr(obj, "tcp_ip_ndp_rnd_rtr", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "TCP-IP-NDP-RTR": lambda obj, elem: setattr(obj, "tcp_ip_ndp_rtr", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "TCP-IP-NDP-SLAAC": lambda obj, elem: setattr(obj, "tcp_ip_ndp_slaac", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
    }


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
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "TCP-IP-NDP-DEFAULT":
                setattr(obj, "tcp_ip_ndp_default", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "TCP-IP-NDP-DEFAULT-ROUTER-LIST-SIZE":
                setattr(obj, "tcp_ip_ndp_default_router_list_size", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "TCP-IP-NDP":
                setattr(obj, "tcp_ip_ndp", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "TCP-IP-NDP-DELAY-FIRST-PROBE-TIME-VALUE":
                setattr(obj, "tcp_ip_ndp_delay_first_probe_time_value", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "TCP-IP-NDP-MAX-RANDOM-FACTOR":
                setattr(obj, "tcp_ip_ndp_max_random_factor", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "TCP-IP-NDP-MAX-RTR":
                setattr(obj, "tcp_ip_ndp_max_rtr", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "TCP-IP-NDP-MIN-RANDOM-FACTOR":
                setattr(obj, "tcp_ip_ndp_min_random_factor", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "TCP-IP-NDP-NUM":
                setattr(obj, "tcp_ip_ndp_num", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "TCP-IP-NDP-PACKET":
                setattr(obj, "tcp_ip_ndp_packet", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "TCP-IP-NDP-PREFIX":
                setattr(obj, "tcp_ip_ndp_prefix", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "TCP-IP-NDP-RND-RTR":
                setattr(obj, "tcp_ip_ndp_rnd_rtr", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "TCP-IP-NDP-RTR":
                setattr(obj, "tcp_ip_ndp_rtr", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "TCP-IP-NDP-SLAAC":
                setattr(obj, "tcp_ip_ndp_slaac", SerializationHelper.deserialize_by_tag(child, "Boolean"))

        return obj



class Ipv6NdpPropsBuilder(BuilderBase):
    """Builder for Ipv6NdpProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: Ipv6NdpProps = Ipv6NdpProps()


    def with_tcp_ip_ndp_default(self, value: Optional[TimeValue]) -> "Ipv6NdpPropsBuilder":
        """Set tcp_ip_ndp_default attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'tcp_ip_ndp_default' is required and cannot be None")
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
            raise ValueError("Attribute 'tcp_ip_ndp_default_router_list_size' is required and cannot be None")
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
            raise ValueError("Attribute 'tcp_ip_ndp' is required and cannot be None")
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
            raise ValueError("Attribute 'tcp_ip_ndp_delay_first_probe_time_value' is required and cannot be None")
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
            raise ValueError("Attribute 'tcp_ip_ndp_max_random_factor' is required and cannot be None")
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
            raise ValueError("Attribute 'tcp_ip_ndp_max_rtr' is required and cannot be None")
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
            raise ValueError("Attribute 'tcp_ip_ndp_min_random_factor' is required and cannot be None")
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
            raise ValueError("Attribute 'tcp_ip_ndp_num' is required and cannot be None")
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
            raise ValueError("Attribute 'tcp_ip_ndp_packet' is required and cannot be None")
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
            raise ValueError("Attribute 'tcp_ip_ndp_prefix' is required and cannot be None")
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
            raise ValueError("Attribute 'tcp_ip_ndp_rnd_rtr' is required and cannot be None")
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
            raise ValueError("Attribute 'tcp_ip_ndp_rtr' is required and cannot be None")
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
            raise ValueError("Attribute 'tcp_ip_ndp_slaac' is required and cannot be None")
        self._obj.tcp_ip_ndp_slaac = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "tcpIpNdp",
        "tcpIpNdpDefault",
        "tcpIpNdpDefaultRouterListSize",
        "tcpIpNdpDelayFirstProbeTimeValue",
        "tcpIpNdpMaxRandomFactor",
        "tcpIpNdpMaxRtr",
        "tcpIpNdpMinRandomFactor",
        "tcpIpNdpNum",
        "tcpIpNdpPacket",
        "tcpIpNdpPrefix",
        "tcpIpNdpRndRtr",
        "tcpIpNdpRtr",
        "tcpIpNdpSlaac",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> Ipv6NdpProps:
        """Build and return the Ipv6NdpProps instance with validation."""
        self._validate_instance()
        return self._obj