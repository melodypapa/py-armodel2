"""TDEventVfb AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)


class TDEventVfb(TimingDescriptionEvent):
    """AUTOSAR TDEventVfb."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("component", None, False, False, any (SwComponent)),  # component
    ]

    def __init__(self) -> None:
        """Initialize TDEventVfb."""
        super().__init__()
        self.component: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TDEventVfb to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventVfb":
        """Create TDEventVfb from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TDEventVfb instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TDEventVfb since parent returns ARObject
        return cast("TDEventVfb", obj)


class TDEventVfbBuilder:
    """Builder for TDEventVfb."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventVfb = TDEventVfb()

    def build(self) -> TDEventVfb:
        """Build and return TDEventVfb object.

        Returns:
            TDEventVfb instance
        """
        # TODO: Add validation
        return self._obj
