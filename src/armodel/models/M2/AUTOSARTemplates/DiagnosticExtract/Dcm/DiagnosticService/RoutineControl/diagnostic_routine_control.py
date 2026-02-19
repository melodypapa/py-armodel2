"""DiagnosticRoutineControl AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 125)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_RoutineControl.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_routine import (
    DiagnosticRoutine,
)


class DiagnosticRoutineControl(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticRoutineControl."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    routine: Optional[DiagnosticRoutine]
    routine_control: Optional[DiagnosticRoutine]
    def __init__(self) -> None:
        """Initialize DiagnosticRoutineControl."""
        super().__init__()
        self.routine: Optional[DiagnosticRoutine] = None
        self.routine_control: Optional[DiagnosticRoutine] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticRoutineControl":
        """Deserialize XML element to DiagnosticRoutineControl object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticRoutineControl object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse routine
        child = ARObject._find_child_element(element, "ROUTINE")
        if child is not None:
            routine_value = ARObject._deserialize_by_tag(child, "DiagnosticRoutine")
            obj.routine = routine_value

        # Parse routine_control
        child = ARObject._find_child_element(element, "ROUTINE-CONTROL")
        if child is not None:
            routine_control_value = ARObject._deserialize_by_tag(child, "DiagnosticRoutine")
            obj.routine_control = routine_control_value

        return obj



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
