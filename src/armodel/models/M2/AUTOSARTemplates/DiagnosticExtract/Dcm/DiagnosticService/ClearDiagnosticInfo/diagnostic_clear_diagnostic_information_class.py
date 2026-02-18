"""DiagnosticClearDiagnosticInformationClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 137)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_ClearDiagnosticInfo.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)


class DiagnosticClearDiagnosticInformationClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticClearDiagnosticInformationClass."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize DiagnosticClearDiagnosticInformationClass."""
        super().__init__()


class DiagnosticClearDiagnosticInformationClassBuilder:
    """Builder for DiagnosticClearDiagnosticInformationClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticClearDiagnosticInformationClass = DiagnosticClearDiagnosticInformationClass()

    def build(self) -> DiagnosticClearDiagnosticInformationClass:
        """Build and return DiagnosticClearDiagnosticInformationClass object.

        Returns:
            DiagnosticClearDiagnosticInformationClass instance
        """
        # TODO: Add validation
        return self._obj
