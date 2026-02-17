"""ComponentInCompositionInstanceRef AUTOSAR element."""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class ComponentInCompositionInstanceRef(ARObject):
    """AUTOSAR ComponentInCompositionInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize ComponentInCompositionInstanceRef."""
        super().__init__()


class ComponentInCompositionInstanceRefBuilder:
    """Builder for ComponentInCompositionInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ComponentInCompositionInstanceRef = ComponentInCompositionInstanceRef()

    def build(self) -> ComponentInCompositionInstanceRef:
        """Build and return ComponentInCompositionInstanceRef object.

        Returns:
            ComponentInCompositionInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
