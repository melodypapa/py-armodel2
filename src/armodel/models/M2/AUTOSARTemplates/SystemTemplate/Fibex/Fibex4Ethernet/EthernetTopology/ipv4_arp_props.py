"""Ipv4ArpProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 146)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    TimeValue,
)


class Ipv4ArpProps(ARObject):
    """AUTOSAR Ipv4ArpProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    tcp_ip_arp_num: Optional[PositiveInteger]
    tcp_ip_arp_packet: Optional[Boolean]
    tcp_ip_arp: Optional[TimeValue]
    tcp_ip_arp_table: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize Ipv4ArpProps."""
        super().__init__()
        self.tcp_ip_arp_num: Optional[PositiveInteger] = None
        self.tcp_ip_arp_packet: Optional[Boolean] = None
        self.tcp_ip_arp: Optional[TimeValue] = None
        self.tcp_ip_arp_table: Optional[TimeValue] = None

    def serialize(self) -> ET.Element:
        """Serialize Ipv4ArpProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Ipv4ArpProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize tcp_ip_arp_num
        if self.tcp_ip_arp_num is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_ip_arp_num, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-IP-ARP-NUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_ip_arp_packet
        if self.tcp_ip_arp_packet is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_ip_arp_packet, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-IP-ARP-PACKET")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_ip_arp
        if self.tcp_ip_arp is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_ip_arp, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-IP-ARP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_ip_arp_table
        if self.tcp_ip_arp_table is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_ip_arp_table, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-IP-ARP-TABLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Ipv4ArpProps":
        """Deserialize XML element to Ipv4ArpProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Ipv4ArpProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Ipv4ArpProps, cls).deserialize(element)

        # Parse tcp_ip_arp_num
        child = SerializationHelper.find_child_element(element, "TCP-IP-ARP-NUM")
        if child is not None:
            tcp_ip_arp_num_value = child.text
            obj.tcp_ip_arp_num = tcp_ip_arp_num_value

        # Parse tcp_ip_arp_packet
        child = SerializationHelper.find_child_element(element, "TCP-IP-ARP-PACKET")
        if child is not None:
            tcp_ip_arp_packet_value = child.text
            obj.tcp_ip_arp_packet = tcp_ip_arp_packet_value

        # Parse tcp_ip_arp
        child = SerializationHelper.find_child_element(element, "TCP-IP-ARP")
        if child is not None:
            tcp_ip_arp_value = child.text
            obj.tcp_ip_arp = tcp_ip_arp_value

        # Parse tcp_ip_arp_table
        child = SerializationHelper.find_child_element(element, "TCP-IP-ARP-TABLE")
        if child is not None:
            tcp_ip_arp_table_value = child.text
            obj.tcp_ip_arp_table = tcp_ip_arp_table_value

        return obj



class Ipv4ArpPropsBuilder:
    """Builder for Ipv4ArpProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Ipv4ArpProps = Ipv4ArpProps()

    def build(self) -> Ipv4ArpProps:
        """Build and return Ipv4ArpProps object.

        Returns:
            Ipv4ArpProps instance
        """
        # TODO: Add validation
        return self._obj
