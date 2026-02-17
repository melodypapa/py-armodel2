"""DiagnosticStorageConditionPortMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 253)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_sw_mapping import (
    DiagnosticSwMapping,
)


class DiagnosticStorageConditionPortMapping(DiagnosticSwMapping):
    """AUTOSAR DiagnosticStorageConditionPortMapping."""

    diagnostic_storage: Optional[Any]
    swc_flat_service: Optional[Any]
    swc_service: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticStorageConditionPortMapping."""
        super().__init__()
        self.diagnostic_storage: Optional[Any] = None
        self.swc_flat_service: Optional[Any] = None
        self.swc_service: Optional[Any] = None


class DiagnosticStorageConditionPortMappingBuilder:
    """Builder for DiagnosticStorageConditionPortMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticStorageConditionPortMapping = DiagnosticStorageConditionPortMapping()

    def build(self) -> DiagnosticStorageConditionPortMapping:
        """Build and return DiagnosticStorageConditionPortMapping object.

        Returns:
            DiagnosticStorageConditionPortMapping instance
        """
        # TODO: Add validation
        return self._obj
