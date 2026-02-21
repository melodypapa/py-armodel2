"""RoughEstimateOfExecutionTime AUTOSAR element.

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
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)


class RoughEstimateOfExecutionTime(ExecutionTime):
    """AUTOSAR RoughEstimateOfExecutionTime."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    additional: Optional[String]
    estimated_execution_time: Optional[MultidimensionalTime]
    def __init__(self) -> None:
        """Initialize RoughEstimateOfExecutionTime."""
        super().__init__()
        self.additional: Optional[String] = None
        self.estimated_execution_time: Optional[MultidimensionalTime] = None

    def serialize(self) -> ET.Element:
        """Serialize RoughEstimateOfExecutionTime to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RoughEstimateOfExecutionTime, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize additional
        if self.additional is not None:
            serialized = SerializationHelper.serialize_item(self.additional, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ADDITIONAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize estimated_execution_time
        if self.estimated_execution_time is not None:
            serialized = SerializationHelper.serialize_item(self.estimated_execution_time, "MultidimensionalTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ESTIMATED-EXECUTION-TIME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RoughEstimateOfExecutionTime":
        """Deserialize XML element to RoughEstimateOfExecutionTime object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RoughEstimateOfExecutionTime object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RoughEstimateOfExecutionTime, cls).deserialize(element)

        # Parse additional
        child = SerializationHelper.find_child_element(element, "ADDITIONAL")
        if child is not None:
            additional_value = child.text
            obj.additional = additional_value

        # Parse estimated_execution_time
        child = SerializationHelper.find_child_element(element, "ESTIMATED-EXECUTION-TIME")
        if child is not None:
            estimated_execution_time_value = SerializationHelper.deserialize_by_tag(child, "MultidimensionalTime")
            obj.estimated_execution_time = estimated_execution_time_value

        return obj



class RoughEstimateOfExecutionTimeBuilder:
    """Builder for RoughEstimateOfExecutionTime."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RoughEstimateOfExecutionTime = RoughEstimateOfExecutionTime()

    def build(self) -> RoughEstimateOfExecutionTime:
        """Build and return RoughEstimateOfExecutionTime object.

        Returns:
            RoughEstimateOfExecutionTime instance
        """
        # TODO: Add validation
        return self._obj
