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

    diagnostic_test_results: list[DiagnosticTestResult]
    request_on: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticRequestOnBoardMonitoringTestResults."""
        super().__init__()
        self.diagnostic_test_results: list[DiagnosticTestResult] = []
        self.request_on: Optional[Any] = None

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

        # Serialize diagnostic_test_results (list to container "DIAGNOSTIC-TEST-RESULTS")
        if self.diagnostic_test_results:
            wrapper = ET.Element("DIAGNOSTIC-TEST-RESULTS")
            for item in self.diagnostic_test_results:
                serialized = ARObject._serialize_item(item, "DiagnosticTestResult")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize request_on
        if self.request_on is not None:
            serialized = ARObject._serialize_item(self.request_on, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REQUEST-ON")
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

        # Parse diagnostic_test_results (list from container "DIAGNOSTIC-TEST-RESULTS")
        obj.diagnostic_test_results = []
        container = ARObject._find_child_element(element, "DIAGNOSTIC-TEST-RESULTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.diagnostic_test_results.append(child_value)

        # Parse request_on
        child = ARObject._find_child_element(element, "REQUEST-ON")
        if child is not None:
            request_on_value = child.text
            obj.request_on = request_on_value

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
