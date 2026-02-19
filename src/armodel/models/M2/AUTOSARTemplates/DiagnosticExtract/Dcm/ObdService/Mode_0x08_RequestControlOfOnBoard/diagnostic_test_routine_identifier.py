"""DiagnosticTestRoutineIdentifier AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 158)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_ObdService_Mode_0x08_RequestControlOfOnBoard.classes.json"""

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


class DiagnosticTestRoutineIdentifier(DiagnosticCommonElement):
    """AUTOSAR DiagnosticTestRoutineIdentifier."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    id: Optional[PositiveInteger]
    request_data: Optional[PositiveInteger]
    response_data: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DiagnosticTestRoutineIdentifier."""
        super().__init__()
        self.id: Optional[PositiveInteger] = None
        self.request_data: Optional[PositiveInteger] = None
        self.response_data: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticTestRoutineIdentifier":
        """Deserialize XML element to DiagnosticTestRoutineIdentifier object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticTestRoutineIdentifier object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse id
        child = ARObject._find_child_element(element, "ID")
        if child is not None:
            id_value = child.text
            obj.id = id_value

        # Parse request_data
        child = ARObject._find_child_element(element, "REQUEST-DATA")
        if child is not None:
            request_data_value = child.text
            obj.request_data = request_data_value

        # Parse response_data
        child = ARObject._find_child_element(element, "RESPONSE-DATA")
        if child is not None:
            response_data_value = child.text
            obj.response_data = response_data_value

        return obj



class DiagnosticTestRoutineIdentifierBuilder:
    """Builder for DiagnosticTestRoutineIdentifier."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticTestRoutineIdentifier = DiagnosticTestRoutineIdentifier()

    def build(self) -> DiagnosticTestRoutineIdentifier:
        """Build and return DiagnosticTestRoutineIdentifier object.

        Returns:
            DiagnosticTestRoutineIdentifier instance
        """
        # TODO: Add validation
        return self._obj
