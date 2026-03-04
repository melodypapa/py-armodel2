"""IndexedArrayElement AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 237)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DataMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class IndexedArrayElement(ARObject):
    """AUTOSAR IndexedArrayElement."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "INDEXED-ARRAY-ELEMENT"


    application_array_ref: Optional[Any]
    implementation_ref: Optional[Any]
    index: Optional[Integer]
    _DESERIALIZE_DISPATCH = {
        "APPLICATION-ARRAY-REF": lambda obj, elem: setattr(obj, "application_array_ref", ARRef.deserialize(elem)),
        "IMPLEMENTATION-REF": lambda obj, elem: setattr(obj, "implementation_ref", ARRef.deserialize(elem)),
        "INDEX": lambda obj, elem: setattr(obj, "index", SerializationHelper.deserialize_by_tag(elem, "Integer")),
    }


    def __init__(self) -> None:
        """Initialize IndexedArrayElement."""
        super().__init__()
        self.application_array_ref: Optional[Any] = None
        self.implementation_ref: Optional[Any] = None
        self.index: Optional[Integer] = None

    def serialize(self) -> ET.Element:
        """Serialize IndexedArrayElement to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IndexedArrayElement, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize application_array_ref
        if self.application_array_ref is not None:
            serialized = SerializationHelper.serialize_item(self.application_array_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("APPLICATION-ARRAY-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize implementation_ref
        if self.implementation_ref is not None:
            serialized = SerializationHelper.serialize_item(self.implementation_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IMPLEMENTATION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize index
        if self.index is not None:
            serialized = SerializationHelper.serialize_item(self.index, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INDEX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IndexedArrayElement":
        """Deserialize XML element to IndexedArrayElement object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IndexedArrayElement object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IndexedArrayElement, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "APPLICATION-ARRAY-REF":
                setattr(obj, "application_array_ref", ARRef.deserialize(child))
            elif tag == "IMPLEMENTATION-REF":
                setattr(obj, "implementation_ref", ARRef.deserialize(child))
            elif tag == "INDEX":
                setattr(obj, "index", SerializationHelper.deserialize_by_tag(child, "Integer"))

        return obj



class IndexedArrayElementBuilder(BuilderBase):
    """Builder for IndexedArrayElement with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: IndexedArrayElement = IndexedArrayElement()


    def with_application_array(self, value: Optional[any (ApplicationArray)]) -> "IndexedArrayElementBuilder":
        """Set application_array attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.application_array = value
        return self

    def with_implementation(self, value: Optional[any (ImplementationData)]) -> "IndexedArrayElementBuilder":
        """Set implementation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.implementation = value
        return self

    def with_index(self, value: Optional[Integer]) -> "IndexedArrayElementBuilder":
        """Set index attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.index = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "applicationArray",
        "implementation",
        "index",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> IndexedArrayElement:
        """Build and return the IndexedArrayElement instance with validation."""
        self._validate_instance()
        return self._obj