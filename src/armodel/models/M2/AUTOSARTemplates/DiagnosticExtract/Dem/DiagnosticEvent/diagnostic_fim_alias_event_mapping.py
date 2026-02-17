"""DiagnosticFimAliasEventMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 262)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticEvent.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event import (
    DiagnosticEvent,
)


class DiagnosticFimAliasEventMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticFimAliasEventMapping."""

    def __init__(self) -> None:
        """Initialize DiagnosticFimAliasEventMapping."""
        super().__init__()
        self.actual_event: Optional[DiagnosticEvent] = None
        self.alias_event_event: Optional[Any] = None


class DiagnosticFimAliasEventMappingBuilder:
    """Builder for DiagnosticFimAliasEventMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticFimAliasEventMapping = DiagnosticFimAliasEventMapping()

    def build(self) -> DiagnosticFimAliasEventMapping:
        """Build and return DiagnosticFimAliasEventMapping object.

        Returns:
            DiagnosticFimAliasEventMapping instance
        """
        # TODO: Add validation
        return self._obj
