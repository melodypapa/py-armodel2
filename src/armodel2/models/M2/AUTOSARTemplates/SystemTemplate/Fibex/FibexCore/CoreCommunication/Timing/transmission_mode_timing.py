"""TransmissionModeTiming AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 393)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication_Timing.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing.cyclic_timing import (
    CyclicTiming,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing.event_controlled_timing import (
    EventControlledTiming,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class TransmissionModeTiming(ARObject):
    """AUTOSAR TransmissionModeTiming."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "TRANSMISSION-MODE-TIMING"


    cyclic_timing: Optional[CyclicTiming]
    event_controlled_timing: Optional[EventControlledTiming]
    _DESERIALIZE_DISPATCH = {
        "CYCLIC-TIMING": lambda obj, elem: setattr(obj, "cyclic_timing", SerializationHelper.deserialize_by_tag(elem, "CyclicTiming")),
        "EVENT-CONTROLLED-TIMING": lambda obj, elem: setattr(obj, "event_controlled_timing", SerializationHelper.deserialize_by_tag(elem, "EventControlledTiming")),
    }


    def __init__(self) -> None:
        """Initialize TransmissionModeTiming."""
        super().__init__()
        self.cyclic_timing: Optional[CyclicTiming] = None
        self.event_controlled_timing: Optional[EventControlledTiming] = None

    def serialize(self) -> ET.Element:
        """Serialize TransmissionModeTiming to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TransmissionModeTiming, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize cyclic_timing
        if self.cyclic_timing is not None:
            serialized = SerializationHelper.serialize_item(self.cyclic_timing, "CyclicTiming")
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

        # Serialize event_controlled_timing
        if self.event_controlled_timing is not None:
            serialized = SerializationHelper.serialize_item(self.event_controlled_timing, "EventControlledTiming")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EVENT-CONTROLLED-TIMING")
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
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TransmissionModeTiming, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CYCLIC-TIMING":
                setattr(obj, "cyclic_timing", SerializationHelper.deserialize_by_tag(child, "CyclicTiming"))
            elif tag == "EVENT-CONTROLLED-TIMING":
                setattr(obj, "event_controlled_timing", SerializationHelper.deserialize_by_tag(child, "EventControlledTiming"))

        return obj



class TransmissionModeTimingBuilder(BuilderBase):
    """Builder for TransmissionModeTiming with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TransmissionModeTiming = TransmissionModeTiming()


    def with_cyclic_timing(self, value: Optional[CyclicTiming]) -> "TransmissionModeTimingBuilder":
        """Set cyclic_timing attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'cyclic_timing' is required and cannot be None")
        self._obj.cyclic_timing = value
        return self

    def with_event_controlled_timing(self, value: Optional[EventControlledTiming]) -> "TransmissionModeTimingBuilder":
        """Set event_controlled_timing attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'event_controlled_timing' is required and cannot be None")
        self._obj.event_controlled_timing = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "cyclicTiming",
        "eventControlledTiming",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> TransmissionModeTiming:
        """Build and return the TransmissionModeTiming instance with validation."""
        self._validate_instance()
        return self._obj