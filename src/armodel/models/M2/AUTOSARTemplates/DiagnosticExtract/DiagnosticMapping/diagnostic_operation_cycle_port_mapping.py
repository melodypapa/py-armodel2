"""DiagnosticOperationCyclePortMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 250)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_sw_mapping import (
    DiagnosticSwMapping,
)


class DiagnosticOperationCyclePortMapping(DiagnosticSwMapping):
    """AUTOSAR DiagnosticOperationCyclePortMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    operation_cycle: Optional[Any]
    swc_flat_service: Optional[Any]
    swc_service: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticOperationCyclePortMapping."""
        super().__init__()
        self.operation_cycle: Optional[Any] = None
        self.swc_flat_service: Optional[Any] = None
        self.swc_service: Optional[Any] = None


class DiagnosticOperationCyclePortMappingBuilder:
    """Builder for DiagnosticOperationCyclePortMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticOperationCyclePortMapping = DiagnosticOperationCyclePortMapping()

    def build(self) -> DiagnosticOperationCyclePortMapping:
        """Build and return DiagnosticOperationCyclePortMapping object.

        Returns:
            DiagnosticOperationCyclePortMapping instance
        """
        # TODO: Add validation
        return self._obj
