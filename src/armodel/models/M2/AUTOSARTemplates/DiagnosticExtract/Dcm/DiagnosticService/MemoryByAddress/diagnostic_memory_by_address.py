"""DiagnosticMemoryByAddress AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 139)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_MemoryByAddress.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from abc import ABC, abstractmethod


class DiagnosticMemoryByAddress(DiagnosticServiceInstance, ABC):
    """AUTOSAR DiagnosticMemoryByAddress."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize DiagnosticMemoryByAddress."""
        super().__init__()


class DiagnosticMemoryByAddressBuilder:
    """Builder for DiagnosticMemoryByAddress."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticMemoryByAddress = DiagnosticMemoryByAddress()

    def build(self) -> DiagnosticMemoryByAddress:
        """Build and return DiagnosticMemoryByAddress object.

        Returns:
            DiagnosticMemoryByAddress instance
        """
        # TODO: Add validation
        return self._obj
