"""EthTcpIpIcmpProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 156)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.tcp_ip_icmpv4_props import (
    TcpIpIcmpv4Props,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.tcp_ip_icmpv6_props import (
    TcpIpIcmpv6Props,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EthTcpIpIcmpProps(ARElement):
    """AUTOSAR EthTcpIpIcmpProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ETH-TCP-IP-ICMP-PROPS"


    icmp_v4_props: Optional[TcpIpIcmpv4Props]
    icmp_v6_props: Optional[TcpIpIcmpv6Props]
    _DESERIALIZE_DISPATCH = {
        "ICMP-V4-PROPS": lambda obj, elem: setattr(obj, "icmp_v4_props", SerializationHelper.deserialize_by_tag(elem, "TcpIpIcmpv4Props")),
        "ICMP-V6-PROPS": lambda obj, elem: setattr(obj, "icmp_v6_props", SerializationHelper.deserialize_by_tag(elem, "TcpIpIcmpv6Props")),
    }


    def __init__(self) -> None:
        """Initialize EthTcpIpIcmpProps."""
        super().__init__()
        self.icmp_v4_props: Optional[TcpIpIcmpv4Props] = None
        self.icmp_v6_props: Optional[TcpIpIcmpv6Props] = None

    def serialize(self) -> ET.Element:
        """Serialize EthTcpIpIcmpProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EthTcpIpIcmpProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize icmp_v4_props
        if self.icmp_v4_props is not None:
            serialized = SerializationHelper.serialize_item(self.icmp_v4_props, "TcpIpIcmpv4Props")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ICMP-V4-PROPS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize icmp_v6_props
        if self.icmp_v6_props is not None:
            serialized = SerializationHelper.serialize_item(self.icmp_v6_props, "TcpIpIcmpv6Props")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ICMP-V6-PROPS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthTcpIpIcmpProps":
        """Deserialize XML element to EthTcpIpIcmpProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EthTcpIpIcmpProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EthTcpIpIcmpProps, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ICMP-V4-PROPS":
                setattr(obj, "icmp_v4_props", SerializationHelper.deserialize_by_tag(child, "TcpIpIcmpv4Props"))
            elif tag == "ICMP-V6-PROPS":
                setattr(obj, "icmp_v6_props", SerializationHelper.deserialize_by_tag(child, "TcpIpIcmpv6Props"))

        return obj



class EthTcpIpIcmpPropsBuilder(ARElementBuilder):
    """Builder for EthTcpIpIcmpProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EthTcpIpIcmpProps = EthTcpIpIcmpProps()


    def with_icmp_v4_props(self, value: Optional[TcpIpIcmpv4Props]) -> "EthTcpIpIcmpPropsBuilder":
        """Set icmp_v4_props attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'icmp_v4_props' is required and cannot be None")
        self._obj.icmp_v4_props = value
        return self

    def with_icmp_v6_props(self, value: Optional[TcpIpIcmpv6Props]) -> "EthTcpIpIcmpPropsBuilder":
        """Set icmp_v6_props attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'icmp_v6_props' is required and cannot be None")
        self._obj.icmp_v6_props = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "icmpV4Props",
        "icmpV6Props",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> EthTcpIpIcmpProps:
        """Build and return the EthTcpIpIcmpProps instance with validation."""
        self._validate_instance()
        return self._obj