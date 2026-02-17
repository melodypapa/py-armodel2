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
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTestResult.diagnostic_test_result import (
    DiagnosticTestResult,
)


class DiagnosticRequestOnBoardMonitoringTestResults(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticRequestOnBoardMonitoringTestResults."""

    diagnostic_test_results: list[DiagnosticTestResult]
    request_on: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticRequestOnBoardMonitoringTestResults."""
        super().__init__()
        self.diagnostic_test_results: list[DiagnosticTestResult] = []
        self.request_on: Optional[Any] = None


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
