"""BswModeReceiverPolicy AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 103)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class BswModeReceiverPolicy(ARObject):
    """AUTOSAR BswModeReceiverPolicy."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    enhanced_mode: Optional[Boolean]
    required_mode: Optional[ModeDeclarationGroup]
    supports: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize BswModeReceiverPolicy."""
        super().__init__()
        self.enhanced_mode: Optional[Boolean] = None
        self.required_mode: Optional[ModeDeclarationGroup] = None
        self.supports: Optional[Boolean] = None


class BswModeReceiverPolicyBuilder:
    """Builder for BswModeReceiverPolicy."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswModeReceiverPolicy = BswModeReceiverPolicy()

    def build(self) -> BswModeReceiverPolicy:
        """Build and return BswModeReceiverPolicy object.

        Returns:
            BswModeReceiverPolicy instance
        """
        # TODO: Add validation
        return self._obj
