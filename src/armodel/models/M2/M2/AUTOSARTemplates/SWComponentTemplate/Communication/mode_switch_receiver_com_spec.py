"""ModeSwitchReceiverComSpec AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 191)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.r_port_com_spec import (
    RPortComSpec,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class ModeSwitchReceiverComSpec(RPortComSpec):
    """AUTOSAR ModeSwitchReceiverComSpec."""

    def __init__(self) -> None:
        """Initialize ModeSwitchReceiverComSpec."""
        super().__init__()
        self.enhanced_mode: Optional[Boolean] = None
        self.mode_group: Optional[ModeDeclarationGroup] = None
        self.supports: Optional[Boolean] = None


class ModeSwitchReceiverComSpecBuilder:
    """Builder for ModeSwitchReceiverComSpec."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeSwitchReceiverComSpec = ModeSwitchReceiverComSpec()

    def build(self) -> ModeSwitchReceiverComSpec:
        """Build and return ModeSwitchReceiverComSpec object.

        Returns:
            ModeSwitchReceiverComSpec instance
        """
        # TODO: Add validation
        return self._obj
