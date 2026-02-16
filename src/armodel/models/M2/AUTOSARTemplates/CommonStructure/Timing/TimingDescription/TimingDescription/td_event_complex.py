"""TDEventComplex AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)


class TDEventComplex(TimingDescriptionEvent):
    """AUTOSAR TDEventComplex."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize TDEventComplex."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TDEventComplex to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventComplex":
        """Create TDEventComplex from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TDEventComplex instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TDEventComplex since parent returns ARObject
        return cast("TDEventComplex", obj)


class TDEventComplexBuilder:
    """Builder for TDEventComplex."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventComplex = TDEventComplex()

    def build(self) -> TDEventComplex:
        """Build and return TDEventComplex object.

        Returns:
            TDEventComplex instance
        """
        # TODO: Add validation
        return self._obj
