"""DiagnosticAging AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 202)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticAging.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DiagnosticAging(DiagnosticCommonElement):
    """AUTOSAR DiagnosticAging."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    aging_cycle: Optional[Any]
    threshold: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DiagnosticAging."""
        super().__init__()
        self.aging_cycle: Optional[Any] = None
        self.threshold: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticAging":
        """Deserialize XML element to DiagnosticAging object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticAging object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticAging, cls).deserialize(element)

        # Parse aging_cycle
        child = ARObject._find_child_element(element, "AGING-CYCLE")
        if child is not None:
            aging_cycle_value = child.text
            obj.aging_cycle = aging_cycle_value

        # Parse threshold
        child = ARObject._find_child_element(element, "THRESHOLD")
        if child is not None:
            threshold_value = child.text
            obj.threshold = threshold_value

        return obj



class DiagnosticAgingBuilder:
    """Builder for DiagnosticAging."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticAging = DiagnosticAging()

    def build(self) -> DiagnosticAging:
        """Build and return DiagnosticAging object.

        Returns:
            DiagnosticAging instance
        """
        # TODO: Add validation
        return self._obj
