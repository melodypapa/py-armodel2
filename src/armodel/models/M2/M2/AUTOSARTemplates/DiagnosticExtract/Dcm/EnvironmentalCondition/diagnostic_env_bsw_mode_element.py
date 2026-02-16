"""DiagnosticEnvBswModeElement AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.EnvironmentalCondition.diagnostic_env_mode_element import (
    DiagnosticEnvModeElement,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)


class DiagnosticEnvBswModeElement(DiagnosticEnvModeElement):
    """AUTOSAR DiagnosticEnvBswModeElement."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "mode": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ModeDeclaration,
        ),  # mode
    }

    def __init__(self) -> None:
        """Initialize DiagnosticEnvBswModeElement."""
        super().__init__()
        self.mode: Optional[ModeDeclaration] = None


class DiagnosticEnvBswModeElementBuilder:
    """Builder for DiagnosticEnvBswModeElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEnvBswModeElement = DiagnosticEnvBswModeElement()

    def build(self) -> DiagnosticEnvBswModeElement:
        """Build and return DiagnosticEnvBswModeElement object.

        Returns:
            DiagnosticEnvBswModeElement instance
        """
        # TODO: Add validation
        return self._obj
