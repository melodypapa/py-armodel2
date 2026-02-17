"""OperationInvokedEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 325)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 543)

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


class OperationInvokedEvent(RTEEvent):
    """AUTOSAR OperationInvokedEvent."""

    def __init__(self) -> None:
        """Initialize OperationInvokedEvent."""
        super().__init__()
        self.operation_instance_ref: Optional[ClientServerOperation] = None


class OperationInvokedEventBuilder:
    """Builder for OperationInvokedEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: OperationInvokedEvent = OperationInvokedEvent()

    def build(self) -> OperationInvokedEvent:
        """Build and return OperationInvokedEvent object.

        Returns:
            OperationInvokedEvent instance
        """
        # TODO: Add validation
        return self._obj
