"""DiagnosticRequestOnBoardMonitoringTestResultsClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 156)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_ObdService_Mode_0x06_RequestOnBoard.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)


class DiagnosticRequestOnBoardMonitoringTestResultsClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticRequestOnBoardMonitoringTestResultsClass."""

    def __init__(self) -> None:
        """Initialize DiagnosticRequestOnBoardMonitoringTestResultsClass."""
        super().__init__()


class DiagnosticRequestOnBoardMonitoringTestResultsClassBuilder:
    """Builder for DiagnosticRequestOnBoardMonitoringTestResultsClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRequestOnBoardMonitoringTestResultsClass = DiagnosticRequestOnBoardMonitoringTestResultsClass()

    def build(self) -> DiagnosticRequestOnBoardMonitoringTestResultsClass:
        """Build and return DiagnosticRequestOnBoardMonitoringTestResultsClass object.

        Returns:
            DiagnosticRequestOnBoardMonitoringTestResultsClass instance
        """
        # TODO: Add validation
        return self._obj
