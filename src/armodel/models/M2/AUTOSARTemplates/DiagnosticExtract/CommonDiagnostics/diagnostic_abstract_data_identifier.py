"""DiagnosticAbstractDataIdentifier AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 34)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_CommonDiagnostics.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DiagnosticAbstractDataIdentifier(DiagnosticCommonElement):
    """AUTOSAR DiagnosticAbstractDataIdentifier."""
    """Abstract base class - do not instantiate directly."""

    def __init__(self) -> None:
        """Initialize DiagnosticAbstractDataIdentifier."""
        super().__init__()
        self.id: Optional[PositiveInteger] = None


class DiagnosticAbstractDataIdentifierBuilder:
    """Builder for DiagnosticAbstractDataIdentifier."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticAbstractDataIdentifier = DiagnosticAbstractDataIdentifier()

    def build(self) -> DiagnosticAbstractDataIdentifier:
        """Build and return DiagnosticAbstractDataIdentifier object.

        Returns:
            DiagnosticAbstractDataIdentifier instance
        """
        # TODO: Add validation
        return self._obj
