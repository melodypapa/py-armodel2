"""HttpTp AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 461)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.transport_protocol_configuration import (
    TransportProtocolConfiguration,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
    UriString,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.tcp_tp import (
    TcpTp,
)


class HttpTp(TransportProtocolConfiguration):
    """AUTOSAR HttpTp."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    content_type: Optional[String]
    protocol_version: Optional[String]
    request_method_enum: Optional[Any]
    tcp_tp_config: Optional[TcpTp]
    uri: Optional[UriString]
    def __init__(self) -> None:
        """Initialize HttpTp."""
        super().__init__()
        self.content_type: Optional[String] = None
        self.protocol_version: Optional[String] = None
        self.request_method_enum: Optional[Any] = None
        self.tcp_tp_config: Optional[TcpTp] = None
        self.uri: Optional[UriString] = None
    def serialize(self) -> ET.Element:
        """Serialize HttpTp to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(HttpTp, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize content_type
        if self.content_type is not None:
            serialized = ARObject._serialize_item(self.content_type, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTENT-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize protocol_version
        if self.protocol_version is not None:
            serialized = ARObject._serialize_item(self.protocol_version, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROTOCOL-VERSION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize request_method_enum
        if self.request_method_enum is not None:
            serialized = ARObject._serialize_item(self.request_method_enum, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REQUEST-METHOD-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_tp_config
        if self.tcp_tp_config is not None:
            serialized = ARObject._serialize_item(self.tcp_tp_config, "TcpTp")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-TP-CONFIG")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize uri
        if self.uri is not None:
            serialized = ARObject._serialize_item(self.uri, "UriString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("URI")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "HttpTp":
        """Deserialize XML element to HttpTp object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized HttpTp object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(HttpTp, cls).deserialize(element)

        # Parse content_type
        child = ARObject._find_child_element(element, "CONTENT-TYPE")
        if child is not None:
            content_type_value = child.text
            obj.content_type = content_type_value

        # Parse protocol_version
        child = ARObject._find_child_element(element, "PROTOCOL-VERSION")
        if child is not None:
            protocol_version_value = child.text
            obj.protocol_version = protocol_version_value

        # Parse request_method_enum
        child = ARObject._find_child_element(element, "REQUEST-METHOD-ENUM")
        if child is not None:
            request_method_enum_value = child.text
            obj.request_method_enum = request_method_enum_value

        # Parse tcp_tp_config
        child = ARObject._find_child_element(element, "TCP-TP-CONFIG")
        if child is not None:
            tcp_tp_config_value = ARObject._deserialize_by_tag(child, "TcpTp")
            obj.tcp_tp_config = tcp_tp_config_value

        # Parse uri
        child = ARObject._find_child_element(element, "URI")
        if child is not None:
            uri_value = child.text
            obj.uri = uri_value

        return obj



class HttpTpBuilder:
    """Builder for HttpTp."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HttpTp = HttpTp()

    def build(self) -> HttpTp:
        """Build and return HttpTp object.

        Returns:
            HttpTp instance
        """
        # TODO: Add validation
        return self._obj
