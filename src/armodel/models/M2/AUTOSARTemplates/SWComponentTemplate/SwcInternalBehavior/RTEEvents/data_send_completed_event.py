"""DataSendCompletedEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 542)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_RTEEvents.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.variable_access import (
    VariableAccess,
)


class DataSendCompletedEvent(RTEEvent):
    """AUTOSAR DataSendCompletedEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    event_source: Optional[VariableAccess]
    def __init__(self) -> None:
        """Initialize DataSendCompletedEvent."""
        super().__init__()
        self.event_source: Optional[VariableAccess] = None


class DataSendCompletedEventBuilder:
    """Builder for DataSendCompletedEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataSendCompletedEvent = DataSendCompletedEvent()

    def build(self) -> DataSendCompletedEvent:
        """Build and return DataSendCompletedEvent object.

        Returns:
            DataSendCompletedEvent instance
        """
        # TODO: Add validation
        return self._obj
