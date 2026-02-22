"""CanControllerConfiguration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 64)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology.abstract_can_communication_controller_attributes import (
    AbstractCanCommunicationControllerAttributes,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class CanControllerConfiguration(AbstractCanCommunicationControllerAttributes):
    """AUTOSAR CanControllerConfiguration."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    prop_seg: Optional[Integer]
    sync_jump_width: Optional[Integer]
    time_seg1: Optional[Integer]
    time_seg2: Optional[Integer]
    def __init__(self) -> None:
        """Initialize CanControllerConfiguration."""
        super().__init__()
        self.prop_seg: Optional[Integer] = None
        self.sync_jump_width: Optional[Integer] = None
        self.time_seg1: Optional[Integer] = None
        self.time_seg2: Optional[Integer] = None

    def serialize(self) -> ET.Element:
        """Serialize CanControllerConfiguration to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CanControllerConfiguration, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize prop_seg
        if self.prop_seg is not None:
            serialized = SerializationHelper.serialize_item(self.prop_seg, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROP-SEG")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sync_jump_width
        if self.sync_jump_width is not None:
            serialized = SerializationHelper.serialize_item(self.sync_jump_width, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SYNC-JUMP-WIDTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize time_seg1
        if self.time_seg1 is not None:
            serialized = SerializationHelper.serialize_item(self.time_seg1, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-SEG1")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize time_seg2
        if self.time_seg2 is not None:
            serialized = SerializationHelper.serialize_item(self.time_seg2, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-SEG2")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanControllerConfiguration":
        """Deserialize XML element to CanControllerConfiguration object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CanControllerConfiguration object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CanControllerConfiguration, cls).deserialize(element)

        # Parse prop_seg
        child = SerializationHelper.find_child_element(element, "PROP-SEG")
        if child is not None:
            prop_seg_value = child.text
            obj.prop_seg = prop_seg_value

        # Parse sync_jump_width
        child = SerializationHelper.find_child_element(element, "SYNC-JUMP-WIDTH")
        if child is not None:
            sync_jump_width_value = child.text
            obj.sync_jump_width = sync_jump_width_value

        # Parse time_seg1
        child = SerializationHelper.find_child_element(element, "TIME-SEG1")
        if child is not None:
            time_seg1_value = child.text
            obj.time_seg1 = time_seg1_value

        # Parse time_seg2
        child = SerializationHelper.find_child_element(element, "TIME-SEG2")
        if child is not None:
            time_seg2_value = child.text
            obj.time_seg2 = time_seg2_value

        return obj



class CanControllerConfigurationBuilder:
    """Builder for CanControllerConfiguration with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: CanControllerConfiguration = CanControllerConfiguration()


    def with_can_controller_fd(self, value: Optional[any (CanControllerFd)]) -> "CanControllerConfigurationBuilder":
        """Set can_controller_fd attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.can_controller_fd = value
        return self

    def with_can_controller_xl(self, value: Optional[any (CanControllerXl)]) -> "CanControllerConfigurationBuilder":
        """Set can_controller_xl attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.can_controller_xl = value
        return self

    def with_prop_seg(self, value: Optional[Integer]) -> "CanControllerConfigurationBuilder":
        """Set prop_seg attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.prop_seg = value
        return self

    def with_sync_jump_width(self, value: Optional[Integer]) -> "CanControllerConfigurationBuilder":
        """Set sync_jump_width attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sync_jump_width = value
        return self

    def with_time_seg1(self, value: Optional[Integer]) -> "CanControllerConfigurationBuilder":
        """Set time_seg1 attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.time_seg1 = value
        return self

    def with_time_seg2(self, value: Optional[Integer]) -> "CanControllerConfigurationBuilder":
        """Set time_seg2 attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.time_seg2 = value
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


    def build(self) -> CanControllerConfiguration:
        """Build and return the CanControllerConfiguration instance with validation."""
        self._validate_instance()
        pass
        return self._obj