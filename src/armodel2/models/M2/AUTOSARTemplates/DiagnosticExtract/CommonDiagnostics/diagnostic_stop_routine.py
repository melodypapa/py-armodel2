"""DiagnosticStopRoutine AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 125)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_CommonDiagnostics.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_routine_subfunction import (
    DiagnosticRoutineSubfunction,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_routine_subfunction import DiagnosticRoutineSubfunctionBuilder
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_parameter import (
    DiagnosticParameter,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticStopRoutine(DiagnosticRoutineSubfunction):
    """AUTOSAR DiagnosticStopRoutine."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    requests: list[DiagnosticParameter]
    responses: list[DiagnosticParameter]
    def __init__(self) -> None:
        """Initialize DiagnosticStopRoutine."""
        super().__init__()
        self.requests: list[DiagnosticParameter] = []
        self.responses: list[DiagnosticParameter] = []

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticStopRoutine to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticStopRoutine, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize requests (list to container "REQUESTS")
        if self.requests:
            wrapper = ET.Element("REQUESTS")
            for item in self.requests:
                serialized = SerializationHelper.serialize_item(item, "DiagnosticParameter")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize responses (list to container "RESPONSES")
        if self.responses:
            wrapper = ET.Element("RESPONSES")
            for item in self.responses:
                serialized = SerializationHelper.serialize_item(item, "DiagnosticParameter")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticStopRoutine":
        """Deserialize XML element to DiagnosticStopRoutine object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticStopRoutine object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticStopRoutine, cls).deserialize(element)

        # Parse requests (list from container "REQUESTS")
        obj.requests = []
        container = SerializationHelper.find_child_element(element, "REQUESTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.requests.append(child_value)

        # Parse responses (list from container "RESPONSES")
        obj.responses = []
        container = SerializationHelper.find_child_element(element, "RESPONSES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.responses.append(child_value)

        return obj



class DiagnosticStopRoutineBuilder(DiagnosticRoutineSubfunctionBuilder):
    """Builder for DiagnosticStopRoutine with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticStopRoutine = DiagnosticStopRoutine()


    def with_requests(self, items: list[DiagnosticParameter]) -> "DiagnosticStopRoutineBuilder":
        """Set requests list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.requests = list(items) if items else []
        return self

    def with_responses(self, items: list[DiagnosticParameter]) -> "DiagnosticStopRoutineBuilder":
        """Set responses list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.responses = list(items) if items else []
        return self


    def add_request(self, item: DiagnosticParameter) -> "DiagnosticStopRoutineBuilder":
        """Add a single item to requests list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.requests.append(item)
        return self

    def clear_requests(self) -> "DiagnosticStopRoutineBuilder":
        """Clear all items from requests list.

        Returns:
            self for method chaining
        """
        self._obj.requests = []
        return self

    def add_respons(self, item: DiagnosticParameter) -> "DiagnosticStopRoutineBuilder":
        """Add a single item to responses list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.responses.append(item)
        return self

    def clear_responses(self) -> "DiagnosticStopRoutineBuilder":
        """Clear all items from responses list.

        Returns:
            self for method chaining
        """
        self._obj.responses = []
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


    def build(self) -> DiagnosticStopRoutine:
        """Build and return the DiagnosticStopRoutine instance with validation."""
        self._validate_instance()
        pass
        return self._obj