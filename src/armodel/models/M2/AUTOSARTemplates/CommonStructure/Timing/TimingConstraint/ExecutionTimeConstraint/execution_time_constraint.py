"""ExecutionTimeConstraint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 130)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_ExecutionTimeConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.timing_constraint import (
    TimingConstraint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionTimeConstraint import (
    ExecutionTimeTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.executable_entity import (
    ExecutableEntity,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)


class ExecutionTimeConstraint(TimingConstraint):
    """AUTOSAR ExecutionTimeConstraint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    component: Optional[Any]
    executable_entity_ref: Optional[ARRef]
    execution_time: Optional[ExecutionTimeTypeEnum]
    maximum: Optional[MultidimensionalTime]
    minimum: Optional[MultidimensionalTime]
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
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ExecutionTimeConstraint, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize component
        if self.component is not None:
            serialized = ARObject._serialize_item(self.component, "Any")
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
            serialized = ARObject._serialize_item(self.executable_entity_ref, "ExecutableEntity")
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
            serialized = ARObject._serialize_item(self.execution_time, "ExecutionTimeTypeEnum")
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
            serialized = ARObject._serialize_item(self.maximum, "MultidimensionalTime")
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
            serialized = ARObject._serialize_item(self.minimum, "MultidimensionalTime")
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

        # Parse component
        child = ARObject._find_child_element(element, "COMPONENT")
        if child is not None:
            component_value = child.text
            obj.component = component_value

        # Parse executable_entity_ref
        child = ARObject._find_child_element(element, "EXECUTABLE-ENTITY-REF")
        if child is not None:
            executable_entity_ref_value = ARRef.deserialize(child)
            obj.executable_entity_ref = executable_entity_ref_value

        # Parse execution_time
        child = ARObject._find_child_element(element, "EXECUTION-TIME")
        if child is not None:
            execution_time_value = ExecutionTimeTypeEnum.deserialize(child)
            obj.execution_time = execution_time_value

        # Parse maximum
        child = ARObject._find_child_element(element, "MAXIMUM")
        if child is not None:
            maximum_value = ARObject._deserialize_by_tag(child, "MultidimensionalTime")
            obj.maximum = maximum_value

        # Parse minimum
        child = ARObject._find_child_element(element, "MINIMUM")
        if child is not None:
            minimum_value = ARObject._deserialize_by_tag(child, "MultidimensionalTime")
            obj.minimum = minimum_value

        return obj



class ExecutionTimeConstraintBuilder:
    """Builder for ExecutionTimeConstraint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ExecutionTimeConstraint = ExecutionTimeConstraint()

    def build(self) -> ExecutionTimeConstraint:
        """Build and return ExecutionTimeConstraint object.

        Returns:
            ExecutionTimeConstraint instance
        """
        # TODO: Add validation
        return self._obj
