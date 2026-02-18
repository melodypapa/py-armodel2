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
