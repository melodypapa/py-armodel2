"""BusMirrorChannelMappingCan AUTOSAR element."""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class BusMirrorChannelMappingCan(BusMirrorChannelMapping):
    """AUTOSAR BusMirrorChannelMappingCan."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize BusMirrorChannelMappingCan."""
        super().__init__()


class BusMirrorChannelMappingCanBuilder:
    """Builder for BusMirrorChannelMappingCan."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BusMirrorChannelMappingCan = BusMirrorChannelMappingCan()

    def build(self) -> BusMirrorChannelMappingCan:
        """Build and return BusMirrorChannelMappingCan object.

        Returns:
            BusMirrorChannelMappingCan instance
        """
        # TODO: Add validation
        return self._obj
