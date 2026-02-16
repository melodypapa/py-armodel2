"""TtcanAbsolutelyScheduledTiming AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_cycle import (
    CommunicationCycle,
)


class TtcanAbsolutelyScheduledTiming(ARObject):
    """AUTOSAR TtcanAbsolutelyScheduledTiming."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "communication_cycle_cycle": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CommunicationCycle,
        ),  # communicationCycleCycle
        "time_mark": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # timeMark
        "trigger": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TtcanTriggerType,
        ),  # trigger
    }

    def __init__(self) -> None:
        """Initialize TtcanAbsolutelyScheduledTiming."""
        super().__init__()
        self.communication_cycle_cycle: Optional[CommunicationCycle] = None
        self.time_mark: Optional[Integer] = None
        self.trigger: Optional[TtcanTriggerType] = None


class TtcanAbsolutelyScheduledTimingBuilder:
    """Builder for TtcanAbsolutelyScheduledTiming."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TtcanAbsolutelyScheduledTiming = TtcanAbsolutelyScheduledTiming()

    def build(self) -> TtcanAbsolutelyScheduledTiming:
        """Build and return TtcanAbsolutelyScheduledTiming object.

        Returns:
            TtcanAbsolutelyScheduledTiming instance
        """
        # TODO: Add validation
        return self._obj
