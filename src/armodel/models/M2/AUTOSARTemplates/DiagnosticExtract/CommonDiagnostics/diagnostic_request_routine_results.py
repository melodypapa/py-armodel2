"""DiagnosticRequestRoutineResults AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 125)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_CommonDiagnostics.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_routine_subfunction import (
    DiagnosticRoutineSubfunction,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_parameter import (
    DiagnosticParameter,
)


class DiagnosticRequestRoutineResults(DiagnosticRoutineSubfunction):
    """AUTOSAR DiagnosticRequestRoutineResults."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "requests": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DiagnosticParameter,
        ),  # requests
        "responses": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DiagnosticParameter,
        ),  # responses
    }

    def __init__(self) -> None:
        """Initialize DiagnosticRequestRoutineResults."""
        super().__init__()
        self.requests: list[DiagnosticParameter] = []
        self.responses: list[DiagnosticParameter] = []


class DiagnosticRequestRoutineResultsBuilder:
    """Builder for DiagnosticRequestRoutineResults."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRequestRoutineResults = DiagnosticRequestRoutineResults()

    def build(self) -> DiagnosticRequestRoutineResults:
        """Build and return DiagnosticRequestRoutineResults object.

        Returns:
            DiagnosticRequestRoutineResults instance
        """
        # TODO: Add validation
        return self._obj
