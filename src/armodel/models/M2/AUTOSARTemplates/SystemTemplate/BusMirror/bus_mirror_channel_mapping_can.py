"""BusMirrorChannelMappingCan AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror.bus_mirror_channel_mapping import (
    BusMirrorChannelMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror.bus_mirror_can_id_range_mapping import (
    BusMirrorCanIdRangeMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror.bus_mirror_can_id_to_can_id_mapping import (
    BusMirrorCanIdToCanIdMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror.bus_mirror_lin_pid_to_can_id_mapping import (
    BusMirrorLinPidToCanIdMapping,
)


class BusMirrorChannelMappingCan(BusMirrorChannelMapping):
    """AUTOSAR BusMirrorChannelMappingCan."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("can_id_ranges", None, False, True, BusMirrorCanIdRangeMapping),  # canIdRanges
        ("can_id_to_can_ids", None, False, True, BusMirrorCanIdToCanIdMapping),  # canIdToCanIds
        ("lin_pid_to_can_ids", None, False, True, BusMirrorLinPidToCanIdMapping),  # linPidToCanIds
        ("mirror_source_lin", None, True, False, None),  # mirrorSourceLin
        ("mirror_status", None, True, False, None),  # mirrorStatus
    ]

    def __init__(self) -> None:
        """Initialize BusMirrorChannelMappingCan."""
        super().__init__()
        self.can_id_ranges: list[BusMirrorCanIdRangeMapping] = []
        self.can_id_to_can_ids: list[BusMirrorCanIdToCanIdMapping] = []
        self.lin_pid_to_can_ids: list[BusMirrorLinPidToCanIdMapping] = []
        self.mirror_source_lin: Optional[PositiveInteger] = None
        self.mirror_status: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BusMirrorChannelMappingCan to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BusMirrorChannelMappingCan":
        """Create BusMirrorChannelMappingCan from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BusMirrorChannelMappingCan instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BusMirrorChannelMappingCan since parent returns ARObject
        return cast("BusMirrorChannelMappingCan", obj)


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
