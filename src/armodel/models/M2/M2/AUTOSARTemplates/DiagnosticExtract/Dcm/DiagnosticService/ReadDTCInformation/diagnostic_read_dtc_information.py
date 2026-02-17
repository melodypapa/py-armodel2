"""DiagnosticReadDTCInformation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 136)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_ReadDTCInformation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)


class DiagnosticReadDTCInformation(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticReadDTCInformation."""

    def __init__(self) -> None:
        """Initialize DiagnosticReadDTCInformation."""
        super().__init__()
        self.read: Optional[Any] = None


class DiagnosticReadDTCInformationBuilder:
    """Builder for DiagnosticReadDTCInformation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticReadDTCInformation = DiagnosticReadDTCInformation()

    def build(self) -> DiagnosticReadDTCInformation:
        """Build and return DiagnosticReadDTCInformation object.

        Returns:
            DiagnosticReadDTCInformation instance
        """
        # TODO: Add validation
        return self._obj
