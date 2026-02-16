"""AclPermission AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("acl_contexts", None, False, True, None),  # aclContexts
        ("acl_object_sets", None, False, True, AclObjectSet),  # aclObjectSets
        ("acl_operations", None, False, True, AclOperation),  # aclOperations
        ("acl_roles", None, False, True, AclRole),  # aclRoles
        ("acl_scope", None, False, False, AclScopeEnum),  # aclScope
    ]

    def __init__(self) -> None:
        """Initialize AclPermission."""
        super().__init__()
        self.acl_contexts: list[NameToken] = []
        self.acl_object_sets: list[AclObjectSet] = []
        self.acl_operations: list[AclOperation] = []
        self.acl_roles: list[AclRole] = []
        self.acl_scope: AclScopeEnum = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert AclPermission to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AclPermission":
        """Create AclPermission from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            AclPermission instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to AclPermission since parent returns ARObject
        return cast("AclPermission", obj)


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
