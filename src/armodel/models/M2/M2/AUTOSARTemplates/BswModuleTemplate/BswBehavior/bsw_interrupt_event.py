"""BswInterruptEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 88)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_event import (
    BswEvent,
)


class BswInterruptEvent(BswEvent):
    """AUTOSAR BswInterruptEvent."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

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
