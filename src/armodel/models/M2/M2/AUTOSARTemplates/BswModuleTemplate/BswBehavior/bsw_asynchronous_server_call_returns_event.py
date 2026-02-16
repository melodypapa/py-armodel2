"""BswAsynchronousServerCallReturnsEvent AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_schedule_event import (
    BswScheduleEvent,
)


class BswAsynchronousServerCallReturnsEvent(BswScheduleEvent):
    """AUTOSAR BswAsynchronousServerCallReturnsEvent."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "event_source": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (BswAsynchronous),
        ),  # eventSource
    }

    def __init__(self) -> None:
        """Initialize BswAsynchronousServerCallReturnsEvent."""
        super().__init__()
        self.event_source: Optional[Any] = None


class BswAsynchronousServerCallReturnsEventBuilder:
    """Builder for BswAsynchronousServerCallReturnsEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswAsynchronousServerCallReturnsEvent = BswAsynchronousServerCallReturnsEvent()

    def build(self) -> BswAsynchronousServerCallReturnsEvent:
        """Build and return BswAsynchronousServerCallReturnsEvent object.

        Returns:
            BswAsynchronousServerCallReturnsEvent instance
        """
        # TODO: Add validation
        return self._obj
