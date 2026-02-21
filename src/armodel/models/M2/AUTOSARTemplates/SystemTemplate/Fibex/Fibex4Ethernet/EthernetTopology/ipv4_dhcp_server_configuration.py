"""Ipv4DhcpServerConfiguration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 131)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.describable import (
    Describable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Ip4AddressString,
    TimeValue,
)


class Ipv4DhcpServerConfiguration(Describable):
    """AUTOSAR Ipv4DhcpServerConfiguration."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    address_range: Optional[Ip4AddressString]
    default_gateway: Optional[Ip4AddressString]
    default_lease: Optional[TimeValue]
    dns_servers: list[Ip4AddressString]
    network_mask: Optional[Ip4AddressString]
    def __init__(self) -> None:
        """Initialize Ipv4DhcpServerConfiguration."""
        super().__init__()
        self.address_range: Optional[Ip4AddressString] = None
        self.default_gateway: Optional[Ip4AddressString] = None
        self.default_lease: Optional[TimeValue] = None
        self.dns_servers: list[Ip4AddressString] = []
        self.network_mask: Optional[Ip4AddressString] = None

    def serialize(self) -> ET.Element:
        """Serialize Ipv4DhcpServerConfiguration to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Ipv4DhcpServerConfiguration, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize address_range
        if self.address_range is not None:
            serialized = SerializationHelper.serialize_item(self.address_range, "Ip4AddressString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ADDRESS-RANGE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize default_gateway
        if self.default_gateway is not None:
            serialized = SerializationHelper.serialize_item(self.default_gateway, "Ip4AddressString")
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

        # Serialize default_lease
        if self.default_lease is not None:
            serialized = SerializationHelper.serialize_item(self.default_lease, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEFAULT-LEASE")
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
                serialized = SerializationHelper.serialize_item(item, "Ip4AddressString")
                if serialized is not None:
                    child_elem = ET.Element("DNS-SERVER")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize network_mask
        if self.network_mask is not None:
            serialized = SerializationHelper.serialize_item(self.network_mask, "Ip4AddressString")
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

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Ipv4DhcpServerConfiguration":
        """Deserialize XML element to Ipv4DhcpServerConfiguration object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Ipv4DhcpServerConfiguration object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Ipv4DhcpServerConfiguration, cls).deserialize(element)

        # Parse address_range
        child = SerializationHelper.find_child_element(element, "ADDRESS-RANGE")
        if child is not None:
            address_range_value = child.text
            obj.address_range = address_range_value

        # Parse default_gateway
        child = SerializationHelper.find_child_element(element, "DEFAULT-GATEWAY")
        if child is not None:
            default_gateway_value = child.text
            obj.default_gateway = default_gateway_value

        # Parse default_lease
        child = SerializationHelper.find_child_element(element, "DEFAULT-LEASE")
        if child is not None:
            default_lease_value = child.text
            obj.default_lease = default_lease_value

        # Parse dns_servers (list from container "DNS-SERVERS")
        obj.dns_servers = []
        container = SerializationHelper.find_child_element(element, "DNS-SERVERS")
        if container is not None:
            for child in container:
                # Extract primitive value (Ip4AddressString) as text
                child_value = child.text
                if child_value is not None:
                    obj.dns_servers.append(child_value)

        # Parse network_mask
        child = SerializationHelper.find_child_element(element, "NETWORK-MASK")
        if child is not None:
            network_mask_value = child.text
            obj.network_mask = network_mask_value

        return obj



class Ipv4DhcpServerConfigurationBuilder:
    """Builder for Ipv4DhcpServerConfiguration."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Ipv4DhcpServerConfiguration = Ipv4DhcpServerConfiguration()

    def build(self) -> Ipv4DhcpServerConfiguration:
        """Build and return Ipv4DhcpServerConfiguration object.

        Returns:
            Ipv4DhcpServerConfiguration instance
        """
        # TODO: Add validation
        return self._obj
