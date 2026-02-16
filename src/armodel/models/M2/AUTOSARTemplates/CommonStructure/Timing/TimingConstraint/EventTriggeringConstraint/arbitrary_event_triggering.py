"""ArbitraryEventTriggering AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint.event_triggering_constraint import (
    EventTriggeringConstraint,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint.confidence_interval import (
    ConfidenceInterval,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)


class ArbitraryEventTriggering(EventTriggeringConstraint):
    """AUTOSAR ArbitraryEventTriggering."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("confidence_intervals", None, False, True, ConfidenceInterval),  # confidenceIntervals
        ("maximums", None, False, True, MultidimensionalTime),  # maximums
        ("minimums", None, False, True, MultidimensionalTime),  # minimums
    ]

    def __init__(self) -> None:
        """Initialize ArbitraryEventTriggering."""
        super().__init__()
        self.confidence_intervals: list[ConfidenceInterval] = []
        self.maximums: list[MultidimensionalTime] = []
        self.minimums: list[MultidimensionalTime] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ArbitraryEventTriggering to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ArbitraryEventTriggering":
        """Create ArbitraryEventTriggering from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ArbitraryEventTriggering instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ArbitraryEventTriggering since parent returns ARObject
        return cast("ArbitraryEventTriggering", obj)


class ArbitraryEventTriggeringBuilder:
    """Builder for ArbitraryEventTriggering."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ArbitraryEventTriggering = ArbitraryEventTriggering()

    def build(self) -> ArbitraryEventTriggering:
        """Build and return ArbitraryEventTriggering object.

        Returns:
            ArbitraryEventTriggering instance
        """
        # TODO: Add validation
        return self._obj
