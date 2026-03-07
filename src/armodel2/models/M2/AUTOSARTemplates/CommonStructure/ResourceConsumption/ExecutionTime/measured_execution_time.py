"""MeasuredExecutionTime AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 166)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ResourceConsumption_ExecutionTime.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.ExecutionTime.execution_time import (
    ExecutionTime,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.ExecutionTime.execution_time import ExecutionTimeBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class MeasuredExecutionTime(ExecutionTime):
    """AUTOSAR MeasuredExecutionTime."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "MEASURED-EXECUTION-TIME"


    maximum_execution_time: Optional[MultidimensionalTime]
    minimum_execution_time: Optional[MultidimensionalTime]
    nominal_execution_time: Optional[MultidimensionalTime]
    _DESERIALIZE_DISPATCH = {
        "MAXIMUM-EXECUTION-TIME": lambda obj, elem: setattr(obj, "maximum_execution_time", SerializationHelper.deserialize_by_tag(elem, "MultidimensionalTime")),
        "MINIMUM-EXECUTION-TIME": lambda obj, elem: setattr(obj, "minimum_execution_time", SerializationHelper.deserialize_by_tag(elem, "MultidimensionalTime")),
        "NOMINAL-EXECUTION-TIME": lambda obj, elem: setattr(obj, "nominal_execution_time", SerializationHelper.deserialize_by_tag(elem, "MultidimensionalTime")),
    }


    def __init__(self) -> None:
        """Initialize MeasuredExecutionTime."""
        super().__init__()
        self.maximum_execution_time: Optional[MultidimensionalTime] = None
        self.minimum_execution_time: Optional[MultidimensionalTime] = None
        self.nominal_execution_time: Optional[MultidimensionalTime] = None

    def serialize(self) -> ET.Element:
        """Serialize MeasuredExecutionTime to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MeasuredExecutionTime, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize maximum_execution_time
        if self.maximum_execution_time is not None:
            serialized = SerializationHelper.serialize_item(self.maximum_execution_time, "MultidimensionalTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAXIMUM-EXECUTION-TIME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize minimum_execution_time
        if self.minimum_execution_time is not None:
            serialized = SerializationHelper.serialize_item(self.minimum_execution_time, "MultidimensionalTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MINIMUM-EXECUTION-TIME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nominal_execution_time
        if self.nominal_execution_time is not None:
            serialized = SerializationHelper.serialize_item(self.nominal_execution_time, "MultidimensionalTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NOMINAL-EXECUTION-TIME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MeasuredExecutionTime":
        """Deserialize XML element to MeasuredExecutionTime object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MeasuredExecutionTime object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MeasuredExecutionTime, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "MAXIMUM-EXECUTION-TIME":
                setattr(obj, "maximum_execution_time", SerializationHelper.deserialize_by_tag(child, "MultidimensionalTime"))
            elif tag == "MINIMUM-EXECUTION-TIME":
                setattr(obj, "minimum_execution_time", SerializationHelper.deserialize_by_tag(child, "MultidimensionalTime"))
            elif tag == "NOMINAL-EXECUTION-TIME":
                setattr(obj, "nominal_execution_time", SerializationHelper.deserialize_by_tag(child, "MultidimensionalTime"))

        return obj



class MeasuredExecutionTimeBuilder(ExecutionTimeBuilder):
    """Builder for MeasuredExecutionTime with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: MeasuredExecutionTime = MeasuredExecutionTime()


    def with_maximum_execution_time(self, value: Optional[MultidimensionalTime]) -> "MeasuredExecutionTimeBuilder":
        """Set maximum_execution_time attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'maximum_execution_time' is required and cannot be None")
        self._obj.maximum_execution_time = value
        return self

    def with_minimum_execution_time(self, value: Optional[MultidimensionalTime]) -> "MeasuredExecutionTimeBuilder":
        """Set minimum_execution_time attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'minimum_execution_time' is required and cannot be None")
        self._obj.minimum_execution_time = value
        return self

    def with_nominal_execution_time(self, value: Optional[MultidimensionalTime]) -> "MeasuredExecutionTimeBuilder":
        """Set nominal_execution_time attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'nominal_execution_time' is required and cannot be None")
        self._obj.nominal_execution_time = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "maximumExecutionTime",
        "minimumExecutionTime",
        "nominalExecutionTime",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> MeasuredExecutionTime:
        """Build and return the MeasuredExecutionTime instance with validation."""
        self._validate_instance()
        return self._obj