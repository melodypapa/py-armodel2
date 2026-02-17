"""DiagnosticReadMemoryByAddressClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 142)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_MemoryByAddress.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)


class DiagnosticReadMemoryByAddressClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticReadMemoryByAddressClass."""

    def __init__(self) -> None:
        """Initialize DiagnosticReadMemoryByAddressClass."""
        super().__init__()


class DiagnosticReadMemoryByAddressClassBuilder:
    """Builder for DiagnosticReadMemoryByAddressClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticReadMemoryByAddressClass = DiagnosticReadMemoryByAddressClass()

    def build(self) -> DiagnosticReadMemoryByAddressClass:
        """Build and return DiagnosticReadMemoryByAddressClass object.

        Returns:
            DiagnosticReadMemoryByAddressClass instance
        """
        # TODO: Add validation
        return self._obj
