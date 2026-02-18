"""DiagnosticAbstractParameter AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 37)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_CommonDiagnostics.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_data_element import (
    DiagnosticDataElement,
)
from abc import ABC, abstractmethod


class DiagnosticAbstractParameter(ARObject, ABC):
    """AUTOSAR DiagnosticAbstractParameter."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    bit_offset: Optional[PositiveInteger]
    data_element: Optional[DiagnosticDataElement]
    parameter_size: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DiagnosticAbstractParameter."""
        super().__init__()
        self.bit_offset: Optional[PositiveInteger] = None
        self.data_element: Optional[DiagnosticDataElement] = None
        self.parameter_size: Optional[PositiveInteger] = None


class DiagnosticAbstractParameterBuilder:
    """Builder for DiagnosticAbstractParameter."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticAbstractParameter = DiagnosticAbstractParameter()

    def build(self) -> DiagnosticAbstractParameter:
        """Build and return DiagnosticAbstractParameter object.

        Returns:
            DiagnosticAbstractParameter instance
        """
        # TODO: Add validation
        return self._obj
