"""RoughEstimateStackUsage AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 151)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ResourceConsumption_StackUsage.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.StackUsage.stack_usage import (
    StackUsage,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class RoughEstimateStackUsage(StackUsage):
    """AUTOSAR RoughEstimateStackUsage."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    memory_consumption: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize RoughEstimateStackUsage."""
        super().__init__()
        self.memory_consumption: Optional[PositiveInteger] = None


class RoughEstimateStackUsageBuilder:
    """Builder for RoughEstimateStackUsage."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RoughEstimateStackUsage = RoughEstimateStackUsage()

    def build(self) -> RoughEstimateStackUsage:
        """Build and return RoughEstimateStackUsage object.

        Returns:
            RoughEstimateStackUsage instance
        """
        # TODO: Add validation
        return self._obj
