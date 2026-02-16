"""TimingClock AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_domain import (
    GlobalTimeDomain,
)


class TimingClock(Identifiable):
    """AUTOSAR TimingClock."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("platform_time", None, False, False, GlobalTimeDomain),  # platformTime
    ]

    def __init__(self) -> None:
        """Initialize TimingClock."""
        super().__init__()
        self.platform_time: Optional[GlobalTimeDomain] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TimingClock to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TimingClock":
        """Create TimingClock from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TimingClock instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TimingClock since parent returns ARObject
        return cast("TimingClock", obj)


class TimingClockBuilder:
    """Builder for TimingClock."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TimingClock = TimingClock()

    def build(self) -> TimingClock:
        """Build and return TimingClock object.

        Returns:
            TimingClock instance
        """
        # TODO: Add validation
        return self._obj
