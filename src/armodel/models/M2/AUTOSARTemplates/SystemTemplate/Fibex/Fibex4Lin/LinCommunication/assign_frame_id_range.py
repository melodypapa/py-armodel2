"""AssignFrameIdRange AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 437)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_configuration_entry import (
    LinConfigurationEntry,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.frame_pid import (
    FramePid,
)


class AssignFrameIdRange(LinConfigurationEntry):
    """AUTOSAR AssignFrameIdRange."""

    frame_pid: FramePid
    start_index: Optional[Integer]
    def __init__(self) -> None:
        """Initialize AssignFrameIdRange."""
        super().__init__()
        self.frame_pid: FramePid = None
        self.start_index: Optional[Integer] = None


class AssignFrameIdRangeBuilder:
    """Builder for AssignFrameIdRange."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AssignFrameIdRange = AssignFrameIdRange()

    def build(self) -> AssignFrameIdRange:
        """Build and return AssignFrameIdRange object.

        Returns:
            AssignFrameIdRange instance
        """
        # TODO: Add validation
        return self._obj
