"""BswModeSenderPolicy AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 102)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_mode_switch_ack_request import (
    BswModeSwitchAckRequest,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class BswModeSenderPolicy(ARObject):
    """AUTOSAR BswModeSenderPolicy."""

    ack_request_request: Optional[BswModeSwitchAckRequest]
    enhanced_mode: Optional[Boolean]
    provided_mode: Optional[ModeDeclarationGroup]
    queue_length: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize BswModeSenderPolicy."""
        super().__init__()
        self.ack_request_request: Optional[BswModeSwitchAckRequest] = None
        self.enhanced_mode: Optional[Boolean] = None
        self.provided_mode: Optional[ModeDeclarationGroup] = None
        self.queue_length: Optional[PositiveInteger] = None


class BswModeSenderPolicyBuilder:
    """Builder for BswModeSenderPolicy."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswModeSenderPolicy = BswModeSenderPolicy()

    def build(self) -> BswModeSenderPolicy:
        """Build and return BswModeSenderPolicy object.

        Returns:
            BswModeSenderPolicy instance
        """
        # TODO: Add validation
        return self._obj
