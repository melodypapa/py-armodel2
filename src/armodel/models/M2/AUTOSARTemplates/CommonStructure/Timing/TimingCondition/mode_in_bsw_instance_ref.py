"""ModeInBswInstanceRef AUTOSAR element."""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class ModeInBswInstanceRef(ARObject):
    """AUTOSAR ModeInBswInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize ModeInBswInstanceRef."""
        super().__init__()


class ModeInBswInstanceRefBuilder:
    """Builder for ModeInBswInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeInBswInstanceRef = ModeInBswInstanceRef()

    def build(self) -> ModeInBswInstanceRef:
        """Build and return ModeInBswInstanceRef object.

        Returns:
            ModeInBswInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
