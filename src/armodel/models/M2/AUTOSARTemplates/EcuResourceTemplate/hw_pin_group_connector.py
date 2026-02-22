"""HwPinGroupConnector AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 22)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_EcuResourceTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.describable import (
    Describable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_pin_connector import (
    HwPinConnector,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_pin_group import (
    HwPinGroup,
)


class HwPinGroupConnector(Describable):
    """AUTOSAR HwPinGroupConnector."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    hw_pins: list[HwPinConnector]
    hw_pin_group_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize HwPinGroupConnector."""
        super().__init__()
        self.hw_pins: list[HwPinConnector] = []
        self.hw_pin_group_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize HwPinGroupConnector to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(HwPinGroupConnector, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize hw_pins (list to container "HW-PINS")
        if self.hw_pins:
            wrapper = ET.Element("HW-PINS")
            for item in self.hw_pins:
                serialized = SerializationHelper.serialize_item(item, "HwPinConnector")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize hw_pin_group_refs (list to container "HW-PIN-GROUP-REFS")
        if self.hw_pin_group_refs:
            wrapper = ET.Element("HW-PIN-GROUP-REFS")
            for item in self.hw_pin_group_refs:
                serialized = SerializationHelper.serialize_item(item, "HwPinGroup")
                if serialized is not None:
                    child_elem = ET.Element("HW-PIN-GROUP-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "HwPinGroupConnector":
        """Deserialize XML element to HwPinGroupConnector object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized HwPinGroupConnector object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(HwPinGroupConnector, cls).deserialize(element)

        # Parse hw_pins (list from container "HW-PINS")
        obj.hw_pins = []
        container = SerializationHelper.find_child_element(element, "HW-PINS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.hw_pins.append(child_value)

        # Parse hw_pin_group_refs (list from container "HW-PIN-GROUP-REFS")
        obj.hw_pin_group_refs = []
        container = SerializationHelper.find_child_element(element, "HW-PIN-GROUP-REFS")
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
                    obj.hw_pin_group_refs.append(child_value)

        return obj



class HwPinGroupConnectorBuilder:
    """Builder for HwPinGroupConnector with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: HwPinGroupConnector = HwPinGroupConnector()


    def with_admin_data(self, value: Optional[AdminData]) -> "HwPinGroupConnectorBuilder":
        """Set admin_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.admin_data = value
        return self

    def with_category(self, value: Optional[CategoryString]) -> "HwPinGroupConnectorBuilder":
        """Set category attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.category = value
        return self

    def with_desc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "HwPinGroupConnectorBuilder":
        """Set desc attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.desc = value
        return self

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "HwPinGroupConnectorBuilder":
        """Set introduction attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.introduction = value
        return self

    def with_hw_pins(self, items: list[HwPinConnector]) -> "HwPinGroupConnectorBuilder":
        """Set hw_pins list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.hw_pins = list(items) if items else []
        return self

    def with_hw_pin_groups(self, items: list[HwPinGroup]) -> "HwPinGroupConnectorBuilder":
        """Set hw_pin_groups list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.hw_pin_groups = list(items) if items else []
        return self


    def add_hw_pin(self, item: HwPinConnector) -> "HwPinGroupConnectorBuilder":
        """Add a single item to hw_pins list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.hw_pins.append(item)
        return self

    def clear_hw_pins(self) -> "HwPinGroupConnectorBuilder":
        """Clear all items from hw_pins list.

        Returns:
            self for method chaining
        """
        self._obj.hw_pins = []
        return self

    def add_hw_pin_group(self, item: HwPinGroup) -> "HwPinGroupConnectorBuilder":
        """Add a single item to hw_pin_groups list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.hw_pin_groups.append(item)
        return self

    def clear_hw_pin_groups(self) -> "HwPinGroupConnectorBuilder":
        """Clear all items from hw_pin_groups list.

        Returns:
            self for method chaining
        """
        self._obj.hw_pin_groups = []
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


    def build(self) -> HwPinGroupConnector:
        """Build and return the HwPinGroupConnector instance with validation."""
        self._validate_instance()
        pass
        return self._obj