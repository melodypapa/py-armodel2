"""AclPermission AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 382)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 159)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_RolesAndRights.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.RolesAndRights import (
    AclScopeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.RolesAndRights.acl_object_set import (
    AclObjectSet,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.RolesAndRights.acl_operation import (
    AclOperation,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.RolesAndRights.acl_role import (
    AclRole,
)


class AclPermission(ARElement):
    """AUTOSAR AclPermission."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    acl_contexts: list[NameToken]
    acl_object_set_refs: list[ARRef]
    acl_operations: list[AclOperation]
    acl_roles: list[AclRole]
    acl_scope: AclScopeEnum
    def __init__(self) -> None:
        """Initialize AclPermission."""
        super().__init__()
        self.acl_contexts: list[NameToken] = []
        self.acl_object_set_refs: list[ARRef] = []
        self.acl_operations: list[AclOperation] = []
        self.acl_roles: list[AclRole] = []
        self.acl_scope: AclScopeEnum = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "AclPermission":
        """Deserialize XML element to AclPermission object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AclPermission object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse acl_contexts (list)
        obj.acl_contexts = []
        for child in ARObject._find_all_child_elements(element, "ACL-CONTEXTS"):
            acl_contexts_value = child.text
            obj.acl_contexts.append(acl_contexts_value)

        # Parse acl_object_set_refs (list)
        obj.acl_object_set_refs = []
        for child in ARObject._find_all_child_elements(element, "ACL-OBJECT-SETS"):
            acl_object_set_refs_value = ARObject._deserialize_by_tag(child, "AclObjectSet")
            obj.acl_object_set_refs.append(acl_object_set_refs_value)

        # Parse acl_operations (list)
        obj.acl_operations = []
        for child in ARObject._find_all_child_elements(element, "ACL-OPERATIONS"):
            acl_operations_value = ARObject._deserialize_by_tag(child, "AclOperation")
            obj.acl_operations.append(acl_operations_value)

        # Parse acl_roles (list)
        obj.acl_roles = []
        for child in ARObject._find_all_child_elements(element, "ACL-ROLES"):
            acl_roles_value = ARObject._deserialize_by_tag(child, "AclRole")
            obj.acl_roles.append(acl_roles_value)

        # Parse acl_scope
        child = ARObject._find_child_element(element, "ACL-SCOPE")
        if child is not None:
            acl_scope_value = child.text
            obj.acl_scope = acl_scope_value

        return obj



class AclPermissionBuilder:
    """Builder for AclPermission."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AclPermission = AclPermission()

    def build(self) -> AclPermission:
        """Build and return AclPermission object.

        Returns:
            AclPermission instance
        """
        # TODO: Add validation
        return self._obj
