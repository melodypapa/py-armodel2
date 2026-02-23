"""DocumentElementScope AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 97)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchange.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common.spec_element_reference import (
    SpecElementReference,
)
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common.spec_element_reference import SpecElementReferenceBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class DocumentElementScope(SpecElementReference):
    """AUTOSAR DocumentElementScope."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    custom_document_ref: Optional[Any]
    tailoring_refs: list[Any]
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
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

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

        # Parse custom_document_ref
        child = SerializationHelper.find_child_element(element, "CUSTOM-DOCUMENT-REF")
        if child is not None:
            custom_document_ref_value = ARRef.deserialize(child)
            obj.custom_document_ref = custom_document_ref_value

        # Parse tailoring_refs (list from container "TAILORING-REFS")
        obj.tailoring_refs = []
        container = SerializationHelper.find_child_element(element, "TAILORING-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.tailoring_refs.append(child_value)

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


    def build(self) -> DocumentElementScope:
        """Build and return the DocumentElementScope instance with validation."""
        self._validate_instance()
        pass
        return self._obj