"""DiagnosticRoutineSubfunction AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.diagnostic_access_permission import (
    DiagnosticAccessPermission,
)


class DiagnosticRoutineSubfunction(Identifiable):
    """AUTOSAR DiagnosticRoutineSubfunction."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "access": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticAccessPermission,
        ),  # access
    }

    def __init__(self) -> None:
        """Initialize DiagnosticRoutineSubfunction."""
        super().__init__()
        self.access: Optional[DiagnosticAccessPermission] = None


class DiagnosticRoutineSubfunctionBuilder:
    """Builder for DiagnosticRoutineSubfunction."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRoutineSubfunction = DiagnosticRoutineSubfunction()

    def build(self) -> DiagnosticRoutineSubfunction:
        """Build and return DiagnosticRoutineSubfunction object.

        Returns:
            DiagnosticRoutineSubfunction instance
        """
        # TODO: Add validation
        return self._obj
