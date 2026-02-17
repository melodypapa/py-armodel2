"""DiagnosticEnvSwcModeElement AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 89)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_EnvironmentalCondition.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.EnvironmentalCondition.diagnostic_env_mode_element import (
    DiagnosticEnvModeElement,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)


class DiagnosticEnvSwcModeElement(DiagnosticEnvModeElement):
    """AUTOSAR DiagnosticEnvSwcModeElement."""

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
        """Initialize DiagnosticEnvSwcModeElement."""
        super().__init__()
        self.mode: Optional[ModeDeclaration] = None


class DiagnosticEnvSwcModeElementBuilder:
    """Builder for DiagnosticEnvSwcModeElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEnvSwcModeElement = DiagnosticEnvSwcModeElement()

    def build(self) -> DiagnosticEnvSwcModeElement:
        """Build and return DiagnosticEnvSwcModeElement object.

        Returns:
            DiagnosticEnvSwcModeElement instance
        """
        # TODO: Add validation
        return self._obj
