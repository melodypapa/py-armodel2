"""ModeInBswModuleDescriptionInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 323)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswOverview_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswOverview.bsw_module_description import (
    BswModuleDescription,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class ModeInBswModuleDescriptionInstanceRef(ARObject):
    """AUTOSAR ModeInBswModuleDescriptionInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    base: Optional[BswModuleDescription]
    context_mode_group_ref: Optional[ARRef]
    target_mode: Optional[ModeDeclaration]
    def __init__(self) -> None:
        """Initialize ModeInBswModuleDescriptionInstanceRef."""
        super().__init__()
        self.base: Optional[BswModuleDescription] = None
        self.context_mode_group_ref: Optional[ARRef] = None
        self.target_mode: Optional[ModeDeclaration] = None


class ModeInBswModuleDescriptionInstanceRefBuilder:
    """Builder for ModeInBswModuleDescriptionInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeInBswModuleDescriptionInstanceRef = ModeInBswModuleDescriptionInstanceRef()

    def build(self) -> ModeInBswModuleDescriptionInstanceRef:
        """Build and return ModeInBswModuleDescriptionInstanceRef object.

        Returns:
            ModeInBswModuleDescriptionInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
