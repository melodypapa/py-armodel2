"""WorstCaseHeapUsage AUTOSAR element.

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
)


class WorstCaseHeapUsage(HeapUsage):
    """AUTOSAR WorstCaseHeapUsage."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    memory_consumption: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize WorstCaseHeapUsage."""
        super().__init__()
        self.memory_consumption: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "WorstCaseHeapUsage":
        """Deserialize XML element to WorstCaseHeapUsage object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized WorstCaseHeapUsage object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(WorstCaseHeapUsage, cls).deserialize(element)

        # Parse memory_consumption
        child = ARObject._find_child_element(element, "MEMORY-CONSUMPTION")
        if child is not None:
            memory_consumption_value = child.text
            obj.memory_consumption = memory_consumption_value

        return obj



class WorstCaseHeapUsageBuilder:
    """Builder for WorstCaseHeapUsage."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: WorstCaseHeapUsage = WorstCaseHeapUsage()

    def build(self) -> WorstCaseHeapUsage:
        """Build and return WorstCaseHeapUsage object.

        Returns:
            WorstCaseHeapUsage instance
        """
        # TODO: Add validation
        return self._obj
