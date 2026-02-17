"""DiagnosticRoutine AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 124)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_CommonDiagnostics.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_start_routine import (
    DiagnosticStartRoutine,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_stop_routine import (
    DiagnosticStopRoutine,
)


class DiagnosticRoutine(DiagnosticCommonElement):
    """AUTOSAR DiagnosticRoutine."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "id": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # id
        "request_result": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (DiagnosticRequest),
        ),  # requestResult
        "routine_info": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # routineInfo
        "start": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticStartRoutine,
        ),  # start
        "stop": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticStopRoutine,
        ),  # stop
    }

    def __init__(self) -> None:
        """Initialize DiagnosticRoutine."""
        super().__init__()
        self.id: Optional[PositiveInteger] = None
        self.request_result: Optional[Any] = None
        self.routine_info: Optional[PositiveInteger] = None
        self.start: Optional[DiagnosticStartRoutine] = None
        self.stop: Optional[DiagnosticStopRoutine] = None


class DiagnosticRoutineBuilder:
    """Builder for DiagnosticRoutine."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRoutine = DiagnosticRoutine()

    def build(self) -> DiagnosticRoutine:
        """Build and return DiagnosticRoutine object.

        Returns:
            DiagnosticRoutine instance
        """
        # TODO: Add validation
        return self._obj
