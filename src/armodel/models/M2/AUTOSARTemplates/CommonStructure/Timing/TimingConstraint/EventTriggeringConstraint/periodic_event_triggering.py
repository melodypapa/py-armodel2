"""PeriodicEventTriggering AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint.event_triggering_constraint import (
    EventTriggeringConstraint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)


class PeriodicEventTriggering(EventTriggeringConstraint):
    """AUTOSAR PeriodicEventTriggering."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("jitter", None, False, False, MultidimensionalTime),  # jitter
        ("minimum_inter", None, False, False, MultidimensionalTime),  # minimumInter
        ("period", None, False, False, MultidimensionalTime),  # period
    ]

    def __init__(self) -> None:
        """Initialize PeriodicEventTriggering."""
        super().__init__()
        self.jitter: Optional[MultidimensionalTime] = None
        self.minimum_inter: Optional[MultidimensionalTime] = None
        self.period: Optional[MultidimensionalTime] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert PeriodicEventTriggering to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PeriodicEventTriggering":
        """Create PeriodicEventTriggering from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            PeriodicEventTriggering instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to PeriodicEventTriggering since parent returns ARObject
        return cast("PeriodicEventTriggering", obj)


class PeriodicEventTriggeringBuilder:
    """Builder for PeriodicEventTriggering."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PeriodicEventTriggering = PeriodicEventTriggering()

    def build(self) -> PeriodicEventTriggering:
        """Build and return PeriodicEventTriggering object.

        Returns:
            PeriodicEventTriggering instance
        """
        # TODO: Add validation
        return self._obj
