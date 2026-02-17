"""RoughEstimateHeapUsage AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 153)

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


class RoughEstimateHeapUsage(HeapUsage):
    """AUTOSAR RoughEstimateHeapUsage."""

    def __init__(self) -> None:
        """Initialize RoughEstimateHeapUsage."""
        super().__init__()
        self.memory_consumption: Optional[PositiveInteger] = None


class RoughEstimateHeapUsageBuilder:
    """Builder for RoughEstimateHeapUsage."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RoughEstimateHeapUsage = RoughEstimateHeapUsage()

    def build(self) -> RoughEstimateHeapUsage:
        """Build and return RoughEstimateHeapUsage object.

        Returns:
            RoughEstimateHeapUsage instance
        """
        # TODO: Add validation
        return self._obj
