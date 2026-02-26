"""RolesAndRights module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.RolesAndRights.acl_permission import (
        AclPermission,
    )
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.RolesAndRights.acl_object_set import (
        AclObjectSet,
    )
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.RolesAndRights.atp_definition import (
        AtpDefinition,
    )
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.RolesAndRights.acl_operation import (
        AclOperation,
    )
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.RolesAndRights.acl_role import (
        AclRole,
    )

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.RolesAndRights.acl_scope_enum import (
    AclScopeEnum,
)

__all__ = [
    "AclObjectSet",
    "AclOperation",
    "AclPermission",
    "AclRole",
    "AclScopeEnum",
    "AtpDefinition",
]
