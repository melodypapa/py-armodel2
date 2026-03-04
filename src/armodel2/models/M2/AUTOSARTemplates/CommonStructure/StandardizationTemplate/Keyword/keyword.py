"""Keyword AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 454)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 194)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_Keyword.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class Keyword(Identifiable):
    """AUTOSAR Keyword."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "KEYWORD"


    abbr_name: NameToken
    classifications: list[NameToken]
    _DESERIALIZE_DISPATCH = {
        "ABBR-NAME": lambda obj, elem: setattr(obj, "abbr_name", SerializationHelper.deserialize_by_tag(elem, "NameToken")),
        "CLASSIFICATIONS": lambda obj, elem: obj.classifications.append(SerializationHelper.deserialize_by_tag(elem, "NameToken")),
    }


    def __init__(self) -> None:
        """Initialize Keyword."""
        super().__init__()
        self.abbr_name: NameToken = None
        self.classifications: list[NameToken] = []

    def serialize(self) -> ET.Element:
        """Serialize Keyword to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Keyword, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize abbr_name
        if self.abbr_name is not None:
            serialized = SerializationHelper.serialize_item(self.abbr_name, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ABBR-NAME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize classifications (list to container "CLASSIFICATIONS")
        if self.classifications:
            wrapper = ET.Element("CLASSIFICATIONS")
            for item in self.classifications:
                serialized = SerializationHelper.serialize_item(item, "NameToken")
                if serialized is not None:
                    child_elem = ET.Element("CLASSIFICATION")
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
    def deserialize(cls, element: ET.Element) -> "Keyword":
        """Deserialize XML element to Keyword object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Keyword object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Keyword, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ABBR-NAME":
                setattr(obj, "abbr_name", SerializationHelper.deserialize_by_tag(child, "NameToken"))
            elif tag == "CLASSIFICATIONS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.classifications.append(SerializationHelper.deserialize_by_tag(item_elem, "NameToken"))

        return obj



class KeywordBuilder(IdentifiableBuilder):
    """Builder for Keyword with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: Keyword = Keyword()


    def with_abbr_name(self, value: NameToken) -> "KeywordBuilder":
        """Set abbr_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.abbr_name = value
        return self

    def with_classifications(self, items: list[NameToken]) -> "KeywordBuilder":
        """Set classifications list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.classifications = list(items) if items else []
        return self


    def add_classification(self, item: NameToken) -> "KeywordBuilder":
        """Add a single item to classifications list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.classifications.append(item)
        return self

    def clear_classifications(self) -> "KeywordBuilder":
        """Clear all items from classifications list.

        Returns:
            self for method chaining
        """
        self._obj.classifications = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "abbrName",
    }
    _OPTIONAL_ATTRIBUTES = {
        "classification",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Validate required attributes using pre-computed constants (O(1) lookup)
        # This is much faster than calling get_type_hints() at runtime
        if getattr(self._obj, "abbrName", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'abbrName' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'abbrName' is None", UserWarning)


    def build(self) -> Keyword:
        """Build and return the Keyword instance with validation."""
        self._validate_instance()
        return self._obj