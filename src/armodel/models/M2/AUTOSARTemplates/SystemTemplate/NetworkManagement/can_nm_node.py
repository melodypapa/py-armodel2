"""CanNmNode AUTOSAR element."""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class CanNmNode(NmNode):
    """AUTOSAR CanNmNode."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize CanNmNode."""
        super().__init__()


class CanNmNodeBuilder:
    """Builder for CanNmNode."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanNmNode = CanNmNode()

    def build(self) -> CanNmNode:
        """Build and return CanNmNode object.

        Returns:
            CanNmNode instance
        """
        # TODO: Add validation
        return self._obj
