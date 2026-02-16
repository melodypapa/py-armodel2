"""VfbTiming AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions.timing_extension import (
    TimingExtension,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.sw_component_type import (
    SwComponentType,
)


class VfbTiming(TimingExtension):
    """AUTOSAR VfbTiming."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("component", None, False, False, SwComponentType),  # component
    ]

    def __init__(self) -> None:
        """Initialize VfbTiming."""
        super().__init__()
        self.component: Optional[SwComponentType] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert VfbTiming to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "VfbTiming":
        """Create VfbTiming from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            VfbTiming instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to VfbTiming since parent returns ARObject
        return cast("VfbTiming", obj)


class VfbTimingBuilder:
    """Builder for VfbTiming."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: VfbTiming = VfbTiming()

    def build(self) -> VfbTiming:
        """Build and return VfbTiming object.

        Returns:
            VfbTiming instance
        """
        # TODO: Add validation
        return self._obj
