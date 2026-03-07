"""ConfidenceInterval AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 112)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_EventTriggeringConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ConfidenceInterval(ARObject):
    """AUTOSAR ConfidenceInterval."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CONFIDENCE-INTERVAL"


    lower_bound: Optional[MultidimensionalTime]
    propability: Optional[Float]
    upper_bound: Optional[MultidimensionalTime]
    _DESERIALIZE_DISPATCH = {
        "LOWER-BOUND": lambda obj, elem: setattr(obj, "lower_bound", SerializationHelper.deserialize_by_tag(elem, "MultidimensionalTime")),
        "PROPABILITY": lambda obj, elem: setattr(obj, "propability", SerializationHelper.deserialize_by_tag(elem, "Float")),
        "UPPER-BOUND": lambda obj, elem: setattr(obj, "upper_bound", SerializationHelper.deserialize_by_tag(elem, "MultidimensionalTime")),
    }


    def __init__(self) -> None:
        """Initialize ConfidenceInterval."""
        super().__init__()
        self.lower_bound: Optional[MultidimensionalTime] = None
        self.propability: Optional[Float] = None
        self.upper_bound: Optional[MultidimensionalTime] = None

    def serialize(self) -> ET.Element:
        """Serialize ConfidenceInterval to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ConfidenceInterval, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize lower_bound
        if self.lower_bound is not None:
            serialized = SerializationHelper.serialize_item(self.lower_bound, "MultidimensionalTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LOWER-BOUND")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize propability
        if self.propability is not None:
            serialized = SerializationHelper.serialize_item(self.propability, "Float")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROPABILITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize upper_bound
        if self.upper_bound is not None:
            serialized = SerializationHelper.serialize_item(self.upper_bound, "MultidimensionalTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UPPER-BOUND")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ConfidenceInterval":
        """Deserialize XML element to ConfidenceInterval object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ConfidenceInterval object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ConfidenceInterval, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "LOWER-BOUND":
                setattr(obj, "lower_bound", SerializationHelper.deserialize_by_tag(child, "MultidimensionalTime"))
            elif tag == "PROPABILITY":
                setattr(obj, "propability", SerializationHelper.deserialize_by_tag(child, "Float"))
            elif tag == "UPPER-BOUND":
                setattr(obj, "upper_bound", SerializationHelper.deserialize_by_tag(child, "MultidimensionalTime"))

        return obj



class ConfidenceIntervalBuilder(BuilderBase):
    """Builder for ConfidenceInterval with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ConfidenceInterval = ConfidenceInterval()


    def with_lower_bound(self, value: Optional[MultidimensionalTime]) -> "ConfidenceIntervalBuilder":
        """Set lower_bound attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'lower_bound' is required and cannot be None")
        self._obj.lower_bound = value
        return self

    def with_propability(self, value: Optional[Float]) -> "ConfidenceIntervalBuilder":
        """Set propability attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'propability' is required and cannot be None")
        self._obj.propability = value
        return self

    def with_upper_bound(self, value: Optional[MultidimensionalTime]) -> "ConfidenceIntervalBuilder":
        """Set upper_bound attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'upper_bound' is required and cannot be None")
        self._obj.upper_bound = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "lowerBound",
        "propability",
        "upperBound",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ConfidenceInterval:
        """Build and return the ConfidenceInterval instance with validation."""
        self._validate_instance()
        return self._obj