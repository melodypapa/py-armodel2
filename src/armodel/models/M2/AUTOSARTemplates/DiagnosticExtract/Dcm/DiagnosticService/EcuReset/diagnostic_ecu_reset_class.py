"""DiagnosticEcuResetClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 102)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_EcuReset.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.EcuReset import (
    DiagnosticResponseToEcuResetEnum,
)


class DiagnosticEcuResetClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticEcuResetClass."""

    respond_to: Optional[DiagnosticResponseToEcuResetEnum]
    def __init__(self) -> None:
        """Initialize DiagnosticEcuResetClass."""
        super().__init__()
        self.respond_to: Optional[DiagnosticResponseToEcuResetEnum] = None


class DiagnosticEcuResetClassBuilder:
    """Builder for DiagnosticEcuResetClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEcuResetClass = DiagnosticEcuResetClass()

    def build(self) -> DiagnosticEcuResetClass:
        """Build and return DiagnosticEcuResetClass object.

        Returns:
            DiagnosticEcuResetClass instance
        """
        # TODO: Add validation
        return self._obj
