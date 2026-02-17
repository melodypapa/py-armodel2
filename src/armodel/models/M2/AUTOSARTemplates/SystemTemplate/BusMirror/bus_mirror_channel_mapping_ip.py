"""BusMirrorChannelMappingIp AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 705)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_BusMirror.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror.bus_mirror_channel_mapping import (
    BusMirrorChannelMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class BusMirrorChannelMappingIp(BusMirrorChannelMapping):
    """AUTOSAR BusMirrorChannelMappingIp."""

    def __init__(self) -> None:
        """Initialize BusMirrorChannelMappingIp."""
        super().__init__()
        self.transmission: Optional[TimeValue] = None


class BusMirrorChannelMappingIpBuilder:
    """Builder for BusMirrorChannelMappingIp."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BusMirrorChannelMappingIp = BusMirrorChannelMappingIp()

    def build(self) -> BusMirrorChannelMappingIp:
        """Build and return BusMirrorChannelMappingIp object.

        Returns:
            BusMirrorChannelMappingIp instance
        """
        # TODO: Add validation
        return self._obj
