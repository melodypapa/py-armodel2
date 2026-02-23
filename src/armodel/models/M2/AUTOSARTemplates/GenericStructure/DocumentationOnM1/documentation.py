"""Documentation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 294)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 439)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 181)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_DocumentationOnM1.classes.json"""

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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.DocumentationOnM1.documentation_context import (
    DocumentationContext,
)
from armodel.models.M2.MSR.Documentation.Chapters.predefined_chapter import (
    PredefinedChapter,
)


class Documentation(ARElement):
    """AUTOSAR Documentation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    contexts: list[DocumentationContext]
    documentation: Optional[PredefinedChapter]
    def __init__(self) -> None:
        """Initialize Documentation."""
        super().__init__()
        self.contexts: list[DocumentationContext] = []
        self.documentation: Optional[PredefinedChapter] = None

    def serialize(self) -> ET.Element:
        """Serialize Documentation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Documentation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize contexts (list to container "CONTEXTS")
        if self.contexts:
            wrapper = ET.Element("CONTEXTS")
            for item in self.contexts:
                serialized = SerializationHelper.serialize_item(item, "DocumentationContext")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize documentation
        if self.documentation is not None:
            serialized = SerializationHelper.serialize_item(self.documentation, "PredefinedChapter")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DOCUMENTATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Documentation":
        """Deserialize XML element to Documentation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Documentation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Documentation, cls).deserialize(element)

        # Parse contexts (list from container "CONTEXTS")
        obj.contexts = []
        container = SerializationHelper.find_child_element(element, "CONTEXTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.contexts.append(child_value)

        # Parse documentation
        child = SerializationHelper.find_child_element(element, "DOCUMENTATION")
        if child is not None:
            documentation_value = SerializationHelper.deserialize_by_tag(child, "PredefinedChapter")
            obj.documentation = documentation_value

        return obj



class DocumentationBuilder(ARElementBuilder):
    """Builder for Documentation with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: Documentation = Documentation()


    def with_contexts(self, items: list[DocumentationContext]) -> "DocumentationBuilder":
        """Set contexts list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.contexts = list(items) if items else []
        return self

    def with_documentation(self, value: Optional[PredefinedChapter]) -> "DocumentationBuilder":
        """Set documentation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.documentation = value
        return self


    def add_context(self, item: DocumentationContext) -> "DocumentationBuilder":
        """Add a single item to contexts list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.contexts.append(item)
        return self

    def clear_contexts(self) -> "DocumentationBuilder":
        """Clear all items from contexts list.

        Returns:
            self for method chaining
        """
        self._obj.contexts = []
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


    def build(self) -> Documentation:
        """Build and return the Documentation instance with validation."""
        self._validate_instance()
        pass
        return self._obj