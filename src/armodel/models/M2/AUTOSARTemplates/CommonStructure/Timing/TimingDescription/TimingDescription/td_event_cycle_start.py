"""TDEventCycleStart AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_com import (
    TDEventCom,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class TDEventCycleStart(TDEventCom):
    """AUTOSAR TDEventCycleStart."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("cycle_repetition", None, True, False, None),  # cycleRepetition
    ]

    def __init__(self) -> None:
        """Initialize TDEventCycleStart."""
        super().__init__()
        self.cycle_repetition: Optional[Integer] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TDEventCycleStart to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventCycleStart":
        """Create TDEventCycleStart from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TDEventCycleStart instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TDEventCycleStart since parent returns ARObject
        return cast("TDEventCycleStart", obj)


class TDEventCycleStartBuilder:
    """Builder for TDEventCycleStart."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventCycleStart = TDEventCycleStart()

    def build(self) -> TDEventCycleStart:
        """Build and return TDEventCycleStart object.

        Returns:
            TDEventCycleStart instance
        """
        # TODO: Add validation
        return self._obj
