"""ModeAccessPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 323)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 634)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_ModeDeclarationGroup.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario.mode_access_point_ident import (
    ModeAccessPointIdent,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class ModeAccessPoint(ARObject):
    """AUTOSAR ModeAccessPoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ident: Optional[ModeAccessPointIdent]
    mode_group_instance_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize ModeAccessPoint."""
        super().__init__()
        self.ident: Optional[ModeAccessPointIdent] = None
        self.mode_group_instance_ref: Optional[ARRef] = None


class ModeAccessPointBuilder:
    """Builder for ModeAccessPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeAccessPoint = ModeAccessPoint()

    def build(self) -> ModeAccessPoint:
        """Build and return ModeAccessPoint object.

        Returns:
            ModeAccessPoint instance
        """
        # TODO: Add validation
        return self._obj
