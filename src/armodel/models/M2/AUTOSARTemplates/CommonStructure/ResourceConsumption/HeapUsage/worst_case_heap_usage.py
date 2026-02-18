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
