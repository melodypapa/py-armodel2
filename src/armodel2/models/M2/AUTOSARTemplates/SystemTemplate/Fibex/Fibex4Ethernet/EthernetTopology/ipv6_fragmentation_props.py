"""Ipv6FragmentationProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 148)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class Ipv6FragmentationProps(ARObject):
    """AUTOSAR Ipv6FragmentationProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "IPV6-FRAGMENTATION-PROPS"


    tcp_ip_ip: Optional[TimeValue]
    tcp_ip_ip_reassembly_buffer_size: Optional[PositiveInteger]
    tcp_ip_ip_tx: Optional[PositiveInteger]
    tcp_ip_ip_tx_fragment_buffer_size: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "TCP-IP-IP": lambda obj, elem: setattr(obj, "tcp_ip_ip", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "TCP-IP-IP-REASSEMBLY-BUFFER-SIZE": lambda obj, elem: setattr(obj, "tcp_ip_ip_reassembly_buffer_size", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "TCP-IP-IP-TX": lambda obj, elem: setattr(obj, "tcp_ip_ip_tx", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "TCP-IP-IP-TX-FRAGMENT-BUFFER-SIZE": lambda obj, elem: setattr(obj, "tcp_ip_ip_tx_fragment_buffer_size", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize Ipv6FragmentationProps."""
        super().__init__()
        self.tcp_ip_ip: Optional[TimeValue] = None
        self.tcp_ip_ip_reassembly_buffer_size: Optional[PositiveInteger] = None
        self.tcp_ip_ip_tx: Optional[PositiveInteger] = None
        self.tcp_ip_ip_tx_fragment_buffer_size: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize Ipv6FragmentationProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Ipv6FragmentationProps, self).serialize()

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
            serialized = SerializationHelper.serialize_item(self.tcp_ip_ip, "TimeValue")
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

        # Serialize tcp_ip_ip_reassembly_buffer_size
        if self.tcp_ip_ip_reassembly_buffer_size is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_ip_ip_reassembly_buffer_size, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-IP-IP-REASSEMBLY-BUFFER-SIZE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_ip_ip_tx
        if self.tcp_ip_ip_tx is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_ip_ip_tx, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-IP-IP-TX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_ip_ip_tx_fragment_buffer_size
        if self.tcp_ip_ip_tx_fragment_buffer_size is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_ip_ip_tx_fragment_buffer_size, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-IP-IP-TX-FRAGMENT-BUFFER-SIZE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Ipv6FragmentationProps":
        """Deserialize XML element to Ipv6FragmentationProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Ipv6FragmentationProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Ipv6FragmentationProps, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "TCP-IP-IP":
                setattr(obj, "tcp_ip_ip", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "TCP-IP-IP-REASSEMBLY-BUFFER-SIZE":
                setattr(obj, "tcp_ip_ip_reassembly_buffer_size", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "TCP-IP-IP-TX":
                setattr(obj, "tcp_ip_ip_tx", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "TCP-IP-IP-TX-FRAGMENT-BUFFER-SIZE":
                setattr(obj, "tcp_ip_ip_tx_fragment_buffer_size", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class Ipv6FragmentationPropsBuilder(BuilderBase):
    """Builder for Ipv6FragmentationProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: Ipv6FragmentationProps = Ipv6FragmentationProps()


    def with_tcp_ip_ip(self, value: Optional[TimeValue]) -> "Ipv6FragmentationPropsBuilder":
        """Set tcp_ip_ip attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'tcp_ip_ip' is required and cannot be None")
        self._obj.tcp_ip_ip = value
        return self

    def with_tcp_ip_ip_reassembly_buffer_size(self, value: Optional[PositiveInteger]) -> "Ipv6FragmentationPropsBuilder":
        """Set tcp_ip_ip_reassembly_buffer_size attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'tcp_ip_ip_reassembly_buffer_size' is required and cannot be None")
        self._obj.tcp_ip_ip_reassembly_buffer_size = value
        return self

    def with_tcp_ip_ip_tx(self, value: Optional[PositiveInteger]) -> "Ipv6FragmentationPropsBuilder":
        """Set tcp_ip_ip_tx attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'tcp_ip_ip_tx' is required and cannot be None")
        self._obj.tcp_ip_ip_tx = value
        return self

    def with_tcp_ip_ip_tx_fragment_buffer_size(self, value: Optional[PositiveInteger]) -> "Ipv6FragmentationPropsBuilder":
        """Set tcp_ip_ip_tx_fragment_buffer_size attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'tcp_ip_ip_tx_fragment_buffer_size' is required and cannot be None")
        self._obj.tcp_ip_ip_tx_fragment_buffer_size = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "tcpIpIp",
        "tcpIpIpReassemblyBufferSize",
        "tcpIpIpTx",
        "tcpIpIpTxFragmentBufferSize",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> Ipv6FragmentationProps:
        """Build and return the Ipv6FragmentationProps instance with validation."""
        self._validate_instance()
        return self._obj