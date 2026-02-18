"""DiagnosticRoutineControlClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 125)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_RoutineControl.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)


class DiagnosticRoutineControlClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticRoutineControlClass."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize DiagnosticRoutineControlClass."""
        super().__init__()


class DiagnosticRoutineControlClassBuilder:
    """Builder for DiagnosticRoutineControlClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRoutineControlClass = DiagnosticRoutineControlClass()

    def build(self) -> DiagnosticRoutineControlClass:
        """Build and return DiagnosticRoutineControlClass object.

        Returns:
            DiagnosticRoutineControlClass instance
        """
        # TODO: Add validation
        return self._obj
