"""DiagnosticOperationCycle AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 201)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticOperationCycle.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticOperationCycle(DiagnosticCommonElement):
    """AUTOSAR DiagnosticOperationCycle."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    type_cycle_type_enum: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticOperationCycle."""
        super().__init__()
        self.type_cycle_type_enum: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticOperationCycle":
        """Deserialize XML element to DiagnosticOperationCycle object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticOperationCycle object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticOperationCycle, cls).deserialize(element)

        # Parse type_cycle_type_enum
        child = ARObject._find_child_element(element, "TYPE-CYCLE-TYPE-ENUM")
        if child is not None:
            type_cycle_type_enum_value = child.text
            obj.type_cycle_type_enum = type_cycle_type_enum_value

        return obj



class DiagnosticOperationCycleBuilder:
    """Builder for DiagnosticOperationCycle."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticOperationCycle = DiagnosticOperationCycle()

    def build(self) -> DiagnosticOperationCycle:
        """Build and return DiagnosticOperationCycle object.

        Returns:
            DiagnosticOperationCycle instance
        """
        # TODO: Add validation
        return self._obj
