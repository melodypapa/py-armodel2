"""EventControlledTiming AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.describable import (
    Describable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing.time_range_type import (
    TimeRangeType,
)


class EventControlledTiming(Describable):
    """AUTOSAR EventControlledTiming."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "number_of": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # numberOf
        "repetition_period": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TimeRangeType,
        ),  # repetitionPeriod
    }

    def __init__(self) -> None:
        """Initialize EventControlledTiming."""
        super().__init__()
        self.number_of: Optional[Integer] = None
        self.repetition_period: Optional[TimeRangeType] = None


class EventControlledTimingBuilder:
    """Builder for EventControlledTiming."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EventControlledTiming = EventControlledTiming()

    def build(self) -> EventControlledTiming:
        """Build and return EventControlledTiming object.

        Returns:
            EventControlledTiming instance
        """
        # TODO: Add validation
        return self._obj
