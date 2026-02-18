"""DiagnosticRequestFileTransfer AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 146)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_RequestFileTransfer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)


class DiagnosticRequestFileTransfer(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticRequestFileTransfer."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    request_file: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticRequestFileTransfer."""
        super().__init__()
        self.request_file: Optional[Any] = None


class DiagnosticRequestFileTransferBuilder:
    """Builder for DiagnosticRequestFileTransfer."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRequestFileTransfer = DiagnosticRequestFileTransfer()

    def build(self) -> DiagnosticRequestFileTransfer:
        """Build and return DiagnosticRequestFileTransfer object.

        Returns:
            DiagnosticRequestFileTransfer instance
        """
        # TODO: Add validation
        return self._obj
