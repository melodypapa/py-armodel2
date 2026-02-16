"""DiagnosticRequestOnBoardMonitoringTestResults AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTestResult.diagnostic_test_result import (
    DiagnosticTestResult,
)


class DiagnosticRequestOnBoardMonitoringTestResults(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticRequestOnBoardMonitoringTestResults."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("diagnostic_test_results", None, False, True, DiagnosticTestResult),  # diagnosticTestResults
        ("request_on", None, False, False, any (DiagnosticRequestOn)),  # requestOn
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticRequestOnBoardMonitoringTestResults."""
        super().__init__()
        self.diagnostic_test_results: list[DiagnosticTestResult] = []
        self.request_on: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticRequestOnBoardMonitoringTestResults to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticRequestOnBoardMonitoringTestResults":
        """Create DiagnosticRequestOnBoardMonitoringTestResults from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticRequestOnBoardMonitoringTestResults instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticRequestOnBoardMonitoringTestResults since parent returns ARObject
        return cast("DiagnosticRequestOnBoardMonitoringTestResults", obj)


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
