"""DiagnosticRoutine AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 124)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_CommonDiagnostics.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import DiagnosticCommonElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_start_routine import (
    DiagnosticStartRoutine,
)
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_stop_routine import (
    DiagnosticStopRoutine,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticRoutine(DiagnosticCommonElement):
    """AUTOSAR DiagnosticRoutine."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    id: Optional[PositiveInteger]
    request_result: Optional[Any]
    routine_info: Optional[PositiveInteger]
    start: Optional[DiagnosticStartRoutine]
    stop: Optional[DiagnosticStopRoutine]
    def __init__(self) -> None:
        """Initialize DiagnosticRoutine."""
        super().__init__()
        self.id: Optional[PositiveInteger] = None
        self.request_result: Optional[Any] = None
        self.routine_info: Optional[PositiveInteger] = None
        self.start: Optional[DiagnosticStartRoutine] = None
        self.stop: Optional[DiagnosticStopRoutine] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticRoutine to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticRoutine, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize id
        if self.id is not None:
            serialized = SerializationHelper.serialize_item(self.id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize request_result
        if self.request_result is not None:
            serialized = SerializationHelper.serialize_item(self.request_result, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REQUEST-RESULT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize routine_info
        if self.routine_info is not None:
            serialized = SerializationHelper.serialize_item(self.routine_info, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ROUTINE-INFO")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize start
        if self.start is not None:
            serialized = SerializationHelper.serialize_item(self.start, "DiagnosticStartRoutine")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("START")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize stop
        if self.stop is not None:
            serialized = SerializationHelper.serialize_item(self.stop, "DiagnosticStopRoutine")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("STOP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticRoutine":
        """Deserialize XML element to DiagnosticRoutine object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticRoutine object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticRoutine, cls).deserialize(element)

        # Parse id
        child = SerializationHelper.find_child_element(element, "ID")
        if child is not None:
            id_value = child.text
            obj.id = id_value

        # Parse request_result
        child = SerializationHelper.find_child_element(element, "REQUEST-RESULT")
        if child is not None:
            request_result_value = child.text
            obj.request_result = request_result_value

        # Parse routine_info
        child = SerializationHelper.find_child_element(element, "ROUTINE-INFO")
        if child is not None:
            routine_info_value = child.text
            obj.routine_info = routine_info_value

        # Parse start
        child = SerializationHelper.find_child_element(element, "START")
        if child is not None:
            start_value = SerializationHelper.deserialize_by_tag(child, "DiagnosticStartRoutine")
            obj.start = start_value

        # Parse stop
        child = SerializationHelper.find_child_element(element, "STOP")
        if child is not None:
            stop_value = SerializationHelper.deserialize_by_tag(child, "DiagnosticStopRoutine")
            obj.stop = stop_value

        return obj



class DiagnosticRoutineBuilder(DiagnosticCommonElementBuilder):
    """Builder for DiagnosticRoutine with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticRoutine = DiagnosticRoutine()


    def with_id(self, value: Optional[PositiveInteger]) -> "DiagnosticRoutineBuilder":
        """Set id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.id = value
        return self

    def with_request_result(self, value: Optional[any (DiagnosticRequest)]) -> "DiagnosticRoutineBuilder":
        """Set request_result attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.request_result = value
        return self

    def with_routine_info(self, value: Optional[PositiveInteger]) -> "DiagnosticRoutineBuilder":
        """Set routine_info attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.routine_info = value
        return self

    def with_start(self, value: Optional[DiagnosticStartRoutine]) -> "DiagnosticRoutineBuilder":
        """Set start attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.start = value
        return self

    def with_stop(self, value: Optional[DiagnosticStopRoutine]) -> "DiagnosticRoutineBuilder":
        """Set stop attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.stop = value
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


    def build(self) -> DiagnosticRoutine:
        """Build and return the DiagnosticRoutine instance with validation."""
        self._validate_instance()
        pass
        return self._obj