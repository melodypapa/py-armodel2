"""DiagnosticRoutineNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 247)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 126)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 780)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    DiagnosticRoutineTypeEnum,
)


class DiagnosticRoutineNeeds(DiagnosticCapabilityElement):
    """AUTOSAR DiagnosticRoutineNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    diag_routine: Optional[DiagnosticRoutineTypeEnum]
    def __init__(self) -> None:
        """Initialize DiagnosticRoutineNeeds."""
        super().__init__()
        self.diag_routine: Optional[DiagnosticRoutineTypeEnum] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticRoutineNeeds":
        """Deserialize XML element to DiagnosticRoutineNeeds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticRoutineNeeds object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticRoutineNeeds, cls).deserialize(element)

        # Parse diag_routine
        child = ARObject._find_child_element(element, "DIAG-ROUTINE")
        if child is not None:
            diag_routine_value = DiagnosticRoutineTypeEnum.deserialize(child)
            obj.diag_routine = diag_routine_value

        return obj



class DiagnosticRoutineNeedsBuilder:
    """Builder for DiagnosticRoutineNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRoutineNeeds = DiagnosticRoutineNeeds()

    def build(self) -> DiagnosticRoutineNeeds:
        """Build and return DiagnosticRoutineNeeds object.

        Returns:
            DiagnosticRoutineNeeds instance
        """
        # TODO: Add validation
        return self._obj
