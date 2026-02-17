"""VariableInAtomicSWCTypeInstanceRef AUTOSAR element."""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class VariableInAtomicSWCTypeInstanceRef(ARObject):
    """AUTOSAR VariableInAtomicSWCTypeInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize VariableInAtomicSWCTypeInstanceRef."""
        super().__init__()


class VariableInAtomicSWCTypeInstanceRefBuilder:
    """Builder for VariableInAtomicSWCTypeInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: VariableInAtomicSWCTypeInstanceRef = VariableInAtomicSWCTypeInstanceRef()

    def build(self) -> VariableInAtomicSWCTypeInstanceRef:
        """Build and return VariableInAtomicSWCTypeInstanceRef object.

        Returns:
            VariableInAtomicSWCTypeInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
