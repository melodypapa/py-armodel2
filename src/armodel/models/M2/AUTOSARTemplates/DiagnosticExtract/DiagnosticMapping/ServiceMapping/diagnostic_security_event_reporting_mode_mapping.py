"""DiagnosticSecurityEventReportingModeMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 243)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping_ServiceMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_data_element import (
    DiagnosticDataElement,
)


class DiagnosticSecurityEventReportingModeMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticSecurityEventReportingModeMapping."""

    data_element: Optional[DiagnosticDataElement]
    security_event_context: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticSecurityEventReportingModeMapping."""
        super().__init__()
        self.data_element: Optional[DiagnosticDataElement] = None
        self.security_event_context: Optional[Any] = None


class DiagnosticSecurityEventReportingModeMappingBuilder:
    """Builder for DiagnosticSecurityEventReportingModeMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticSecurityEventReportingModeMapping = DiagnosticSecurityEventReportingModeMapping()

    def build(self) -> DiagnosticSecurityEventReportingModeMapping:
        """Build and return DiagnosticSecurityEventReportingModeMapping object.

        Returns:
            DiagnosticSecurityEventReportingModeMapping instance
        """
        # TODO: Add validation
        return self._obj
