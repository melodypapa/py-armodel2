"""TtcanCommunicationController AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 76)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ttcan_TtcanTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import atp_variant

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
)


@atp_variant()

class TtcanCommunicationController(ARObject):
    """AUTOSAR TtcanCommunicationController."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    appl_watchdog: Optional[Integer]
    expected_tx: Optional[Integer]
    external_clock: Optional[Boolean]
    initial_ref_offset: Optional[Integer]
    master: Optional[Boolean]
    time_master: Optional[Integer]
    time_triggered: Optional[Integer]
    tx_enable: Optional[Integer]
    def __init__(self) -> None:
        """Initialize TtcanCommunicationController."""
        super().__init__()
        self.appl_watchdog: Optional[Integer] = None
        self.expected_tx: Optional[Integer] = None
        self.external_clock: Optional[Boolean] = None
        self.initial_ref_offset: Optional[Integer] = None
        self.master: Optional[Boolean] = None
        self.time_master: Optional[Integer] = None
        self.time_triggered: Optional[Integer] = None
        self.tx_enable: Optional[Integer] = None

    def serialize(self) -> ET.Element:
        """Serialize TtcanCommunicationController to XML element with atp_variant wrapper.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TtcanCommunicationController, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Create inner element to hold attributes before wrapping
        inner_elem = ET.Element("INNER")

        # Serialize appl_watchdog
        if self.appl_watchdog is not None:
            serialized = SerializationHelper.serialize_item(self.appl_watchdog, "Integer")
            if serialized is not None:
                wrapped = ET.Element("APPL-WATCHDOG")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize expected_tx
        if self.expected_tx is not None:
            serialized = SerializationHelper.serialize_item(self.expected_tx, "Integer")
            if serialized is not None:
                wrapped = ET.Element("EXPECTED-TX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize external_clock
        if self.external_clock is not None:
            serialized = SerializationHelper.serialize_item(self.external_clock, "Boolean")
            if serialized is not None:
                wrapped = ET.Element("EXTERNAL-CLOCK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize initial_ref_offset
        if self.initial_ref_offset is not None:
            serialized = SerializationHelper.serialize_item(self.initial_ref_offset, "Integer")
            if serialized is not None:
                wrapped = ET.Element("INITIAL-REF-OFFSET")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize master
        if self.master is not None:
            serialized = SerializationHelper.serialize_item(self.master, "Boolean")
            if serialized is not None:
                wrapped = ET.Element("MASTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize time_master
        if self.time_master is not None:
            serialized = SerializationHelper.serialize_item(self.time_master, "Integer")
            if serialized is not None:
                wrapped = ET.Element("TIME-MASTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize time_triggered
        if self.time_triggered is not None:
            serialized = SerializationHelper.serialize_item(self.time_triggered, "Integer")
            if serialized is not None:
                wrapped = ET.Element("TIME-TRIGGERED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize tx_enable
        if self.tx_enable is not None:
            serialized = SerializationHelper.serialize_item(self.tx_enable, "Integer")
            if serialized is not None:
                wrapped = ET.Element("TX-ENABLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Wrap inner element in atp_variant VARIANTS/CONDITIONAL structure
        wrapped = SerializationHelper.serialize_with_atp_variant(inner_elem, "TtcanCommunicationController")
        elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TtcanCommunicationController":
        """Deserialize XML element to TtcanCommunicationController object with atp_variant unwrapping.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TtcanCommunicationController object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TtcanCommunicationController, cls).deserialize(element)

        # Unwrap atp_variant VARIANTS/CONDITIONAL structure
        inner_elem = SerializationHelper.deserialize_from_atp_variant(element, "TtcanCommunicationController")
        if inner_elem is None:
            # No wrapper structure found, return object with default values
            return obj

        # Parse appl_watchdog
        child = SerializationHelper.find_child_element(inner_elem, "APPL-WATCHDOG")
        if child is not None:
            appl_watchdog_value = child.text
            obj.appl_watchdog = appl_watchdog_value

        # Parse expected_tx
        child = SerializationHelper.find_child_element(inner_elem, "EXPECTED-TX")
        if child is not None:
            expected_tx_value = child.text
            obj.expected_tx = expected_tx_value

        # Parse external_clock
        child = SerializationHelper.find_child_element(inner_elem, "EXTERNAL-CLOCK")
        if child is not None:
            external_clock_value = child.text
            obj.external_clock = external_clock_value

        # Parse initial_ref_offset
        child = SerializationHelper.find_child_element(inner_elem, "INITIAL-REF-OFFSET")
        if child is not None:
            initial_ref_offset_value = child.text
            obj.initial_ref_offset = initial_ref_offset_value

        # Parse master
        child = SerializationHelper.find_child_element(inner_elem, "MASTER")
        if child is not None:
            master_value = child.text
            obj.master = master_value

        # Parse time_master
        child = SerializationHelper.find_child_element(inner_elem, "TIME-MASTER")
        if child is not None:
            time_master_value = child.text
            obj.time_master = time_master_value

        # Parse time_triggered
        child = SerializationHelper.find_child_element(inner_elem, "TIME-TRIGGERED")
        if child is not None:
            time_triggered_value = child.text
            obj.time_triggered = time_triggered_value

        # Parse tx_enable
        child = SerializationHelper.find_child_element(inner_elem, "TX-ENABLE")
        if child is not None:
            tx_enable_value = child.text
            obj.tx_enable = tx_enable_value

        return obj



class TtcanCommunicationControllerBuilder:
    """Builder for TtcanCommunicationController with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: TtcanCommunicationController = TtcanCommunicationController()


    def with_appl_watchdog(self, value: Optional[Integer]) -> "TtcanCommunicationControllerBuilder":
        """Set appl_watchdog attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.appl_watchdog = value
        return self

    def with_expected_tx(self, value: Optional[Integer]) -> "TtcanCommunicationControllerBuilder":
        """Set expected_tx attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.expected_tx = value
        return self

    def with_external_clock(self, value: Optional[Boolean]) -> "TtcanCommunicationControllerBuilder":
        """Set external_clock attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.external_clock = value
        return self

    def with_initial_ref_offset(self, value: Optional[Integer]) -> "TtcanCommunicationControllerBuilder":
        """Set initial_ref_offset attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.initial_ref_offset = value
        return self

    def with_master(self, value: Optional[Boolean]) -> "TtcanCommunicationControllerBuilder":
        """Set master attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.master = value
        return self

    def with_time_master(self, value: Optional[Integer]) -> "TtcanCommunicationControllerBuilder":
        """Set time_master attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.time_master = value
        return self

    def with_time_triggered(self, value: Optional[Integer]) -> "TtcanCommunicationControllerBuilder":
        """Set time_triggered attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.time_triggered = value
        return self

    def with_tx_enable(self, value: Optional[Integer]) -> "TtcanCommunicationControllerBuilder":
        """Set tx_enable attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tx_enable = value
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


    def build(self) -> TtcanCommunicationController:
        """Build and return the TtcanCommunicationController instance with validation."""
        self._validate_instance()
        pass
        return self._obj