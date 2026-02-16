"""BswCompositionTiming AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions.timing_extension import (
    TimingExtension,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswImplementation.bsw_implementation import (
    BswImplementation,
)


class BswCompositionTiming(TimingExtension):
    """AUTOSAR BswCompositionTiming."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("implementations", None, False, True, BswImplementation),  # implementations
    ]

    def __init__(self) -> None:
        """Initialize BswCompositionTiming."""
        super().__init__()
        self.implementations: list[BswImplementation] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BswCompositionTiming to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswCompositionTiming":
        """Create BswCompositionTiming from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BswCompositionTiming instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BswCompositionTiming since parent returns ARObject
        return cast("BswCompositionTiming", obj)


class BswCompositionTimingBuilder:
    """Builder for BswCompositionTiming."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswCompositionTiming = BswCompositionTiming()

    def build(self) -> BswCompositionTiming:
        """Build and return BswCompositionTiming object.

        Returns:
            BswCompositionTiming instance
        """
        # TODO: Add validation
        return self._obj
