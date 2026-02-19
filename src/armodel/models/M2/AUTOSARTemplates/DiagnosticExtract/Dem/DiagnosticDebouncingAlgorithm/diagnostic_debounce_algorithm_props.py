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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticDebounceAlgorithmProps":
        """Deserialize XML element to DiagnosticDebounceAlgorithmProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticDebounceAlgorithmProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticDebounceAlgorithmProps, cls).deserialize(element)

        # Parse debounce
        child = ARObject._find_child_element(element, "DEBOUNCE")
        if child is not None:
            debounce_value = child.text
            obj.debounce = debounce_value

        return obj



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
