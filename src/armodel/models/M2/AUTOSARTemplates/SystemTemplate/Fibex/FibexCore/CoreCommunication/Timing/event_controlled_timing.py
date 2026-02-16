"""EventControlledTiming AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
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
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("number_of", None, True, False, None),  # numberOf
        ("repetition_period", None, False, False, TimeRangeType),  # repetitionPeriod
    ]

    def __init__(self) -> None:
        """Initialize EventControlledTiming."""
        super().__init__()
        self.number_of: Optional[Integer] = None
        self.repetition_period: Optional[TimeRangeType] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EventControlledTiming to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EventControlledTiming":
        """Create EventControlledTiming from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EventControlledTiming instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EventControlledTiming since parent returns ARObject
        return cast("EventControlledTiming", obj)


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
