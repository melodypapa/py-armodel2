"""DiagnosticJ1939Spn AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 219)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_J1939.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DiagnosticJ1939Spn(DiagnosticCommonElement):
    """AUTOSAR DiagnosticJ1939Spn."""

    def __init__(self) -> None:
        """Initialize DiagnosticJ1939Spn."""
        super().__init__()
        self.spn: Optional[PositiveInteger] = None


class DiagnosticJ1939SpnBuilder:
    """Builder for DiagnosticJ1939Spn."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticJ1939Spn = DiagnosticJ1939Spn()

    def build(self) -> DiagnosticJ1939Spn:
        """Build and return DiagnosticJ1939Spn object.

        Returns:
            DiagnosticJ1939Spn instance
        """
        # TODO: Add validation
        return self._obj
