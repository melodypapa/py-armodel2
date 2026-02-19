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
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticParameterIdent, cls).deserialize(element)

        # Parse sub_elements (list from container "SUB-ELEMENTS")
        obj.sub_elements = []
        container = ARObject._find_child_element(element, "SUB-ELEMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sub_elements.append(child_value)

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
