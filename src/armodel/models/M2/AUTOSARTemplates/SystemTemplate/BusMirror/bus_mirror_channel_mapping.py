"""BusMirrorChannelMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
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
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("mirroring", None, False, False, MirroringProtocolEnum),  # mirroring
        ("source_channel", None, False, False, BusMirrorChannel),  # sourceChannel
        ("target_channel", None, False, False, BusMirrorChannel),  # targetChannel
        ("target_pdus", None, False, True, PduTriggering),  # targetPdus
    ]

    def __init__(self) -> None:
        """Initialize BusMirrorChannelMapping."""
        super().__init__()
        self.mirroring: Optional[MirroringProtocolEnum] = None
        self.source_channel: Optional[BusMirrorChannel] = None
        self.target_channel: Optional[BusMirrorChannel] = None
        self.target_pdus: list[PduTriggering] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BusMirrorChannelMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BusMirrorChannelMapping":
        """Create BusMirrorChannelMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BusMirrorChannelMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BusMirrorChannelMapping since parent returns ARObject
        return cast("BusMirrorChannelMapping", obj)


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
