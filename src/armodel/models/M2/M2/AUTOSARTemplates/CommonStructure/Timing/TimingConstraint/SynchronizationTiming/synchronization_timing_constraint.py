"""SynchronizationTimingConstraint AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.timing_constraint import (
    TimingConstraint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)


class SynchronizationTimingConstraint(TimingConstraint):
    """AUTOSAR SynchronizationTimingConstraint."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "event": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=EventOccurrenceKindEnum,
        ),  # event
        "scopes": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=TimingDescriptionEvent,
        ),  # scopes
        "scope_events": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=TimingDescriptionEvent,
        ),  # scopeEvents
        "synchronization": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SynchronizationTypeEnum,
        ),  # synchronization
        "tolerance": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=MultidimensionalTime,
        ),  # tolerance
    }

    def __init__(self) -> None:
        """Initialize SynchronizationTimingConstraint."""
        super().__init__()
        self.event: Optional[EventOccurrenceKindEnum] = None
        self.scopes: list[TimingDescriptionEvent] = []
        self.scope_events: list[TimingDescriptionEvent] = []
        self.synchronization: Optional[SynchronizationTypeEnum] = None
        self.tolerance: Optional[MultidimensionalTime] = None


class SynchronizationTimingConstraintBuilder:
    """Builder for SynchronizationTimingConstraint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SynchronizationTimingConstraint = SynchronizationTimingConstraint()

    def build(self) -> SynchronizationTimingConstraint:
        """Build and return SynchronizationTimingConstraint object.

        Returns:
            SynchronizationTimingConstraint instance
        """
        # TODO: Add validation
        return self._obj
