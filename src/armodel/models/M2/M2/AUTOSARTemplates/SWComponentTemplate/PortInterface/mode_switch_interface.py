"""ModeSwitchInterface AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 113)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2039)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface import (
    PortInterface,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class ModeSwitchInterface(PortInterface):
    """AUTOSAR ModeSwitchInterface."""

    def __init__(self) -> None:
        """Initialize ModeSwitchInterface."""
        super().__init__()
        self.mode_group: Optional[ModeDeclarationGroup] = None


class ModeSwitchInterfaceBuilder:
    """Builder for ModeSwitchInterface."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeSwitchInterface = ModeSwitchInterface()

    def build(self) -> ModeSwitchInterface:
        """Build and return ModeSwitchInterface object.

        Returns:
            ModeSwitchInterface instance
        """
        # TODO: Add validation
        return self._obj
