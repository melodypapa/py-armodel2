"""DiagnosticFimAliasEventGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 263)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Fim.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_abstract_alias_event import (
    DiagnosticAbstractAliasEvent,
)


class DiagnosticFimAliasEventGroup(DiagnosticAbstractAliasEvent):
    """AUTOSAR DiagnosticFimAliasEventGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    grouped_aliases: list[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticFimAliasEventGroup."""
        super().__init__()
        self.grouped_aliases: list[Any] = []


class DiagnosticFimAliasEventGroupBuilder:
    """Builder for DiagnosticFimAliasEventGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticFimAliasEventGroup = DiagnosticFimAliasEventGroup()

    def build(self) -> DiagnosticFimAliasEventGroup:
        """Build and return DiagnosticFimAliasEventGroup object.

        Returns:
            DiagnosticFimAliasEventGroup instance
        """
        # TODO: Add validation
        return self._obj
