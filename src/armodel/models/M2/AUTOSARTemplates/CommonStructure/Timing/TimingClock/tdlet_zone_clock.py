"""TDLETZoneClock AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingClock.timing_clock import (
    TimingClock,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)


class TDLETZoneClock(TimingClock):
    """AUTOSAR TDLETZoneClock."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("accuracy_ext", None, False, False, MultidimensionalTime),  # accuracyExt
        ("accuracy_int", None, False, False, MultidimensionalTime),  # accuracyInt
    ]

    def __init__(self) -> None:
        """Initialize TDLETZoneClock."""
        super().__init__()
        self.accuracy_ext: Optional[MultidimensionalTime] = None
        self.accuracy_int: Optional[MultidimensionalTime] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TDLETZoneClock to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDLETZoneClock":
        """Create TDLETZoneClock from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TDLETZoneClock instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TDLETZoneClock since parent returns ARObject
        return cast("TDLETZoneClock", obj)


class TDLETZoneClockBuilder:
    """Builder for TDLETZoneClock."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDLETZoneClock = TDLETZoneClock()

    def build(self) -> TDLETZoneClock:
        """Build and return TDLETZoneClock object.

        Returns:
            TDLETZoneClock instance
        """
        # TODO: Add validation
        return self._obj
