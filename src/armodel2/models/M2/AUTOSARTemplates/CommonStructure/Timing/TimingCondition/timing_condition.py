"""TimingCondition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 35)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingCondition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class TimingCondition(Identifiable):
    """AUTOSAR TimingCondition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "TIMING-CONDITION"


    timing_condition: Optional[TimingCondition]
    _DESERIALIZE_DISPATCH = {
        "TIMING-CONDITION": lambda obj, elem: setattr(obj, "timing_condition", SerializationHelper.deserialize_by_tag(elem, "TimingCondition")),
    }


    def __init__(self) -> None:
        """Initialize TimingCondition."""
        super().__init__()
        self.timing_condition: Optional[TimingCondition] = None

    def serialize(self) -> ET.Element:
        """Serialize TimingCondition to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TimingCondition, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize timing_condition
        if self.timing_condition is not None:
            serialized = SerializationHelper.serialize_item(self.timing_condition, "TimingCondition")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMING-CONDITION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TimingCondition":
        """Deserialize XML element to TimingCondition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TimingCondition object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TimingCondition, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "TIMING-CONDITION":
                setattr(obj, "timing_condition", SerializationHelper.deserialize_by_tag(child, "TimingCondition"))

        return obj



class TimingConditionBuilder(IdentifiableBuilder):
    """Builder for TimingCondition with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TimingCondition = TimingCondition()


    def with_timing_condition(self, value: Optional[TimingCondition]) -> "TimingConditionBuilder":
        """Set timing_condition attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'timing_condition' is required and cannot be None")
        self._obj.timing_condition = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "timingCondition",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> TimingCondition:
        """Build and return the TimingCondition instance with validation."""
        self._validate_instance()
        return self._obj