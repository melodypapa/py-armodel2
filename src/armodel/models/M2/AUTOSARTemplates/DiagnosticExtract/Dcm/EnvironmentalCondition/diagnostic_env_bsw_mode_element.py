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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEnvBswModeElement":
        """Deserialize XML element to DiagnosticEnvBswModeElement object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticEnvBswModeElement object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse mode
        child = ARObject._find_child_element(element, "MODE")
        if child is not None:
            mode_value = ARObject._deserialize_by_tag(child, "ModeDeclaration")
            obj.mode = mode_value

        return obj



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
