"""DiagnosticFunctionIdentifierInhibit AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 215)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Fim.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import DiagnosticCommonElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Fim import (
    DiagnosticInhibitionMaskEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticFunctionIdentifierInhibit(DiagnosticCommonElement):
    """AUTOSAR DiagnosticFunctionIdentifierInhibit."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-FUNCTION-IDENTIFIER-INHIBIT"


    function_ref: Optional[Any]
    inhibition_mask: Optional[DiagnosticInhibitionMaskEnum]
    inhibit_sources: list[Any]
    _DESERIALIZE_DISPATCH = {
        "FUNCTION-REF": lambda obj, elem: setattr(obj, "function_ref", ARRef.deserialize(elem)),
        "INHIBITION-MASK": lambda obj, elem: setattr(obj, "inhibition_mask", DiagnosticInhibitionMaskEnum.deserialize(elem)),
        "INHIBIT-SOURCES": lambda obj, elem: obj.inhibit_sources.append(any (DiagnosticFunction).deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticFunctionIdentifierInhibit."""
        super().__init__()
        self.function_ref: Optional[Any] = None
        self.inhibition_mask: Optional[DiagnosticInhibitionMaskEnum] = None
        self.inhibit_sources: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticFunctionIdentifierInhibit to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticFunctionIdentifierInhibit, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize function_ref
        if self.function_ref is not None:
            serialized = SerializationHelper.serialize_item(self.function_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FUNCTION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize inhibition_mask
        if self.inhibition_mask is not None:
            serialized = SerializationHelper.serialize_item(self.inhibition_mask, "DiagnosticInhibitionMaskEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INHIBITION-MASK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize inhibit_sources (list to container "INHIBIT-SOURCES")
        if self.inhibit_sources:
            wrapper = ET.Element("INHIBIT-SOURCES")
            for item in self.inhibit_sources:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticFunctionIdentifierInhibit":
        """Deserialize XML element to DiagnosticFunctionIdentifierInhibit object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticFunctionIdentifierInhibit object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticFunctionIdentifierInhibit, cls).deserialize(element)

        # Parse function_ref
        child = SerializationHelper.find_child_element(element, "FUNCTION-REF")
        if child is not None:
            function_ref_value = ARRef.deserialize(child)
            obj.function_ref = function_ref_value

        # Parse inhibition_mask
        child = SerializationHelper.find_child_element(element, "INHIBITION-MASK")
        if child is not None:
            inhibition_mask_value = DiagnosticInhibitionMaskEnum.deserialize(child)
            obj.inhibition_mask = inhibition_mask_value

        # Parse inhibit_sources (list from container "INHIBIT-SOURCES")
        obj.inhibit_sources = []
        container = SerializationHelper.find_child_element(element, "INHIBIT-SOURCES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.inhibit_sources.append(child_value)

        return obj



class DiagnosticFunctionIdentifierInhibitBuilder(DiagnosticCommonElementBuilder):
    """Builder for DiagnosticFunctionIdentifierInhibit with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticFunctionIdentifierInhibit = DiagnosticFunctionIdentifierInhibit()


    def with_function(self, value: Optional[any (DiagnosticFunction)]) -> "DiagnosticFunctionIdentifierInhibitBuilder":
        """Set function attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.function = value
        return self

    def with_inhibition_mask(self, value: Optional[DiagnosticInhibitionMaskEnum]) -> "DiagnosticFunctionIdentifierInhibitBuilder":
        """Set inhibition_mask attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.inhibition_mask = value
        return self

    def with_inhibit_sources(self, items: list[any (DiagnosticFunction)]) -> "DiagnosticFunctionIdentifierInhibitBuilder":
        """Set inhibit_sources list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.inhibit_sources = list(items) if items else []
        return self


    def add_inhibit_source(self, item: any (DiagnosticFunction)) -> "DiagnosticFunctionIdentifierInhibitBuilder":
        """Add a single item to inhibit_sources list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.inhibit_sources.append(item)
        return self

    def clear_inhibit_sources(self) -> "DiagnosticFunctionIdentifierInhibitBuilder":
        """Clear all items from inhibit_sources list.

        Returns:
            self for method chaining
        """
        self._obj.inhibit_sources = []
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


    def build(self) -> DiagnosticFunctionIdentifierInhibit:
        """Build and return the DiagnosticFunctionIdentifierInhibit instance with validation."""
        self._validate_instance()
        pass
        return self._obj