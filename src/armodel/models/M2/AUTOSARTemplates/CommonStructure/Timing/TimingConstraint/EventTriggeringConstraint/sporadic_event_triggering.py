"""SporadicEventTriggering AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint.event_triggering_constraint import (
    EventTriggeringConstraint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)


class SporadicEventTriggering(EventTriggeringConstraint):
    """AUTOSAR SporadicEventTriggering."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("jitter", None, False, False, MultidimensionalTime),  # jitter
        ("maximum_inter", None, False, False, MultidimensionalTime),  # maximumInter
        ("minimum_inter", None, False, False, MultidimensionalTime),  # minimumInter
        ("period", None, False, False, MultidimensionalTime),  # period
    ]

    def __init__(self) -> None:
        """Initialize SporadicEventTriggering."""
        super().__init__()
        self.jitter: Optional[MultidimensionalTime] = None
        self.maximum_inter: Optional[MultidimensionalTime] = None
        self.minimum_inter: Optional[MultidimensionalTime] = None
        self.period: Optional[MultidimensionalTime] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SporadicEventTriggering to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SporadicEventTriggering":
        """Create SporadicEventTriggering from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SporadicEventTriggering instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SporadicEventTriggering since parent returns ARObject
        return cast("SporadicEventTriggering", obj)


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
