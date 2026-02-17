"""DiagnosticReadDataByIdentifier AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 112)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_DataByIdentifier.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.DataByIdentifier.diagnostic_data_by_identifier import (
    DiagnosticDataByIdentifier,
)


class DiagnosticReadDataByIdentifier(DiagnosticDataByIdentifier):
    """AUTOSAR DiagnosticReadDataByIdentifier."""

    read_class: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticReadDataByIdentifier."""
        super().__init__()
        self.read_class: Optional[Any] = None


class DiagnosticReadDataByIdentifierBuilder:
    """Builder for DiagnosticReadDataByIdentifier."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticReadDataByIdentifier = DiagnosticReadDataByIdentifier()

    def build(self) -> DiagnosticReadDataByIdentifier:
        """Build and return DiagnosticReadDataByIdentifier object.

        Returns:
            DiagnosticReadDataByIdentifier instance
        """
        # TODO: Add validation
        return self._obj
