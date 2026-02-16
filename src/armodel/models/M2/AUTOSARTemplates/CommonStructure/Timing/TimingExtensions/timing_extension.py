"""TimingExtension AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingClock.timing_clock import (
    TimingClock,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingClock.timing_clock_sync_accuracy import (
    TimingClockSyncAccuracy,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.timing_condition import (
    TimingCondition,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.timing_constraint import (
    TimingConstraint,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions.timing_extension import (
    TimingExtension,
)


class TimingExtension(ARElement):
    """AUTOSAR TimingExtension."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("timing_clocks", None, False, True, TimingClock),  # timingClocks
        ("timing_clock_syncs", None, False, True, TimingClockSyncAccuracy),  # timingClockSyncs
        ("timing_conditions", None, False, True, TimingCondition),  # timingConditions
        ("timings", None, False, True, TimingConstraint),  # timings
        ("timing_resource", None, False, False, TimingExtension),  # timingResource
    ]

    def __init__(self) -> None:
        """Initialize TimingExtension."""
        super().__init__()
        self.timing_clocks: list[TimingClock] = []
        self.timing_clock_syncs: list[TimingClockSyncAccuracy] = []
        self.timing_conditions: list[TimingCondition] = []
        self.timings: list[TimingConstraint] = []
        self.timing_resource: Optional[TimingExtension] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TimingExtension to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TimingExtension":
        """Create TimingExtension from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TimingExtension instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TimingExtension since parent returns ARObject
        return cast("TimingExtension", obj)


class TimingExtensionBuilder:
    """Builder for TimingExtension."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TimingExtension = TimingExtension()

    def build(self) -> TimingExtension:
        """Build and return TimingExtension object.

        Returns:
            TimingExtension instance
        """
        # TODO: Add validation
        return self._obj
