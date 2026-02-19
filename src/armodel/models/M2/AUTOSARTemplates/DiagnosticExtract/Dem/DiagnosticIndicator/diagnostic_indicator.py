"""DiagnosticIndicator AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 203)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticIndicator.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticIndicator import (
    DiagnosticIndicatorTypeEnum,
)


class DiagnosticIndicator(DiagnosticCommonElement):
    """AUTOSAR DiagnosticIndicator."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    type: Optional[DiagnosticIndicatorTypeEnum]
    def __init__(self) -> None:
        """Initialize DiagnosticIndicator."""
        super().__init__()
        self.type: Optional[DiagnosticIndicatorTypeEnum] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticIndicator":
        """Deserialize XML element to DiagnosticIndicator object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticIndicator object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticIndicator, cls).deserialize(element)

        # Parse type
        child = ARObject._find_child_element(element, "TYPE")
        if child is not None:
            type_value = DiagnosticIndicatorTypeEnum.deserialize(child)
            obj.type = type_value

        return obj



class DiagnosticIndicatorBuilder:
    """Builder for DiagnosticIndicator."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticIndicator = DiagnosticIndicator()

    def build(self) -> DiagnosticIndicator:
        """Build and return DiagnosticIndicator object.

        Returns:
            DiagnosticIndicator instance
        """
        # TODO: Add validation
        return self._obj
