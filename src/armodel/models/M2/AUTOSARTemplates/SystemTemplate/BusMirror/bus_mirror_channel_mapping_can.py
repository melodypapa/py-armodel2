"""BusMirrorChannelMappingCan AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "can_id_ranges": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=BusMirrorCanIdRangeMapping,
        ),  # canIdRanges
        "can_id_to_can_ids": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=BusMirrorCanIdToCanIdMapping,
        ),  # canIdToCanIds
        "lin_pid_to_can_ids": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=BusMirrorLinPidToCanIdMapping,
        ),  # linPidToCanIds
        "mirror_source_lin": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # mirrorSourceLin
        "mirror_status": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # mirrorStatus
    }

    def __init__(self) -> None:
        """Initialize BusMirrorChannelMappingCan."""
        super().__init__()
        self.can_id_ranges: list[BusMirrorCanIdRangeMapping] = []
        self.can_id_to_can_ids: list[BusMirrorCanIdToCanIdMapping] = []
        self.lin_pid_to_can_ids: list[BusMirrorLinPidToCanIdMapping] = []
        self.mirror_source_lin: Optional[PositiveInteger] = None
        self.mirror_status: Optional[PositiveInteger] = None


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
