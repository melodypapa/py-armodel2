"""BswModuleDependency AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 47)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswInterfaces.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswOverview.bsw_module_description import (
        BswModuleDescription,
    )



class BswModuleDependency(Identifiable):
    """AUTOSAR BswModuleDependency."""

    target_module_id: Optional[PositiveInteger]
    target_module: Optional[BswModuleDescription]
    def __init__(self) -> None:
        """Initialize BswModuleDependency."""
        super().__init__()
        self.target_module_id: Optional[PositiveInteger] = None
        self.target_module: Optional[BswModuleDescription] = None


class BswModuleDependencyBuilder:
    """Builder for BswModuleDependency."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswModuleDependency = BswModuleDependency()

    def build(self) -> BswModuleDependency:
        """Build and return BswModuleDependency object.

        Returns:
            BswModuleDependency instance
        """
        # TODO: Add validation
        return self._obj
