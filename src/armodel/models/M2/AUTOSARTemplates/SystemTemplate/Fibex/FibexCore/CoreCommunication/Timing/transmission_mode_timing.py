"""TransmissionModeTiming AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 393)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication_Timing.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing.cyclic_timing import (
    CyclicTiming,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing.event_controlled_timing import (
    EventControlledTiming,
)


class TransmissionModeTiming(ARObject):
    """AUTOSAR TransmissionModeTiming."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    cyclic_timing: Optional[CyclicTiming]
    event_controlled_timing_timing: Optional[EventControlledTiming]
    def __init__(self) -> None:
        """Initialize TransmissionModeTiming."""
        super().__init__()
        self.cyclic_timing: Optional[CyclicTiming] = None
        self.event_controlled_timing_timing: Optional[EventControlledTiming] = None

    def serialize(self) -> ET.Element:
        """Serialize TransmissionModeTiming to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize cyclic_timing
        if self.cyclic_timing is not None:
            serialized = ARObject._serialize_item(self.cyclic_timing, "CyclicTiming")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CYCLIC-TIMING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize event_controlled_timing_timing
        if self.event_controlled_timing_timing is not None:
            serialized = ARObject._serialize_item(self.event_controlled_timing_timing, "EventControlledTiming")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EVENT-CONTROLLED-TIMING-TIMING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TransmissionModeTiming":
        """Deserialize XML element to TransmissionModeTiming object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TransmissionModeTiming object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse cyclic_timing
        child = ARObject._find_child_element(element, "CYCLIC-TIMING")
        if child is not None:
            cyclic_timing_value = ARObject._deserialize_by_tag(child, "CyclicTiming")
            obj.cyclic_timing = cyclic_timing_value

        # Parse event_controlled_timing_timing
        child = ARObject._find_child_element(element, "EVENT-CONTROLLED-TIMING-TIMING")
        if child is not None:
            event_controlled_timing_timing_value = ARObject._deserialize_by_tag(child, "EventControlledTiming")
            obj.event_controlled_timing_timing = event_controlled_timing_timing_value

        return obj



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
