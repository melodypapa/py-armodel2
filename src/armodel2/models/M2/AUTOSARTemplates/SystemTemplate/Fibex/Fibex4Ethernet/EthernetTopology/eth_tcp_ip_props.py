"""EthTcpIpProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 153)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.tcp_props import (
    TcpProps,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.udp_props import (
    UdpProps,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EthTcpIpProps(ARElement):
    """AUTOSAR EthTcpIpProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ETH-TCP-IP-PROPS"


    tcp_props: Optional[TcpProps]
    udp_props: Optional[UdpProps]
    _DESERIALIZE_DISPATCH = {
        "TCP-PROPS": lambda obj, elem: setattr(obj, "tcp_props", SerializationHelper.deserialize_by_tag(elem, "TcpProps")),
        "UDP-PROPS": lambda obj, elem: setattr(obj, "udp_props", SerializationHelper.deserialize_by_tag(elem, "UdpProps")),
    }


    def __init__(self) -> None:
        """Initialize EthTcpIpProps."""
        super().__init__()
        self.tcp_props: Optional[TcpProps] = None
        self.udp_props: Optional[UdpProps] = None

    def serialize(self) -> ET.Element:
        """Serialize EthTcpIpProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EthTcpIpProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize tcp_props
        if self.tcp_props is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_props, "TcpProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-PROPS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize udp_props
        if self.udp_props is not None:
            serialized = SerializationHelper.serialize_item(self.udp_props, "UdpProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UDP-PROPS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthTcpIpProps":
        """Deserialize XML element to EthTcpIpProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EthTcpIpProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EthTcpIpProps, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "TCP-PROPS":
                setattr(obj, "tcp_props", SerializationHelper.deserialize_by_tag(child, "TcpProps"))
            elif tag == "UDP-PROPS":
                setattr(obj, "udp_props", SerializationHelper.deserialize_by_tag(child, "UdpProps"))

        return obj



class EthTcpIpPropsBuilder(ARElementBuilder):
    """Builder for EthTcpIpProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EthTcpIpProps = EthTcpIpProps()


    def with_tcp_props(self, value: Optional[TcpProps]) -> "EthTcpIpPropsBuilder":
        """Set tcp_props attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'tcp_props' is required and cannot be None")
        self._obj.tcp_props = value
        return self

    def with_udp_props(self, value: Optional[UdpProps]) -> "EthTcpIpPropsBuilder":
        """Set udp_props attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'udp_props' is required and cannot be None")
        self._obj.udp_props = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "tcpProps",
        "udpProps",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> EthTcpIpProps:
        """Build and return the EthTcpIpProps instance with validation."""
        self._validate_instance()
        return self._obj