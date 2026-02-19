"""DiagnosticAuthRole AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 77)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class DiagnosticAuthRole(DiagnosticCommonElement):
    """AUTOSAR DiagnosticAuthRole."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bit_position: Optional[PositiveInteger]
    is_default: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize DiagnosticAuthRole."""
        super().__init__()
        self.bit_position: Optional[PositiveInteger] = None
        self.is_default: Optional[Boolean] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticAuthRole":
        """Deserialize XML element to DiagnosticAuthRole object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticAuthRole object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse bit_position
        child = ARObject._find_child_element(element, "BIT-POSITION")
        if child is not None:
            bit_position_value = child.text
            obj.bit_position = bit_position_value

        # Parse is_default
        child = ARObject._find_child_element(element, "IS-DEFAULT")
        if child is not None:
            is_default_value = child.text
            obj.is_default = is_default_value

        return obj



class DiagnosticAuthRoleBuilder:
    """Builder for DiagnosticAuthRole."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticAuthRole = DiagnosticAuthRole()

    def build(self) -> DiagnosticAuthRole:
        """Build and return DiagnosticAuthRole object.

        Returns:
            DiagnosticAuthRole instance
        """
        # TODO: Add validation
        return self._obj
