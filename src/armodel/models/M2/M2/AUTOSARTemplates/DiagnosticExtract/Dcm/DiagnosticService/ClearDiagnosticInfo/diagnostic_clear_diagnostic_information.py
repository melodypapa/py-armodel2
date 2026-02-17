"""DiagnosticClearDiagnosticInformation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 137)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_ClearDiagnosticInfo.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)


class DiagnosticClearDiagnosticInformation(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticClearDiagnosticInformation."""

    def __init__(self) -> None:
        """Initialize DiagnosticClearDiagnosticInformation."""
        super().__init__()
        self.clear_diagnostic: Optional[Any] = None


class DiagnosticClearDiagnosticInformationBuilder:
    """Builder for DiagnosticClearDiagnosticInformation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticClearDiagnosticInformation = DiagnosticClearDiagnosticInformation()

    def build(self) -> DiagnosticClearDiagnosticInformation:
        """Build and return DiagnosticClearDiagnosticInformation object.

        Returns:
            DiagnosticClearDiagnosticInformation instance
        """
        # TODO: Add validation
        return self._obj
