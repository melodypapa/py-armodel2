"""DhcpServerConfiguration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 131)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ipv4_dhcp_server_configuration import (
    Ipv4DhcpServerConfiguration,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ipv6_dhcp_server_configuration import (
    Ipv6DhcpServerConfiguration,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DhcpServerConfiguration(ARObject):
    """AUTOSAR DhcpServerConfiguration."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DHCP-SERVER-CONFIGURATION"


    ipv4_dhcp_server: Optional[Ipv4DhcpServerConfiguration]
    ipv6_dhcp_server: Optional[Ipv6DhcpServerConfiguration]
    _DESERIALIZE_DISPATCH = {
        "IPV4-DHCP-SERVER": lambda obj, elem: setattr(obj, "ipv4_dhcp_server", SerializationHelper.deserialize_by_tag(elem, "Ipv4DhcpServerConfiguration")),
        "IPV6-DHCP-SERVER": lambda obj, elem: setattr(obj, "ipv6_dhcp_server", SerializationHelper.deserialize_by_tag(elem, "Ipv6DhcpServerConfiguration")),
    }


    def __init__(self) -> None:
        """Initialize DhcpServerConfiguration."""
        super().__init__()
        self.ipv4_dhcp_server: Optional[Ipv4DhcpServerConfiguration] = None
        self.ipv6_dhcp_server: Optional[Ipv6DhcpServerConfiguration] = None

    def serialize(self) -> ET.Element:
        """Serialize DhcpServerConfiguration to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DhcpServerConfiguration, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ipv4_dhcp_server
        if self.ipv4_dhcp_server is not None:
            serialized = SerializationHelper.serialize_item(self.ipv4_dhcp_server, "Ipv4DhcpServerConfiguration")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IPV4-DHCP-SERVER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ipv6_dhcp_server
        if self.ipv6_dhcp_server is not None:
            serialized = SerializationHelper.serialize_item(self.ipv6_dhcp_server, "Ipv6DhcpServerConfiguration")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IPV6-DHCP-SERVER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DhcpServerConfiguration":
        """Deserialize XML element to DhcpServerConfiguration object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DhcpServerConfiguration object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DhcpServerConfiguration, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "IPV4-DHCP-SERVER":
                setattr(obj, "ipv4_dhcp_server", SerializationHelper.deserialize_by_tag(child, "Ipv4DhcpServerConfiguration"))
            elif tag == "IPV6-DHCP-SERVER":
                setattr(obj, "ipv6_dhcp_server", SerializationHelper.deserialize_by_tag(child, "Ipv6DhcpServerConfiguration"))

        return obj



class DhcpServerConfigurationBuilder(BuilderBase):
    """Builder for DhcpServerConfiguration with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DhcpServerConfiguration = DhcpServerConfiguration()


    def with_ipv4_dhcp_server(self, value: Optional[Ipv4DhcpServerConfiguration]) -> "DhcpServerConfigurationBuilder":
        """Set ipv4_dhcp_server attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ipv4_dhcp_server = value
        return self

    def with_ipv6_dhcp_server(self, value: Optional[Ipv6DhcpServerConfiguration]) -> "DhcpServerConfigurationBuilder":
        """Set ipv6_dhcp_server attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ipv6_dhcp_server = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "ipv4DhcpServer",
        "ipv6DhcpServer",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DhcpServerConfiguration:
        """Build and return the DhcpServerConfiguration instance with validation."""
        self._validate_instance()
        return self._obj