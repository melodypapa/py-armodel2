"""KeywordSet AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 194)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_Keyword.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.Keyword.keyword import (
    Keyword,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class KeywordSet(ARElement):
    """AUTOSAR KeywordSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "KEYWORD-SET"


    keywords: list[Keyword]
    _DESERIALIZE_DISPATCH = {
        "KEYWORDS": lambda obj, elem: obj.keywords.append(SerializationHelper.deserialize_by_tag(elem, "Keyword")),
    }


    def __init__(self) -> None:
        """Initialize KeywordSet."""
        super().__init__()
        self.keywords: list[Keyword] = []

    def serialize(self) -> ET.Element:
        """Serialize KeywordSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(KeywordSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize keywords (list to container "KEYWORDS")
        if self.keywords:
            wrapper = ET.Element("KEYWORDS")
            for item in self.keywords:
                serialized = SerializationHelper.serialize_item(item, "Keyword")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "KeywordSet":
        """Deserialize XML element to KeywordSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized KeywordSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(KeywordSet, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "KEYWORDS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.keywords.append(SerializationHelper.deserialize_by_tag(item_elem, "Keyword"))

        return obj



class KeywordSetBuilder(ARElementBuilder):
    """Builder for KeywordSet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: KeywordSet = KeywordSet()


    def with_keywords(self, items: list[Keyword]) -> "KeywordSetBuilder":
        """Set keywords list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.keywords = list(items) if items else []
        return self


    def add_keyword(self, item: Keyword) -> "KeywordSetBuilder":
        """Add a single item to keywords list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.keywords.append(item)
        return self

    def clear_keywords(self) -> "KeywordSetBuilder":
        """Clear all items from keywords list.

        Returns:
            self for method chaining
        """
        self._obj.keywords = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "keyword",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> KeywordSet:
        """Build and return the KeywordSet instance with validation."""
        self._validate_instance()
        return self._obj