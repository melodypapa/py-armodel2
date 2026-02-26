"""Mode_0x06_RequestOnBoard module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.ObdService.Mode_0x06_RequestOnBoard.diagnostic_request_on_board_monitoring_test_results import (
        DiagnosticRequestOnBoardMonitoringTestResults,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.ObdService.Mode_0x06_RequestOnBoard.diagnostic_request_on_board_monitoring_test_results_class import (
        DiagnosticRequestOnBoardMonitoringTestResultsClass,
    )

__all__ = [
    "DiagnosticRequestOnBoardMonitoringTestResults",
    "DiagnosticRequestOnBoardMonitoringTestResultsClass",
]
