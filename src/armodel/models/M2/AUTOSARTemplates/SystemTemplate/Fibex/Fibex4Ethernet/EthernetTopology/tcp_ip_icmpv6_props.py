"""TcpIpIcmpv6Props AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 156)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class TcpIpIcmpv6Props(ARObject):
    """AUTOSAR TcpIpIcmpv6Props."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    tcp_ip_icmp: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize TcpIpIcmpv6Props."""
        super().__init__()
        self.tcp_ip_icmp: Optional[Boolean] = None
    def serialize(self) -> ET.Element:
        """Serialize TcpIpIcmpv6Props to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
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

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TcpIpIcmpv6Props":
        """Deserialize XML element to TcpIpIcmpv6Props object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TcpIpIcmpv6Props object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse tcp_ip_icmp
        child = ARObject._find_child_element(element, "TCP-IP-ICMP")
        if child is not None:
            tcp_ip_icmp_value = child.text
            obj.tcp_ip_icmp = tcp_ip_icmp_value

        return obj



class TcpIpIcmpv6PropsBuilder:
    """Builder for TcpIpIcmpv6Props."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TcpIpIcmpv6Props = TcpIpIcmpv6Props()

    def build(self) -> TcpIpIcmpv6Props:
        """Build and return TcpIpIcmpv6Props object.

        Returns:
            TcpIpIcmpv6Props instance
        """
        # TODO: Add validation
        return self._obj
