"""KeywordSet AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 194)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_Keyword.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.Keyword.keyword import (
    Keyword,
)


class KeywordSet(ARElement):
    """AUTOSAR KeywordSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    keywords: list[Keyword]
    def __init__(self) -> None:
        """Initialize KeywordSet."""
        super().__init__()
        self.keywords: list[Keyword] = []

    def serialize(self) -> ET.Element:
        """Serialize KeywordSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

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

        # Parse keywords (list from container "KEYWORDS")
        obj.keywords = []
        container = SerializationHelper.find_child_element(element, "KEYWORDS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.keywords.append(child_value)

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


    def build(self) -> KeywordSet:
        """Build and return the KeywordSet instance with validation."""
        self._validate_instance()
        pass
        return self._obj