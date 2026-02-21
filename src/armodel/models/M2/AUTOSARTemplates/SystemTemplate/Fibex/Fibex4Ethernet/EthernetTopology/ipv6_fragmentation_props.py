"""Ipv6FragmentationProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 148)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)


class Ipv6FragmentationProps(ARObject):
    """AUTOSAR Ipv6FragmentationProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    tcp_ip_ip: Optional[TimeValue]
    tcp_ip_ip_reassembly_buffer_size: Optional[PositiveInteger]
    tcp_ip_ip_tx: Optional[PositiveInteger]
    tcp_ip_ip_tx_fragment_buffer_size: Optional[PositiveInteger]
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
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

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

        # Parse tcp_ip_ip
        child = SerializationHelper.find_child_element(element, "TCP-IP-IP")
        if child is not None:
            tcp_ip_ip_value = child.text
            obj.tcp_ip_ip = tcp_ip_ip_value

        # Parse tcp_ip_ip_reassembly_buffer_size
        child = SerializationHelper.find_child_element(element, "TCP-IP-IP-REASSEMBLY-BUFFER-SIZE")
        if child is not None:
            tcp_ip_ip_reassembly_buffer_size_value = child.text
            obj.tcp_ip_ip_reassembly_buffer_size = tcp_ip_ip_reassembly_buffer_size_value

        # Parse tcp_ip_ip_tx
        child = SerializationHelper.find_child_element(element, "TCP-IP-IP-TX")
        if child is not None:
            tcp_ip_ip_tx_value = child.text
            obj.tcp_ip_ip_tx = tcp_ip_ip_tx_value

        # Parse tcp_ip_ip_tx_fragment_buffer_size
        child = SerializationHelper.find_child_element(element, "TCP-IP-IP-TX-FRAGMENT-BUFFER-SIZE")
        if child is not None:
            tcp_ip_ip_tx_fragment_buffer_size_value = child.text
            obj.tcp_ip_ip_tx_fragment_buffer_size = tcp_ip_ip_tx_fragment_buffer_size_value

        return obj



class Ipv6FragmentationPropsBuilder:
    """Builder for Ipv6FragmentationProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Ipv6FragmentationProps = Ipv6FragmentationProps()

    def build(self) -> Ipv6FragmentationProps:
        """Build and return Ipv6FragmentationProps object.

        Returns:
            Ipv6FragmentationProps instance
        """
        # TODO: Add validation
        return self._obj
