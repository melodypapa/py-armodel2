"""DiagnosticEnvBswModeElement AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 90)

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


class DiagnosticEnvBswModeElement(DiagnosticEnvModeElement):
    """AUTOSAR DiagnosticEnvBswModeElement."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    mode: Optional[ModeDeclaration]
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
