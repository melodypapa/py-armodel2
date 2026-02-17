"""DiagnosticIoControlClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 118)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_IOControl.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)


class DiagnosticIoControlClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticIoControlClass."""

    def __init__(self) -> None:
        """Initialize DiagnosticIoControlClass."""
        super().__init__()


class DiagnosticIoControlClassBuilder:
    """Builder for DiagnosticIoControlClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticIoControlClass = DiagnosticIoControlClass()

    def build(self) -> DiagnosticIoControlClass:
        """Build and return DiagnosticIoControlClass object.

        Returns:
            DiagnosticIoControlClass instance
        """
        # TODO: Add validation
        return self._obj
