"""DiagnosticFimAliasEventGroupMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 263)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping_FimMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Fim.diagnostic_fim_event_group import (
    DiagnosticFimEventGroup,
)


class DiagnosticFimAliasEventGroupMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticFimAliasEventGroupMapping."""

    def __init__(self) -> None:
        """Initialize DiagnosticFimAliasEventGroupMapping."""
        super().__init__()
        self.actual_event: Optional[DiagnosticFimEventGroup] = None
        self.alias_event: Optional[Any] = None


class DiagnosticFimAliasEventGroupMappingBuilder:
    """Builder for DiagnosticFimAliasEventGroupMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticFimAliasEventGroupMapping = DiagnosticFimAliasEventGroupMapping()

    def build(self) -> DiagnosticFimAliasEventGroupMapping:
        """Build and return DiagnosticFimAliasEventGroupMapping object.

        Returns:
            DiagnosticFimAliasEventGroupMapping instance
        """
        # TODO: Add validation
        return self._obj
