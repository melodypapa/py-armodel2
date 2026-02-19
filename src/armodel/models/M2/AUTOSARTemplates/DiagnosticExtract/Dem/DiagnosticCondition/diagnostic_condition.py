"""DiagnosticCondition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 194)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticCondition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from abc import ABC, abstractmethod


class DiagnosticCondition(DiagnosticCommonElement, ABC):
    """AUTOSAR DiagnosticCondition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    init_value: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize DiagnosticCondition."""
        super().__init__()
        self.init_value: Optional[Boolean] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticCondition":
        """Deserialize XML element to DiagnosticCondition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticCondition object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse init_value
        child = ARObject._find_child_element(element, "INIT-VALUE")
        if child is not None:
            init_value_value = child.text
            obj.init_value = init_value_value

        return obj



class DiagnosticConditionBuilder:
    """Builder for DiagnosticCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticCondition = DiagnosticCondition()

    def build(self) -> DiagnosticCondition:
        """Build and return DiagnosticCondition object.

        Returns:
            DiagnosticCondition instance
        """
        # TODO: Add validation
        return self._obj
