"""UnassignFrameId AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 436)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_configuration_entry import (
    LinConfigurationEntry,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_frame_triggering import (
    LinFrameTriggering,
)


class UnassignFrameId(LinConfigurationEntry):
    """AUTOSAR UnassignFrameId."""

    def __init__(self) -> None:
        """Initialize UnassignFrameId."""
        super().__init__()
        self.unassigned: Optional[LinFrameTriggering] = None


class UnassignFrameIdBuilder:
    """Builder for UnassignFrameId."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UnassignFrameId = UnassignFrameId()

    def build(self) -> UnassignFrameId:
        """Build and return UnassignFrameId object.

        Returns:
            UnassignFrameId instance
        """
        # TODO: Add validation
        return self._obj
