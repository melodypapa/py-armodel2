"""DiagnosticOperationCycle AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)


class DiagnosticOperationCycle(DiagnosticCommonElement):
    """AUTOSAR DiagnosticOperationCycle."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "type_cycle_type_enum": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (DiagnosticOperation),
        ),  # typeCycleTypeEnum
    }

    def __init__(self) -> None:
        """Initialize DiagnosticOperationCycle."""
        super().__init__()
        self.type_cycle_type_enum: Optional[Any] = None


class DiagnosticOperationCycleBuilder:
    """Builder for DiagnosticOperationCycle."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticOperationCycle = DiagnosticOperationCycle()

    def build(self) -> DiagnosticOperationCycle:
        """Build and return DiagnosticOperationCycle object.

        Returns:
            DiagnosticOperationCycle instance
        """
        # TODO: Add validation
        return self._obj
