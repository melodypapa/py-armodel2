"""DiagnosticDebounceAlgorithmProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 195)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 438)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticDebouncingAlgorithm.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class DiagnosticDebounceAlgorithmProps(Identifiable):
    """AUTOSAR DiagnosticDebounceAlgorithmProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    debounce: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize DiagnosticDebounceAlgorithmProps."""
        super().__init__()
        self.debounce: Optional[Boolean] = None


class DiagnosticDebounceAlgorithmPropsBuilder:
    """Builder for DiagnosticDebounceAlgorithmProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticDebounceAlgorithmProps = DiagnosticDebounceAlgorithmProps()

    def build(self) -> DiagnosticDebounceAlgorithmProps:
        """Build and return DiagnosticDebounceAlgorithmProps object.

        Returns:
            DiagnosticDebounceAlgorithmProps instance
        """
        # TODO: Add validation
        return self._obj
