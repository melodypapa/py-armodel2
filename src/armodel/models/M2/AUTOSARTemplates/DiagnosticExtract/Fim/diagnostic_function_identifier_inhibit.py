"""DiagnosticFunctionIdentifierInhibit AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 215)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Fim.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Fim import (
    DiagnosticInhibitionMaskEnum,
)


class DiagnosticFunctionIdentifierInhibit(DiagnosticCommonElement):
    """AUTOSAR DiagnosticFunctionIdentifierInhibit."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    function: Optional[Any]
    inhibition_mask: Optional[DiagnosticInhibitionMaskEnum]
    inhibit_sources: list[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticFunctionIdentifierInhibit."""
        super().__init__()
        self.function: Optional[Any] = None
        self.inhibition_mask: Optional[DiagnosticInhibitionMaskEnum] = None
        self.inhibit_sources: list[Any] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticFunctionIdentifierInhibit":
        """Deserialize XML element to DiagnosticFunctionIdentifierInhibit object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticFunctionIdentifierInhibit object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse function
        child = ARObject._find_child_element(element, "FUNCTION")
        if child is not None:
            function_value = child.text
            obj.function = function_value

        # Parse inhibition_mask
        child = ARObject._find_child_element(element, "INHIBITION-MASK")
        if child is not None:
            inhibition_mask_value = child.text
            obj.inhibition_mask = inhibition_mask_value

        # Parse inhibit_sources (list)
        obj.inhibit_sources = []
        for child in ARObject._find_all_child_elements(element, "INHIBIT-SOURCES"):
            inhibit_sources_value = child.text
            obj.inhibit_sources.append(inhibit_sources_value)

        return obj



class DiagnosticFunctionIdentifierInhibitBuilder:
    """Builder for DiagnosticFunctionIdentifierInhibit."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticFunctionIdentifierInhibit = DiagnosticFunctionIdentifierInhibit()

    def build(self) -> DiagnosticFunctionIdentifierInhibit:
        """Build and return DiagnosticFunctionIdentifierInhibit object.

        Returns:
            DiagnosticFunctionIdentifierInhibit instance
        """
        # TODO: Add validation
        return self._obj
