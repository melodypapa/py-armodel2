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
    acl_operation_refs: list[ARRef]
    acl_role_refs: list[ARRef]
    acl_scope: AclScopeEnum
    def __init__(self) -> None:
        """Initialize AclPermission."""
        super().__init__()
        self.acl_contexts: list[NameToken] = []
        self.acl_object_set_refs: list[ARRef] = []
        self.acl_operation_refs: list[ARRef] = []
        self.acl_role_refs: list[ARRef] = []
        self.acl_scope: AclScopeEnum = None

    def serialize(self) -> ET.Element:
        """Serialize AclPermission to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AclPermission, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize acl_contexts (list to container "ACL-CONTEXTS")
        if self.acl_contexts:
            wrapper = ET.Element("ACL-CONTEXTS")
            for item in self.acl_contexts:
                serialized = ARObject._serialize_item(item, "NameToken")
                if serialized is not None:
                    child_elem = ET.Element("ACL-CONTEXT")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize acl_object_set_refs (list to container "ACL-OBJECT-SET-REFS")
        if self.acl_object_set_refs:
            wrapper = ET.Element("ACL-OBJECT-SET-REFS")
            for item in self.acl_object_set_refs:
                serialized = ARObject._serialize_item(item, "AclObjectSet")
                if serialized is not None:
                    child_elem = ET.Element("ACL-OBJECT-SET-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize acl_operation_refs (list to container "ACL-OPERATION-REFS")
        if self.acl_operation_refs:
            wrapper = ET.Element("ACL-OPERATION-REFS")
            for item in self.acl_operation_refs:
                serialized = ARObject._serialize_item(item, "AclOperation")
                if serialized is not None:
                    child_elem = ET.Element("ACL-OPERATION-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize acl_role_refs (list to container "ACL-ROLE-REFS")
        if self.acl_role_refs:
            wrapper = ET.Element("ACL-ROLE-REFS")
            for item in self.acl_role_refs:
                serialized = ARObject._serialize_item(item, "AclRole")
                if serialized is not None:
                    child_elem = ET.Element("ACL-ROLE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize acl_scope
        if self.acl_scope is not None:
            serialized = ARObject._serialize_item(self.acl_scope, "AclScopeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ACL-SCOPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

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
                # Extract primitive value (NameToken) as text
                child_value = child.text
                if child_value is not None:
                    obj.acl_contexts.append(child_value)

        # Parse acl_object_set_refs (list from container "ACL-OBJECT-SET-REFS")
        obj.acl_object_set_refs = []
        container = ARObject._find_child_element(element, "ACL-OBJECT-SET-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.acl_object_set_refs.append(child_value)

        # Parse acl_operation_refs (list from container "ACL-OPERATION-REFS")
        obj.acl_operation_refs = []
        container = ARObject._find_child_element(element, "ACL-OPERATION-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.acl_operation_refs.append(child_value)

        # Parse acl_role_refs (list from container "ACL-ROLE-REFS")
        obj.acl_role_refs = []
        container = ARObject._find_child_element(element, "ACL-ROLE-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.acl_role_refs.append(child_value)

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
