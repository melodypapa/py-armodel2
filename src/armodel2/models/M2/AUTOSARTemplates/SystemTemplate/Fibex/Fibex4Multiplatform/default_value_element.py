"""DefaultValueElement AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 841)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Multiplatform.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DefaultValueElement(ARObject):
    """AUTOSAR DefaultValueElement."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DEFAULT-VALUE-ELEMENT"


    element_byte_value: Optional[Integer]
    element_position: Optional[Integer]
    _DESERIALIZE_DISPATCH = {
        "ELEMENT-BYTE-VALUE": lambda obj, elem: setattr(obj, "element_byte_value", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "ELEMENT-POSITION": lambda obj, elem: setattr(obj, "element_position", SerializationHelper.deserialize_by_tag(elem, "Integer")),
    }


    def __init__(self) -> None:
        """Initialize DefaultValueElement."""
        super().__init__()
        self.element_byte_value: Optional[Integer] = None
        self.element_position: Optional[Integer] = None

    def serialize(self) -> ET.Element:
        """Serialize DefaultValueElement to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DefaultValueElement, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize element_byte_value
        if self.element_byte_value is not None:
            serialized = SerializationHelper.serialize_item(self.element_byte_value, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ELEMENT-BYTE-VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize element_position
        if self.element_position is not None:
            serialized = SerializationHelper.serialize_item(self.element_position, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ELEMENT-POSITION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DefaultValueElement":
        """Deserialize XML element to DefaultValueElement object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DefaultValueElement object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DefaultValueElement, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ELEMENT-BYTE-VALUE":
                setattr(obj, "element_byte_value", SerializationHelper.deserialize_by_tag(child, "Integer"))
            elif tag == "ELEMENT-POSITION":
                setattr(obj, "element_position", SerializationHelper.deserialize_by_tag(child, "Integer"))

        return obj



class DefaultValueElementBuilder(BuilderBase):
    """Builder for DefaultValueElement with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DefaultValueElement = DefaultValueElement()


    def with_element_byte_value(self, value: Optional[Integer]) -> "DefaultValueElementBuilder":
        """Set element_byte_value attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.element_byte_value = value
        return self

    def with_element_position(self, value: Optional[Integer]) -> "DefaultValueElementBuilder":
        """Set element_position attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.element_position = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "elementByteValue",
        "elementPosition",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DefaultValueElement:
        """Build and return the DefaultValueElement instance with validation."""
        self._validate_instance()
        return self._obj