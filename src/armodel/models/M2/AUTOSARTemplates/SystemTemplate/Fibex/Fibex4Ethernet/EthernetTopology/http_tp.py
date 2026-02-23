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
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.transport_protocol_configuration import TransportProtocolConfigurationBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
    UriString,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.tcp_tp import (
    TcpTp,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


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
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

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

        # Parse content_type
        child = SerializationHelper.find_child_element(element, "CONTENT-TYPE")
        if child is not None:
            content_type_value = child.text
            obj.content_type = content_type_value

        # Parse protocol_version
        child = SerializationHelper.find_child_element(element, "PROTOCOL-VERSION")
        if child is not None:
            protocol_version_value = child.text
            obj.protocol_version = protocol_version_value

        # Parse request_method_enum
        child = SerializationHelper.find_child_element(element, "REQUEST-METHOD-ENUM")
        if child is not None:
            request_method_enum_value = child.text
            obj.request_method_enum = request_method_enum_value

        # Parse tcp_tp_config
        child = SerializationHelper.find_child_element(element, "TCP-TP-CONFIG")
        if child is not None:
            tcp_tp_config_value = SerializationHelper.deserialize_by_tag(child, "TcpTp")
            obj.tcp_tp_config = tcp_tp_config_value

        # Parse uri
        child = SerializationHelper.find_child_element(element, "URI")
        if child is not None:
            uri_value = child.text
            obj.uri = uri_value

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
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
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
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.protocol_version = value
        return self

    def with_request_method_enum(self, value: Optional[any (RequestMethodEnum)]) -> "HttpTpBuilder":
        """Set request_method_enum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
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
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
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
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.uri = value
        return self




    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Get type hints for the class
        try:
            type_hints_dict = get_type_hints(type(self._obj))
        except Exception:
            # Cannot resolve type hints (e.g., forward references), skip validation
            return

        for attr_name, attr_type in type_hints_dict.items():
            if attr_name.startswith("_"):
                continue

            value = getattr(self._obj, attr_name)

            # Check required fields (not Optional)
            if value is None and not self._is_optional_type(attr_type):
                if mode == BuilderValidationMode.STRICT:
                    raise ValueError(
                        f"Required attribute '{attr_name}' is None"
                    )
                elif mode == BuilderValidationMode.LENIENT:
                    import warnings
                    warnings.warn(
                        f"Required attribute '{attr_name}' is None",
                        UserWarning
                    )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type is Optional, False otherwise
        """
        origin = getattr(type_hint, "__origin__", None)
        return origin is Union

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract expected type from type hint.

        Args:
            type_hint: Type hint to extract from

        Returns:
            Expected type
        """
        if isinstance(type_hint, str):
            return object
        origin = getattr(type_hint, "__origin__", None)
        if origin is Union:
            args = getattr(type_hint, "__args__", [])
            for arg in args:
                if arg is not type(None):
                    return arg
        elif origin is list:
            args = getattr(type_hint, "__args__", [object])
            return args[0] if args else object
        return type_hint if isinstance(type_hint, type) else object


    def build(self) -> HttpTp:
        """Build and return the HttpTp instance with validation."""
        self._validate_instance()
        pass
        return self._obj