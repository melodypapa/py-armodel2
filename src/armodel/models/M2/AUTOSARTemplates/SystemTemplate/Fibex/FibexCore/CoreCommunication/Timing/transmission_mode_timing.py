"""TransmissionModeTiming AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing.cyclic_timing import (
    CyclicTiming,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing.event_controlled_timing import (
    EventControlledTiming,
)


class TransmissionModeTiming(ARObject):
    """AUTOSAR TransmissionModeTiming."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("cyclic_timing", None, False, False, CyclicTiming),  # cyclicTiming
        ("event_controlled_timing_timing", None, False, False, EventControlledTiming),  # eventControlledTimingTiming
    ]

    def __init__(self) -> None:
        """Initialize TransmissionModeTiming."""
        super().__init__()
        self.cyclic_timing: Optional[CyclicTiming] = None
        self.event_controlled_timing_timing: Optional[EventControlledTiming] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TransmissionModeTiming to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TransmissionModeTiming":
        """Create TransmissionModeTiming from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TransmissionModeTiming instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TransmissionModeTiming since parent returns ARObject
        return cast("TransmissionModeTiming", obj)


class TransmissionModeTimingBuilder:
    """Builder for TransmissionModeTiming."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TransmissionModeTiming = TransmissionModeTiming()

    def build(self) -> TransmissionModeTiming:
        """Build and return TransmissionModeTiming object.

        Returns:
            TransmissionModeTiming instance
        """
        # TODO: Add validation
        return self._obj
