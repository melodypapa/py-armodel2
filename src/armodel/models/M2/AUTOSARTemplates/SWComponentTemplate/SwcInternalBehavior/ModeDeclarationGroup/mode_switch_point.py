"""ModeSwitchPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 323)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 633)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_ModeDeclarationGroup.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount.abstract_access_point import (
    AbstractAccessPoint,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class ModeSwitchPoint(AbstractAccessPoint):
    """AUTOSAR ModeSwitchPoint."""

    mode_group_swc_instance_ref: Optional[ModeDeclarationGroup]
    def __init__(self) -> None:
        """Initialize ModeSwitchPoint."""
        super().__init__()
        self.mode_group_swc_instance_ref: Optional[ModeDeclarationGroup] = None


class ModeSwitchPointBuilder:
    """Builder for ModeSwitchPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeSwitchPoint = ModeSwitchPoint()

    def build(self) -> ModeSwitchPoint:
        """Build and return ModeSwitchPoint object.

        Returns:
            ModeSwitchPoint instance
        """
        # TODO: Add validation
        return self._obj
