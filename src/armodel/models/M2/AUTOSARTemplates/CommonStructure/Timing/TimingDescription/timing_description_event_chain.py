"""TimingDescriptionEventChain AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description import (
    TimingDescription,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)


class TimingDescriptionEventChain(TimingDescription):
    """AUTOSAR TimingDescriptionEventChain."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("is_pipelining", None, True, False, None),  # isPipelining
        ("response", None, False, False, TimingDescriptionEvent),  # response
        ("segments", None, False, True, TimingDescriptionEvent),  # segments
        ("stimulus", None, False, False, TimingDescriptionEvent),  # stimulus
    ]

    def __init__(self) -> None:
        """Initialize TimingDescriptionEventChain."""
        super().__init__()
        self.is_pipelining: Optional[Boolean] = None
        self.response: Optional[TimingDescriptionEvent] = None
        self.segments: list[TimingDescriptionEvent] = []
        self.stimulus: Optional[TimingDescriptionEvent] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TimingDescriptionEventChain to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TimingDescriptionEventChain":
        """Create TimingDescriptionEventChain from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TimingDescriptionEventChain instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TimingDescriptionEventChain since parent returns ARObject
        return cast("TimingDescriptionEventChain", obj)


class TimingDescriptionEventChainBuilder:
    """Builder for TimingDescriptionEventChain."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TimingDescriptionEventChain = TimingDescriptionEventChain()

    def build(self) -> TimingDescriptionEventChain:
        """Build and return TimingDescriptionEventChain object.

        Returns:
            TimingDescriptionEventChain instance
        """
        # TODO: Add validation
        return self._obj
