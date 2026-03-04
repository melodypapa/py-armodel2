"""DocumentElementScope AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 97)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchange.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common.spec_element_reference import (
    SpecElementReference,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common.spec_element_reference import SpecElementReferenceBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DocumentElementScope(SpecElementReference):
    """AUTOSAR DocumentElementScope."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DOCUMENT-ELEMENT-SCOPE"


    custom_document_ref: Optional[Any]
    tailoring_refs: list[Any]
    _DESERIALIZE_DISPATCH = {
        "CUSTOM-DOCUMENT-REF": lambda obj, elem: setattr(obj, "custom_document_ref", ARRef.deserialize(elem)),
        "TAILORING-REFS": lambda obj, elem: [obj.tailoring_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
    }


    def __init__(self) -> None:
        """Initialize DocumentElementScope."""
        super().__init__()
        self.custom_document_ref: Optional[Any] = None
        self.tailoring_refs: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize DocumentElementScope to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DocumentElementScope, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize custom_document_ref
        if self.custom_document_ref is not None:
            serialized = SerializationHelper.serialize_item(self.custom_document_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CUSTOM-DOCUMENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tailoring_refs (list to container "TAILORING-REFS")
        if self.tailoring_refs:
            wrapper = ET.Element("TAILORING-REFS")
            for item in self.tailoring_refs:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("TAILORING-REF")
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
    def deserialize(cls, element: ET.Element) -> "DocumentElementScope":
        """Deserialize XML element to DocumentElementScope object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DocumentElementScope object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DocumentElementScope, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CUSTOM-DOCUMENT-REF":
                setattr(obj, "custom_document_ref", ARRef.deserialize(child))
            elif tag == "TAILORING-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.tailoring_refs.append(ARRef.deserialize(item_elem))

        return obj



class DocumentElementScopeBuilder(SpecElementReferenceBuilder):
    """Builder for DocumentElementScope with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DocumentElementScope = DocumentElementScope()


    def with_custom_document(self, value: Optional[any (TraceableElement)]) -> "DocumentElementScopeBuilder":
        """Set custom_document attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.custom_document = value
        return self

    def with_tailorings(self, items: list[any (DataFormatElement)]) -> "DocumentElementScopeBuilder":
        """Set tailorings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.tailorings = list(items) if items else []
        return self


    def add_tailoring(self, item: any (DataFormatElement)) -> "DocumentElementScopeBuilder":
        """Add a single item to tailorings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.tailorings.append(item)
        return self

    def clear_tailorings(self) -> "DocumentElementScopeBuilder":
        """Clear all items from tailorings list.

        Returns:
            self for method chaining
        """
        self._obj.tailorings = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "customDocument",
        "tailoring",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DocumentElementScope:
        """Build and return the DocumentElementScope instance with validation."""
        self._validate_instance()
        return self._obj