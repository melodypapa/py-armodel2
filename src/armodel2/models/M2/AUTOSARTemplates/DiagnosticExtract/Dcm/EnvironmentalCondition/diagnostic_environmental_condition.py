"""DiagnosticEnvironmentalCondition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 79)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_EnvironmentalCondition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import DiagnosticCommonElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticEnvironmentalCondition(DiagnosticCommonElement):
    """AUTOSAR DiagnosticEnvironmentalCondition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    formula: Optional[Any]
    mode_elements: list[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticEnvironmentalCondition."""
        super().__init__()
        self.formula: Optional[Any] = None
        self.mode_elements: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticEnvironmentalCondition to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticEnvironmentalCondition, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize formula
        if self.formula is not None:
            serialized = SerializationHelper.serialize_item(self.formula, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FORMULA")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mode_elements (list to container "MODE-ELEMENTS")
        if self.mode_elements:
            wrapper = ET.Element("MODE-ELEMENTS")
            for item in self.mode_elements:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEnvironmentalCondition":
        """Deserialize XML element to DiagnosticEnvironmentalCondition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticEnvironmentalCondition object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticEnvironmentalCondition, cls).deserialize(element)

        # Parse formula
        child = SerializationHelper.find_child_element(element, "FORMULA")
        if child is not None:
            formula_value = child.text
            obj.formula = formula_value

        # Parse mode_elements (list from container "MODE-ELEMENTS")
        obj.mode_elements = []
        container = SerializationHelper.find_child_element(element, "MODE-ELEMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mode_elements.append(child_value)

        return obj



class DiagnosticEnvironmentalConditionBuilder(DiagnosticCommonElementBuilder):
    """Builder for DiagnosticEnvironmentalCondition with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticEnvironmentalCondition = DiagnosticEnvironmentalCondition()


    def with_formula(self, value: Optional[any (DiagnosticEnvCondition)]) -> "DiagnosticEnvironmentalConditionBuilder":
        """Set formula attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.formula = value
        return self

    def with_mode_elements(self, items: list[any (DiagnosticEnvMode)]) -> "DiagnosticEnvironmentalConditionBuilder":
        """Set mode_elements list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.mode_elements = list(items) if items else []
        return self


    def add_mode_element(self, item: any (DiagnosticEnvMode)) -> "DiagnosticEnvironmentalConditionBuilder":
        """Add a single item to mode_elements list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.mode_elements.append(item)
        return self

    def clear_mode_elements(self) -> "DiagnosticEnvironmentalConditionBuilder":
        """Clear all items from mode_elements list.

        Returns:
            self for method chaining
        """
        self._obj.mode_elements = []
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


    def build(self) -> DiagnosticEnvironmentalCondition:
        """Build and return the DiagnosticEnvironmentalCondition instance with validation."""
        self._validate_instance()
        pass
        return self._obj