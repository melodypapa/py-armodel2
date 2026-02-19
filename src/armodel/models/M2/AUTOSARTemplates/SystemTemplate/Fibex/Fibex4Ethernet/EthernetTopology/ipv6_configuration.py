"""Ipv6Configuration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 466)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.network_endpoint_address import (
    NetworkEndpointAddress,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    IpAddressKeepEnum,
    Ipv6AddressSourceEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Ip6AddressString,
    PositiveInteger,
)


class Ipv6Configuration(NetworkEndpointAddress):
    """AUTOSAR Ipv6Configuration."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    assignment: Optional[PositiveInteger]
    default_router: Optional[Ip6AddressString]
    dns_servers: list[Ip6AddressString]
    enable_anycast: Optional[Boolean]
    hop_count: Optional[PositiveInteger]
    ip_address_keep_enum: Optional[IpAddressKeepEnum]
    ip_address_prefix: Optional[PositiveInteger]
    ipv6_address: Optional[Ip6AddressString]
    ipv6_address_source: Optional[Ipv6AddressSourceEnum]
    def __init__(self) -> None:
        """Initialize Ipv6Configuration."""
        super().__init__()
        self.assignment: Optional[PositiveInteger] = None
        self.default_router: Optional[Ip6AddressString] = None
        self.dns_servers: list[Ip6AddressString] = []
        self.enable_anycast: Optional[Boolean] = None
        self.hop_count: Optional[PositiveInteger] = None
        self.ip_address_keep_enum: Optional[IpAddressKeepEnum] = None
        self.ip_address_prefix: Optional[PositiveInteger] = None
        self.ipv6_address: Optional[Ip6AddressString] = None
        self.ipv6_address_source: Optional[Ipv6AddressSourceEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize Ipv6Configuration to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Ipv6Configuration, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize assignment
        if self.assignment is not None:
            serialized = ARObject._serialize_item(self.assignment, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ASSIGNMENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize default_router
        if self.default_router is not None:
            serialized = ARObject._serialize_item(self.default_router, "Ip6AddressString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEFAULT-ROUTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize dns_servers (list to container "DNS-SERVERS")
        if self.dns_servers:
            wrapper = ET.Element("DNS-SERVERS")
            for item in self.dns_servers:
                serialized = ARObject._serialize_item(item, "Ip6AddressString")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize enable_anycast
        if self.enable_anycast is not None:
            serialized = ARObject._serialize_item(self.enable_anycast, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ENABLE-ANYCAST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize hop_count
        if self.hop_count is not None:
            serialized = ARObject._serialize_item(self.hop_count, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HOP-COUNT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ip_address_keep_enum
        if self.ip_address_keep_enum is not None:
            serialized = ARObject._serialize_item(self.ip_address_keep_enum, "IpAddressKeepEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IP-ADDRESS-KEEP-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ip_address_prefix
        if self.ip_address_prefix is not None:
            serialized = ARObject._serialize_item(self.ip_address_prefix, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IP-ADDRESS-PREFIX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ipv6_address
        if self.ipv6_address is not None:
            serialized = ARObject._serialize_item(self.ipv6_address, "Ip6AddressString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IPV6-ADDRESS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ipv6_address_source
        if self.ipv6_address_source is not None:
            serialized = ARObject._serialize_item(self.ipv6_address_source, "Ipv6AddressSourceEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IPV6-ADDRESS-SOURCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Ipv6Configuration":
        """Deserialize XML element to Ipv6Configuration object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Ipv6Configuration object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Ipv6Configuration, cls).deserialize(element)

        # Parse assignment
        child = ARObject._find_child_element(element, "ASSIGNMENT")
        if child is not None:
            assignment_value = child.text
            obj.assignment = assignment_value

        # Parse default_router
        child = ARObject._find_child_element(element, "DEFAULT-ROUTER")
        if child is not None:
            default_router_value = child.text
            obj.default_router = default_router_value

        # Parse dns_servers (list from container "DNS-SERVERS")
        obj.dns_servers = []
        container = ARObject._find_child_element(element, "DNS-SERVERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.dns_servers.append(child_value)

        # Parse enable_anycast
        child = ARObject._find_child_element(element, "ENABLE-ANYCAST")
        if child is not None:
            enable_anycast_value = child.text
            obj.enable_anycast = enable_anycast_value

        # Parse hop_count
        child = ARObject._find_child_element(element, "HOP-COUNT")
        if child is not None:
            hop_count_value = child.text
            obj.hop_count = hop_count_value

        # Parse ip_address_keep_enum
        child = ARObject._find_child_element(element, "IP-ADDRESS-KEEP-ENUM")
        if child is not None:
            ip_address_keep_enum_value = IpAddressKeepEnum.deserialize(child)
            obj.ip_address_keep_enum = ip_address_keep_enum_value

        # Parse ip_address_prefix
        child = ARObject._find_child_element(element, "IP-ADDRESS-PREFIX")
        if child is not None:
            ip_address_prefix_value = child.text
            obj.ip_address_prefix = ip_address_prefix_value

        # Parse ipv6_address
        child = ARObject._find_child_element(element, "IPV6-ADDRESS")
        if child is not None:
            ipv6_address_value = child.text
            obj.ipv6_address = ipv6_address_value

        # Parse ipv6_address_source
        child = ARObject._find_child_element(element, "IPV6-ADDRESS-SOURCE")
        if child is not None:
            ipv6_address_source_value = Ipv6AddressSourceEnum.deserialize(child)
            obj.ipv6_address_source = ipv6_address_source_value

        return obj



class Ipv6ConfigurationBuilder:
    """Builder for Ipv6Configuration."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Ipv6Configuration = Ipv6Configuration()

    def build(self) -> Ipv6Configuration:
        """Build and return Ipv6Configuration object.

        Returns:
            Ipv6Configuration instance
        """
        # TODO: Add validation
        return self._obj
