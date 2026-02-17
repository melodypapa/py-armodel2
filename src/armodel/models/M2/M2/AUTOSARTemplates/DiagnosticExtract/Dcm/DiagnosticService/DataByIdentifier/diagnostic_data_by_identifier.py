"""DiagnosticDataByIdentifier AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 113)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_DataByIdentifier.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_abstract_data_identifier import (
    DiagnosticAbstractDataIdentifier,
)


class DiagnosticDataByIdentifier(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticDataByIdentifier."""
    """Abstract base class - do not instantiate directly."""

    def __init__(self) -> None:
        """Initialize DiagnosticDataByIdentifier."""
        super().__init__()
        self.data_identifier: Optional[DiagnosticAbstractDataIdentifier] = None


class DiagnosticDataByIdentifierBuilder:
    """Builder for DiagnosticDataByIdentifier."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticDataByIdentifier = DiagnosticDataByIdentifier()

    def build(self) -> DiagnosticDataByIdentifier:
        """Build and return DiagnosticDataByIdentifier object.

        Returns:
            DiagnosticDataByIdentifier instance
        """
        # TODO: Add validation
        return self._obj
