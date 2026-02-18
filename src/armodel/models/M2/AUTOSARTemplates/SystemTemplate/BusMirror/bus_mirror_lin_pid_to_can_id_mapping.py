"""BusMirrorLinPidToCanIdMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 702)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_BusMirror.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_frame_triggering import (
    LinFrameTriggering,
)


class BusMirrorLinPidToCanIdMapping(ARObject):
    """AUTOSAR BusMirrorLinPidToCanIdMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    remapped_can_id: Optional[PositiveInteger]
    source_lin_pid_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize BusMirrorLinPidToCanIdMapping."""
        super().__init__()
        self.remapped_can_id: Optional[PositiveInteger] = None
        self.source_lin_pid_ref: Optional[ARRef] = None


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
