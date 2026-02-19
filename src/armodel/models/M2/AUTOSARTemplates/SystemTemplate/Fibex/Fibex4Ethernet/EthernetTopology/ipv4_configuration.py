"""Ipv4Configuration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 465)

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
    Ipv4AddressSourceEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Ip4AddressString,
    PositiveInteger,
)


class Ipv4Configuration(NetworkEndpointAddress):
    """AUTOSAR Ipv4Configuration."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    assignment: Optional[PositiveInteger]
    default_gateway: Optional[Ip4AddressString]
    dns_servers: list[Ip4AddressString]
    ip_address_keep_enum: Optional[IpAddressKeepEnum]
    ipv4_address: Optional[Ip4AddressString]
    ipv4_address_source: Optional[Ipv4AddressSourceEnum]
    network_mask: Optional[Ip4AddressString]
    ttl: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize Ipv4Configuration."""
        super().__init__()
        self.assignment: Optional[PositiveInteger] = None
        self.default_gateway: Optional[Ip4AddressString] = None
        self.dns_servers: list[Ip4AddressString] = []
        self.ip_address_keep_enum: Optional[IpAddressKeepEnum] = None
        self.ipv4_address: Optional[Ip4AddressString] = None
        self.ipv4_address_source: Optional[Ipv4AddressSourceEnum] = None
        self.network_mask: Optional[Ip4AddressString] = None
        self.ttl: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize Ipv4Configuration to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Ipv4Configuration, self).serialize()

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

        # Serialize default_gateway
        if self.default_gateway is not None:
            serialized = ARObject._serialize_item(self.default_gateway, "Ip4AddressString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEFAULT-GATEWAY")
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
                serialized = ARObject._serialize_item(item, "Ip4AddressString")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

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

        # Serialize ipv4_address
        if self.ipv4_address is not None:
            serialized = ARObject._serialize_item(self.ipv4_address, "Ip4AddressString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IPV4-ADDRESS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ipv4_address_source
        if self.ipv4_address_source is not None:
            serialized = ARObject._serialize_item(self.ipv4_address_source, "Ipv4AddressSourceEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IPV4-ADDRESS-SOURCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize network_mask
        if self.network_mask is not None:
            serialized = ARObject._serialize_item(self.network_mask, "Ip4AddressString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NETWORK-MASK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ttl
        if self.ttl is not None:
            serialized = ARObject._serialize_item(self.ttl, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TTL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Ipv4Configuration":
        """Deserialize XML element to Ipv4Configuration object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Ipv4Configuration object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Ipv4Configuration, cls).deserialize(element)

        # Parse assignment
        child = ARObject._find_child_element(element, "ASSIGNMENT")
        if child is not None:
            assignment_value = child.text
            obj.assignment = assignment_value

        # Parse default_gateway
        child = ARObject._find_child_element(element, "DEFAULT-GATEWAY")
        if child is not None:
            default_gateway_value = child.text
            obj.default_gateway = default_gateway_value

        # Parse dns_servers (list from container "DNS-SERVERS")
        obj.dns_servers = []
        container = ARObject._find_child_element(element, "DNS-SERVERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.dns_servers.append(child_value)

        # Parse ip_address_keep_enum
        child = ARObject._find_child_element(element, "IP-ADDRESS-KEEP-ENUM")
        if child is not None:
            ip_address_keep_enum_value = IpAddressKeepEnum.deserialize(child)
            obj.ip_address_keep_enum = ip_address_keep_enum_value

        # Parse ipv4_address
        child = ARObject._find_child_element(element, "IPV4-ADDRESS")
        if child is not None:
            ipv4_address_value = child.text
            obj.ipv4_address = ipv4_address_value

        # Parse ipv4_address_source
        child = ARObject._find_child_element(element, "IPV4-ADDRESS-SOURCE")
        if child is not None:
            ipv4_address_source_value = Ipv4AddressSourceEnum.deserialize(child)
            obj.ipv4_address_source = ipv4_address_source_value

        # Parse network_mask
        child = ARObject._find_child_element(element, "NETWORK-MASK")
        if child is not None:
            network_mask_value = child.text
            obj.network_mask = network_mask_value

        # Parse ttl
        child = ARObject._find_child_element(element, "TTL")
        if child is not None:
            ttl_value = child.text
            obj.ttl = ttl_value

        return obj



class Ipv4ConfigurationBuilder:
    """Builder for Ipv4Configuration."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Ipv4Configuration = Ipv4Configuration()

    def build(self) -> Ipv4Configuration:
        """Build and return Ipv4Configuration object.

        Returns:
            Ipv4Configuration instance
        """
        # TODO: Add validation
        return self._obj
