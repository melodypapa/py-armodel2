"""SenderRecArrayTypeMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 235)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DataMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.sender_rec_composite_type_mapping import (
    SenderRecCompositeTypeMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.text_table_mapping import (
    TextTableMapping,
)


class SenderRecArrayTypeMapping(SenderRecCompositeTypeMapping):
    """AUTOSAR SenderRecArrayTypeMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    array_elements: list[Any]
    sender_to_signal_ref: Optional[ARRef]
    signal_to_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize SenderRecArrayTypeMapping."""
        super().__init__()
        self.array_elements: list[Any] = []
        self.sender_to_signal_ref: Optional[ARRef] = None
        self.signal_to_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize SenderRecArrayTypeMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SenderRecArrayTypeMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize array_elements (list to container "ARRAY-ELEMENTS")
        if self.array_elements:
            wrapper = ET.Element("ARRAY-ELEMENTS")
            for item in self.array_elements:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize sender_to_signal_ref
        if self.sender_to_signal_ref is not None:
            serialized = SerializationHelper.serialize_item(self.sender_to_signal_ref, "TextTableMapping")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SENDER-TO-SIGNAL-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize signal_to_ref
        if self.signal_to_ref is not None:
            serialized = SerializationHelper.serialize_item(self.signal_to_ref, "TextTableMapping")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SIGNAL-TO-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SenderRecArrayTypeMapping":
        """Deserialize XML element to SenderRecArrayTypeMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SenderRecArrayTypeMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SenderRecArrayTypeMapping, cls).deserialize(element)

        # Parse array_elements (list from container "ARRAY-ELEMENTS")
        obj.array_elements = []
        container = SerializationHelper.find_child_element(element, "ARRAY-ELEMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.array_elements.append(child_value)

        # Parse sender_to_signal_ref
        child = SerializationHelper.find_child_element(element, "SENDER-TO-SIGNAL-REF")
        if child is not None:
            sender_to_signal_ref_value = ARRef.deserialize(child)
            obj.sender_to_signal_ref = sender_to_signal_ref_value

        # Parse signal_to_ref
        child = SerializationHelper.find_child_element(element, "SIGNAL-TO-REF")
        if child is not None:
            signal_to_ref_value = ARRef.deserialize(child)
            obj.signal_to_ref = signal_to_ref_value

        return obj



class SenderRecArrayTypeMappingBuilder:
    """Builder for SenderRecArrayTypeMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: SenderRecArrayTypeMapping = SenderRecArrayTypeMapping()


    def with_array_elements(self, items: list[any (SenderRecArray)]) -> "SenderRecArrayTypeMappingBuilder":
        """Set array_elements list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.array_elements = list(items) if items else []
        return self

    def with_sender_to_signal(self, value: Optional[TextTableMapping]) -> "SenderRecArrayTypeMappingBuilder":
        """Set sender_to_signal attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sender_to_signal = value
        return self

    def with_signal_to(self, value: Optional[TextTableMapping]) -> "SenderRecArrayTypeMappingBuilder":
        """Set signal_to attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.signal_to = value
        return self


    def add_array_element(self, item: any (SenderRecArray)) -> "SenderRecArrayTypeMappingBuilder":
        """Add a single item to array_elements list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.array_elements.append(item)
        return self

    def clear_array_elements(self) -> "SenderRecArrayTypeMappingBuilder":
        """Clear all items from array_elements list.

        Returns:
            self for method chaining
        """
        self._obj.array_elements = []
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


    def build(self) -> SenderRecArrayTypeMapping:
        """Build and return the SenderRecArrayTypeMapping instance with validation."""
        self._validate_instance()
        pass
        return self._obj