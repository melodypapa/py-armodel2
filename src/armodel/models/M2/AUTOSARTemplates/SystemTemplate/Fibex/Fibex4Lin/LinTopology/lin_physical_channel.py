"""LinPhysicalChannel AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 99)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_schedule_table import (
    LinScheduleTable,
)


class LinPhysicalChannel(PhysicalChannel):
    """AUTOSAR LinPhysicalChannel."""

    def __init__(self) -> None:
        """Initialize LinPhysicalChannel."""
        super().__init__()
        self.bus_idle_timeout: Optional[TimeValue] = None
        self.schedule_tables: list[LinScheduleTable] = []


class LinPhysicalChannelBuilder:
    """Builder for LinPhysicalChannel."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinPhysicalChannel = LinPhysicalChannel()

    def build(self) -> LinPhysicalChannel:
        """Build and return LinPhysicalChannel object.

        Returns:
            LinPhysicalChannel instance
        """
        # TODO: Add validation
        return self._obj
