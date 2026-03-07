"""TagWithOptionalValue AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 477)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 166)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_TagWithOptionalValue.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    String,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class TagWithOptionalValue(ARObject):
    """AUTOSAR TagWithOptionalValue."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "TAG-WITH-OPTIONAL-VALUE"


    key: Optional[String]
    sequence_offset: Optional[Integer]
    value: Optional[String]
    _DESERIALIZE_DISPATCH = {
        "KEY": lambda obj, elem: setattr(obj, "key", SerializationHelper.deserialize_by_tag(elem, "String")),
        "SEQUENCE-OFFSET": lambda obj, elem: setattr(obj, "sequence_offset", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "VALUE": lambda obj, elem: setattr(obj, "value", SerializationHelper.deserialize_by_tag(elem, "String")),
    }


    def __init__(self) -> None:
        """Initialize TagWithOptionalValue."""
        super().__init__()
        self.key: Optional[String] = None
        self.sequence_offset: Optional[Integer] = None
        self.value: Optional[String] = None

    def serialize(self) -> ET.Element:
        """Serialize TagWithOptionalValue to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TagWithOptionalValue, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize key
        if self.key is not None:
            serialized = SerializationHelper.serialize_item(self.key, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("KEY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sequence_offset
        if self.sequence_offset is not None:
            serialized = SerializationHelper.serialize_item(self.sequence_offset, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SEQUENCE-OFFSET")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize value
        if self.value is not None:
            serialized = SerializationHelper.serialize_item(self.value, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TagWithOptionalValue":
        """Deserialize XML element to TagWithOptionalValue object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TagWithOptionalValue object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TagWithOptionalValue, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "KEY":
                setattr(obj, "key", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "SEQUENCE-OFFSET":
                setattr(obj, "sequence_offset", SerializationHelper.deserialize_by_tag(child, "Integer"))
            elif tag == "VALUE":
                setattr(obj, "value", SerializationHelper.deserialize_by_tag(child, "String"))

        return obj



class TagWithOptionalValueBuilder(BuilderBase):
    """Builder for TagWithOptionalValue with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TagWithOptionalValue = TagWithOptionalValue()


    def with_key(self, value: Optional[String]) -> "TagWithOptionalValueBuilder":
        """Set key attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'key' is required and cannot be None")
        self._obj.key = value
        return self

    def with_sequence_offset(self, value: Optional[Integer]) -> "TagWithOptionalValueBuilder":
        """Set sequence_offset attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'sequence_offset' is required and cannot be None")
        self._obj.sequence_offset = value
        return self

    def with_value(self, value: Optional[String]) -> "TagWithOptionalValueBuilder":
        """Set value attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'value' is required and cannot be None")
        self._obj.value = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "key",
        "sequenceOffset",
        "value",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> TagWithOptionalValue:
        """Build and return the TagWithOptionalValue instance with validation."""
        self._validate_instance()
        return self._obj