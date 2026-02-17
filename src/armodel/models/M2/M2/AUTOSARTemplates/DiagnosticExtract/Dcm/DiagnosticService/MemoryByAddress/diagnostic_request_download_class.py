"""DiagnosticRequestDownloadClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 144)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_MemoryByAddress.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)


class DiagnosticRequestDownloadClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticRequestDownloadClass."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize DiagnosticRequestDownloadClass."""
        super().__init__()


class DiagnosticRequestDownloadClassBuilder:
    """Builder for DiagnosticRequestDownloadClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRequestDownloadClass = DiagnosticRequestDownloadClass()

    def build(self) -> DiagnosticRequestDownloadClass:
        """Build and return DiagnosticRequestDownloadClass object.

        Returns:
            DiagnosticRequestDownloadClass instance
        """
        # TODO: Add validation
        return self._obj
