"""DiagnosticFunctionInhibitSource AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 216)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Fim.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)


class DiagnosticFunctionInhibitSource(Identifiable):
    """AUTOSAR DiagnosticFunctionInhibitSource."""

    event: Optional[Any]
    event_group: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticFunctionInhibitSource."""
        super().__init__()
        self.event: Optional[Any] = None
        self.event_group: Optional[Any] = None


class DiagnosticFunctionInhibitSourceBuilder:
    """Builder for DiagnosticFunctionInhibitSource."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticFunctionInhibitSource = DiagnosticFunctionInhibitSource()

    def build(self) -> DiagnosticFunctionInhibitSource:
        """Build and return DiagnosticFunctionInhibitSource object.

        Returns:
            DiagnosticFunctionInhibitSource instance
        """
        # TODO: Add validation
        return self._obj
