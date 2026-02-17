"""BusMirrorChannelMappingFlexray AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 704)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_BusMirror.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror.bus_mirror_channel_mapping import (
    BusMirrorChannelMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class BusMirrorChannelMappingFlexray(BusMirrorChannelMapping):
    """AUTOSAR BusMirrorChannelMappingFlexray."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "transmission": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # transmission
    }

    def __init__(self) -> None:
        """Initialize BusMirrorChannelMappingFlexray."""
        super().__init__()
        self.transmission: Optional[TimeValue] = None


class BusMirrorChannelMappingFlexrayBuilder:
    """Builder for BusMirrorChannelMappingFlexray."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BusMirrorChannelMappingFlexray = BusMirrorChannelMappingFlexray()

    def build(self) -> BusMirrorChannelMappingFlexray:
        """Build and return BusMirrorChannelMappingFlexray object.

        Returns:
            BusMirrorChannelMappingFlexray instance
        """
        # TODO: Add validation
        return self._obj
