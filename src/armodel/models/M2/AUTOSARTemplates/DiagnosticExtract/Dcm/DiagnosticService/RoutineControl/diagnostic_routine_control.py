"""DiagnosticRoutineControl AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 125)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_RoutineControl.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_routine import (
    DiagnosticRoutine,
)


class DiagnosticRoutineControl(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticRoutineControl."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "routine": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticRoutine,
        ),  # routine
        "routine_control": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticRoutine,
        ),  # routineControl
    }

    def __init__(self) -> None:
        """Initialize DiagnosticRoutineControl."""
        super().__init__()
        self.routine: Optional[DiagnosticRoutine] = None
        self.routine_control: Optional[DiagnosticRoutine] = None


class DiagnosticRoutineControlBuilder:
    """Builder for DiagnosticRoutineControl."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRoutineControl = DiagnosticRoutineControl()

    def build(self) -> DiagnosticRoutineControl:
        """Build and return DiagnosticRoutineControl object.

        Returns:
            DiagnosticRoutineControl instance
        """
        # TODO: Add validation
        return self._obj
