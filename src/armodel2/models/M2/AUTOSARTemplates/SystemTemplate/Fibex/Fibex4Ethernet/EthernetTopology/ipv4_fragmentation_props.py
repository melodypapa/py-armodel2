"""Ipv4FragmentationProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 147)

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


class Ipv4FragmentationProps(ARObject):
    """AUTOSAR Ipv4FragmentationProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "IPV4-FRAGMENTATION-PROPS"


    tcp_ip_ip: Optional[Boolean]
    tcp_ip_ip_num: Optional[PositiveInteger]
    tcp_ip_ip_reass: Optional[TimeValue]
    _DESERIALIZE_DISPATCH = {
        "TCP-IP-IP": lambda obj, elem: setattr(obj, "tcp_ip_ip", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "TCP-IP-IP-NUM": lambda obj, elem: setattr(obj, "tcp_ip_ip_num", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "TCP-IP-IP-REASS": lambda obj, elem: setattr(obj, "tcp_ip_ip_reass", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
    }


    def __init__(self) -> None:
        """Initialize Ipv4FragmentationProps."""
        super().__init__()
        self.tcp_ip_ip: Optional[Boolean] = None
        self.tcp_ip_ip_num: Optional[PositiveInteger] = None
        self.tcp_ip_ip_reass: Optional[TimeValue] = None

    def serialize(self) -> ET.Element:
        """Serialize Ipv4FragmentationProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Ipv4FragmentationProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize tcp_ip_ip
        if self.tcp_ip_ip is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_ip_ip, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-IP-IP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_ip_ip_num
        if self.tcp_ip_ip_num is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_ip_ip_num, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-IP-IP-NUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_ip_ip_reass
        if self.tcp_ip_ip_reass is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_ip_ip_reass, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-IP-IP-REASS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Ipv4FragmentationProps":
        """Deserialize XML element to Ipv4FragmentationProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Ipv4FragmentationProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Ipv4FragmentationProps, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "TCP-IP-IP":
                setattr(obj, "tcp_ip_ip", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "TCP-IP-IP-NUM":
                setattr(obj, "tcp_ip_ip_num", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "TCP-IP-IP-REASS":
                setattr(obj, "tcp_ip_ip_reass", SerializationHelper.deserialize_by_tag(child, "TimeValue"))

        return obj



class Ipv4FragmentationPropsBuilder(BuilderBase):
    """Builder for Ipv4FragmentationProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: Ipv4FragmentationProps = Ipv4FragmentationProps()


    def with_tcp_ip_ip(self, value: Optional[Boolean]) -> "Ipv4FragmentationPropsBuilder":
        """Set tcp_ip_ip attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tcp_ip_ip = value
        return self

    def with_tcp_ip_ip_num(self, value: Optional[PositiveInteger]) -> "Ipv4FragmentationPropsBuilder":
        """Set tcp_ip_ip_num attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tcp_ip_ip_num = value
        return self

    def with_tcp_ip_ip_reass(self, value: Optional[TimeValue]) -> "Ipv4FragmentationPropsBuilder":
        """Set tcp_ip_ip_reass attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tcp_ip_ip_reass = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "tcpIpIp",
        "tcpIpIpNum",
        "tcpIpIpReass",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> Ipv4FragmentationProps:
        """Build and return the Ipv4FragmentationProps instance with validation."""
        self._validate_instance()
        return self._obj