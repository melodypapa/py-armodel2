"""DiagnosticRequestOnBoardMonitoringTestResults AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 156)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_ObdService_Mode_0x06_RequestOnBoard.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import DiagnosticServiceInstanceBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTestResult.diagnostic_test_result import (
    DiagnosticTestResult,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticRequestOnBoardMonitoringTestResults(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticRequestOnBoardMonitoringTestResults."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-REQUEST-ON-BOARD-MONITORING-TEST-RESULTS"


    diagnostic_test_result_refs: list[ARRef]
    request_on_ref: Optional[Any]
    _DESERIALIZE_DISPATCH = {
        "DIAGNOSTIC-TEST-RESULTS": lambda obj, elem: obj.diagnostic_test_result_refs.append(ARRef.deserialize(elem)),
        "REQUEST-ON-REF": lambda obj, elem: setattr(obj, "request_on_ref", ARRef.deserialize(elem)),
    }


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
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DIAGNOSTIC-TEST-RESULTS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.diagnostic_test_result_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "DiagnosticTestResult"))
            elif tag == "REQUEST-ON-REF":
                setattr(obj, "request_on_ref", ARRef.deserialize(child))

        return obj



class DiagnosticRequestOnBoardMonitoringTestResultsBuilder(DiagnosticServiceInstanceBuilder):
    """Builder for DiagnosticRequestOnBoardMonitoringTestResults with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticRequestOnBoardMonitoringTestResults = DiagnosticRequestOnBoardMonitoringTestResults()


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


    def build(self) -> DiagnosticRequestOnBoardMonitoringTestResults:
        """Build and return the DiagnosticRequestOnBoardMonitoringTestResults instance with validation."""
        self._validate_instance()
        pass
        return self._obj