"""TcpProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 154)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class TcpProps(ARObject):
    """AUTOSAR TcpProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "TCP-PROPS"


    tcp_congestion: Optional[Boolean]
    tcp_delayed_ack: Optional[TimeValue]
    tcp_fast_recovery: Optional[Any]
    tcp_fast: Optional[Boolean]
    tcp_fin: Optional[TimeValue]
    tcp_keep_alive: Optional[TimeValue]
    tcp_max_rtx: Optional[PositiveInteger]
    tcp_msl: Optional[TimeValue]
    tcp_nagle: Optional[Boolean]
    tcp_receive_window_max: Optional[PositiveInteger]
    tcp: Optional[TimeValue]
    tcp_slow_start: Optional[Boolean]
    tcp_syn_max_rtx: Optional[PositiveInteger]
    tcp_syn_received: Optional[TimeValue]
    tcp_ttl: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "TCP-CONGESTION": lambda obj, elem: setattr(obj, "tcp_congestion", elem.text),
        "TCP-DELAYED-ACK": lambda obj, elem: setattr(obj, "tcp_delayed_ack", elem.text),
        "TCP-FAST-RECOVERY": lambda obj, elem: setattr(obj, "tcp_fast_recovery", any (BooleanRecovery).deserialize(elem)),
        "TCP-FAST": lambda obj, elem: setattr(obj, "tcp_fast", elem.text),
        "TCP-FIN": lambda obj, elem: setattr(obj, "tcp_fin", elem.text),
        "TCP-KEEP-ALIVE": lambda obj, elem: setattr(obj, "tcp_keep_alive", elem.text),
        "TCP-MAX-RTX": lambda obj, elem: setattr(obj, "tcp_max_rtx", elem.text),
        "TCP-MSL": lambda obj, elem: setattr(obj, "tcp_msl", elem.text),
        "TCP-NAGLE": lambda obj, elem: setattr(obj, "tcp_nagle", elem.text),
        "TCP-RECEIVE-WINDOW-MAX": lambda obj, elem: setattr(obj, "tcp_receive_window_max", elem.text),
        "TCP": lambda obj, elem: setattr(obj, "tcp", elem.text),
        "TCP-SLOW-START": lambda obj, elem: setattr(obj, "tcp_slow_start", elem.text),
        "TCP-SYN-MAX-RTX": lambda obj, elem: setattr(obj, "tcp_syn_max_rtx", elem.text),
        "TCP-SYN-RECEIVED": lambda obj, elem: setattr(obj, "tcp_syn_received", elem.text),
        "TCP-TTL": lambda obj, elem: setattr(obj, "tcp_ttl", elem.text),
    }


    def __init__(self) -> None:
        """Initialize TcpProps."""
        super().__init__()
        self.tcp_congestion: Optional[Boolean] = None
        self.tcp_delayed_ack: Optional[TimeValue] = None
        self.tcp_fast_recovery: Optional[Any] = None
        self.tcp_fast: Optional[Boolean] = None
        self.tcp_fin: Optional[TimeValue] = None
        self.tcp_keep_alive: Optional[TimeValue] = None
        self.tcp_max_rtx: Optional[PositiveInteger] = None
        self.tcp_msl: Optional[TimeValue] = None
        self.tcp_nagle: Optional[Boolean] = None
        self.tcp_receive_window_max: Optional[PositiveInteger] = None
        self.tcp: Optional[TimeValue] = None
        self.tcp_slow_start: Optional[Boolean] = None
        self.tcp_syn_max_rtx: Optional[PositiveInteger] = None
        self.tcp_syn_received: Optional[TimeValue] = None
        self.tcp_ttl: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize TcpProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TcpProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize tcp_congestion
        if self.tcp_congestion is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_congestion, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-CONGESTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_delayed_ack
        if self.tcp_delayed_ack is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_delayed_ack, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-DELAYED-ACK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_fast_recovery
        if self.tcp_fast_recovery is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_fast_recovery, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-FAST-RECOVERY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_fast
        if self.tcp_fast is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_fast, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-FAST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_fin
        if self.tcp_fin is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_fin, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-FIN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_keep_alive
        if self.tcp_keep_alive is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_keep_alive, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-KEEP-ALIVE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_max_rtx
        if self.tcp_max_rtx is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_max_rtx, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-MAX-RTX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_msl
        if self.tcp_msl is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_msl, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-MSL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_nagle
        if self.tcp_nagle is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_nagle, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-NAGLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_receive_window_max
        if self.tcp_receive_window_max is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_receive_window_max, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-RECEIVE-WINDOW-MAX")
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

        # Serialize tcp_slow_start
        if self.tcp_slow_start is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_slow_start, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-SLOW-START")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_syn_max_rtx
        if self.tcp_syn_max_rtx is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_syn_max_rtx, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-SYN-MAX-RTX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_syn_received
        if self.tcp_syn_received is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_syn_received, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-SYN-RECEIVED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_ttl
        if self.tcp_ttl is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_ttl, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-TTL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TcpProps":
        """Deserialize XML element to TcpProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TcpProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TcpProps, cls).deserialize(element)

        # Parse tcp_congestion
        child = SerializationHelper.find_child_element(element, "TCP-CONGESTION")
        if child is not None:
            tcp_congestion_value = child.text
            obj.tcp_congestion = tcp_congestion_value

        # Parse tcp_delayed_ack
        child = SerializationHelper.find_child_element(element, "TCP-DELAYED-ACK")
        if child is not None:
            tcp_delayed_ack_value = child.text
            obj.tcp_delayed_ack = tcp_delayed_ack_value

        # Parse tcp_fast_recovery
        child = SerializationHelper.find_child_element(element, "TCP-FAST-RECOVERY")
        if child is not None:
            tcp_fast_recovery_value = child.text
            obj.tcp_fast_recovery = tcp_fast_recovery_value

        # Parse tcp_fast
        child = SerializationHelper.find_child_element(element, "TCP-FAST")
        if child is not None:
            tcp_fast_value = child.text
            obj.tcp_fast = tcp_fast_value

        # Parse tcp_fin
        child = SerializationHelper.find_child_element(element, "TCP-FIN")
        if child is not None:
            tcp_fin_value = child.text
            obj.tcp_fin = tcp_fin_value

        # Parse tcp_keep_alive
        child = SerializationHelper.find_child_element(element, "TCP-KEEP-ALIVE")
        if child is not None:
            tcp_keep_alive_value = child.text
            obj.tcp_keep_alive = tcp_keep_alive_value

        # Parse tcp_max_rtx
        child = SerializationHelper.find_child_element(element, "TCP-MAX-RTX")
        if child is not None:
            tcp_max_rtx_value = child.text
            obj.tcp_max_rtx = tcp_max_rtx_value

        # Parse tcp_msl
        child = SerializationHelper.find_child_element(element, "TCP-MSL")
        if child is not None:
            tcp_msl_value = child.text
            obj.tcp_msl = tcp_msl_value

        # Parse tcp_nagle
        child = SerializationHelper.find_child_element(element, "TCP-NAGLE")
        if child is not None:
            tcp_nagle_value = child.text
            obj.tcp_nagle = tcp_nagle_value

        # Parse tcp_receive_window_max
        child = SerializationHelper.find_child_element(element, "TCP-RECEIVE-WINDOW-MAX")
        if child is not None:
            tcp_receive_window_max_value = child.text
            obj.tcp_receive_window_max = tcp_receive_window_max_value

        # Parse tcp
        child = SerializationHelper.find_child_element(element, "TCP")
        if child is not None:
            tcp_value = child.text
            obj.tcp = tcp_value

        # Parse tcp_slow_start
        child = SerializationHelper.find_child_element(element, "TCP-SLOW-START")
        if child is not None:
            tcp_slow_start_value = child.text
            obj.tcp_slow_start = tcp_slow_start_value

        # Parse tcp_syn_max_rtx
        child = SerializationHelper.find_child_element(element, "TCP-SYN-MAX-RTX")
        if child is not None:
            tcp_syn_max_rtx_value = child.text
            obj.tcp_syn_max_rtx = tcp_syn_max_rtx_value

        # Parse tcp_syn_received
        child = SerializationHelper.find_child_element(element, "TCP-SYN-RECEIVED")
        if child is not None:
            tcp_syn_received_value = child.text
            obj.tcp_syn_received = tcp_syn_received_value

        # Parse tcp_ttl
        child = SerializationHelper.find_child_element(element, "TCP-TTL")
        if child is not None:
            tcp_ttl_value = child.text
            obj.tcp_ttl = tcp_ttl_value

        return obj



class TcpPropsBuilder(BuilderBase):
    """Builder for TcpProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TcpProps = TcpProps()


    def with_tcp_congestion(self, value: Optional[Boolean]) -> "TcpPropsBuilder":
        """Set tcp_congestion attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tcp_congestion = value
        return self

    def with_tcp_delayed_ack(self, value: Optional[TimeValue]) -> "TcpPropsBuilder":
        """Set tcp_delayed_ack attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tcp_delayed_ack = value
        return self

    def with_tcp_fast_recovery(self, value: Optional[any (BooleanRecovery)]) -> "TcpPropsBuilder":
        """Set tcp_fast_recovery attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tcp_fast_recovery = value
        return self

    def with_tcp_fast(self, value: Optional[Boolean]) -> "TcpPropsBuilder":
        """Set tcp_fast attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tcp_fast = value
        return self

    def with_tcp_fin(self, value: Optional[TimeValue]) -> "TcpPropsBuilder":
        """Set tcp_fin attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tcp_fin = value
        return self

    def with_tcp_keep_alive(self, value: Optional[TimeValue]) -> "TcpPropsBuilder":
        """Set tcp_keep_alive attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tcp_keep_alive = value
        return self

    def with_tcp_max_rtx(self, value: Optional[PositiveInteger]) -> "TcpPropsBuilder":
        """Set tcp_max_rtx attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tcp_max_rtx = value
        return self

    def with_tcp_msl(self, value: Optional[TimeValue]) -> "TcpPropsBuilder":
        """Set tcp_msl attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tcp_msl = value
        return self

    def with_tcp_nagle(self, value: Optional[Boolean]) -> "TcpPropsBuilder":
        """Set tcp_nagle attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tcp_nagle = value
        return self

    def with_tcp_receive_window_max(self, value: Optional[PositiveInteger]) -> "TcpPropsBuilder":
        """Set tcp_receive_window_max attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tcp_receive_window_max = value
        return self

    def with_tcp(self, value: Optional[TimeValue]) -> "TcpPropsBuilder":
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

    def with_tcp_slow_start(self, value: Optional[Boolean]) -> "TcpPropsBuilder":
        """Set tcp_slow_start attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tcp_slow_start = value
        return self

    def with_tcp_syn_max_rtx(self, value: Optional[PositiveInteger]) -> "TcpPropsBuilder":
        """Set tcp_syn_max_rtx attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tcp_syn_max_rtx = value
        return self

    def with_tcp_syn_received(self, value: Optional[TimeValue]) -> "TcpPropsBuilder":
        """Set tcp_syn_received attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tcp_syn_received = value
        return self

    def with_tcp_ttl(self, value: Optional[PositiveInteger]) -> "TcpPropsBuilder":
        """Set tcp_ttl attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tcp_ttl = value
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


    def build(self) -> TcpProps:
        """Build and return the TcpProps instance with validation."""
        self._validate_instance()
        pass
        return self._obj