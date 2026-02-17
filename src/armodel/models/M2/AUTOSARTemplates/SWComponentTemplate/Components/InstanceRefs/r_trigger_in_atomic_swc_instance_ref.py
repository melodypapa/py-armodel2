"""RTriggerInAtomicSwcInstanceRef AUTOSAR element."""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class RTriggerInAtomicSwcInstanceRef(TriggerInAtomicSwcInstanceRef):
    """AUTOSAR RTriggerInAtomicSwcInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize RTriggerInAtomicSwcInstanceRef."""
        super().__init__()


class RTriggerInAtomicSwcInstanceRefBuilder:
    """Builder for RTriggerInAtomicSwcInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RTriggerInAtomicSwcInstanceRef = RTriggerInAtomicSwcInstanceRef()

    def build(self) -> RTriggerInAtomicSwcInstanceRef:
        """Build and return RTriggerInAtomicSwcInstanceRef object.

        Returns:
            RTriggerInAtomicSwcInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
