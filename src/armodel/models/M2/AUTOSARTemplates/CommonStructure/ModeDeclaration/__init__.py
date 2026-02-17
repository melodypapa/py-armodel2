"""ModeDeclaration module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group_prototype import (
        ModeDeclarationGroupPrototype,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
        ModeDeclarationGroup,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
        ModeDeclaration,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_transition import (
        ModeTransition,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_error_behavior import (
        ModeErrorBehavior,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_request_type_map import (
        ModeRequestTypeMap,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group_prototype_mapping import (
        ModeDeclarationGroupPrototypeMapping,
    )

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_error_reaction_policy_enum import (
    ModeErrorReactionPolicyEnum,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_activation_kind import (
    ModeActivationKind,
)

__all__ = [
    "ModeActivationKind",
    "ModeDeclaration",
    "ModeDeclarationGroup",
    "ModeDeclarationGroupPrototype",
    "ModeDeclarationGroupPrototypeMapping",
    "ModeErrorBehavior",
    "ModeErrorReactionPolicyEnum",
    "ModeRequestTypeMap",
    "ModeTransition",
]
