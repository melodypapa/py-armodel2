"""TcpTp AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 460)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.tcp_udp_config import (
    TcpUdpConfig,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.tcp_udp_config import TcpUdpConfigBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.tp_port import (
    TpPort,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class TcpTp(TcpUdpConfig):
    """AUTOSAR TcpTp."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    keep_alive: Optional[PositiveInteger]
    keep_alives: Optional[Boolean]
    keep_alive_time: Optional[TimeValue]
    nagles_algorithm: Optional[Boolean]
    receive_window_min: Optional[PositiveInteger]
    tcp: Optional[TimeValue]
    tcp_tp_port: Optional[TpPort]
    def __init__(self) -> None:
        """Initialize TcpTp."""
        super().__init__()
        self.keep_alive: Optional[PositiveInteger] = None
        self.keep_alives: Optional[Boolean] = None
        self.keep_alive_time: Optional[TimeValue] = None
        self.nagles_algorithm: Optional[Boolean] = None
        self.receive_window_min: Optional[PositiveInteger] = None
        self.tcp: Optional[TimeValue] = None
        self.tcp_tp_port: Optional[TpPort] = None

    def serialize(self) -> ET.Element:
        """Serialize TcpTp to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TcpTp, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize keep_alive
        if self.keep_alive is not None:
            serialized = SerializationHelper.serialize_item(self.keep_alive, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("KEEP-ALIVE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize keep_alives
        if self.keep_alives is not None:
            serialized = SerializationHelper.serialize_item(self.keep_alives, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("KEEP-ALIVES")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize keep_alive_time
        if self.keep_alive_time is not None:
            serialized = SerializationHelper.serialize_item(self.keep_alive_time, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("KEEP-ALIVE-TIME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nagles_algorithm
        if self.nagles_algorithm is not None:
            serialized = SerializationHelper.serialize_item(self.nagles_algorithm, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NAGLES-ALGORITHM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize receive_window_min
        if self.receive_window_min is not None:
            serialized = SerializationHelper.serialize_item(self.receive_window_min, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RECEIVE-WINDOW-MIN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp
        if self.tcp is not None:
            serialized = SerializationHelper.serialize_item(self.tcp, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_tp_port
        if self.tcp_tp_port is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_tp_port, "TpPort")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-TP-PORT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TcpTp":
        """Deserialize XML element to TcpTp object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TcpTp object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TcpTp, cls).deserialize(element)

        # Parse keep_alive
        child = SerializationHelper.find_child_element(element, "KEEP-ALIVE")
        if child is not None:
            keep_alive_value = child.text
            obj.keep_alive = keep_alive_value

        # Parse keep_alives
        child = SerializationHelper.find_child_element(element, "KEEP-ALIVES")
        if child is not None:
            keep_alives_value = child.text
            obj.keep_alives = keep_alives_value

        # Parse keep_alive_time
        child = SerializationHelper.find_child_element(element, "KEEP-ALIVE-TIME")
        if child is not None:
            keep_alive_time_value = child.text
            obj.keep_alive_time = keep_alive_time_value

        # Parse nagles_algorithm
        child = SerializationHelper.find_child_element(element, "NAGLES-ALGORITHM")
        if child is not None:
            nagles_algorithm_value = child.text
            obj.nagles_algorithm = nagles_algorithm_value

        # Parse receive_window_min
        child = SerializationHelper.find_child_element(element, "RECEIVE-WINDOW-MIN")
        if child is not None:
            receive_window_min_value = child.text
            obj.receive_window_min = receive_window_min_value

        # Parse tcp
        child = SerializationHelper.find_child_element(element, "TCP")
        if child is not None:
            tcp_value = child.text
            obj.tcp = tcp_value

        # Parse tcp_tp_port
        child = SerializationHelper.find_child_element(element, "TCP-TP-PORT")
        if child is not None:
            tcp_tp_port_value = SerializationHelper.deserialize_by_tag(child, "TpPort")
            obj.tcp_tp_port = tcp_tp_port_value

        return obj



class TcpTpBuilder(TcpUdpConfigBuilder):
    """Builder for TcpTp with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TcpTp = TcpTp()


    def with_keep_alive(self, value: Optional[PositiveInteger]) -> "TcpTpBuilder":
        """Set keep_alive attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.keep_alive = value
        return self

    def with_keep_alives(self, value: Optional[Boolean]) -> "TcpTpBuilder":
        """Set keep_alives attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.keep_alives = value
        return self

    def with_keep_alive_time(self, value: Optional[TimeValue]) -> "TcpTpBuilder":
        """Set keep_alive_time attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.keep_alive_time = value
        return self

    def with_nagles_algorithm(self, value: Optional[Boolean]) -> "TcpTpBuilder":
        """Set nagles_algorithm attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nagles_algorithm = value
        return self

    def with_receive_window_min(self, value: Optional[PositiveInteger]) -> "TcpTpBuilder":
        """Set receive_window_min attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.receive_window_min = value
        return self

    def with_tcp(self, value: Optional[TimeValue]) -> "TcpTpBuilder":
        """Set tcp attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tcp = value
        return self

    def with_tcp_tp_port(self, value: Optional[TpPort]) -> "TcpTpBuilder":
        """Set tcp_tp_port attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tcp_tp_port = value
        return self




    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

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


    def build(self) -> TcpTp:
        """Build and return the TcpTp instance with validation."""
        self._validate_instance()
        pass
        return self._obj