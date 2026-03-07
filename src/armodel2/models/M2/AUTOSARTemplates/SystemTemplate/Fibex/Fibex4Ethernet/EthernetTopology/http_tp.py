"""HttpTp AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 461)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.transport_protocol_configuration import (
    TransportProtocolConfiguration,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.transport_protocol_configuration import TransportProtocolConfigurationBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
    UriString,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.tcp_tp import (
    TcpTp,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class HttpTp(TransportProtocolConfiguration):
    """AUTOSAR HttpTp."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "HTTP-TP"


    content_type: Optional[String]
    protocol_version: Optional[String]
    request_method_enum: Optional[Any]
    tcp_tp_config: Optional[TcpTp]
    uri: Optional[UriString]
    _DESERIALIZE_DISPATCH = {
        "CONTENT-TYPE": lambda obj, elem: setattr(obj, "content_type", SerializationHelper.deserialize_by_tag(elem, "String")),
        "PROTOCOL-VERSION": lambda obj, elem: setattr(obj, "protocol_version", SerializationHelper.deserialize_by_tag(elem, "String")),
        "REQUEST-METHOD-ENUM": lambda obj, elem: setattr(obj, "request_method_enum", SerializationHelper.deserialize_by_tag(elem, "any (RequestMethodEnum)")),
        "TCP-TP-CONFIG": lambda obj, elem: setattr(obj, "tcp_tp_config", SerializationHelper.deserialize_by_tag(elem, "TcpTp")),
        "URI": lambda obj, elem: setattr(obj, "uri", SerializationHelper.deserialize_by_tag(elem, "UriString")),
    }


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
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(HttpTp, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize content_type
        if self.content_type is not None:
            serialized = SerializationHelper.serialize_item(self.content_type, "String")
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
            serialized = SerializationHelper.serialize_item(self.protocol_version, "String")
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
            serialized = SerializationHelper.serialize_item(self.request_method_enum, "Any")
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
            serialized = SerializationHelper.serialize_item(self.tcp_tp_config, "TcpTp")
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
            serialized = SerializationHelper.serialize_item(self.uri, "UriString")
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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CONTENT-TYPE":
                setattr(obj, "content_type", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "PROTOCOL-VERSION":
                setattr(obj, "protocol_version", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "REQUEST-METHOD-ENUM":
                setattr(obj, "request_method_enum", SerializationHelper.deserialize_by_tag(child, "any (RequestMethodEnum)"))
            elif tag == "TCP-TP-CONFIG":
                setattr(obj, "tcp_tp_config", SerializationHelper.deserialize_by_tag(child, "TcpTp"))
            elif tag == "URI":
                setattr(obj, "uri", SerializationHelper.deserialize_by_tag(child, "UriString"))

        return obj



class HttpTpBuilder(TransportProtocolConfigurationBuilder):
    """Builder for HttpTp with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: HttpTp = HttpTp()


    def with_content_type(self, value: Optional[String]) -> "HttpTpBuilder":
        """Set content_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'content_type' is required and cannot be None")
        self._obj.content_type = value
        return self

    def with_protocol_version(self, value: Optional[String]) -> "HttpTpBuilder":
        """Set protocol_version attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'protocol_version' is required and cannot be None")
        self._obj.protocol_version = value
        return self

    def with_request_method_enum(self, value: Optional[Any]) -> "HttpTpBuilder":
        """Set request_method_enum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'request_method_enum' is required and cannot be None")
        self._obj.request_method_enum = value
        return self

    def with_tcp_tp_config(self, value: Optional[TcpTp]) -> "HttpTpBuilder":
        """Set tcp_tp_config attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'tcp_tp_config' is required and cannot be None")
        self._obj.tcp_tp_config = value
        return self

    def with_uri(self, value: Optional[UriString]) -> "HttpTpBuilder":
        """Set uri attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'uri' is required and cannot be None")
        self._obj.uri = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "contentType",
        "protocolVersion",
        "requestMethodEnum",
        "tcpTpConfig",
        "uri",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> HttpTp:
        """Build and return the HttpTp instance with validation."""
        self._validate_instance()
        return self._obj