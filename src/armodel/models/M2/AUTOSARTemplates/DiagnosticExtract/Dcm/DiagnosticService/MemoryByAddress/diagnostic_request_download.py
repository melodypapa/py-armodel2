"""DiagnosticRequestDownload AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 144)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_MemoryByAddress.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.MemoryByAddress.diagnostic_memory_addressable_range_access import (
    DiagnosticMemoryAddressableRangeAccess,
)


class DiagnosticRequestDownload(DiagnosticMemoryAddressableRangeAccess):
    """AUTOSAR DiagnosticRequestDownload."""

    def __init__(self) -> None:
        """Initialize DiagnosticRequestDownload."""
        super().__init__()
        self.request: Optional[Any] = None


class DiagnosticRequestDownloadBuilder:
    """Builder for DiagnosticRequestDownload."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRequestDownload = DiagnosticRequestDownload()

    def build(self) -> DiagnosticRequestDownload:
        """Build and return DiagnosticRequestDownload object.

        Returns:
            DiagnosticRequestDownload instance
        """
        # TODO: Add validation
        return self._obj
