"""DiagnosticWriteDataByIdentifier AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 113)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_DataByIdentifier.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.DataByIdentifier.diagnostic_data_by_identifier import (
    DiagnosticDataByIdentifier,
)


class DiagnosticWriteDataByIdentifier(DiagnosticDataByIdentifier):
    """AUTOSAR DiagnosticWriteDataByIdentifier."""

    write_class: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticWriteDataByIdentifier."""
        super().__init__()
        self.write_class: Optional[Any] = None


class DiagnosticWriteDataByIdentifierBuilder:
    """Builder for DiagnosticWriteDataByIdentifier."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticWriteDataByIdentifier = DiagnosticWriteDataByIdentifier()

    def build(self) -> DiagnosticWriteDataByIdentifier:
        """Build and return DiagnosticWriteDataByIdentifier object.

        Returns:
            DiagnosticWriteDataByIdentifier instance
        """
        # TODO: Add validation
        return self._obj
