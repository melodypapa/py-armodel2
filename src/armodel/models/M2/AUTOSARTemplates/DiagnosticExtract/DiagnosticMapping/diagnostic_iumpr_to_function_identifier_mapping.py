"""DiagnosticIumprToFunctionIdentifierMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 265)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_iumpr import (
    DiagnosticIumpr,
)


class DiagnosticIumprToFunctionIdentifierMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticIumprToFunctionIdentifierMapping."""

    def __init__(self) -> None:
        """Initialize DiagnosticIumprToFunctionIdentifierMapping."""
        super().__init__()
        self.function: Optional[Any] = None
        self.iumpr: Optional[DiagnosticIumpr] = None


class DiagnosticIumprToFunctionIdentifierMappingBuilder:
    """Builder for DiagnosticIumprToFunctionIdentifierMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticIumprToFunctionIdentifierMapping = DiagnosticIumprToFunctionIdentifierMapping()

    def build(self) -> DiagnosticIumprToFunctionIdentifierMapping:
        """Build and return DiagnosticIumprToFunctionIdentifierMapping object.

        Returns:
            DiagnosticIumprToFunctionIdentifierMapping instance
        """
        # TODO: Add validation
        return self._obj
