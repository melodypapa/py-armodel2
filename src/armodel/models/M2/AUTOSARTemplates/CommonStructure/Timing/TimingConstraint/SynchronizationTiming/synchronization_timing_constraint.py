"""SynchronizationTimingConstraint AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
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
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("event", None, False, False, EventOccurrenceKindEnum),  # event
        ("scopes", None, False, True, TimingDescriptionEvent),  # scopes
        ("scope_events", None, False, True, TimingDescriptionEvent),  # scopeEvents
        ("synchronization", None, False, False, SynchronizationTypeEnum),  # synchronization
        ("tolerance", None, False, False, MultidimensionalTime),  # tolerance
    ]

    def __init__(self) -> None:
        """Initialize SynchronizationTimingConstraint."""
        super().__init__()
        self.event: Optional[EventOccurrenceKindEnum] = None
        self.scopes: list[TimingDescriptionEvent] = []
        self.scope_events: list[TimingDescriptionEvent] = []
        self.synchronization: Optional[SynchronizationTypeEnum] = None
        self.tolerance: Optional[MultidimensionalTime] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SynchronizationTimingConstraint to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SynchronizationTimingConstraint":
        """Create SynchronizationTimingConstraint from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SynchronizationTimingConstraint instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SynchronizationTimingConstraint since parent returns ARObject
        return cast("SynchronizationTimingConstraint", obj)


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
