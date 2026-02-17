"""DiagnosticMemoryByAddress AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 139)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_MemoryByAddress.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)


class DiagnosticMemoryByAddress(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticMemoryByAddress."""
    """Abstract base class - do not instantiate directly."""

    def __init__(self) -> None:
        """Initialize DiagnosticMemoryByAddress."""
        super().__init__()


class DiagnosticMemoryByAddressBuilder:
    """Builder for DiagnosticMemoryByAddress."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticMemoryByAddress = DiagnosticMemoryByAddress()

    def build(self) -> DiagnosticMemoryByAddress:
        """Build and return DiagnosticMemoryByAddress object.

        Returns:
            DiagnosticMemoryByAddress instance
        """
        # TODO: Add validation
        return self._obj
