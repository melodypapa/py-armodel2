"""SimulatedExecutionTime AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 167)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ResourceConsumption_ExecutionTime.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.ExecutionTime.execution_time import (
    ExecutionTime,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)


class SimulatedExecutionTime(ExecutionTime):
    """AUTOSAR SimulatedExecutionTime."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    maximum_execution_time: Optional[MultidimensionalTime]
    minimum_execution_time: Optional[MultidimensionalTime]
    nominal_execution_time: Optional[MultidimensionalTime]
    def __init__(self) -> None:
        """Initialize SimulatedExecutionTime."""
        super().__init__()
        self.maximum_execution_time: Optional[MultidimensionalTime] = None
        self.minimum_execution_time: Optional[MultidimensionalTime] = None
        self.nominal_execution_time: Optional[MultidimensionalTime] = None

    def serialize(self) -> ET.Element:
        """Serialize SimulatedExecutionTime to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SimulatedExecutionTime, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize maximum_execution_time
        if self.maximum_execution_time is not None:
            serialized = ARObject._serialize_item(self.maximum_execution_time, "MultidimensionalTime")
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
            serialized = ARObject._serialize_item(self.minimum_execution_time, "MultidimensionalTime")
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
            serialized = ARObject._serialize_item(self.nominal_execution_time, "MultidimensionalTime")
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
    def deserialize(cls, element: ET.Element) -> "SimulatedExecutionTime":
        """Deserialize XML element to SimulatedExecutionTime object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SimulatedExecutionTime object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SimulatedExecutionTime, cls).deserialize(element)

        # Parse maximum_execution_time
        child = ARObject._find_child_element(element, "MAXIMUM-EXECUTION-TIME")
        if child is not None:
            maximum_execution_time_value = ARObject._deserialize_by_tag(child, "MultidimensionalTime")
            obj.maximum_execution_time = maximum_execution_time_value

        # Parse minimum_execution_time
        child = ARObject._find_child_element(element, "MINIMUM-EXECUTION-TIME")
        if child is not None:
            minimum_execution_time_value = ARObject._deserialize_by_tag(child, "MultidimensionalTime")
            obj.minimum_execution_time = minimum_execution_time_value

        # Parse nominal_execution_time
        child = ARObject._find_child_element(element, "NOMINAL-EXECUTION-TIME")
        if child is not None:
            nominal_execution_time_value = ARObject._deserialize_by_tag(child, "MultidimensionalTime")
            obj.nominal_execution_time = nominal_execution_time_value

        return obj



class SimulatedExecutionTimeBuilder:
    """Builder for SimulatedExecutionTime."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SimulatedExecutionTime = SimulatedExecutionTime()

    def build(self) -> SimulatedExecutionTime:
        """Build and return SimulatedExecutionTime object.

        Returns:
            SimulatedExecutionTime instance
        """
        # TODO: Add validation
        return self._obj
