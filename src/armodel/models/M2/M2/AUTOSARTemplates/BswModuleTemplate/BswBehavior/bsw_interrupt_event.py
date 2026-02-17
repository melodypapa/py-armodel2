"""BswInterruptEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 88)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_event import (
    BswEvent,
)


class BswInterruptEvent(BswEvent):
    """AUTOSAR BswInterruptEvent."""

    def __init__(self) -> None:
        """Initialize BswInterruptEvent."""
        super().__init__()


class BswInterruptEventBuilder:
    """Builder for BswInterruptEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswInterruptEvent = BswInterruptEvent()

    def build(self) -> BswInterruptEvent:
        """Build and return BswInterruptEvent object.

        Returns:
            BswInterruptEvent instance
        """
        # TODO: Add validation
        return self._obj
