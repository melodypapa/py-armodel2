"""DataSendCompletedEvent AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.variable_access import (
    VariableAccess,
)


class DataSendCompletedEvent(RTEEvent):
    """AUTOSAR DataSendCompletedEvent."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "event_source": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=VariableAccess,
        ),  # eventSource
    }

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
