"""DiagnosticStartRoutine AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 124)

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


class DiagnosticStartRoutine(DiagnosticRoutineSubfunction):
    """AUTOSAR DiagnosticStartRoutine."""

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
        """Initialize DiagnosticStartRoutine."""
        super().__init__()
        self.requests: list[DiagnosticParameter] = []
        self.responses: list[DiagnosticParameter] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticStartRoutine":
        """Deserialize XML element to DiagnosticStartRoutine object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticStartRoutine object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticStartRoutine, cls).deserialize(element)

        # Parse requests (list from container "REQUESTS")
        obj.requests = []
        container = ARObject._find_child_element(element, "REQUESTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.requests.append(child_value)

        # Parse responses (list from container "RESPONSES")
        obj.responses = []
        container = ARObject._find_child_element(element, "RESPONSES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.responses.append(child_value)

        return obj



class DiagnosticStartRoutineBuilder:
    """Builder for DiagnosticStartRoutine."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticStartRoutine = DiagnosticStartRoutine()

    def build(self) -> DiagnosticStartRoutine:
        """Build and return DiagnosticStartRoutine object.

        Returns:
            DiagnosticStartRoutine instance
        """
        # TODO: Add validation
        return self._obj
