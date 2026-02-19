"""MeasuredHeapUsage AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 152)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ResourceConsumption_HeapUsage.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.HeapUsage.heap_usage import (
    HeapUsage,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)


class MeasuredHeapUsage(HeapUsage):
    """AUTOSAR MeasuredHeapUsage."""

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
        """Initialize MeasuredHeapUsage."""
        super().__init__()
        self.average_memory_consumption: Optional[PositiveInteger] = None
        self.maximum_memory_consumption: Optional[PositiveInteger] = None
        self.minimum_memory_consumption: Optional[PositiveInteger] = None
        self.test_pattern: Optional[String] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "MeasuredHeapUsage":
        """Deserialize XML element to MeasuredHeapUsage object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MeasuredHeapUsage object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

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



class MeasuredHeapUsageBuilder:
    """Builder for MeasuredHeapUsage."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MeasuredHeapUsage = MeasuredHeapUsage()

    def build(self) -> MeasuredHeapUsage:
        """Build and return MeasuredHeapUsage object.

        Returns:
            MeasuredHeapUsage instance
        """
        # TODO: Add validation
        return self._obj
