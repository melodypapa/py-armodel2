"""TDEventTrigger AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_vfb_port import (
    TDEventVfbPort,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)


class TDEventTrigger(TDEventVfbPort):
    """AUTOSAR TDEventTrigger."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "td_event_trigger": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TDEventTriggerTypeEnum,
        ),  # tdEventTrigger
        "trigger": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Trigger,
        ),  # trigger
    }

    def __init__(self) -> None:
        """Initialize TDEventTrigger."""
        super().__init__()
        self.td_event_trigger: Optional[TDEventTriggerTypeEnum] = None
        self.trigger: Optional[Trigger] = None


class TDEventTriggerBuilder:
    """Builder for TDEventTrigger."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventTrigger = TDEventTrigger()

    def build(self) -> TDEventTrigger:
        """Build and return TDEventTrigger object.

        Returns:
            TDEventTrigger instance
        """
        # TODO: Add validation
        return self._obj
