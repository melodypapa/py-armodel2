"""DiagnosticEventToDebounceAlgorithmMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 246)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event import (
    DiagnosticEvent,
)


class DiagnosticEventToDebounceAlgorithmMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticEventToDebounceAlgorithmMapping."""

    debounce: Optional[Any]
    diagnostic_event: Optional[DiagnosticEvent]
    def __init__(self) -> None:
        """Initialize DiagnosticEventToDebounceAlgorithmMapping."""
        super().__init__()
        self.debounce: Optional[Any] = None
        self.diagnostic_event: Optional[DiagnosticEvent] = None


class DiagnosticEventToDebounceAlgorithmMappingBuilder:
    """Builder for DiagnosticEventToDebounceAlgorithmMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEventToDebounceAlgorithmMapping = DiagnosticEventToDebounceAlgorithmMapping()

    def build(self) -> DiagnosticEventToDebounceAlgorithmMapping:
        """Build and return DiagnosticEventToDebounceAlgorithmMapping object.

        Returns:
            DiagnosticEventToDebounceAlgorithmMapping instance
        """
        # TODO: Add validation
        return self._obj
