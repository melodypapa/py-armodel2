"""BswModuleTiming AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions.timing_extension import (
    TimingExtension,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_internal_behavior import (
    BswInternalBehavior,
)


class BswModuleTiming(TimingExtension):
    """AUTOSAR BswModuleTiming."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("behavior", None, False, False, BswInternalBehavior),  # behavior
    ]

    def __init__(self) -> None:
        """Initialize BswModuleTiming."""
        super().__init__()
        self.behavior: Optional[BswInternalBehavior] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BswModuleTiming to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswModuleTiming":
        """Create BswModuleTiming from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BswModuleTiming instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BswModuleTiming since parent returns ARObject
        return cast("BswModuleTiming", obj)


class BswModuleTimingBuilder:
    """Builder for BswModuleTiming."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswModuleTiming = BswModuleTiming()

    def build(self) -> BswModuleTiming:
        """Build and return BswModuleTiming object.

        Returns:
            BswModuleTiming instance
        """
        # TODO: Add validation
        return self._obj
