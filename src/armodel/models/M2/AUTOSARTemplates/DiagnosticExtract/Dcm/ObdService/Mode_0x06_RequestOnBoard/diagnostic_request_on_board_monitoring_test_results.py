"""DiagnosticRequestOnBoardMonitoringTestResults AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 156)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_ObdService_Mode_0x06_RequestOnBoard.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTestResult.diagnostic_test_result import (
    DiagnosticTestResult,
)


class DiagnosticRequestOnBoardMonitoringTestResults(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticRequestOnBoardMonitoringTestResults."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    diagnostic_test_result_refs: list[ARRef]
    request_on_ref: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticRequestOnBoardMonitoringTestResults."""
        super().__init__()
        self.diagnostic_test_result_refs: list[ARRef] = []
        self.request_on_ref: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticRequestOnBoardMonitoringTestResults to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticRequestOnBoardMonitoringTestResults, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize diagnostic_test_result_refs (list to container "DIAGNOSTIC-TEST-RESULT-REFS")
        if self.diagnostic_test_result_refs:
            wrapper = ET.Element("DIAGNOSTIC-TEST-RESULT-REFS")
            for item in self.diagnostic_test_result_refs:
                serialized = SerializationHelper.serialize_item(item, "DiagnosticTestResult")
                if serialized is not None:
                    child_elem = ET.Element("DIAGNOSTIC-TEST-RESULT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize request_on_ref
        if self.request_on_ref is not None:
            serialized = SerializationHelper.serialize_item(self.request_on_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REQUEST-ON-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticRequestOnBoardMonitoringTestResults":
        """Deserialize XML element to DiagnosticRequestOnBoardMonitoringTestResults object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticRequestOnBoardMonitoringTestResults object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticRequestOnBoardMonitoringTestResults, cls).deserialize(element)

        # Parse diagnostic_test_result_refs (list from container "DIAGNOSTIC-TEST-RESULT-REFS")
        obj.diagnostic_test_result_refs = []
        container = SerializationHelper.find_child_element(element, "DIAGNOSTIC-TEST-RESULT-REFS")
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
                    obj.diagnostic_test_result_refs.append(child_value)

        # Parse request_on_ref
        child = SerializationHelper.find_child_element(element, "REQUEST-ON-REF")
        if child is not None:
            request_on_ref_value = ARRef.deserialize(child)
            obj.request_on_ref = request_on_ref_value

        return obj



class DiagnosticRequestOnBoardMonitoringTestResultsBuilder:
    """Builder for DiagnosticRequestOnBoardMonitoringTestResults with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: DiagnosticRequestOnBoardMonitoringTestResults = DiagnosticRequestOnBoardMonitoringTestResults()


    def with_short_name(self, value: Identifier) -> "DiagnosticRequestOnBoardMonitoringTestResultsBuilder":
        """Set short_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.short_name = value
        return self

    def with_short_name_fragments(self, items: list[ShortNameFragment]) -> "DiagnosticRequestOnBoardMonitoringTestResultsBuilder":
        """Set short_name_fragments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = list(items) if items else []
        return self

    def with_long_name(self, value: Optional[MultilanguageLongName]) -> "DiagnosticRequestOnBoardMonitoringTestResultsBuilder":
        """Set long_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.long_name = value
        return self

    def with_admin_data(self, value: Optional[AdminData]) -> "DiagnosticRequestOnBoardMonitoringTestResultsBuilder":
        """Set admin_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.admin_data = value
        return self

    def with_annotations(self, items: list[Annotation]) -> "DiagnosticRequestOnBoardMonitoringTestResultsBuilder":
        """Set annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.annotations = list(items) if items else []
        return self

    def with_desc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "DiagnosticRequestOnBoardMonitoringTestResultsBuilder":
        """Set desc attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.desc = value
        return self

    def with_category(self, value: Optional[CategoryString]) -> "DiagnosticRequestOnBoardMonitoringTestResultsBuilder":
        """Set category attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.category = value
        return self

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "DiagnosticRequestOnBoardMonitoringTestResultsBuilder":
        """Set introduction attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.introduction = value
        return self

    def with_uuid(self, value: Optional[String]) -> "DiagnosticRequestOnBoardMonitoringTestResultsBuilder":
        """Set uuid attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.uuid = value
        return self

    def with_access(self, value: Optional[DiagnosticAccessPermission]) -> "DiagnosticRequestOnBoardMonitoringTestResultsBuilder":
        """Set access attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.access = value
        return self

    def with_service_class(self, value: Optional[DiagnosticServiceClass]) -> "DiagnosticRequestOnBoardMonitoringTestResultsBuilder":
        """Set service_class attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.service_class = value
        return self

    def with_diagnostic_test_results(self, items: list[DiagnosticTestResult]) -> "DiagnosticRequestOnBoardMonitoringTestResultsBuilder":
        """Set diagnostic_test_results list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.diagnostic_test_results = list(items) if items else []
        return self

    def with_request_on(self, value: Optional[any (DiagnosticRequestOn)]) -> "DiagnosticRequestOnBoardMonitoringTestResultsBuilder":
        """Set request_on attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.request_on = value
        return self


    def add_short_name_fragment(self, item: ShortNameFragment) -> "DiagnosticRequestOnBoardMonitoringTestResultsBuilder":
        """Add a single item to short_name_fragments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments.append(item)
        return self

    def clear_short_name_fragments(self) -> "DiagnosticRequestOnBoardMonitoringTestResultsBuilder":
        """Clear all items from short_name_fragments list.

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = []
        return self

    def add_annotation(self, item: Annotation) -> "DiagnosticRequestOnBoardMonitoringTestResultsBuilder":
        """Add a single item to annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.annotations.append(item)
        return self

    def clear_annotations(self) -> "DiagnosticRequestOnBoardMonitoringTestResultsBuilder":
        """Clear all items from annotations list.

        Returns:
            self for method chaining
        """
        self._obj.annotations = []
        return self

    def add_diagnostic_test_result(self, item: DiagnosticTestResult) -> "DiagnosticRequestOnBoardMonitoringTestResultsBuilder":
        """Add a single item to diagnostic_test_results list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.diagnostic_test_results.append(item)
        return self

    def clear_diagnostic_test_results(self) -> "DiagnosticRequestOnBoardMonitoringTestResultsBuilder":
        """Clear all items from diagnostic_test_results list.

        Returns:
            self for method chaining
        """
        self._obj.diagnostic_test_results = []
        return self


    @staticmethod
    def _coerce_to_int(value: Any) -> int:
        """Coerce value to int.

        Args:
            value: Value to coerce

        Returns:
            Integer value

        Raises:
            ValueError: If value cannot be coerced to int
        """
        if isinstance(value, int):
            return value
        if isinstance(value, str) and value.isdigit():
            return int(value)
        if isinstance(value, float):
            return int(value)
        if isinstance(value, bool):
            return int(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to int: {value}")

    @staticmethod
    def _coerce_to_float(value: Any) -> float:
        """Coerce value to float.

        Args:
            value: Value to coerce

        Returns:
            Float value

        Raises:
            ValueError: If value cannot be coerced to float
        """
        if isinstance(value, float):
            return value
        if isinstance(value, int):
            return float(value)
        if isinstance(value, str):
            try:
                return float(value)
            except ValueError:
                pass
        raise ValueError(f"Cannot coerce {type(value).__name__} to float: {value}")

    @staticmethod
    def _coerce_to_bool(value: Any) -> bool:
        """Coerce value to bool.

        Args:
            value: Value to coerce

        Returns:
            Boolean value

        Raises:
            ValueError: If value cannot be coerced to bool
        """
        if isinstance(value, bool):
            return value
        if isinstance(value, int):
            return bool(value)
        if isinstance(value, str):
            if value.lower() in ("true", "1", "yes"):
                return True
            if value.lower() in ("false", "0", "no"):
                return False
        raise ValueError(f"Cannot coerce {type(value).__name__} to bool: {value}")

    @staticmethod
    def _coerce_to_str(value: Any) -> str:
        """Coerce value to str.

        Args:
            value: Value to coerce

        Returns:
            String value
        """
        return str(value)


    @staticmethod
    def _coerce_to_list(value: Any, item_type: str) -> list:
        """Coerce value to list.

        Args:
            value: Value to coerce
            item_type: Expected item type (for error messages)

        Returns:
            List value

        Raises:
            ValueError: If value cannot be coerced to list
        """
        if isinstance(value, list):
            return value
        if isinstance(value, tuple):
            return list(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to list[{item_type}]: {value}")


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


    def build(self) -> DiagnosticRequestOnBoardMonitoringTestResults:
        """Build and return the DiagnosticRequestOnBoardMonitoringTestResults instance with validation."""
        self._validate_instance()
        pass
        return self._obj