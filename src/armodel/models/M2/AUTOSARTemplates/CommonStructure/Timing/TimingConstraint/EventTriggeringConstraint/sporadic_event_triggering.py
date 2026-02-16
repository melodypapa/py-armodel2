"""SporadicEventTriggering AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint.event_triggering_constraint import (
    EventTriggeringConstraint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)


class SporadicEventTriggering(EventTriggeringConstraint):
    """AUTOSAR SporadicEventTriggering."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "jitter": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=MultidimensionalTime,
        ),  # jitter
        "maximum_inter": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=MultidimensionalTime,
        ),  # maximumInter
        "minimum_inter": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=MultidimensionalTime,
        ),  # minimumInter
        "period": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=MultidimensionalTime,
        ),  # period
    }

    def __init__(self) -> None:
        """Initialize SporadicEventTriggering."""
        super().__init__()
        self.jitter: Optional[MultidimensionalTime] = None
        self.maximum_inter: Optional[MultidimensionalTime] = None
        self.minimum_inter: Optional[MultidimensionalTime] = None
        self.period: Optional[MultidimensionalTime] = None


class SporadicEventTriggeringBuilder:
    """Builder for SporadicEventTriggering."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SporadicEventTriggering = SporadicEventTriggering()

    def build(self) -> SporadicEventTriggering:
        """Build and return SporadicEventTriggering object.

        Returns:
            SporadicEventTriggering instance
        """
        # TODO: Add validation
        return self._obj
