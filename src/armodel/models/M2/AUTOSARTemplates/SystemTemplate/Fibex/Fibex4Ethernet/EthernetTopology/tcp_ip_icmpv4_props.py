"""TcpIpIcmpv4Props AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 156)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class TcpIpIcmpv4Props(ARObject):
    """AUTOSAR TcpIpIcmpv4Props."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    tcp_ip_icmp: Optional[Boolean]
    tcp_ip_icmp_v4_ttl: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize TcpIpIcmpv4Props."""
        super().__init__()
        self.tcp_ip_icmp: Optional[Boolean] = None
        self.tcp_ip_icmp_v4_ttl: Optional[PositiveInteger] = None
    def serialize(self) -> ET.Element:
        """Serialize TcpIpIcmpv4Props to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize tcp_ip_icmp
        if self.tcp_ip_icmp is not None:
            serialized = ARObject._serialize_item(self.tcp_ip_icmp, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-IP-ICMP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_ip_icmp_v4_ttl
        if self.tcp_ip_icmp_v4_ttl is not None:
            serialized = ARObject._serialize_item(self.tcp_ip_icmp_v4_ttl, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-IP-ICMP-V4-TTL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TcpIpIcmpv4Props":
        """Deserialize XML element to TcpIpIcmpv4Props object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TcpIpIcmpv4Props object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse tcp_ip_icmp
        child = ARObject._find_child_element(element, "TCP-IP-ICMP")
        if child is not None:
            tcp_ip_icmp_value = child.text
            obj.tcp_ip_icmp = tcp_ip_icmp_value

        # Parse tcp_ip_icmp_v4_ttl
        child = ARObject._find_child_element(element, "TCP-IP-ICMP-V4-TTL")
        if child is not None:
            tcp_ip_icmp_v4_ttl_value = child.text
            obj.tcp_ip_icmp_v4_ttl = tcp_ip_icmp_v4_ttl_value

        return obj



class TcpIpIcmpv4PropsBuilder:
    """Builder for TcpIpIcmpv4Props."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TcpIpIcmpv4Props = TcpIpIcmpv4Props()

    def build(self) -> TcpIpIcmpv4Props:
        """Build and return TcpIpIcmpv4Props object.

        Returns:
            TcpIpIcmpv4Props instance
        """
        # TODO: Add validation
        return self._obj
