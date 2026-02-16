"""TDEventSwc AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)


class TDEventSwc(TimingDescriptionEvent):
    """AUTOSAR TDEventSwc."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("component", None, False, False, any (SwComponent)),  # component
    ]

    def __init__(self) -> None:
        """Initialize TDEventSwc."""
        super().__init__()
        self.component: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TDEventSwc to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventSwc":
        """Create TDEventSwc from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TDEventSwc instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TDEventSwc since parent returns ARObject
        return cast("TDEventSwc", obj)


class TDEventSwcBuilder:
    """Builder for TDEventSwc."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventSwc = TDEventSwc()

    def build(self) -> TDEventSwc:
        """Build and return TDEventSwc object.

        Returns:
            TDEventSwc instance
        """
        # TODO: Add validation
        return self._obj
