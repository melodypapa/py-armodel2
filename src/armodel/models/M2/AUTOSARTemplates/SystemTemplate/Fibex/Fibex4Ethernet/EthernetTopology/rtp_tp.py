"""RtpTp AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 460)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.transport_protocol_configuration import (
    TransportProtocolConfiguration,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.tcp_udp_config import (
    TcpUdpConfig,
)


class RtpTp(TransportProtocolConfiguration):
    """AUTOSAR RtpTp."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ssrc: Optional[PositiveInteger]
    tcp_udp_config: Optional[TcpUdpConfig]
    def __init__(self) -> None:
        """Initialize RtpTp."""
        super().__init__()
        self.ssrc: Optional[PositiveInteger] = None
        self.tcp_udp_config: Optional[TcpUdpConfig] = None
    def serialize(self) -> ET.Element:
        """Serialize RtpTp to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RtpTp, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ssrc
        if self.ssrc is not None:
            serialized = ARObject._serialize_item(self.ssrc, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SSRC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_udp_config
        if self.tcp_udp_config is not None:
            serialized = ARObject._serialize_item(self.tcp_udp_config, "TcpUdpConfig")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-UDP-CONFIG")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RtpTp":
        """Deserialize XML element to RtpTp object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RtpTp object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RtpTp, cls).deserialize(element)

        # Parse ssrc
        child = ARObject._find_child_element(element, "SSRC")
        if child is not None:
            ssrc_value = child.text
            obj.ssrc = ssrc_value

        # Parse tcp_udp_config
        child = ARObject._find_child_element(element, "TCP-UDP-CONFIG")
        if child is not None:
            tcp_udp_config_value = ARObject._deserialize_by_tag(child, "TcpUdpConfig")
            obj.tcp_udp_config = tcp_udp_config_value

        return obj



class RtpTpBuilder:
    """Builder for RtpTp."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RtpTp = RtpTp()

    def build(self) -> RtpTp:
        """Build and return RtpTp object.

        Returns:
            RtpTp instance
        """
        # TODO: Add validation
        return self._obj
