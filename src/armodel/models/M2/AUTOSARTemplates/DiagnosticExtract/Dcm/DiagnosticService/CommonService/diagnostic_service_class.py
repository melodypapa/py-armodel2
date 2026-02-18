"""DiagnosticServiceClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 69)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_CommonService.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from abc import ABC, abstractmethod


class DiagnosticServiceClass(DiagnosticCommonElement, ABC):
    """AUTOSAR DiagnosticServiceClass."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize DiagnosticServiceClass."""
        super().__init__()


class DiagnosticServiceClassBuilder:
    """Builder for DiagnosticServiceClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticServiceClass = DiagnosticServiceClass()

    def build(self) -> DiagnosticServiceClass:
        """Build and return DiagnosticServiceClass object.

        Returns:
            DiagnosticServiceClass instance
        """
        # TODO: Add validation
        return self._obj
