"""DiagnosticJ1939Spn AUTOSAR element."""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticJ1939Spn(DiagnosticCommonElement):
    """AUTOSAR DiagnosticJ1939Spn."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize DiagnosticJ1939Spn."""
        super().__init__()


class DiagnosticJ1939SpnBuilder:
    """Builder for DiagnosticJ1939Spn."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticJ1939Spn = DiagnosticJ1939Spn()

    def build(self) -> DiagnosticJ1939Spn:
        """Build and return DiagnosticJ1939Spn object.

        Returns:
            DiagnosticJ1939Spn instance
        """
        # TODO: Add validation
        return self._obj
