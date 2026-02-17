"""DiagnosticTestResult AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 204)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 804)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticTestResult.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event import (
    DiagnosticEvent,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTestResult.diagnostic_test_identifier import (
    DiagnosticTestIdentifier,
)


class DiagnosticTestResult(DiagnosticCommonElement):
    """AUTOSAR DiagnosticTestResult."""

    diagnostic_event: Optional[DiagnosticEvent]
    monitored: Optional[Any]
    test_identifier: Optional[DiagnosticTestIdentifier]
    update_kind: Optional[DiagnosticTestResult]
    def __init__(self) -> None:
        """Initialize DiagnosticTestResult."""
        super().__init__()
        self.diagnostic_event: Optional[DiagnosticEvent] = None
        self.monitored: Optional[Any] = None
        self.test_identifier: Optional[DiagnosticTestIdentifier] = None
        self.update_kind: Optional[DiagnosticTestResult] = None


class DiagnosticTestResultBuilder:
    """Builder for DiagnosticTestResult."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticTestResult = DiagnosticTestResult()

    def build(self) -> DiagnosticTestResult:
        """Build and return DiagnosticTestResult object.

        Returns:
            DiagnosticTestResult instance
        """
        # TODO: Add validation
        return self._obj
