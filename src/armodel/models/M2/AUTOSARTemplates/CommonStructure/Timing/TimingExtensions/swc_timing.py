"""SwcTiming AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions.timing_extension import (
    TimingExtension,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.swc_internal_behavior import (
    SwcInternalBehavior,
)


class SwcTiming(TimingExtension):
    """AUTOSAR SwcTiming."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("behavior", None, False, False, SwcInternalBehavior),  # behavior
    ]

    def __init__(self) -> None:
        """Initialize SwcTiming."""
        super().__init__()
        self.behavior: Optional[SwcInternalBehavior] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwcTiming to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcTiming":
        """Create SwcTiming from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwcTiming instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwcTiming since parent returns ARObject
        return cast("SwcTiming", obj)


class SwcTimingBuilder:
    """Builder for SwcTiming."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcTiming = SwcTiming()

    def build(self) -> SwcTiming:
        """Build and return SwcTiming object.

        Returns:
            SwcTiming instance
        """
        # TODO: Add validation
        return self._obj
