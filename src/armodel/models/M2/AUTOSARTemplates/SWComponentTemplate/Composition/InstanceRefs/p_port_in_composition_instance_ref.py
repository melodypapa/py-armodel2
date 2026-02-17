"""PPortInCompositionInstanceRef AUTOSAR element."""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class PPortInCompositionInstanceRef(PortInCompositionTypeInstanceRef):
    """AUTOSAR PPortInCompositionInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize PPortInCompositionInstanceRef."""
        super().__init__()


class PPortInCompositionInstanceRefBuilder:
    """Builder for PPortInCompositionInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PPortInCompositionInstanceRef = PPortInCompositionInstanceRef()

    def build(self) -> PPortInCompositionInstanceRef:
        """Build and return PPortInCompositionInstanceRef object.

        Returns:
            PPortInCompositionInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
