"""DiagnosticEnableConditionPortMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 251)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_sw_mapping import (
    DiagnosticSwMapping,
)


class DiagnosticEnableConditionPortMapping(DiagnosticSwMapping):
    """AUTOSAR DiagnosticEnableConditionPortMapping."""

    def __init__(self) -> None:
        """Initialize DiagnosticEnableConditionPortMapping."""
        super().__init__()
        self.enable_condition: Optional[Any] = None
        self.swc_flat_service: Optional[Any] = None
        self.swc_service: Optional[Any] = None


class DiagnosticEnableConditionPortMappingBuilder:
    """Builder for DiagnosticEnableConditionPortMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEnableConditionPortMapping = DiagnosticEnableConditionPortMapping()

    def build(self) -> DiagnosticEnableConditionPortMapping:
        """Build and return DiagnosticEnableConditionPortMapping object.

        Returns:
            DiagnosticEnableConditionPortMapping instance
        """
        # TODO: Add validation
        return self._obj
