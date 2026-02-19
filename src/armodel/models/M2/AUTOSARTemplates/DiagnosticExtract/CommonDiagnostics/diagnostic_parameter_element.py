"""DiagnosticParameterElement AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 36)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_CommonDiagnostics.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_parameter import (
    DiagnosticParameter,
)


class DiagnosticParameterElement(Identifiable):
    """AUTOSAR DiagnosticParameterElement."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    array_size: Optional[PositiveInteger]
    sub_elements: list[DiagnosticParameter]
    def __init__(self) -> None:
        """Initialize DiagnosticParameterElement."""
        super().__init__()
        self.array_size: Optional[PositiveInteger] = None
        self.sub_elements: list[DiagnosticParameter] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticParameterElement":
        """Deserialize XML element to DiagnosticParameterElement object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticParameterElement object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse array_size
        child = ARObject._find_child_element(element, "ARRAY-SIZE")
        if child is not None:
            array_size_value = child.text
            obj.array_size = array_size_value

        # Parse sub_elements (list)
        obj.sub_elements = []
        for child in ARObject._find_all_child_elements(element, "SUB-ELEMENTS"):
            sub_elements_value = ARObject._deserialize_by_tag(child, "DiagnosticParameter")
            obj.sub_elements.append(sub_elements_value)

        return obj



class DiagnosticParameterElementBuilder:
    """Builder for DiagnosticParameterElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticParameterElement = DiagnosticParameterElement()

    def build(self) -> DiagnosticParameterElement:
        """Build and return DiagnosticParameterElement object.

        Returns:
            DiagnosticParameterElement instance
        """
        # TODO: Add validation
        return self._obj
