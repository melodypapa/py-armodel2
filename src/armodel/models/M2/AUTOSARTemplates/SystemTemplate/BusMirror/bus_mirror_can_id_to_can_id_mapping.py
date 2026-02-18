"""BusMirrorCanIdToCanIdMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 702)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_BusMirror.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication.can_frame_triggering import (
    CanFrameTriggering,
)


class BusMirrorCanIdToCanIdMapping(ARObject):
    """AUTOSAR BusMirrorCanIdToCanIdMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    remapped_can_id: Optional[PositiveInteger]
    souce_can_id: Optional[CanFrameTriggering]
    def __init__(self) -> None:
        """Initialize BusMirrorCanIdToCanIdMapping."""
        super().__init__()
        self.remapped_can_id: Optional[PositiveInteger] = None
        self.souce_can_id: Optional[CanFrameTriggering] = None


class BusMirrorCanIdToCanIdMappingBuilder:
    """Builder for BusMirrorCanIdToCanIdMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BusMirrorCanIdToCanIdMapping = BusMirrorCanIdToCanIdMapping()

    def build(self) -> BusMirrorCanIdToCanIdMapping:
        """Build and return BusMirrorCanIdToCanIdMapping object.

        Returns:
            BusMirrorCanIdToCanIdMapping instance
        """
        # TODO: Add validation
        return self._obj
