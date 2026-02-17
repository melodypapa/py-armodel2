"""RModeGroupInAtomicSWCInstanceRef AUTOSAR element."""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class RModeGroupInAtomicSWCInstanceRef(ModeGroupInAtomicSwcInstanceRef):
    """AUTOSAR RModeGroupInAtomicSWCInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize RModeGroupInAtomicSWCInstanceRef."""
        super().__init__()


class RModeGroupInAtomicSWCInstanceRefBuilder:
    """Builder for RModeGroupInAtomicSWCInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RModeGroupInAtomicSWCInstanceRef = RModeGroupInAtomicSWCInstanceRef()

    def build(self) -> RModeGroupInAtomicSWCInstanceRef:
        """Build and return RModeGroupInAtomicSWCInstanceRef object.

        Returns:
            RModeGroupInAtomicSWCInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
