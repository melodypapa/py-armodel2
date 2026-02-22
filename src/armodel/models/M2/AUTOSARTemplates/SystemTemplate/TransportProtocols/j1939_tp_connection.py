"""J1939TpConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 624)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.tp_connection import (
    TpConnection,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.j1939_tp_node import (
    J1939TpNode,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.j1939_tp_pg import (
    J1939TpPg,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.n_pdu import (
    NPdu,
)


class J1939TpConnection(TpConnection):
    """AUTOSAR J1939TpConnection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    broadcast: Optional[Boolean]
    buffer_ratio: Optional[PositiveInteger]
    cancellation: Optional[Boolean]
    data_pdu_ref: Optional[ARRef]
    dynamic_bs: Optional[Boolean]
    flow_control_pdu: NPdu
    max_bs: Optional[PositiveInteger]
    max_exp_bs: Optional[PositiveInteger]
    receiver_refs: list[ARRef]
    retry: Optional[Boolean]
    tp_pgs: list[J1939TpPg]
    transmitter_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize J1939TpConnection."""
        super().__init__()
        self.broadcast: Optional[Boolean] = None
        self.buffer_ratio: Optional[PositiveInteger] = None
        self.cancellation: Optional[Boolean] = None
        self.data_pdu_ref: Optional[ARRef] = None
        self.dynamic_bs: Optional[Boolean] = None
        self.flow_control_pdu: NPdu = None
        self.max_bs: Optional[PositiveInteger] = None
        self.max_exp_bs: Optional[PositiveInteger] = None
        self.receiver_refs: list[ARRef] = []
        self.retry: Optional[Boolean] = None
        self.tp_pgs: list[J1939TpPg] = []
        self.transmitter_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize J1939TpConnection to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(J1939TpConnection, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize broadcast
        if self.broadcast is not None:
            serialized = SerializationHelper.serialize_item(self.broadcast, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BROADCAST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize buffer_ratio
        if self.buffer_ratio is not None:
            serialized = SerializationHelper.serialize_item(self.buffer_ratio, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BUFFER-RATIO")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize cancellation
        if self.cancellation is not None:
            serialized = SerializationHelper.serialize_item(self.cancellation, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CANCELLATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize data_pdu_ref
        if self.data_pdu_ref is not None:
            serialized = SerializationHelper.serialize_item(self.data_pdu_ref, "NPdu")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-PDU-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize dynamic_bs
        if self.dynamic_bs is not None:
            serialized = SerializationHelper.serialize_item(self.dynamic_bs, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DYNAMIC-BS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize flow_control_pdu
        if self.flow_control_pdu is not None:
            serialized = SerializationHelper.serialize_item(self.flow_control_pdu, "NPdu")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FLOW-CONTROL-PDU")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_bs
        if self.max_bs is not None:
            serialized = SerializationHelper.serialize_item(self.max_bs, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-BS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_exp_bs
        if self.max_exp_bs is not None:
            serialized = SerializationHelper.serialize_item(self.max_exp_bs, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-EXP-BS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize receiver_refs (list to container "RECEIVER-REFS")
        if self.receiver_refs:
            wrapper = ET.Element("RECEIVER-REFS")
            for item in self.receiver_refs:
                serialized = SerializationHelper.serialize_item(item, "J1939TpNode")
                if serialized is not None:
                    child_elem = ET.Element("RECEIVER-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize retry
        if self.retry is not None:
            serialized = SerializationHelper.serialize_item(self.retry, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RETRY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tp_pgs (list to container "TP-PGS")
        if self.tp_pgs:
            wrapper = ET.Element("TP-PGS")
            for item in self.tp_pgs:
                serialized = SerializationHelper.serialize_item(item, "J1939TpPg")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize transmitter_ref
        if self.transmitter_ref is not None:
            serialized = SerializationHelper.serialize_item(self.transmitter_ref, "J1939TpNode")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRANSMITTER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "J1939TpConnection":
        """Deserialize XML element to J1939TpConnection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized J1939TpConnection object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(J1939TpConnection, cls).deserialize(element)

        # Parse broadcast
        child = SerializationHelper.find_child_element(element, "BROADCAST")
        if child is not None:
            broadcast_value = child.text
            obj.broadcast = broadcast_value

        # Parse buffer_ratio
        child = SerializationHelper.find_child_element(element, "BUFFER-RATIO")
        if child is not None:
            buffer_ratio_value = child.text
            obj.buffer_ratio = buffer_ratio_value

        # Parse cancellation
        child = SerializationHelper.find_child_element(element, "CANCELLATION")
        if child is not None:
            cancellation_value = child.text
            obj.cancellation = cancellation_value

        # Parse data_pdu_ref
        child = SerializationHelper.find_child_element(element, "DATA-PDU-REF")
        if child is not None:
            data_pdu_ref_value = ARRef.deserialize(child)
            obj.data_pdu_ref = data_pdu_ref_value

        # Parse dynamic_bs
        child = SerializationHelper.find_child_element(element, "DYNAMIC-BS")
        if child is not None:
            dynamic_bs_value = child.text
            obj.dynamic_bs = dynamic_bs_value

        # Parse flow_control_pdu
        child = SerializationHelper.find_child_element(element, "FLOW-CONTROL-PDU")
        if child is not None:
            flow_control_pdu_value = SerializationHelper.deserialize_by_tag(child, "NPdu")
            obj.flow_control_pdu = flow_control_pdu_value

        # Parse max_bs
        child = SerializationHelper.find_child_element(element, "MAX-BS")
        if child is not None:
            max_bs_value = child.text
            obj.max_bs = max_bs_value

        # Parse max_exp_bs
        child = SerializationHelper.find_child_element(element, "MAX-EXP-BS")
        if child is not None:
            max_exp_bs_value = child.text
            obj.max_exp_bs = max_exp_bs_value

        # Parse receiver_refs (list from container "RECEIVER-REFS")
        obj.receiver_refs = []
        container = SerializationHelper.find_child_element(element, "RECEIVER-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.receiver_refs.append(child_value)

        # Parse retry
        child = SerializationHelper.find_child_element(element, "RETRY")
        if child is not None:
            retry_value = child.text
            obj.retry = retry_value

        # Parse tp_pgs (list from container "TP-PGS")
        obj.tp_pgs = []
        container = SerializationHelper.find_child_element(element, "TP-PGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.tp_pgs.append(child_value)

        # Parse transmitter_ref
        child = SerializationHelper.find_child_element(element, "TRANSMITTER-REF")
        if child is not None:
            transmitter_ref_value = ARRef.deserialize(child)
            obj.transmitter_ref = transmitter_ref_value

        return obj



class J1939TpConnectionBuilder:
    """Builder for J1939TpConnection with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: J1939TpConnection = J1939TpConnection()


    def with_ident(self, value: Optional[TpConnectionIdent]) -> "J1939TpConnectionBuilder":
        """Set ident attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ident = value
        return self

    def with_broadcast(self, value: Optional[Boolean]) -> "J1939TpConnectionBuilder":
        """Set broadcast attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.broadcast = value
        return self

    def with_buffer_ratio(self, value: Optional[PositiveInteger]) -> "J1939TpConnectionBuilder":
        """Set buffer_ratio attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.buffer_ratio = value
        return self

    def with_cancellation(self, value: Optional[Boolean]) -> "J1939TpConnectionBuilder":
        """Set cancellation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.cancellation = value
        return self

    def with_data_pdu(self, value: Optional[NPdu]) -> "J1939TpConnectionBuilder":
        """Set data_pdu attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.data_pdu = value
        return self

    def with_dynamic_bs(self, value: Optional[Boolean]) -> "J1939TpConnectionBuilder":
        """Set dynamic_bs attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.dynamic_bs = value
        return self

    def with_flow_control_pdu(self, value: NPdu) -> "J1939TpConnectionBuilder":
        """Set flow_control_pdu attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.flow_control_pdu = value
        return self

    def with_max_bs(self, value: Optional[PositiveInteger]) -> "J1939TpConnectionBuilder":
        """Set max_bs attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_bs = value
        return self

    def with_max_exp_bs(self, value: Optional[PositiveInteger]) -> "J1939TpConnectionBuilder":
        """Set max_exp_bs attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_exp_bs = value
        return self

    def with_receivers(self, items: list[J1939TpNode]) -> "J1939TpConnectionBuilder":
        """Set receivers list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.receivers = list(items) if items else []
        return self

    def with_retry(self, value: Optional[Boolean]) -> "J1939TpConnectionBuilder":
        """Set retry attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.retry = value
        return self

    def with_tp_pgs(self, items: list[J1939TpPg]) -> "J1939TpConnectionBuilder":
        """Set tp_pgs list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.tp_pgs = list(items) if items else []
        return self

    def with_transmitter(self, value: Optional[J1939TpNode]) -> "J1939TpConnectionBuilder":
        """Set transmitter attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.transmitter = value
        return self


    def add_receiver(self, item: J1939TpNode) -> "J1939TpConnectionBuilder":
        """Add a single item to receivers list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.receivers.append(item)
        return self

    def clear_receivers(self) -> "J1939TpConnectionBuilder":
        """Clear all items from receivers list.

        Returns:
            self for method chaining
        """
        self._obj.receivers = []
        return self

    def add_tp_pg(self, item: J1939TpPg) -> "J1939TpConnectionBuilder":
        """Add a single item to tp_pgs list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.tp_pgs.append(item)
        return self

    def clear_tp_pgs(self) -> "J1939TpConnectionBuilder":
        """Clear all items from tp_pgs list.

        Returns:
            self for method chaining
        """
        self._obj.tp_pgs = []
        return self


    @staticmethod
    def _coerce_to_int(value: Any) -> int:
        """Coerce value to int.

        Args:
            value: Value to coerce

        Returns:
            Integer value

        Raises:
            ValueError: If value cannot be coerced to int
        """
        if isinstance(value, int):
            return value
        if isinstance(value, str) and value.isdigit():
            return int(value)
        if isinstance(value, float):
            return int(value)
        if isinstance(value, bool):
            return int(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to int: {value}")

    @staticmethod
    def _coerce_to_float(value: Any) -> float:
        """Coerce value to float.

        Args:
            value: Value to coerce

        Returns:
            Float value

        Raises:
            ValueError: If value cannot be coerced to float
        """
        if isinstance(value, float):
            return value
        if isinstance(value, int):
            return float(value)
        if isinstance(value, str):
            try:
                return float(value)
            except ValueError:
                pass
        raise ValueError(f"Cannot coerce {type(value).__name__} to float: {value}")

    @staticmethod
    def _coerce_to_bool(value: Any) -> bool:
        """Coerce value to bool.

        Args:
            value: Value to coerce

        Returns:
            Boolean value

        Raises:
            ValueError: If value cannot be coerced to bool
        """
        if isinstance(value, bool):
            return value
        if isinstance(value, int):
            return bool(value)
        if isinstance(value, str):
            if value.lower() in ("true", "1", "yes"):
                return True
            if value.lower() in ("false", "0", "no"):
                return False
        raise ValueError(f"Cannot coerce {type(value).__name__} to bool: {value}")

    @staticmethod
    def _coerce_to_str(value: Any) -> str:
        """Coerce value to str.

        Args:
            value: Value to coerce

        Returns:
            String value
        """
        return str(value)


    @staticmethod
    def _coerce_to_list(value: Any, item_type: str) -> list:
        """Coerce value to list.

        Args:
            value: Value to coerce
            item_type: Expected item type (for error messages)

        Returns:
            List value

        Raises:
            ValueError: If value cannot be coerced to list
        """
        if isinstance(value, list):
            return value
        if isinstance(value, tuple):
            return list(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to list[{item_type}]: {value}")


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


    def build(self) -> J1939TpConnection:
        """Build and return the J1939TpConnection instance with validation."""
        self._validate_instance()
        pass
        return self._obj