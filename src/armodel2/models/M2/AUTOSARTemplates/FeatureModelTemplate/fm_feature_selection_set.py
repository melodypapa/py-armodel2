"""FMFeatureSelectionSet AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 44)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_FeatureModelTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature_model import (
    FMFeatureModel,
)
from armodel2.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature_selection import (
    FMFeatureSelection,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class FMFeatureSelectionSet(ARElement):
    """AUTOSAR FMFeatureSelectionSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "F-M-FEATURE-SELECTION-SET"


    feature_model_refs: list[ARRef]
    include_refs: list[ARRef]
    selections: list[FMFeatureSelection]
    _DESERIALIZE_DISPATCH = {
        "FEATURE-MODELS": lambda obj, elem: obj.feature_model_refs.append(ARRef.deserialize(elem)),
        "INCLUDES": lambda obj, elem: obj.include_refs.append(ARRef.deserialize(elem)),
        "SELECTIONS": lambda obj, elem: obj.selections.append(SerializationHelper.deserialize_by_tag(elem, "FMFeatureSelection")),
    }


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
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "FEATURE-MODELS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.feature_model_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "FMFeatureModel"))
            elif tag == "INCLUDES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.include_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "FMFeatureSelectionSet"))
            elif tag == "SELECTIONS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.selections.append(SerializationHelper.deserialize_by_tag(item_elem, "FMFeatureSelection"))

        return obj



class FMFeatureSelectionSetBuilder(ARElementBuilder):
    """Builder for FMFeatureSelectionSet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: FMFeatureSelectionSet = FMFeatureSelectionSet()


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


    def build(self) -> FMFeatureSelectionSet:
        """Build and return the FMFeatureSelectionSet instance with validation."""
        self._validate_instance()
        pass
        return self._obj