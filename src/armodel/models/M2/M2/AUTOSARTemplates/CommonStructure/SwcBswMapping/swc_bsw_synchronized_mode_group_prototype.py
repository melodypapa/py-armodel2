"""SwcBswSynchronizedModeGroupPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 111)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_SwcBswMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class SwcBswSynchronizedModeGroupPrototype(ARObject):
    """AUTOSAR SwcBswSynchronizedModeGroupPrototype."""

    def __init__(self) -> None:
        """Initialize SwcBswSynchronizedModeGroupPrototype."""
        super().__init__()
        self.bsw_mode_group_prototype: Optional[ModeDeclarationGroup] = None
        self.swc_mode_group_swc_instance_ref: Optional[ModeDeclarationGroup] = None


class SwcBswSynchronizedModeGroupPrototypeBuilder:
    """Builder for SwcBswSynchronizedModeGroupPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcBswSynchronizedModeGroupPrototype = SwcBswSynchronizedModeGroupPrototype()

    def build(self) -> SwcBswSynchronizedModeGroupPrototype:
        """Build and return SwcBswSynchronizedModeGroupPrototype object.

        Returns:
            SwcBswSynchronizedModeGroupPrototype instance
        """
        # TODO: Add validation
        return self._obj
