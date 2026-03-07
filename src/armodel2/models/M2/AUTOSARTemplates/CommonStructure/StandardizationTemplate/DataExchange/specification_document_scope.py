"""SpecificationDocumentScope AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 97)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchange.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common.spec_element_reference import (
    SpecElementReference,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common.spec_element_reference import SpecElementReferenceBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchange.document_element_scope import (
    DocumentElementScope,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.DocumentationOnM1.documentation import (
    Documentation,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SpecificationDocumentScope(SpecElementReference):
    """AUTOSAR SpecificationDocumentScope."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SPECIFICATION-DOCUMENT-SCOPE"


    custom_documentation_ref: Optional[ARRef]
    documents: list[DocumentElementScope]
    _DESERIALIZE_DISPATCH = {
        "CUSTOM-DOCUMENTATION-REF": lambda obj, elem: setattr(obj, "custom_documentation_ref", ARRef.deserialize(elem)),
        "DOCUMENTS": lambda obj, elem: obj.documents.append(SerializationHelper.deserialize_by_tag(elem, "DocumentElementScope")),
    }


    def __init__(self) -> None:
        """Initialize SpecificationDocumentScope."""
        super().__init__()
        self.custom_documentation_ref: Optional[ARRef] = None
        self.documents: list[DocumentElementScope] = []

    def serialize(self) -> ET.Element:
        """Serialize SpecificationDocumentScope to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SpecificationDocumentScope, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize custom_documentation_ref
        if self.custom_documentation_ref is not None:
            serialized = SerializationHelper.serialize_item(self.custom_documentation_ref, "Documentation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CUSTOM-DOCUMENTATION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize documents (list to container "DOCUMENTS")
        if self.documents:
            wrapper = ET.Element("DOCUMENTS")
            for item in self.documents:
                serialized = SerializationHelper.serialize_item(item, "DocumentElementScope")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SpecificationDocumentScope":
        """Deserialize XML element to SpecificationDocumentScope object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SpecificationDocumentScope object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SpecificationDocumentScope, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CUSTOM-DOCUMENTATION-REF":
                setattr(obj, "custom_documentation_ref", ARRef.deserialize(child))
            elif tag == "DOCUMENTS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.documents.append(SerializationHelper.deserialize_by_tag(item_elem, "DocumentElementScope"))

        return obj



class SpecificationDocumentScopeBuilder(SpecElementReferenceBuilder):
    """Builder for SpecificationDocumentScope with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SpecificationDocumentScope = SpecificationDocumentScope()


    def with_custom_documentation(self, value: Optional[Documentation]) -> "SpecificationDocumentScopeBuilder":
        """Set custom_documentation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'custom_documentation' is required and cannot be None")
        self._obj.custom_documentation = value
        return self

    def with_documents(self, items: list[DocumentElementScope]) -> "SpecificationDocumentScopeBuilder":
        """Set documents list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.documents = list(items) if items else []
        return self


    def add_document(self, item: DocumentElementScope) -> "SpecificationDocumentScopeBuilder":
        """Add a single item to documents list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.documents.append(item)
        return self

    def clear_documents(self) -> "SpecificationDocumentScopeBuilder":
        """Clear all items from documents list.

        Returns:
            self for method chaining
        """
        self._obj.documents = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "customDocumentation",
        "document",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> SpecificationDocumentScope:
        """Build and return the SpecificationDocumentScope instance with validation."""
        self._validate_instance()
        return self._obj