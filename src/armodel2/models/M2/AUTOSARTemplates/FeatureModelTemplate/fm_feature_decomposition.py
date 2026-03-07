"""FMFeatureDecomposition AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 27)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_FeatureModelTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CategoryString,
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature import (
    FMFeature,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class FMFeatureDecomposition(ARObject):
    """AUTOSAR FMFeatureDecomposition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "F-M-FEATURE-DECOMPOSITION"


    category: Optional[CategoryString]
    feature_refs: list[ARRef]
    max: Optional[PositiveInteger]
    min: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "CATEGORY": lambda obj, elem: setattr(obj, "category", SerializationHelper.deserialize_by_tag(elem, "CategoryString")),
        "FEATURE-REFS": lambda obj, elem: [obj.feature_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "MAX": lambda obj, elem: setattr(obj, "max", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "MIN": lambda obj, elem: setattr(obj, "min", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize FMFeatureDecomposition."""
        super().__init__()
        self.category: Optional[CategoryString] = None
        self.feature_refs: list[ARRef] = []
        self.max: Optional[PositiveInteger] = None
        self.min: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize FMFeatureDecomposition to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FMFeatureDecomposition, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize category
        if self.category is not None:
            serialized = SerializationHelper.serialize_item(self.category, "CategoryString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CATEGORY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize feature_refs (list to container "FEATURE-REFS")
        if self.feature_refs:
            wrapper = ET.Element("FEATURE-REFS")
            for item in self.feature_refs:
                serialized = SerializationHelper.serialize_item(item, "FMFeature")
                if serialized is not None:
                    child_elem = ET.Element("FEATURE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize max
        if self.max is not None:
            serialized = SerializationHelper.serialize_item(self.max, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize min
        if self.min is not None:
            serialized = SerializationHelper.serialize_item(self.min, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MIN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FMFeatureDecomposition":
        """Deserialize XML element to FMFeatureDecomposition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FMFeatureDecomposition object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FMFeatureDecomposition, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CATEGORY":
                setattr(obj, "category", SerializationHelper.deserialize_by_tag(child, "CategoryString"))
            elif tag == "FEATURE-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.feature_refs.append(ARRef.deserialize(item_elem))
            elif tag == "MAX":
                setattr(obj, "max", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "MIN":
                setattr(obj, "min", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class FMFeatureDecompositionBuilder(BuilderBase):
    """Builder for FMFeatureDecomposition with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: FMFeatureDecomposition = FMFeatureDecomposition()


    def with_category(self, value: Optional[CategoryString]) -> "FMFeatureDecompositionBuilder":
        """Set category attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'category' is required and cannot be None")
        self._obj.category = value
        return self

    def with_features(self, items: list[FMFeature]) -> "FMFeatureDecompositionBuilder":
        """Set features list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.features = list(items) if items else []
        return self

    def with_max(self, value: Optional[PositiveInteger]) -> "FMFeatureDecompositionBuilder":
        """Set max attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'max' is required and cannot be None")
        self._obj.max = value
        return self

    def with_min(self, value: Optional[PositiveInteger]) -> "FMFeatureDecompositionBuilder":
        """Set min attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'min' is required and cannot be None")
        self._obj.min = value
        return self


    def add_feature(self, item: FMFeature) -> "FMFeatureDecompositionBuilder":
        """Add a single item to features list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.features.append(item)
        return self

    def clear_features(self) -> "FMFeatureDecompositionBuilder":
        """Clear all items from features list.

        Returns:
            self for method chaining
        """
        self._obj.features = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "category",
        "feature",
        "max",
        "min",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> FMFeatureDecomposition:
        """Build and return the FMFeatureDecomposition instance with validation."""
        self._validate_instance()
        return self._obj