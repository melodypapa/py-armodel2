"""PostBuildVariantCriterionValueSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 1000)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 56)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 258)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class PostBuildVariantCriterionValueSet(ARElement):
    """AUTOSAR PostBuildVariantCriterionValueSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "POST-BUILD-VARIANT-CRITERION-VALUE-SET"


    post_build_variants: list[Any]
    _DESERIALIZE_DISPATCH = {
        "POST-BUILD-VARIANTS": lambda obj, elem: obj.post_build_variants.append(SerializationHelper.deserialize_by_tag(elem, "any (PostBuildVariant)")),
    }


    def __init__(self) -> None:
        """Initialize PostBuildVariantCriterionValueSet."""
        super().__init__()
        self.post_build_variants: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize PostBuildVariantCriterionValueSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PostBuildVariantCriterionValueSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize post_build_variants (list to container "POST-BUILD-VARIANTS")
        if self.post_build_variants:
            wrapper = ET.Element("POST-BUILD-VARIANTS")
            for item in self.post_build_variants:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PostBuildVariantCriterionValueSet":
        """Deserialize XML element to PostBuildVariantCriterionValueSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PostBuildVariantCriterionValueSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PostBuildVariantCriterionValueSet, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "POST-BUILD-VARIANTS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.post_build_variants.append(SerializationHelper.deserialize_by_tag(item_elem, "any (PostBuildVariant)"))

        return obj



class PostBuildVariantCriterionValueSetBuilder(ARElementBuilder):
    """Builder for PostBuildVariantCriterionValueSet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: PostBuildVariantCriterionValueSet = PostBuildVariantCriterionValueSet()


    def with_post_build_variants(self, items: list[Any]) -> "PostBuildVariantCriterionValueSetBuilder":
        """Set post_build_variants list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.post_build_variants = list(items) if items else []
        return self


    def add_post_build_variant(self, item: Any) -> "PostBuildVariantCriterionValueSetBuilder":
        """Add a single item to post_build_variants list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.post_build_variants.append(item)
        return self

    def clear_post_build_variants(self) -> "PostBuildVariantCriterionValueSetBuilder":
        """Clear all items from post_build_variants list.

        Returns:
            self for method chaining
        """
        self._obj.post_build_variants = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "postBuildVariant",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> PostBuildVariantCriterionValueSet:
        """Build and return the PostBuildVariantCriterionValueSet instance with validation."""
        self._validate_instance()
        return self._obj