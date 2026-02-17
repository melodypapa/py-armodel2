"""DiagnosticParameterElement AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 36)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_CommonDiagnostics.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_parameter import (
    DiagnosticParameter,
)


class DiagnosticParameterElement(Identifiable):
    """AUTOSAR DiagnosticParameterElement."""

    array_size: Optional[PositiveInteger]
    sub_elements: list[DiagnosticParameter]
    def __init__(self) -> None:
        """Initialize DiagnosticParameterElement."""
        super().__init__()
        self.array_size: Optional[PositiveInteger] = None
        self.sub_elements: list[DiagnosticParameter] = []


class DiagnosticParameterElementBuilder:
    """Builder for DiagnosticParameterElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticParameterElement = DiagnosticParameterElement()

    def build(self) -> DiagnosticParameterElement:
        """Build and return DiagnosticParameterElement object.

        Returns:
            DiagnosticParameterElement instance
        """
        # TODO: Add validation
        return self._obj
