"""DiagnosticRequestCurrentPowertrainData AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 150)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_ObdService_Mode_0x01_RequestCurrentPowertrain.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_parameter import (
    DiagnosticParameter,
)


class DiagnosticRequestCurrentPowertrainData(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticRequestCurrentPowertrainData."""

    def __init__(self) -> None:
        """Initialize DiagnosticRequestCurrentPowertrainData."""
        super().__init__()
        self.pid: Optional[DiagnosticParameter] = None
        self.request_current: Optional[Any] = None


class DiagnosticRequestCurrentPowertrainDataBuilder:
    """Builder for DiagnosticRequestCurrentPowertrainData."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRequestCurrentPowertrainData = DiagnosticRequestCurrentPowertrainData()

    def build(self) -> DiagnosticRequestCurrentPowertrainData:
        """Build and return DiagnosticRequestCurrentPowertrainData object.

        Returns:
            DiagnosticRequestCurrentPowertrainData instance
        """
        # TODO: Add validation
        return self._obj
