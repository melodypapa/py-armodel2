"""CyclicTiming AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.describable import (
    Describable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing.time_range_type import (
    TimeRangeType,
)


class CyclicTiming(Describable):
    """AUTOSAR CyclicTiming."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "time_offset": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TimeRangeType,
        ),  # timeOffset
        "time_period": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TimeRangeType,
        ),  # timePeriod
    }

    def __init__(self) -> None:
        """Initialize CyclicTiming."""
        super().__init__()
        self.time_offset: Optional[TimeRangeType] = None
        self.time_period: Optional[TimeRangeType] = None


class CyclicTimingBuilder:
    """Builder for CyclicTiming."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CyclicTiming = CyclicTiming()

    def build(self) -> CyclicTiming:
        """Build and return CyclicTiming object.

        Returns:
            CyclicTiming instance
        """
        # TODO: Add validation
        return self._obj
