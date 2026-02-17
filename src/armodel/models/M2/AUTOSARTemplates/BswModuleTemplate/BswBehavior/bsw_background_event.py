"""BswBackgroundEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 89)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_schedule_event import (
    BswScheduleEvent,
)


class BswBackgroundEvent(BswScheduleEvent):
    """AUTOSAR BswBackgroundEvent."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize BswBackgroundEvent."""
        super().__init__()


class BswBackgroundEventBuilder:
    """Builder for BswBackgroundEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswBackgroundEvent = BswBackgroundEvent()

    def build(self) -> BswBackgroundEvent:
        """Build and return BswBackgroundEvent object.

        Returns:
            BswBackgroundEvent instance
        """
        # TODO: Add validation
        return self._obj
