"""BusMirrorChannelMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 697)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_BusMirror.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror import (
    MirroringProtocolEnum,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror.bus_mirror_channel import (
    BusMirrorChannel,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class BusMirrorChannelMapping(FibexElement):
    """AUTOSAR BusMirrorChannelMapping."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "mirroring": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=MirroringProtocolEnum,
        ),  # mirroring
        "source_channel": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=BusMirrorChannel,
        ),  # sourceChannel
        "target_channel": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=BusMirrorChannel,
        ),  # targetChannel
        "target_pdus": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=PduTriggering,
        ),  # targetPdus
    }

    def __init__(self) -> None:
        """Initialize BusMirrorChannelMapping."""
        super().__init__()
        self.mirroring: Optional[MirroringProtocolEnum] = None
        self.source_channel: Optional[BusMirrorChannel] = None
        self.target_channel: Optional[BusMirrorChannel] = None
        self.target_pdus: list[PduTriggering] = []


class BusMirrorChannelMappingBuilder:
    """Builder for BusMirrorChannelMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BusMirrorChannelMapping = BusMirrorChannelMapping()

    def build(self) -> BusMirrorChannelMapping:
        """Build and return BusMirrorChannelMapping object.

        Returns:
            BusMirrorChannelMapping instance
        """
        # TODO: Add validation
        return self._obj
