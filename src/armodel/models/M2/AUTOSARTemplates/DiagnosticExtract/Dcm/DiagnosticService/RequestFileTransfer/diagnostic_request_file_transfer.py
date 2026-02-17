"""DiagnosticRequestFileTransfer AUTOSAR element."""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticRequestFileTransfer(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticRequestFileTransfer."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize DiagnosticRequestFileTransfer."""
        super().__init__()


class DiagnosticRequestFileTransferBuilder:
    """Builder for DiagnosticRequestFileTransfer."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRequestFileTransfer = DiagnosticRequestFileTransfer()

    def build(self) -> DiagnosticRequestFileTransfer:
        """Build and return DiagnosticRequestFileTransfer object.

        Returns:
            DiagnosticRequestFileTransfer instance
        """
        # TODO: Add validation
        return self._obj
