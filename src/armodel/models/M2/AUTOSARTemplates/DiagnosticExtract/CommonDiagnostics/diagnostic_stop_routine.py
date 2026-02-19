"""DiagnosticStopRoutine AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 125)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_CommonDiagnostics.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_routine_subfunction import (
    DiagnosticRoutineSubfunction,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_parameter import (
    DiagnosticParameter,
)


class DiagnosticStopRoutine(DiagnosticRoutineSubfunction):
    """AUTOSAR DiagnosticStopRoutine."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    requests: list[DiagnosticParameter]
    responses: list[DiagnosticParameter]
    def __init__(self) -> None:
        """Initialize DiagnosticStopRoutine."""
        super().__init__()
        self.requests: list[DiagnosticParameter] = []
        self.responses: list[DiagnosticParameter] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticStopRoutine":
        """Deserialize XML element to DiagnosticStopRoutine object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticStopRoutine object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse requests (list)
        obj.requests = []
        for child in ARObject._find_all_child_elements(element, "REQUESTS"):
            requests_value = ARObject._deserialize_by_tag(child, "DiagnosticParameter")
            obj.requests.append(requests_value)

        # Parse responses (list)
        obj.responses = []
        for child in ARObject._find_all_child_elements(element, "RESPONSES"):
            responses_value = ARObject._deserialize_by_tag(child, "DiagnosticParameter")
            obj.responses.append(responses_value)

        return obj



class DiagnosticStopRoutineBuilder:
    """Builder for DiagnosticStopRoutine."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticStopRoutine = DiagnosticStopRoutine()

    def build(self) -> DiagnosticStopRoutine:
        """Build and return DiagnosticStopRoutine object.

        Returns:
            DiagnosticStopRoutine instance
        """
        # TODO: Add validation
        return self._obj
