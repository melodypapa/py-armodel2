"""BswTimingEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 88)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 217)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_schedule_event import (
    BswScheduleEvent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class BswTimingEvent(BswScheduleEvent):
    """AUTOSAR BswTimingEvent."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "period": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # period
    }

    def __init__(self) -> None:
        """Initialize BswTimingEvent."""
        super().__init__()
        self.period: Optional[TimeValue] = None


class BswTimingEventBuilder:
    """Builder for BswTimingEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswTimingEvent = BswTimingEvent()

    def build(self) -> BswTimingEvent:
        """Build and return BswTimingEvent object.

        Returns:
            BswTimingEvent instance
        """
        # TODO: Add validation
        return self._obj
