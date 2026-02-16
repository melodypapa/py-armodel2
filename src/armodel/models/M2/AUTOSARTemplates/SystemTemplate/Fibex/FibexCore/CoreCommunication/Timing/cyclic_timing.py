"""CyclicTiming AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.describable import (
    Describable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing.time_range_type import (
    TimeRangeType,
)


class CyclicTiming(Describable):
    """AUTOSAR CyclicTiming."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("time_offset", None, False, False, TimeRangeType),  # timeOffset
        ("time_period", None, False, False, TimeRangeType),  # timePeriod
    ]

    def __init__(self) -> None:
        """Initialize CyclicTiming."""
        super().__init__()
        self.time_offset: Optional[TimeRangeType] = None
        self.time_period: Optional[TimeRangeType] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CyclicTiming to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CyclicTiming":
        """Create CyclicTiming from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CyclicTiming instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CyclicTiming since parent returns ARObject
        return cast("CyclicTiming", obj)


class CyclicTimingBuilder:
    """Builder for CyclicTiming."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CyclicTiming = CyclicTiming()

    def build(self) -> CyclicTiming:
        """Build and return CyclicTiming object.

        Returns:
            CyclicTiming instance
        """
        # TODO: Add validation
        return self._obj
