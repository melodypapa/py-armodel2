"""BuildEngineeringObject AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 372)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_BuildActionManifest.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject.engineering_object import (
    EngineeringObject,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    RegularExpression,
    UriString,
)


class BuildEngineeringObject(EngineeringObject):
    """AUTOSAR BuildEngineeringObject."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    file_type: NameToken
    file_type_pattern: RegularExpression
    intended: Optional[UriString]
    def __init__(self) -> None:
        """Initialize BuildEngineeringObject."""
        super().__init__()
        self.file_type: NameToken = None
        self.file_type_pattern: RegularExpression = None
        self.intended: Optional[UriString] = None

    def serialize(self) -> ET.Element:
        """Serialize BuildEngineeringObject to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BuildEngineeringObject, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize file_type
        if self.file_type is not None:
            serialized = SerializationHelper.serialize_item(self.file_type, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FILE-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize file_type_pattern
        if self.file_type_pattern is not None:
            serialized = SerializationHelper.serialize_item(self.file_type_pattern, "RegularExpression")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FILE-TYPE-PATTERN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize intended
        if self.intended is not None:
            serialized = SerializationHelper.serialize_item(self.intended, "UriString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INTENDED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BuildEngineeringObject":
        """Deserialize XML element to BuildEngineeringObject object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BuildEngineeringObject object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BuildEngineeringObject, cls).deserialize(element)

        # Parse file_type
        child = SerializationHelper.find_child_element(element, "FILE-TYPE")
        if child is not None:
            file_type_value = child.text
            obj.file_type = file_type_value

        # Parse file_type_pattern
        child = SerializationHelper.find_child_element(element, "FILE-TYPE-PATTERN")
        if child is not None:
            file_type_pattern_value = child.text
            obj.file_type_pattern = file_type_pattern_value

        # Parse intended
        child = SerializationHelper.find_child_element(element, "INTENDED")
        if child is not None:
            intended_value = child.text
            obj.intended = intended_value

        return obj



class BuildEngineeringObjectBuilder:
    """Builder for BuildEngineeringObject with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: BuildEngineeringObject = BuildEngineeringObject()


    def with_category(self, value: NameToken) -> "BuildEngineeringObjectBuilder":
        """Set category attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.category = value
        return self

    def with_domain(self, value: Optional[NameToken]) -> "BuildEngineeringObjectBuilder":
        """Set domain attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.domain = value
        return self

    def with_revision_label_strings(self, items: list[RevisionLabelString]) -> "BuildEngineeringObjectBuilder":
        """Set revision_label_strings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.revision_label_strings = list(items) if items else []
        return self

    def with_short_label(self, value: NameToken) -> "BuildEngineeringObjectBuilder":
        """Set short_label attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.short_label = value
        return self

    def with_file_type(self, value: NameToken) -> "BuildEngineeringObjectBuilder":
        """Set file_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.file_type = value
        return self

    def with_file_type_pattern(self, value: RegularExpression) -> "BuildEngineeringObjectBuilder":
        """Set file_type_pattern attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.file_type_pattern = value
        return self

    def with_intended(self, value: Optional[UriString]) -> "BuildEngineeringObjectBuilder":
        """Set intended attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.intended = value
        return self


    def add_revision_label_string(self, item: RevisionLabelString) -> "BuildEngineeringObjectBuilder":
        """Add a single item to revision_label_strings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.revision_label_strings.append(item)
        return self

    def clear_revision_label_strings(self) -> "BuildEngineeringObjectBuilder":
        """Clear all items from revision_label_strings list.

        Returns:
            self for method chaining
        """
        self._obj.revision_label_strings = []
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


    def build(self) -> BuildEngineeringObject:
        """Build and return the BuildEngineeringObject instance with validation."""
        self._validate_instance()
        pass
        return self._obj