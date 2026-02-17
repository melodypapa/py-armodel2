"""WorstCaseStackUsage AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 150)

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


class WorstCaseStackUsage(StackUsage):
    """AUTOSAR WorstCaseStackUsage."""

    memory_consumption: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize WorstCaseStackUsage."""
        super().__init__()
        self.memory_consumption: Optional[PositiveInteger] = None


class WorstCaseStackUsageBuilder:
    """Builder for WorstCaseStackUsage."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: WorstCaseStackUsage = WorstCaseStackUsage()

    def build(self) -> WorstCaseStackUsage:
        """Build and return WorstCaseStackUsage object.

        Returns:
            WorstCaseStackUsage instance
        """
        # TODO: Add validation
        return self._obj
