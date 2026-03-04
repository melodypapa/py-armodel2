"""TextTableValuePair AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 146)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class TextTableValuePair(ARObject):
    """AUTOSAR TextTableValuePair."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "TEXT-TABLE-VALUE-PAIR"


    first_value: Optional[Numerical]
    second_value: Optional[Numerical]
    _DESERIALIZE_DISPATCH = {
        "FIRST-VALUE": lambda obj, elem: setattr(obj, "first_value", SerializationHelper.deserialize_by_tag(elem, "Numerical")),
        "SECOND-VALUE": lambda obj, elem: setattr(obj, "second_value", SerializationHelper.deserialize_by_tag(elem, "Numerical")),
    }


    def __init__(self) -> None:
        """Initialize TextTableValuePair."""
        super().__init__()
        self.first_value: Optional[Numerical] = None
        self.second_value: Optional[Numerical] = None

    def serialize(self) -> ET.Element:
        """Serialize TextTableValuePair to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TextTableValuePair, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize first_value
        if self.first_value is not None:
            serialized = SerializationHelper.serialize_item(self.first_value, "Numerical")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FIRST-VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize second_value
        if self.second_value is not None:
            serialized = SerializationHelper.serialize_item(self.second_value, "Numerical")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SECOND-VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TextTableValuePair":
        """Deserialize XML element to TextTableValuePair object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TextTableValuePair object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TextTableValuePair, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "FIRST-VALUE":
                setattr(obj, "first_value", SerializationHelper.deserialize_by_tag(child, "Numerical"))
            elif tag == "SECOND-VALUE":
                setattr(obj, "second_value", SerializationHelper.deserialize_by_tag(child, "Numerical"))

        return obj



class TextTableValuePairBuilder(BuilderBase):
    """Builder for TextTableValuePair with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TextTableValuePair = TextTableValuePair()


    def with_first_value(self, value: Optional[Numerical]) -> "TextTableValuePairBuilder":
        """Set first_value attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.first_value = value
        return self

    def with_second_value(self, value: Optional[Numerical]) -> "TextTableValuePairBuilder":
        """Set second_value attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.second_value = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "firstValue",
        "secondValue",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> TextTableValuePair:
        """Build and return the TextTableValuePair instance with validation."""
        self._validate_instance()
        return self._obj