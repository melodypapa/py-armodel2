"""BswModeSenderPolicy AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 102)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "ack_request_request": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=BswModeSwitchAckRequest,
        ),  # ackRequestRequest
        "enhanced_mode": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # enhancedMode
        "provided_mode": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ModeDeclarationGroup,
        ),  # providedMode
        "queue_length": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # queueLength
    }

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
