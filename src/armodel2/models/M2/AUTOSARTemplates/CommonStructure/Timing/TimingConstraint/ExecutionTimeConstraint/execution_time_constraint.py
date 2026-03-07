"""ExecutionTimeConstraint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 130)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_ExecutionTimeConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.timing_constraint import (
    TimingConstraint,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.timing_constraint import TimingConstraintBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionTimeConstraint import (
    ExecutionTimeTypeEnum,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.executable_entity import (
    ExecutableEntity,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ExecutionTimeConstraint(TimingConstraint):
    """AUTOSAR ExecutionTimeConstraint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "EXECUTION-TIME-CONSTRAINT"


    component: Optional[Any]
    executable_entity_ref: Optional[ARRef]
    execution_time: Optional[ExecutionTimeTypeEnum]
    maximum: Optional[MultidimensionalTime]
    minimum: Optional[MultidimensionalTime]
    _DESERIALIZE_DISPATCH = {
        "COMPONENT": lambda obj, elem: setattr(obj, "component", SerializationHelper.deserialize_by_tag(elem, "any (SwComponent)")),
        "EXECUTABLE-ENTITY-REF": ("_POLYMORPHIC", "executable_entity_ref", ["BswCalledEntity", "BswInterruptEntity", "BswModuleEntity", "BswSchedulableEntity", "RunnableEntity"]),
        "EXECUTION-TIME": lambda obj, elem: setattr(obj, "execution_time", ExecutionTimeTypeEnum.deserialize(elem)),
        "MAXIMUM": lambda obj, elem: setattr(obj, "maximum", SerializationHelper.deserialize_by_tag(elem, "MultidimensionalTime")),
        "MINIMUM": lambda obj, elem: setattr(obj, "minimum", SerializationHelper.deserialize_by_tag(elem, "MultidimensionalTime")),
    }


    def __init__(self) -> None:
        """Initialize ExecutionTimeConstraint."""
        super().__init__()
        self.component: Optional[Any] = None
        self.executable_entity_ref: Optional[ARRef] = None
        self.execution_time: Optional[ExecutionTimeTypeEnum] = None
        self.maximum: Optional[MultidimensionalTime] = None
        self.minimum: Optional[MultidimensionalTime] = None

    def serialize(self) -> ET.Element:
        """Serialize ExecutionTimeConstraint to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ExecutionTimeConstraint, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize component
        if self.component is not None:
            serialized = SerializationHelper.serialize_item(self.component, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMPONENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize executable_entity_ref
        if self.executable_entity_ref is not None:
            serialized = SerializationHelper.serialize_item(self.executable_entity_ref, "ExecutableEntity")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EXECUTABLE-ENTITY-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize execution_time
        if self.execution_time is not None:
            serialized = SerializationHelper.serialize_item(self.execution_time, "ExecutionTimeTypeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EXECUTION-TIME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize maximum
        if self.maximum is not None:
            serialized = SerializationHelper.serialize_item(self.maximum, "MultidimensionalTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAXIMUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize minimum
        if self.minimum is not None:
            serialized = SerializationHelper.serialize_item(self.minimum, "MultidimensionalTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MINIMUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ExecutionTimeConstraint":
        """Deserialize XML element to ExecutionTimeConstraint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ExecutionTimeConstraint object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ExecutionTimeConstraint, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "COMPONENT":
                setattr(obj, "component", SerializationHelper.deserialize_by_tag(child, "any (SwComponent)"))
            elif tag == "EXECUTABLE-ENTITY-REF":
                setattr(obj, "executable_entity_ref", ARRef.deserialize(child))
            elif tag == "EXECUTION-TIME":
                setattr(obj, "execution_time", ExecutionTimeTypeEnum.deserialize(child))
            elif tag == "MAXIMUM":
                setattr(obj, "maximum", SerializationHelper.deserialize_by_tag(child, "MultidimensionalTime"))
            elif tag == "MINIMUM":
                setattr(obj, "minimum", SerializationHelper.deserialize_by_tag(child, "MultidimensionalTime"))

        return obj



class ExecutionTimeConstraintBuilder(TimingConstraintBuilder):
    """Builder for ExecutionTimeConstraint with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ExecutionTimeConstraint = ExecutionTimeConstraint()


    def with_component(self, value: Optional[Any]) -> "ExecutionTimeConstraintBuilder":
        """Set component attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'component' is required and cannot be None")
        self._obj.component = value
        return self

    def with_executable_entity(self, value: Optional[ExecutableEntity]) -> "ExecutionTimeConstraintBuilder":
        """Set executable_entity attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'executable_entity' is required and cannot be None")
        self._obj.executable_entity = value
        return self

    def with_execution_time(self, value: Optional[ExecutionTimeTypeEnum]) -> "ExecutionTimeConstraintBuilder":
        """Set execution_time attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'execution_time' is required and cannot be None")
        self._obj.execution_time = value
        return self

    def with_maximum(self, value: Optional[MultidimensionalTime]) -> "ExecutionTimeConstraintBuilder":
        """Set maximum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'maximum' is required and cannot be None")
        self._obj.maximum = value
        return self

    def with_minimum(self, value: Optional[MultidimensionalTime]) -> "ExecutionTimeConstraintBuilder":
        """Set minimum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'minimum' is required and cannot be None")
        self._obj.minimum = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "component",
        "executableEntity",
        "executionTime",
        "maximum",
        "minimum",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ExecutionTimeConstraint:
        """Build and return the ExecutionTimeConstraint instance with validation."""
        self._validate_instance()
        return self._obj