"""FMFeatureSelectionSet AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 44)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_FeatureModelTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature_model import (
    FMFeatureModel,
)
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature_selection import (
    FMFeatureSelection,
)


class FMFeatureSelectionSet(ARElement):
    """AUTOSAR FMFeatureSelectionSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    feature_model_refs: list[ARRef]
    include_refs: list[ARRef]
    selections: list[FMFeatureSelection]
    def __init__(self) -> None:
        """Initialize FMFeatureSelectionSet."""
        super().__init__()
        self.feature_model_refs: list[ARRef] = []
        self.include_refs: list[ARRef] = []
        self.selections: list[FMFeatureSelection] = []

    def serialize(self) -> ET.Element:
        """Serialize FMFeatureSelectionSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FMFeatureSelectionSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize feature_model_refs (list to container "FEATURE-MODEL-REFS")
        if self.feature_model_refs:
            wrapper = ET.Element("FEATURE-MODEL-REFS")
            for item in self.feature_model_refs:
                serialized = SerializationHelper.serialize_item(item, "FMFeatureModel")
                if serialized is not None:
                    child_elem = ET.Element("FEATURE-MODEL-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize include_refs (list to container "INCLUDE-REFS")
        if self.include_refs:
            wrapper = ET.Element("INCLUDE-REFS")
            for item in self.include_refs:
                serialized = SerializationHelper.serialize_item(item, "FMFeatureSelectionSet")
                if serialized is not None:
                    child_elem = ET.Element("INCLUDE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize selections (list to container "SELECTIONS")
        if self.selections:
            wrapper = ET.Element("SELECTIONS")
            for item in self.selections:
                serialized = SerializationHelper.serialize_item(item, "FMFeatureSelection")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FMFeatureSelectionSet":
        """Deserialize XML element to FMFeatureSelectionSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FMFeatureSelectionSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FMFeatureSelectionSet, cls).deserialize(element)

        # Parse feature_model_refs (list from container "FEATURE-MODEL-REFS")
        obj.feature_model_refs = []
        container = SerializationHelper.find_child_element(element, "FEATURE-MODEL-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.feature_model_refs.append(child_value)

        # Parse include_refs (list from container "INCLUDE-REFS")
        obj.include_refs = []
        container = SerializationHelper.find_child_element(element, "INCLUDE-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.include_refs.append(child_value)

        # Parse selections (list from container "SELECTIONS")
        obj.selections = []
        container = SerializationHelper.find_child_element(element, "SELECTIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.selections.append(child_value)

        return obj



class FMFeatureSelectionSetBuilder:
    """Builder for FMFeatureSelectionSet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: FMFeatureSelectionSet = FMFeatureSelectionSet()


    def with_short_name(self, value: Identifier) -> "FMFeatureSelectionSetBuilder":
        """Set short_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.short_name = value
        return self

    def with_short_name_fragments(self, items: list[ShortNameFragment]) -> "FMFeatureSelectionSetBuilder":
        """Set short_name_fragments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = list(items) if items else []
        return self

    def with_long_name(self, value: Optional[MultilanguageLongName]) -> "FMFeatureSelectionSetBuilder":
        """Set long_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.long_name = value
        return self

    def with_admin_data(self, value: Optional[AdminData]) -> "FMFeatureSelectionSetBuilder":
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

    def with_annotations(self, items: list[Annotation]) -> "FMFeatureSelectionSetBuilder":
        """Set annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.annotations = list(items) if items else []
        return self

    def with_desc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "FMFeatureSelectionSetBuilder":
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

    def with_category(self, value: Optional[CategoryString]) -> "FMFeatureSelectionSetBuilder":
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

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "FMFeatureSelectionSetBuilder":
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

    def with_uuid(self, value: Optional[String]) -> "FMFeatureSelectionSetBuilder":
        """Set uuid attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.uuid = value
        return self

    def with_feature_models(self, items: list[FMFeatureModel]) -> "FMFeatureSelectionSetBuilder":
        """Set feature_models list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.feature_models = list(items) if items else []
        return self

    def with_includes(self, items: list[FMFeatureSelectionSet]) -> "FMFeatureSelectionSetBuilder":
        """Set includes list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.includes = list(items) if items else []
        return self

    def with_selections(self, items: list[FMFeatureSelection]) -> "FMFeatureSelectionSetBuilder":
        """Set selections list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.selections = list(items) if items else []
        return self


    def add_short_name_fragment(self, item: ShortNameFragment) -> "FMFeatureSelectionSetBuilder":
        """Add a single item to short_name_fragments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments.append(item)
        return self

    def clear_short_name_fragments(self) -> "FMFeatureSelectionSetBuilder":
        """Clear all items from short_name_fragments list.

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = []
        return self

    def add_annotation(self, item: Annotation) -> "FMFeatureSelectionSetBuilder":
        """Add a single item to annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.annotations.append(item)
        return self

    def clear_annotations(self) -> "FMFeatureSelectionSetBuilder":
        """Clear all items from annotations list.

        Returns:
            self for method chaining
        """
        self._obj.annotations = []
        return self

    def add_feature_model(self, item: FMFeatureModel) -> "FMFeatureSelectionSetBuilder":
        """Add a single item to feature_models list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.feature_models.append(item)
        return self

    def clear_feature_models(self) -> "FMFeatureSelectionSetBuilder":
        """Clear all items from feature_models list.

        Returns:
            self for method chaining
        """
        self._obj.feature_models = []
        return self

    def add_include(self, item: FMFeatureSelectionSet) -> "FMFeatureSelectionSetBuilder":
        """Add a single item to includes list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.includes.append(item)
        return self

    def clear_includes(self) -> "FMFeatureSelectionSetBuilder":
        """Clear all items from includes list.

        Returns:
            self for method chaining
        """
        self._obj.includes = []
        return self

    def add_selection(self, item: FMFeatureSelection) -> "FMFeatureSelectionSetBuilder":
        """Add a single item to selections list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.selections.append(item)
        return self

    def clear_selections(self) -> "FMFeatureSelectionSetBuilder":
        """Clear all items from selections list.

        Returns:
            self for method chaining
        """
        self._obj.selections = []
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


    def build(self) -> FMFeatureSelectionSet:
        """Build and return the FMFeatureSelectionSet instance with validation."""
        self._validate_instance()
        pass
        return self._obj