"""DiagnosticFimAliasEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 214)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Fim.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_abstract_alias_event import (
    DiagnosticAbstractAliasEvent,
)


class DiagnosticFimAliasEvent(DiagnosticAbstractAliasEvent):
    """AUTOSAR DiagnosticFimAliasEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize DiagnosticFimAliasEvent."""
        super().__init__()


class DiagnosticFimAliasEventBuilder:
    """Builder for DiagnosticFimAliasEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticFimAliasEvent = DiagnosticFimAliasEvent()

    def build(self) -> DiagnosticFimAliasEvent:
        """Build and return DiagnosticFimAliasEvent object.

        Returns:
            DiagnosticFimAliasEvent instance
        """
        # TODO: Add validation
        return self._obj
