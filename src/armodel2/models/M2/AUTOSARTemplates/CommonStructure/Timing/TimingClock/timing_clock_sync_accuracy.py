"""TimingClockSyncAccuracy AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 252)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingClock.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingClock.timing_clock import (
    TimingClock,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class TimingClockSyncAccuracy(Identifiable):
    """AUTOSAR TimingClockSyncAccuracy."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "TIMING-CLOCK-SYNC-ACCURACY"


    accuracy: Optional[MultidimensionalTime]
    lower_ref: Optional[ARRef]
    upper_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "ACCURACY": lambda obj, elem: setattr(obj, "accuracy", SerializationHelper.deserialize_by_tag(elem, "MultidimensionalTime")),
        "LOWER-REF": ("_POLYMORPHIC", "lower_ref", ["TDLETZoneClock"]),
        "UPPER-REF": ("_POLYMORPHIC", "upper_ref", ["TDLETZoneClock"]),
    }


    def __init__(self) -> None:
        """Initialize TimingClockSyncAccuracy."""
        super().__init__()
        self.accuracy: Optional[MultidimensionalTime] = None
        self.lower_ref: Optional[ARRef] = None
        self.upper_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize TimingClockSyncAccuracy to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TimingClockSyncAccuracy, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize accuracy
        if self.accuracy is not None:
            serialized = SerializationHelper.serialize_item(self.accuracy, "MultidimensionalTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ACCURACY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize lower_ref
        if self.lower_ref is not None:
            serialized = SerializationHelper.serialize_item(self.lower_ref, "TimingClock")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LOWER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize upper_ref
        if self.upper_ref is not None:
            serialized = SerializationHelper.serialize_item(self.upper_ref, "TimingClock")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UPPER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TimingClockSyncAccuracy":
        """Deserialize XML element to TimingClockSyncAccuracy object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TimingClockSyncAccuracy object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TimingClockSyncAccuracy, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ACCURACY":
                setattr(obj, "accuracy", SerializationHelper.deserialize_by_tag(child, "MultidimensionalTime"))
            elif tag == "LOWER-REF":
                setattr(obj, "lower_ref", ARRef.deserialize(child))
            elif tag == "UPPER-REF":
                setattr(obj, "upper_ref", ARRef.deserialize(child))

        return obj



class TimingClockSyncAccuracyBuilder(IdentifiableBuilder):
    """Builder for TimingClockSyncAccuracy with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TimingClockSyncAccuracy = TimingClockSyncAccuracy()


    def with_accuracy(self, value: Optional[MultidimensionalTime]) -> "TimingClockSyncAccuracyBuilder":
        """Set accuracy attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'accuracy' is required and cannot be None")
        self._obj.accuracy = value
        return self

    def with_lower(self, value: Optional[TimingClock]) -> "TimingClockSyncAccuracyBuilder":
        """Set lower attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'lower' is required and cannot be None")
        self._obj.lower = value
        return self

    def with_upper(self, value: Optional[TimingClock]) -> "TimingClockSyncAccuracyBuilder":
        """Set upper attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'upper' is required and cannot be None")
        self._obj.upper = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "accuracy",
        "lower",
        "upper",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> TimingClockSyncAccuracy:
        """Build and return the TimingClockSyncAccuracy instance with validation."""
        self._validate_instance()
        return self._obj