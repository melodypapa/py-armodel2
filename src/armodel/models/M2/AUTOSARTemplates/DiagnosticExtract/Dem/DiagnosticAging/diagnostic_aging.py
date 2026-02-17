"""DiagnosticAging AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 202)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticAging.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DiagnosticAging(DiagnosticCommonElement):
    """AUTOSAR DiagnosticAging."""

    aging_cycle: Optional[Any]
    threshold: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DiagnosticAging."""
        super().__init__()
        self.aging_cycle: Optional[Any] = None
        self.threshold: Optional[PositiveInteger] = None


class DiagnosticAgingBuilder:
    """Builder for DiagnosticAging."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticAging = DiagnosticAging()

    def build(self) -> DiagnosticAging:
        """Build and return DiagnosticAging object.

        Returns:
            DiagnosticAging instance
        """
        # TODO: Add validation
        return self._obj
