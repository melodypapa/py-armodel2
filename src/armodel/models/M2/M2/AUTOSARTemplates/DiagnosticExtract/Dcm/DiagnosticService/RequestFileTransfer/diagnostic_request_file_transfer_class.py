"""DiagnosticRequestFileTransferClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 147)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_RequestFileTransfer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)


class DiagnosticRequestFileTransferClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticRequestFileTransferClass."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize DiagnosticRequestFileTransferClass."""
        super().__init__()


class DiagnosticRequestFileTransferClassBuilder:
    """Builder for DiagnosticRequestFileTransferClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRequestFileTransferClass = DiagnosticRequestFileTransferClass()

    def build(self) -> DiagnosticRequestFileTransferClass:
        """Build and return DiagnosticRequestFileTransferClass object.

        Returns:
            DiagnosticRequestFileTransferClass instance
        """
        # TODO: Add validation
        return self._obj
