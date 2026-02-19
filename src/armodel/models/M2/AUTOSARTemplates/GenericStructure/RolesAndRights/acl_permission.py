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
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AclPermission, cls).deserialize(element)

        # Parse acl_contexts (list from container "ACL-CONTEXTS")
        obj.acl_contexts = []
        container = ARObject._find_child_element(element, "ACL-CONTEXTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.acl_contexts.append(child_value)

        # Parse acl_object_set_refs (list from container "ACL-OBJECT-SETS")
        obj.acl_object_set_refs = []
        container = ARObject._find_child_element(element, "ACL-OBJECT-SETS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.acl_object_set_refs.append(child_value)

        # Parse acl_operations (list from container "ACL-OPERATIONS")
        obj.acl_operations = []
        container = ARObject._find_child_element(element, "ACL-OPERATIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.acl_operations.append(child_value)

        # Parse acl_roles (list from container "ACL-ROLES")
        obj.acl_roles = []
        container = ARObject._find_child_element(element, "ACL-ROLES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.acl_roles.append(child_value)

        # Parse acl_scope
        child = ARObject._find_child_element(element, "ACL-SCOPE")
        if child is not None:
            acl_scope_value = AclScopeEnum.deserialize(child)
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
