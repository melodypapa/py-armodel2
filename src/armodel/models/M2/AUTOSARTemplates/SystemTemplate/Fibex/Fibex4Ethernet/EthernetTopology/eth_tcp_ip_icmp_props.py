"""EthTcpIpIcmpProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 156)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.tcp_ip_icmpv4_props import (
    TcpIpIcmpv4Props,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.tcp_ip_icmpv6_props import (
    TcpIpIcmpv6Props,
)


class EthTcpIpIcmpProps(ARElement):
    """AUTOSAR EthTcpIpIcmpProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    icmp_v4_props: Optional[TcpIpIcmpv4Props]
    icmp_v6_props: Optional[TcpIpIcmpv6Props]
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
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EthTcpIpIcmpProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize icmp_v4_props
        if self.icmp_v4_props is not None:
            serialized = ARObject._serialize_item(self.icmp_v4_props, "TcpIpIcmpv4Props")
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
            serialized = ARObject._serialize_item(self.icmp_v6_props, "TcpIpIcmpv6Props")
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

        # Parse icmp_v4_props
        child = ARObject._find_child_element(element, "ICMP-V4-PROPS")
        if child is not None:
            icmp_v4_props_value = ARObject._deserialize_by_tag(child, "TcpIpIcmpv4Props")
            obj.icmp_v4_props = icmp_v4_props_value

        # Parse icmp_v6_props
        child = ARObject._find_child_element(element, "ICMP-V6-PROPS")
        if child is not None:
            icmp_v6_props_value = ARObject._deserialize_by_tag(child, "TcpIpIcmpv6Props")
            obj.icmp_v6_props = icmp_v6_props_value

        return obj



class EthTcpIpIcmpPropsBuilder:
    """Builder for EthTcpIpIcmpProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EthTcpIpIcmpProps = EthTcpIpIcmpProps()

    def build(self) -> EthTcpIpIcmpProps:
        """Build and return EthTcpIpIcmpProps object.

        Returns:
            EthTcpIpIcmpProps instance
        """
        # TODO: Add validation
        return self._obj
