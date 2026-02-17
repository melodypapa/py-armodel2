"""DataReceivedEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 542)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_RTEEvents.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class DataReceivedEvent(RTEEvent):
    """AUTOSAR DataReceivedEvent."""

    data: Optional[VariableDataPrototype]
    def __init__(self) -> None:
        """Initialize DataReceivedEvent."""
        super().__init__()
        self.data: Optional[VariableDataPrototype] = None


class DataReceivedEventBuilder:
    """Builder for DataReceivedEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataReceivedEvent = DataReceivedEvent()

    def build(self) -> DataReceivedEvent:
        """Build and return DataReceivedEvent object.

        Returns:
            DataReceivedEvent instance
        """
        # TODO: Add validation
        return self._obj
