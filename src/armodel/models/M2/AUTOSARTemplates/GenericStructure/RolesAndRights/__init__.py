"""RolesAndRights module."""
from armodel.models.M2.AUTOSARTemplates.GenericStructure.RolesAndRights.acl_permission import (
    AclPermission,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.RolesAndRights.acl_object_set import (
    AclObjectSet,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.RolesAndRights.atp_definition import (
    AtpDefinition,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.RolesAndRights.acl_operation import (
    AclOperation,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.RolesAndRights.acl_role import (
    AclRole,
)

__all__ = [
    "AclObjectSet",
    "AclOperation",
    "AclPermission",
    "AclRole",
    "AtpDefinition",
]
