"""BusMirrorLinPidToCanIdMapping AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_frame_triggering import (
    LinFrameTriggering,
)


class BusMirrorLinPidToCanIdMapping(ARObject):
    """AUTOSAR BusMirrorLinPidToCanIdMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "remapped_can_id": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # remappedCanId
        "source_lin_pid": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=LinFrameTriggering,
        ),  # sourceLinPid
    }

    def __init__(self) -> None:
        """Initialize BusMirrorLinPidToCanIdMapping."""
        super().__init__()
        self.remapped_can_id: Optional[PositiveInteger] = None
        self.source_lin_pid: Optional[LinFrameTriggering] = None


class BusMirrorLinPidToCanIdMappingBuilder:
    """Builder for BusMirrorLinPidToCanIdMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BusMirrorLinPidToCanIdMapping = BusMirrorLinPidToCanIdMapping()

    def build(self) -> BusMirrorLinPidToCanIdMapping:
        """Build and return BusMirrorLinPidToCanIdMapping object.

        Returns:
            BusMirrorLinPidToCanIdMapping instance
        """
        # TODO: Add validation
        return self._obj
