"""ModeInSwcInstanceRef AUTOSAR element."""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class ModeInSwcInstanceRef(ARObject):
    """AUTOSAR ModeInSwcInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize ModeInSwcInstanceRef."""
        super().__init__()


class ModeInSwcInstanceRefBuilder:
    """Builder for ModeInSwcInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeInSwcInstanceRef = ModeInSwcInstanceRef()

    def build(self) -> ModeInSwcInstanceRef:
        """Build and return ModeInSwcInstanceRef object.

        Returns:
            ModeInSwcInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
