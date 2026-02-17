"""BswModeSwitchEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 94)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_schedule_event import (
    BswScheduleEvent,
)


class BswModeSwitchEvent(BswScheduleEvent):
    """AUTOSAR BswModeSwitchEvent."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "activation": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ModeActivationKind,
        ),  # activation
    }

    def __init__(self) -> None:
        """Initialize BswModeSwitchEvent."""
        super().__init__()
        self.activation: Optional[ModeActivationKind] = None


class BswModeSwitchEventBuilder:
    """Builder for BswModeSwitchEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswModeSwitchEvent = BswModeSwitchEvent()

    def build(self) -> BswModeSwitchEvent:
        """Build and return BswModeSwitchEvent object.

        Returns:
            BswModeSwitchEvent instance
        """
        # TODO: Add validation
        return self._obj
