"""DiagnosticRequestControlOfOnBoardDeviceClass AUTOSAR element."""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticRequestControlOfOnBoardDeviceClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticRequestControlOfOnBoardDeviceClass."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize DiagnosticRequestControlOfOnBoardDeviceClass."""
        super().__init__()


class DiagnosticRequestControlOfOnBoardDeviceClassBuilder:
    """Builder for DiagnosticRequestControlOfOnBoardDeviceClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRequestControlOfOnBoardDeviceClass = DiagnosticRequestControlOfOnBoardDeviceClass()

    def build(self) -> DiagnosticRequestControlOfOnBoardDeviceClass:
        """Build and return DiagnosticRequestControlOfOnBoardDeviceClass object.

        Returns:
            DiagnosticRequestControlOfOnBoardDeviceClass instance
        """
        # TODO: Add validation
        return self._obj
