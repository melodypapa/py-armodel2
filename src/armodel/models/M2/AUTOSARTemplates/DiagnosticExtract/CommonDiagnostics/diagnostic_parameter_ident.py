"""DiagnosticParameterIdent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 37)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_CommonDiagnostics.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario.ident_caption import (
    IdentCaption,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_parameter import (
    DiagnosticParameter,
)


class DiagnosticParameterIdent(IdentCaption):
    """AUTOSAR DiagnosticParameterIdent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    sub_elements: list[DiagnosticParameter]
    def __init__(self) -> None:
        """Initialize DiagnosticParameterIdent."""
        super().__init__()
        self.sub_elements: list[DiagnosticParameter] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticParameterIdent":
        """Deserialize XML element to DiagnosticParameterIdent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticParameterIdent object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse sub_elements (list)
        obj.sub_elements = []
        for child in ARObject._find_all_child_elements(element, "SUB-ELEMENTS"):
            sub_elements_value = ARObject._deserialize_by_tag(child, "DiagnosticParameter")
            obj.sub_elements.append(sub_elements_value)

        return obj



class DiagnosticParameterIdentBuilder:
    """Builder for DiagnosticParameterIdent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticParameterIdent = DiagnosticParameterIdent()

    def build(self) -> DiagnosticParameterIdent:
        """Build and return DiagnosticParameterIdent object.

        Returns:
            DiagnosticParameterIdent instance
        """
        # TODO: Add validation
        return self._obj
