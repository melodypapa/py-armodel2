"""DiagnosticRoutineSubfunction AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 121)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_CommonDiagnostics.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.diagnostic_access_permission import (
    DiagnosticAccessPermission,
)


class DiagnosticRoutineSubfunction(Identifiable):
    """AUTOSAR DiagnosticRoutineSubfunction."""
    """Abstract base class - do not instantiate directly."""

    access: Optional[DiagnosticAccessPermission]
    def __init__(self) -> None:
        """Initialize DiagnosticRoutineSubfunction."""
        super().__init__()
        self.access: Optional[DiagnosticAccessPermission] = None


class DiagnosticRoutineSubfunctionBuilder:
    """Builder for DiagnosticRoutineSubfunction."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRoutineSubfunction = DiagnosticRoutineSubfunction()

    def build(self) -> DiagnosticRoutineSubfunction:
        """Build and return DiagnosticRoutineSubfunction object.

        Returns:
            DiagnosticRoutineSubfunction instance
        """
        # TODO: Add validation
        return self._obj
