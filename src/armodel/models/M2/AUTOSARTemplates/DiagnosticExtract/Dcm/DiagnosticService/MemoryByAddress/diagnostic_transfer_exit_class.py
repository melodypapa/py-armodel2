"""DiagnosticTransferExitClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 143)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_MemoryByAddress.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)


class DiagnosticTransferExitClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticTransferExitClass."""

    def __init__(self) -> None:
        """Initialize DiagnosticTransferExitClass."""
        super().__init__()


class DiagnosticTransferExitClassBuilder:
    """Builder for DiagnosticTransferExitClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticTransferExitClass = DiagnosticTransferExitClass()

    def build(self) -> DiagnosticTransferExitClass:
        """Build and return DiagnosticTransferExitClass object.

        Returns:
            DiagnosticTransferExitClass instance
        """
        # TODO: Add validation
        return self._obj
