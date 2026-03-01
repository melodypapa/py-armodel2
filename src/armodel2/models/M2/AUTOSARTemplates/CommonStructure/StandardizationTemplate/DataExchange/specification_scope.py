"""SpecificationScope AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 96)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchange.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchange.specification_document_scope import (
    SpecificationDocumentScope,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SpecificationScope(ARObject):
    """AUTOSAR SpecificationScope."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SPECIFICATION-SCOPE"


    specification_documents: list[SpecificationDocumentScope]
    _DESERIALIZE_DISPATCH = {
        "SPECIFICATION-DOCUMENTS": lambda obj, elem: obj.specification_documents.append(SerializationHelper.deserialize_by_tag(elem, "SpecificationDocumentScope")),
    }


    def __init__(self) -> None:
        """Initialize SpecificationScope."""
        super().__init__()
        self.specification_documents: list[SpecificationDocumentScope] = []

    def serialize(self) -> ET.Element:
        """Serialize SpecificationScope to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SpecificationScope, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize specification_documents (list to container "SPECIFICATION-DOCUMENTS")
        if self.specification_documents:
            wrapper = ET.Element("SPECIFICATION-DOCUMENTS")
            for item in self.specification_documents:
                serialized = SerializationHelper.serialize_item(item, "SpecificationDocumentScope")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SpecificationScope":
        """Deserialize XML element to SpecificationScope object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SpecificationScope object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SpecificationScope, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "SPECIFICATION-DOCUMENTS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.specification_documents.append(SerializationHelper.deserialize_by_tag(item_elem, "SpecificationDocumentScope"))

        return obj



class SpecificationScopeBuilder(BuilderBase):
    """Builder for SpecificationScope with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SpecificationScope = SpecificationScope()


    def with_specification_documents(self, items: list[SpecificationDocumentScope]) -> "SpecificationScopeBuilder":
        """Set specification_documents list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.specification_documents = list(items) if items else []
        return self


    def add_specification_document(self, item: SpecificationDocumentScope) -> "SpecificationScopeBuilder":
        """Add a single item to specification_documents list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.specification_documents.append(item)
        return self

    def clear_specification_documents(self) -> "SpecificationScopeBuilder":
        """Clear all items from specification_documents list.

        Returns:
            self for method chaining
        """
        self._obj.specification_documents = []
        return self



    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

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


    def build(self) -> SpecificationScope:
        """Build and return the SpecificationScope instance with validation."""
        self._validate_instance()
        pass
        return self._obj