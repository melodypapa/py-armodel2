"""DiagnosticMemoryDestinationPrimary AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 184)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticMemoryDestination.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticMemoryDestination.diagnostic_memory_destination import (
    DiagnosticMemoryDestination,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode import (
    DiagnosticTypeOfDtcSupportedEnum,
)


class DiagnosticMemoryDestinationPrimary(DiagnosticMemoryDestination):
    """AUTOSAR DiagnosticMemoryDestinationPrimary."""

    type_of_dtc: Optional[DiagnosticTypeOfDtcSupportedEnum]
    def __init__(self) -> None:
        """Initialize DiagnosticMemoryDestinationPrimary."""
        super().__init__()
        self.type_of_dtc: Optional[DiagnosticTypeOfDtcSupportedEnum] = None


class DiagnosticMemoryDestinationPrimaryBuilder:
    """Builder for DiagnosticMemoryDestinationPrimary."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticMemoryDestinationPrimary = DiagnosticMemoryDestinationPrimary()

    def build(self) -> DiagnosticMemoryDestinationPrimary:
        """Build and return DiagnosticMemoryDestinationPrimary object.

        Returns:
            DiagnosticMemoryDestinationPrimary instance
        """
        # TODO: Add validation
        return self._obj
