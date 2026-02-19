"""EthTcpIpProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 153)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.tcp_props import (
    TcpProps,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.udp_props import (
    UdpProps,
)


class EthTcpIpProps(ARElement):
    """AUTOSAR EthTcpIpProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    tcp_props: Optional[TcpProps]
    udp_props: Optional[UdpProps]
    def __init__(self) -> None:
        """Initialize EthTcpIpProps."""
        super().__init__()
        self.tcp_props: Optional[TcpProps] = None
        self.udp_props: Optional[UdpProps] = None
    def serialize(self) -> ET.Element:
        """Serialize EthTcpIpProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EthTcpIpProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize tcp_props
        if self.tcp_props is not None:
            serialized = ARObject._serialize_item(self.tcp_props, "TcpProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-PROPS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize udp_props
        if self.udp_props is not None:
            serialized = ARObject._serialize_item(self.udp_props, "UdpProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UDP-PROPS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthTcpIpProps":
        """Deserialize XML element to EthTcpIpProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EthTcpIpProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EthTcpIpProps, cls).deserialize(element)

        # Parse tcp_props
        child = ARObject._find_child_element(element, "TCP-PROPS")
        if child is not None:
            tcp_props_value = ARObject._deserialize_by_tag(child, "TcpProps")
            obj.tcp_props = tcp_props_value

        # Parse udp_props
        child = ARObject._find_child_element(element, "UDP-PROPS")
        if child is not None:
            udp_props_value = ARObject._deserialize_by_tag(child, "UdpProps")
            obj.udp_props = udp_props_value

        return obj



class EthTcpIpPropsBuilder:
    """Builder for EthTcpIpProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EthTcpIpProps = EthTcpIpProps()

    def build(self) -> EthTcpIpProps:
        """Build and return EthTcpIpProps object.

        Returns:
            EthTcpIpProps instance
        """
        # TODO: Add validation
        return self._obj
