"""GlobalTimeCanSlave AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 864)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime_CAN.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_slave import (
    GlobalTimeSlave,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class GlobalTimeCanSlave(GlobalTimeSlave):
    """AUTOSAR GlobalTimeCanSlave."""

    crc_validated: Optional[Any]
    sequence: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize GlobalTimeCanSlave."""
        super().__init__()
        self.crc_validated: Optional[Any] = None
        self.sequence: Optional[PositiveInteger] = None


class GlobalTimeCanSlaveBuilder:
    """Builder for GlobalTimeCanSlave."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GlobalTimeCanSlave = GlobalTimeCanSlave()

    def build(self) -> GlobalTimeCanSlave:
        """Build and return GlobalTimeCanSlave object.

        Returns:
            GlobalTimeCanSlave instance
        """
        # TODO: Add validation
        return self._obj
