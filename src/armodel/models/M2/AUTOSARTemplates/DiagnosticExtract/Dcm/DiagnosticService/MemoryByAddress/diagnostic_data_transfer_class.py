"""DiagnosticDataTransferClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 144)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_MemoryByAddress.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)


class DiagnosticDataTransferClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticDataTransferClass."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize DiagnosticDataTransferClass."""
        super().__init__()


class DiagnosticDataTransferClassBuilder:
    """Builder for DiagnosticDataTransferClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticDataTransferClass = DiagnosticDataTransferClass()

    def build(self) -> DiagnosticDataTransferClass:
        """Build and return DiagnosticDataTransferClass object.

        Returns:
            DiagnosticDataTransferClass instance
        """
        # TODO: Add validation
        return self._obj
