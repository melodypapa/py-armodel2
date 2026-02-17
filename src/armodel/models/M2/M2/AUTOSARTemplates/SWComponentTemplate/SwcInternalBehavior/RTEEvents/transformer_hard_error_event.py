"""TransformerHardErrorEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 546)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_RTEEvents.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)


class TransformerHardErrorEvent(RTEEvent):
    """AUTOSAR TransformerHardErrorEvent."""

    def __init__(self) -> None:
        """Initialize TransformerHardErrorEvent."""
        super().__init__()
        self.operation: Optional[ClientServerOperation] = None
        self.required_trigger: Optional[Trigger] = None


class TransformerHardErrorEventBuilder:
    """Builder for TransformerHardErrorEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TransformerHardErrorEvent = TransformerHardErrorEvent()

    def build(self) -> TransformerHardErrorEvent:
        """Build and return TransformerHardErrorEvent object.

        Returns:
            TransformerHardErrorEvent instance
        """
        # TODO: Add validation
        return self._obj
