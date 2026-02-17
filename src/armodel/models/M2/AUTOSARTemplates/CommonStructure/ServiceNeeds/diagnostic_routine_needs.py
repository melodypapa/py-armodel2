"""DiagnosticRoutineNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 247)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 126)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 780)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)


class DiagnosticRoutineNeeds(DiagnosticCapabilityElement):
    """AUTOSAR DiagnosticRoutineNeeds."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "diag_routine": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticRoutineTypeEnum,
        ),  # diagRoutine
    }

    def __init__(self) -> None:
        """Initialize DiagnosticRoutineNeeds."""
        super().__init__()
        self.diag_routine: Optional[DiagnosticRoutineTypeEnum] = None


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
