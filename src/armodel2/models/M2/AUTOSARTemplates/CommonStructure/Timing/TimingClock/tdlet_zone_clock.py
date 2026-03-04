"""TDLETZoneClock AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 252)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingClock.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingClock.timing_clock import (
    TimingClock,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingClock.timing_clock import TimingClockBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class TDLETZoneClock(TimingClock):
    """AUTOSAR TDLETZoneClock."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "T-D-L-E-T-ZONE-CLOCK"


    accuracy_ext: Optional[MultidimensionalTime]
    accuracy_int: Optional[MultidimensionalTime]
    _DESERIALIZE_DISPATCH = {
        "ACCURACY-EXT": lambda obj, elem: setattr(obj, "accuracy_ext", SerializationHelper.deserialize_by_tag(elem, "MultidimensionalTime")),
        "ACCURACY-INT": lambda obj, elem: setattr(obj, "accuracy_int", SerializationHelper.deserialize_by_tag(elem, "MultidimensionalTime")),
    }


    def __init__(self) -> None:
        """Initialize TDLETZoneClock."""
        super().__init__()
        self.accuracy_ext: Optional[MultidimensionalTime] = None
        self.accuracy_int: Optional[MultidimensionalTime] = None

    def serialize(self) -> ET.Element:
        """Serialize TDLETZoneClock to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TDLETZoneClock, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize accuracy_ext
        if self.accuracy_ext is not None:
            serialized = SerializationHelper.serialize_item(self.accuracy_ext, "MultidimensionalTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ACCURACY-EXT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize accuracy_int
        if self.accuracy_int is not None:
            serialized = SerializationHelper.serialize_item(self.accuracy_int, "MultidimensionalTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ACCURACY-INT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDLETZoneClock":
        """Deserialize XML element to TDLETZoneClock object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDLETZoneClock object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDLETZoneClock, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ACCURACY-EXT":
                setattr(obj, "accuracy_ext", SerializationHelper.deserialize_by_tag(child, "MultidimensionalTime"))
            elif tag == "ACCURACY-INT":
                setattr(obj, "accuracy_int", SerializationHelper.deserialize_by_tag(child, "MultidimensionalTime"))

        return obj



class TDLETZoneClockBuilder(TimingClockBuilder):
    """Builder for TDLETZoneClock with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TDLETZoneClock = TDLETZoneClock()


    def with_accuracy_ext(self, value: Optional[MultidimensionalTime]) -> "TDLETZoneClockBuilder":
        """Set accuracy_ext attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.accuracy_ext = value
        return self

    def with_accuracy_int(self, value: Optional[MultidimensionalTime]) -> "TDLETZoneClockBuilder":
        """Set accuracy_int attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.accuracy_int = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "accuracyExt",
        "accuracyInt",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> TDLETZoneClock:
        """Build and return the TDLETZoneClock instance with validation."""
        self._validate_instance()
        return self._obj