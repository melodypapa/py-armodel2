"""DiagnosticRequestUpload AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 145)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_MemoryByAddress.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.MemoryByAddress.diagnostic_memory_addressable_range_access import (
    DiagnosticMemoryAddressableRangeAccess,
)


class DiagnosticRequestUpload(DiagnosticMemoryAddressableRangeAccess):
    """AUTOSAR DiagnosticRequestUpload."""

    request_upload: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticRequestUpload."""
        super().__init__()
        self.request_upload: Optional[Any] = None


class DiagnosticRequestUploadBuilder:
    """Builder for DiagnosticRequestUpload."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRequestUpload = DiagnosticRequestUpload()

    def build(self) -> DiagnosticRequestUpload:
        """Build and return DiagnosticRequestUpload object.

        Returns:
            DiagnosticRequestUpload instance
        """
        # TODO: Add validation
        return self._obj
