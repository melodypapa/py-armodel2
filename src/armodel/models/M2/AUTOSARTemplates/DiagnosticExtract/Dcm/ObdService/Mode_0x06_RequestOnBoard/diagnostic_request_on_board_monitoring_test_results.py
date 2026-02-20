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
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticRequestOnBoardMonitoringTestResults, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize diagnostic_test_result_refs (list to container "DIAGNOSTIC-TEST-RESULT-REFS")
        if self.diagnostic_test_result_refs:
            wrapper = ET.Element("DIAGNOSTIC-TEST-RESULT-REFS")
            for item in self.diagnostic_test_result_refs:
                serialized = ARObject._serialize_item(item, "DiagnosticTestResult")
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
            serialized = ARObject._serialize_item(self.request_on_ref, "Any")
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
        container = ARObject._find_child_element(element, "DIAGNOSTIC-TEST-RESULT-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.diagnostic_test_result_refs.append(child_value)

        # Parse request_on_ref
        child = ARObject._find_child_element(element, "REQUEST-ON-REF")
        if child is not None:
            request_on_ref_value = ARRef.deserialize(child)
            obj.request_on_ref = request_on_ref_value

        return obj



class DiagnosticRequestOnBoardMonitoringTestResultsBuilder:
    """Builder for DiagnosticRequestOnBoardMonitoringTestResults."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRequestOnBoardMonitoringTestResults = DiagnosticRequestOnBoardMonitoringTestResults()

    def build(self) -> DiagnosticRequestOnBoardMonitoringTestResults:
        """Build and return DiagnosticRequestOnBoardMonitoringTestResults object.

        Returns:
            DiagnosticRequestOnBoardMonitoringTestResults instance
        """
        # TODO: Add validation
        return self._obj
