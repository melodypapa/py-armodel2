"""DiagnosticReadDataByPeriodicID AUTOSAR element."""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticReadDataByPeriodicID(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticReadDataByPeriodicID."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize DiagnosticReadDataByPeriodicID."""
        super().__init__()


class DiagnosticReadDataByPeriodicIDBuilder:
    """Builder for DiagnosticReadDataByPeriodicID."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticReadDataByPeriodicID = DiagnosticReadDataByPeriodicID()

    def build(self) -> DiagnosticReadDataByPeriodicID:
        """Build and return DiagnosticReadDataByPeriodicID object.

        Returns:
            DiagnosticReadDataByPeriodicID instance
        """
        # TODO: Add validation
        return self._obj
