"""DiagnosticDataTransfer AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 143)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_MemoryByAddress.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.MemoryByAddress.diagnostic_memory_by_address import (
    DiagnosticMemoryByAddress,
)


class DiagnosticDataTransfer(DiagnosticMemoryByAddress):
    """AUTOSAR DiagnosticDataTransfer."""

    data_transfer: Optional[DiagnosticDataTransfer]
    def __init__(self) -> None:
        """Initialize DiagnosticDataTransfer."""
        super().__init__()
        self.data_transfer: Optional[DiagnosticDataTransfer] = None


class DiagnosticDataTransferBuilder:
    """Builder for DiagnosticDataTransfer."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticDataTransfer = DiagnosticDataTransfer()

    def build(self) -> DiagnosticDataTransfer:
        """Build and return DiagnosticDataTransfer object.

        Returns:
            DiagnosticDataTransfer instance
        """
        # TODO: Add validation
        return self._obj
