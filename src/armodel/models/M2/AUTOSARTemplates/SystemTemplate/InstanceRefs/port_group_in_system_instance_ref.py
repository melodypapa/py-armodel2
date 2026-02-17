"""PortGroupInSystemInstanceRef AUTOSAR element."""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class PortGroupInSystemInstanceRef(ARObject):
    """AUTOSAR PortGroupInSystemInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize PortGroupInSystemInstanceRef."""
        super().__init__()


class PortGroupInSystemInstanceRefBuilder:
    """Builder for PortGroupInSystemInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PortGroupInSystemInstanceRef = PortGroupInSystemInstanceRef()

    def build(self) -> PortGroupInSystemInstanceRef:
        """Build and return PortGroupInSystemInstanceRef object.

        Returns:
            PortGroupInSystemInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
