"""UdpTp AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 459)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.tcp_udp_config import (
    TcpUdpConfig,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.tp_port import (
    TpPort,
)


class UdpTp(TcpUdpConfig):
    """AUTOSAR UdpTp."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    udp_tp_port: Optional[TpPort]
    def __init__(self) -> None:
        """Initialize UdpTp."""
        super().__init__()
        self.udp_tp_port: Optional[TpPort] = None

    def serialize(self) -> ET.Element:
        """Serialize UdpTp to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(UdpTp, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize udp_tp_port
        if self.udp_tp_port is not None:
            serialized = ARObject._serialize_item(self.udp_tp_port, "TpPort")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UDP-TP-PORT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "UdpTp":
        """Deserialize XML element to UdpTp object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized UdpTp object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(UdpTp, cls).deserialize(element)

        # Parse udp_tp_port
        child = ARObject._find_child_element(element, "UDP-TP-PORT")
        if child is not None:
            udp_tp_port_value = ARObject._deserialize_by_tag(child, "TpPort")
            obj.udp_tp_port = udp_tp_port_value

        return obj



class UdpTpBuilder:
    """Builder for UdpTp."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UdpTp = UdpTp()

    def build(self) -> UdpTp:
        """Build and return UdpTp object.

        Returns:
            UdpTp instance
        """
        # TODO: Add validation
        return self._obj
