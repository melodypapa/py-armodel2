"""IEEE1722TpAcfCanPart AUTOSAR element."""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class IEEE1722TpAcfCanPart(IEEE1722TpAcfBusPart):
    """AUTOSAR IEEE1722TpAcfCanPart."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize IEEE1722TpAcfCanPart."""
        super().__init__()


class IEEE1722TpAcfCanPartBuilder:
    """Builder for IEEE1722TpAcfCanPart."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IEEE1722TpAcfCanPart = IEEE1722TpAcfCanPart()

    def build(self) -> IEEE1722TpAcfCanPart:
        """Build and return IEEE1722TpAcfCanPart object.

        Returns:
            IEEE1722TpAcfCanPart instance
        """
        # TODO: Add validation
        return self._obj
