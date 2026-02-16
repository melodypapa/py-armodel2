"""TimeRangeType AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing.time_range_type import (
    TimeRangeType,
)


class TimeRangeType(ARObject):
    """AUTOSAR TimeRangeType."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("tolerance_tolerance", None, False, False, TimeRangeType),  # toleranceTolerance
        ("value", None, True, False, None),  # value
    ]

    def __init__(self) -> None:
        """Initialize TimeRangeType."""
        super().__init__()
        self.tolerance_tolerance: Optional[TimeRangeType] = None
        self.value: Optional[TimeValue] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TimeRangeType to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TimeRangeType":
        """Create TimeRangeType from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TimeRangeType instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TimeRangeType since parent returns ARObject
        return cast("TimeRangeType", obj)


class TimeRangeTypeBuilder:
    """Builder for TimeRangeType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TimeRangeType = TimeRangeType()

    def build(self) -> TimeRangeType:
        """Build and return TimeRangeType object.

        Returns:
            TimeRangeType instance
        """
        # TODO: Add validation
        return self._obj
