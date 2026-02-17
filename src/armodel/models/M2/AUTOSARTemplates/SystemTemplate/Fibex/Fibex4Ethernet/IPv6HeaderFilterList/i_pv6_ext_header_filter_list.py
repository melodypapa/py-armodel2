"""IPv6ExtHeaderFilterList AUTOSAR element."""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class IPv6ExtHeaderFilterList(Identifiable):
    """AUTOSAR IPv6ExtHeaderFilterList."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize IPv6ExtHeaderFilterList."""
        super().__init__()


class IPv6ExtHeaderFilterListBuilder:
    """Builder for IPv6ExtHeaderFilterList."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IPv6ExtHeaderFilterList = IPv6ExtHeaderFilterList()

    def build(self) -> IPv6ExtHeaderFilterList:
        """Build and return IPv6ExtHeaderFilterList object.

        Returns:
            IPv6ExtHeaderFilterList instance
        """
        # TODO: Add validation
        return self._obj
