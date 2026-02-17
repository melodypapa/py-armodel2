"""BswInterruptEntity AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 75)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 212)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_module_entity import (
    BswModuleEntity,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import (
    BswInterruptCategory,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class BswInterruptEntity(BswModuleEntity):
    """AUTOSAR BswInterruptEntity."""

    def __init__(self) -> None:
        """Initialize BswInterruptEntity."""
        super().__init__()
        self.interrupt_category: Optional[BswInterruptCategory] = None
        self.interrupt_source: Optional[String] = None


class BswInterruptEntityBuilder:
    """Builder for BswInterruptEntity."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswInterruptEntity = BswInterruptEntity()

    def build(self) -> BswInterruptEntity:
        """Build and return BswInterruptEntity object.

        Returns:
            BswInterruptEntity instance
        """
        # TODO: Add validation
        return self._obj
