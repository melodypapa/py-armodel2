"""DataFormatTailoring AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 180)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.class_tailoring import (
    ClassTailoring,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.constraint_tailoring import (
    ConstraintTailoring,
)


class DataFormatTailoring(ARObject):
    """AUTOSAR DataFormatTailoring."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    class_tailorings: list[ClassTailoring]
    constraints: list[ConstraintTailoring]
    def __init__(self) -> None:
        """Initialize DataFormatTailoring."""
        super().__init__()
        self.class_tailorings: list[ClassTailoring] = []
        self.constraints: list[ConstraintTailoring] = []

    def serialize(self) -> ET.Element:
        """Serialize DataFormatTailoring to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DataFormatTailoring, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize class_tailorings (list to container "CLASS-TAILORINGS")
        if self.class_tailorings:
            wrapper = ET.Element("CLASS-TAILORINGS")
            for item in self.class_tailorings:
                serialized = SerializationHelper.serialize_item(item, "ClassTailoring")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize constraints (list to container "CONSTRAINTS")
        if self.constraints:
            wrapper = ET.Element("CONSTRAINTS")
            for item in self.constraints:
                serialized = SerializationHelper.serialize_item(item, "ConstraintTailoring")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataFormatTailoring":
        """Deserialize XML element to DataFormatTailoring object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataFormatTailoring object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DataFormatTailoring, cls).deserialize(element)

        # Parse class_tailorings (list from container "CLASS-TAILORINGS")
        obj.class_tailorings = []
        container = SerializationHelper.find_child_element(element, "CLASS-TAILORINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.class_tailorings.append(child_value)

        # Parse constraints (list from container "CONSTRAINTS")
        obj.constraints = []
        container = SerializationHelper.find_child_element(element, "CONSTRAINTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.constraints.append(child_value)

        return obj



class DataFormatTailoringBuilder:
    """Builder for DataFormatTailoring with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: DataFormatTailoring = DataFormatTailoring()


    def with_class_tailorings(self, items: list[ClassTailoring]) -> "DataFormatTailoringBuilder":
        """Set class_tailorings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.class_tailorings = list(items) if items else []
        return self

    def with_constraints(self, items: list[ConstraintTailoring]) -> "DataFormatTailoringBuilder":
        """Set constraints list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.constraints = list(items) if items else []
        return self


    def add_class_tailoring(self, item: ClassTailoring) -> "DataFormatTailoringBuilder":
        """Add a single item to class_tailorings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.class_tailorings.append(item)
        return self

    def clear_class_tailorings(self) -> "DataFormatTailoringBuilder":
        """Clear all items from class_tailorings list.

        Returns:
            self for method chaining
        """
        self._obj.class_tailorings = []
        return self

    def add_constraint(self, item: ConstraintTailoring) -> "DataFormatTailoringBuilder":
        """Add a single item to constraints list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.constraints.append(item)
        return self

    def clear_constraints(self) -> "DataFormatTailoringBuilder":
        """Clear all items from constraints list.

        Returns:
            self for method chaining
        """
        self._obj.constraints = []
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


    def build(self) -> DataFormatTailoring:
        """Build and return the DataFormatTailoring instance with validation."""
        self._validate_instance()
        pass
        return self._obj