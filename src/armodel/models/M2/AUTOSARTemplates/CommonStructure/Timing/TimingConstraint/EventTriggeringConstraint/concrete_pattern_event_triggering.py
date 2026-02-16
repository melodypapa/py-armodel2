"""ConcretePatternEventTriggering AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint.event_triggering_constraint import (
    EventTriggeringConstraint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)


class ConcretePatternEventTriggering(EventTriggeringConstraint):
    """AUTOSAR ConcretePatternEventTriggering."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("offsets", None, False, True, MultidimensionalTime),  # offsets
        ("pattern_jitter", None, False, False, MultidimensionalTime),  # patternJitter
        ("pattern_length", None, False, False, MultidimensionalTime),  # patternLength
        ("pattern_period", None, False, False, MultidimensionalTime),  # patternPeriod
    ]

    def __init__(self) -> None:
        """Initialize ConcretePatternEventTriggering."""
        super().__init__()
        self.offsets: list[MultidimensionalTime] = []
        self.pattern_jitter: Optional[MultidimensionalTime] = None
        self.pattern_length: Optional[MultidimensionalTime] = None
        self.pattern_period: Optional[MultidimensionalTime] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ConcretePatternEventTriggering to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ConcretePatternEventTriggering":
        """Create ConcretePatternEventTriggering from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ConcretePatternEventTriggering instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ConcretePatternEventTriggering since parent returns ARObject
        return cast("ConcretePatternEventTriggering", obj)


class ConcretePatternEventTriggeringBuilder:
    """Builder for ConcretePatternEventTriggering."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ConcretePatternEventTriggering = ConcretePatternEventTriggering()

    def build(self) -> ConcretePatternEventTriggering:
        """Build and return ConcretePatternEventTriggering object.

        Returns:
            ConcretePatternEventTriggering instance
        """
        # TODO: Add validation
        return self._obj
