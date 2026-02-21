"""MeasuredStackUsage AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 150)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ResourceConsumption_StackUsage.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.StackUsage.stack_usage import (
    StackUsage,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)


class MeasuredStackUsage(StackUsage):
    """AUTOSAR MeasuredStackUsage."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    average_memory_consumption: Optional[PositiveInteger]
    maximum_memory_consumption: Optional[PositiveInteger]
    minimum_memory_consumption: Optional[PositiveInteger]
    test_pattern: Optional[String]
    def __init__(self) -> None:
        """Initialize MeasuredStackUsage."""
        super().__init__()
        self.average_memory_consumption: Optional[PositiveInteger] = None
        self.maximum_memory_consumption: Optional[PositiveInteger] = None
        self.minimum_memory_consumption: Optional[PositiveInteger] = None
        self.test_pattern: Optional[String] = None

    def serialize(self) -> ET.Element:
        """Serialize MeasuredStackUsage to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MeasuredStackUsage, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize average_memory_consumption
        if self.average_memory_consumption is not None:
            serialized = ARObject._serialize_item(self.average_memory_consumption, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AVERAGE-MEMORY-CONSUMPTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize maximum_memory_consumption
        if self.maximum_memory_consumption is not None:
            serialized = ARObject._serialize_item(self.maximum_memory_consumption, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAXIMUM-MEMORY-CONSUMPTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize minimum_memory_consumption
        if self.minimum_memory_consumption is not None:
            serialized = ARObject._serialize_item(self.minimum_memory_consumption, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MINIMUM-MEMORY-CONSUMPTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize test_pattern
        if self.test_pattern is not None:
            serialized = ARObject._serialize_item(self.test_pattern, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TEST-PATTERN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MeasuredStackUsage":
        """Deserialize XML element to MeasuredStackUsage object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MeasuredStackUsage object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MeasuredStackUsage, cls).deserialize(element)

        # Parse average_memory_consumption
        child = ARObject._find_child_element(element, "AVERAGE-MEMORY-CONSUMPTION")
        if child is not None:
            average_memory_consumption_value = child.text
            obj.average_memory_consumption = average_memory_consumption_value

        # Parse maximum_memory_consumption
        child = ARObject._find_child_element(element, "MAXIMUM-MEMORY-CONSUMPTION")
        if child is not None:
            maximum_memory_consumption_value = child.text
            obj.maximum_memory_consumption = maximum_memory_consumption_value

        # Parse minimum_memory_consumption
        child = ARObject._find_child_element(element, "MINIMUM-MEMORY-CONSUMPTION")
        if child is not None:
            minimum_memory_consumption_value = child.text
            obj.minimum_memory_consumption = minimum_memory_consumption_value

        # Parse test_pattern
        child = ARObject._find_child_element(element, "TEST-PATTERN")
        if child is not None:
            test_pattern_value = child.text
            obj.test_pattern = test_pattern_value

        return obj



class MeasuredStackUsageBuilder:
    """Builder for MeasuredStackUsage."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MeasuredStackUsage = MeasuredStackUsage()

    def build(self) -> MeasuredStackUsage:
        """Build and return MeasuredStackUsage object.

        Returns:
            MeasuredStackUsage instance
        """
        # TODO: Add validation
        return self._obj
