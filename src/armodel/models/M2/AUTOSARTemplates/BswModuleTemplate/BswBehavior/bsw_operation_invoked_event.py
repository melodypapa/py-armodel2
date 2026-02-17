"""BswOperationInvokedEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 97)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_event import (
    BswEvent,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_client_server_entry import (
    BswModuleClientServerEntry,
)


class BswOperationInvokedEvent(BswEvent):
    """AUTOSAR BswOperationInvokedEvent."""

    entry: Optional[BswModuleClientServerEntry]
    def __init__(self) -> None:
        """Initialize BswOperationInvokedEvent."""
        super().__init__()
        self.entry: Optional[BswModuleClientServerEntry] = None


class BswOperationInvokedEventBuilder:
    """Builder for BswOperationInvokedEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswOperationInvokedEvent = BswOperationInvokedEvent()

    def build(self) -> BswOperationInvokedEvent:
        """Build and return BswOperationInvokedEvent object.

        Returns:
            BswOperationInvokedEvent instance
        """
        # TODO: Add validation
        return self._obj
