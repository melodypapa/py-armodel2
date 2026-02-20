"""Ipv4FragmentationProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 147)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    TimeValue,
)


class Ipv4FragmentationProps(ARObject):
    """AUTOSAR Ipv4FragmentationProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    tcp_ip_ip: Optional[Boolean]
    tcp_ip_ip_num: Optional[PositiveInteger]
    tcp_ip_ip_reass: Optional[TimeValue]
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
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize tcp_ip_ip
        if self.tcp_ip_ip is not None:
            serialized = ARObject._serialize_item(self.tcp_ip_ip, "Boolean")
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
            serialized = ARObject._serialize_item(self.tcp_ip_ip_num, "PositiveInteger")
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
            serialized = ARObject._serialize_item(self.tcp_ip_ip_reass, "TimeValue")
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
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse tcp_ip_ip
        child = ARObject._find_child_element(element, "TCP-IP-IP")
        if child is not None:
            tcp_ip_ip_value = child.text
            obj.tcp_ip_ip = tcp_ip_ip_value

        # Parse tcp_ip_ip_num
        child = ARObject._find_child_element(element, "TCP-IP-IP-NUM")
        if child is not None:
            tcp_ip_ip_num_value = child.text
            obj.tcp_ip_ip_num = tcp_ip_ip_num_value

        # Parse tcp_ip_ip_reass
        child = ARObject._find_child_element(element, "TCP-IP-IP-REASS")
        if child is not None:
            tcp_ip_ip_reass_value = child.text
            obj.tcp_ip_ip_reass = tcp_ip_ip_reass_value

        return obj



class Ipv4FragmentationPropsBuilder:
    """Builder for Ipv4FragmentationProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Ipv4FragmentationProps = Ipv4FragmentationProps()

    def build(self) -> Ipv4FragmentationProps:
        """Build and return Ipv4FragmentationProps object.

        Returns:
            Ipv4FragmentationProps instance
        """
        # TODO: Add validation
        return self._obj
