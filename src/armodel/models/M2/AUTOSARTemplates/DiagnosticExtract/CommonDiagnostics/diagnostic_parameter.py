"""DiagnosticParameter AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 36)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_CommonDiagnostics.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_abstract_parameter import (
    DiagnosticAbstractParameter,
)


class DiagnosticParameter(DiagnosticAbstractParameter):
    """AUTOSAR DiagnosticParameter."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ident: Optional[DiagnosticParameter]
    support_info: Optional[DiagnosticParameter]
    def __init__(self) -> None:
        """Initialize DiagnosticParameter."""
        super().__init__()
        self.ident: Optional[DiagnosticParameter] = None
        self.support_info: Optional[DiagnosticParameter] = None


class DiagnosticParameterBuilder:
    """Builder for DiagnosticParameter."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticParameter = DiagnosticParameter()

    def build(self) -> DiagnosticParameter:
        """Build and return DiagnosticParameter object.

        Returns:
            DiagnosticParameter instance
        """
        # TODO: Add validation
        return self._obj
