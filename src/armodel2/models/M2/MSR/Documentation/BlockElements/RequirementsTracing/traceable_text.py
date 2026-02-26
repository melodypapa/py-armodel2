"""TraceableText AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 178)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 313)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 222)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_RequirementsTracing.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import PaginateableBuilder

if TYPE_CHECKING:
    from armodel2.models.M2.MSR.Documentation.BlockElements.documentation_block import (
        DocumentationBlock,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class TraceableText(Paginateable):
    """AUTOSAR TraceableText."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    text: DocumentationBlock
    def __init__(self) -> None:
        """Initialize TraceableText."""
        super().__init__()
        self.text: DocumentationBlock = None

    def serialize(self) -> ET.Element:
        """Serialize TraceableText to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TraceableText, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize text (atp_mixed - append children directly)
        if self.text is not None:
            serialized = SerializationHelper.serialize_item(self.text, "DocumentationBlock")
            if serialized is not None:
                # atpMixed type: append children directly without wrapper
                if hasattr(serialized, 'attrib'):
                    elem.attrib.update(serialized.attrib)
                # Only copy text if it's a non-empty string (not None or whitespace)
                if serialized.text and serialized.text.strip():
                    elem.text = serialized.text
                for child in serialized:
                    elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TraceableText":
        """Deserialize XML element to TraceableText object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TraceableText object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TraceableText, cls).deserialize(element)

        # Parse text
        child = SerializationHelper.find_child_element(element, "TEXT")
        if child is not None:
            text_value = SerializationHelper.deserialize_by_tag(child, "DocumentationBlock")
            obj.text = text_value

        return obj



class TraceableTextBuilder(PaginateableBuilder):
    """Builder for TraceableText with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TraceableText = TraceableText()


    def with_text(self, value: DocumentationBlock) -> "TraceableTextBuilder":
        """Set text attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.text = value
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


    def build(self) -> TraceableText:
        """Build and return the TraceableText instance with validation."""
        self._validate_instance()
        pass
        return self._obj