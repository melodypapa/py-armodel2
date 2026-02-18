"""DiagnosticEnvSwcModeElement AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 89)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_EnvironmentalCondition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.EnvironmentalCondition.diagnostic_env_mode_element import (
    DiagnosticEnvModeElement,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)


class DiagnosticEnvSwcModeElement(DiagnosticEnvModeElement):
    """AUTOSAR DiagnosticEnvSwcModeElement."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    mode: Optional[ModeDeclaration]
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
