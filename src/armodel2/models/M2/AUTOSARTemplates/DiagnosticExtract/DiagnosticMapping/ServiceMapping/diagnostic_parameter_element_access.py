"""DiagnosticParameterElementAccess AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 229)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping_ServiceMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_parameter import (
    DiagnosticParameter,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticParameterElementAccess(ARObject):
    """AUTOSAR DiagnosticParameterElementAccess."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-PARAMETER-ELEMENT-ACCESS"


    context_element_refs: list[ARRef]
    target_element_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "CONTEXT-ELEMENTS": lambda obj, elem: obj.context_element_refs.append(ARRef.deserialize(elem)),
        "TARGET-ELEMENT-REF": lambda obj, elem: setattr(obj, "target_element_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticParameterElementAccess."""
        super().__init__()
        self.context_element_refs: list[ARRef] = []
        self.target_element_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticParameterElementAccess to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticParameterElementAccess, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize context_element_refs (list to container "CONTEXT-ELEMENT-REFS")
        if self.context_element_refs:
            wrapper = ET.Element("CONTEXT-ELEMENT-REFS")
            for item in self.context_element_refs:
                serialized = SerializationHelper.serialize_item(item, "DiagnosticParameter")
                if serialized is not None:
                    child_elem = ET.Element("CONTEXT-ELEMENT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize target_element_ref
        if self.target_element_ref is not None:
            serialized = SerializationHelper.serialize_item(self.target_element_ref, "DiagnosticParameter")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-ELEMENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticParameterElementAccess":
        """Deserialize XML element to DiagnosticParameterElementAccess object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticParameterElementAccess object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticParameterElementAccess, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "CONTEXT-ELEMENTS":
                obj.context_element_refs.append(ARRef.deserialize(child))
            elif tag == "TARGET-ELEMENT-REF":
                setattr(obj, "target_element_ref", ARRef.deserialize(child))

        return obj



class DiagnosticParameterElementAccessBuilder(BuilderBase):
    """Builder for DiagnosticParameterElementAccess with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticParameterElementAccess = DiagnosticParameterElementAccess()


    def with_context_elements(self, items: list[DiagnosticParameter]) -> "DiagnosticParameterElementAccessBuilder":
        """Set context_elements list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.context_elements = list(items) if items else []
        return self

    def with_target_element(self, value: Optional[DiagnosticParameter]) -> "DiagnosticParameterElementAccessBuilder":
        """Set target_element attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.target_element = value
        return self


    def add_context_element(self, item: DiagnosticParameter) -> "DiagnosticParameterElementAccessBuilder":
        """Add a single item to context_elements list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.context_elements.append(item)
        return self

    def clear_context_elements(self) -> "DiagnosticParameterElementAccessBuilder":
        """Clear all items from context_elements list.

        Returns:
            self for method chaining
        """
        self._obj.context_elements = []
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


    def build(self) -> DiagnosticParameterElementAccess:
        """Build and return the DiagnosticParameterElementAccess instance with validation."""
        self._validate_instance()
        pass
        return self._obj