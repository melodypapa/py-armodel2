"""PeriodicEventTriggering AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 101)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_EventTriggeringConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint.event_triggering_constraint import (
    EventTriggeringConstraint,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint.event_triggering_constraint import EventTriggeringConstraintBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class PeriodicEventTriggering(EventTriggeringConstraint):
    """AUTOSAR PeriodicEventTriggering."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "PERIODIC-EVENT-TRIGGERING"


    jitter: Optional[MultidimensionalTime]
    minimum_inter: Optional[MultidimensionalTime]
    period: Optional[MultidimensionalTime]
    _DESERIALIZE_DISPATCH = {
        "JITTER": lambda obj, elem: setattr(obj, "jitter", SerializationHelper.deserialize_by_tag(elem, "MultidimensionalTime")),
        "MINIMUM-INTER": lambda obj, elem: setattr(obj, "minimum_inter", SerializationHelper.deserialize_by_tag(elem, "MultidimensionalTime")),
        "PERIOD": lambda obj, elem: setattr(obj, "period", SerializationHelper.deserialize_by_tag(elem, "MultidimensionalTime")),
    }


    def __init__(self) -> None:
        """Initialize PeriodicEventTriggering."""
        super().__init__()
        self.jitter: Optional[MultidimensionalTime] = None
        self.minimum_inter: Optional[MultidimensionalTime] = None
        self.period: Optional[MultidimensionalTime] = None

    def serialize(self) -> ET.Element:
        """Serialize PeriodicEventTriggering to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PeriodicEventTriggering, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize jitter
        if self.jitter is not None:
            serialized = SerializationHelper.serialize_item(self.jitter, "MultidimensionalTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("JITTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize minimum_inter
        if self.minimum_inter is not None:
            serialized = SerializationHelper.serialize_item(self.minimum_inter, "MultidimensionalTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MINIMUM-INTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize period
        if self.period is not None:
            serialized = SerializationHelper.serialize_item(self.period, "MultidimensionalTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PERIOD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PeriodicEventTriggering":
        """Deserialize XML element to PeriodicEventTriggering object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PeriodicEventTriggering object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PeriodicEventTriggering, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "JITTER":
                setattr(obj, "jitter", SerializationHelper.deserialize_by_tag(child, "MultidimensionalTime"))
            elif tag == "MINIMUM-INTER":
                setattr(obj, "minimum_inter", SerializationHelper.deserialize_by_tag(child, "MultidimensionalTime"))
            elif tag == "PERIOD":
                setattr(obj, "period", SerializationHelper.deserialize_by_tag(child, "MultidimensionalTime"))

        return obj



class PeriodicEventTriggeringBuilder(EventTriggeringConstraintBuilder):
    """Builder for PeriodicEventTriggering with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: PeriodicEventTriggering = PeriodicEventTriggering()


    def with_jitter(self, value: Optional[MultidimensionalTime]) -> "PeriodicEventTriggeringBuilder":
        """Set jitter attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'jitter' is required and cannot be None")
        self._obj.jitter = value
        return self

    def with_minimum_inter(self, value: Optional[MultidimensionalTime]) -> "PeriodicEventTriggeringBuilder":
        """Set minimum_inter attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'minimum_inter' is required and cannot be None")
        self._obj.minimum_inter = value
        return self

    def with_period(self, value: Optional[MultidimensionalTime]) -> "PeriodicEventTriggeringBuilder":
        """Set period attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'period' is required and cannot be None")
        self._obj.period = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "jitter",
        "minimumInter",
        "period",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> PeriodicEventTriggering:
        """Build and return the PeriodicEventTriggering instance with validation."""
        self._validate_instance()
        return self._obj