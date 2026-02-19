"""DiagnosticInfoType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 160)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_CommonDiagnostics.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_parameter import (
    DiagnosticParameter,
)


class DiagnosticInfoType(DiagnosticCommonElement):
    """AUTOSAR DiagnosticInfoType."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_elements: list[DiagnosticParameter]
    id: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DiagnosticInfoType."""
        super().__init__()
        self.data_elements: list[DiagnosticParameter] = []
        self.id: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticInfoType":
        """Deserialize XML element to DiagnosticInfoType object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticInfoType object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse data_elements (list)
        obj.data_elements = []
        for child in ARObject._find_all_child_elements(element, "DATA-ELEMENTS"):
            data_elements_value = ARObject._deserialize_by_tag(child, "DiagnosticParameter")
            obj.data_elements.append(data_elements_value)

        # Parse id
        child = ARObject._find_child_element(element, "ID")
        if child is not None:
            id_value = child.text
            obj.id = id_value

        return obj



class DiagnosticInfoTypeBuilder:
    """Builder for DiagnosticInfoType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticInfoType = DiagnosticInfoType()

    def build(self) -> DiagnosticInfoType:
        """Build and return DiagnosticInfoType object.

        Returns:
            DiagnosticInfoType instance
        """
        # TODO: Add validation
        return self._obj
