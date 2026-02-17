"""DiagnosticConnectedIndicator AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 166)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticEvent.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticIndicator.diagnostic_indicator import (
    DiagnosticIndicator,
)


class DiagnosticConnectedIndicator(Identifiable):
    """AUTOSAR DiagnosticConnectedIndicator."""

    behavior_indicator_behavior_enum: Optional[Any]
    healing_cycle: Optional[PositiveInteger]
    indicator: Optional[DiagnosticIndicator]
    indicator_failure: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DiagnosticConnectedIndicator."""
        super().__init__()
        self.behavior_indicator_behavior_enum: Optional[Any] = None
        self.healing_cycle: Optional[PositiveInteger] = None
        self.indicator: Optional[DiagnosticIndicator] = None
        self.indicator_failure: Optional[PositiveInteger] = None


class DiagnosticConnectedIndicatorBuilder:
    """Builder for DiagnosticConnectedIndicator."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticConnectedIndicator = DiagnosticConnectedIndicator()

    def build(self) -> DiagnosticConnectedIndicator:
        """Build and return DiagnosticConnectedIndicator object.

        Returns:
            DiagnosticConnectedIndicator instance
        """
        # TODO: Add validation
        return self._obj
