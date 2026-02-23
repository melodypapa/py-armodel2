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
from armodel.serialization import SerializationHelper
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
        tag = SerializationHelper.get_xml_tag(self.__class__)
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
                serialized = SerializationHelper.serialize_item(item, "NameToken")
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
                serialized = SerializationHelper.serialize_item(item, "AclObjectSet")
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
                serialized = SerializationHelper.serialize_item(item, "AclOperation")
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
                serialized = SerializationHelper.serialize_item(item, "AclRole")
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
            serialized = SerializationHelper.serialize_item(self.acl_scope, "AclScopeEnum")
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
        container = SerializationHelper.find_child_element(element, "ACL-CONTEXTS")
        if container is not None:
            for child in container:
                # Extract primitive value (NameToken) as text
                child_value = child.text
                if child_value is not None:
                    obj.acl_contexts.append(child_value)

        # Parse acl_object_set_refs (list from container "ACL-OBJECT-SET-REFS")
        obj.acl_object_set_refs = []
        container = SerializationHelper.find_child_element(element, "ACL-OBJECT-SET-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.acl_object_set_refs.append(child_value)

        # Parse acl_operation_refs (list from container "ACL-OPERATION-REFS")
        obj.acl_operation_refs = []
        container = SerializationHelper.find_child_element(element, "ACL-OPERATION-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.acl_operation_refs.append(child_value)

        # Parse acl_role_refs (list from container "ACL-ROLE-REFS")
        obj.acl_role_refs = []
        container = SerializationHelper.find_child_element(element, "ACL-ROLE-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.acl_role_refs.append(child_value)

        # Parse acl_scope
        child = SerializationHelper.find_child_element(element, "ACL-SCOPE")
        if child is not None:
            acl_scope_value = AclScopeEnum.deserialize(child)
            obj.acl_scope = acl_scope_value

        return obj



class AclPermissionBuilder:
    """Builder for AclPermission with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: AclPermission = AclPermission()


    def with_short_name(self, value: Identifier) -> "AclPermissionBuilder":
        """Set short_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.short_name = value
        return self

    def with_short_name_fragments(self, items: list[ShortNameFragment]) -> "AclPermissionBuilder":
        """Set short_name_fragments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = list(items) if items else []
        return self

    def with_long_name(self, value: Optional[MultilanguageLongName]) -> "AclPermissionBuilder":
        """Set long_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.long_name = value
        return self

    def with_admin_data(self, value: Optional[AdminData]) -> "AclPermissionBuilder":
        """Set admin_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.admin_data = value
        return self

    def with_annotations(self, items: list[Annotation]) -> "AclPermissionBuilder":
        """Set annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.annotations = list(items) if items else []
        return self

    def with_desc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "AclPermissionBuilder":
        """Set desc attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.desc = value
        return self

    def with_category(self, value: Optional[CategoryString]) -> "AclPermissionBuilder":
        """Set category attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.category = value
        return self

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "AclPermissionBuilder":
        """Set introduction attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.introduction = value
        return self

    def with_uuid(self, value: Optional[String]) -> "AclPermissionBuilder":
        """Set uuid attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.uuid = value
        return self

    def with_acl_contexts(self, items: list[NameToken]) -> "AclPermissionBuilder":
        """Set acl_contexts list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.acl_contexts = list(items) if items else []
        return self

    def with_acl_object_sets(self, items: list[AclObjectSet]) -> "AclPermissionBuilder":
        """Set acl_object_sets list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.acl_object_sets = list(items) if items else []
        return self

    def with_acl_operations(self, items: list[AclOperation]) -> "AclPermissionBuilder":
        """Set acl_operations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.acl_operations = list(items) if items else []
        return self

    def with_acl_roles(self, items: list[AclRole]) -> "AclPermissionBuilder":
        """Set acl_roles list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.acl_roles = list(items) if items else []
        return self

    def with_acl_scope(self, value: AclScopeEnum) -> "AclPermissionBuilder":
        """Set acl_scope attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.acl_scope = value
        return self


    def add_short_name_fragment(self, item: ShortNameFragment) -> "AclPermissionBuilder":
        """Add a single item to short_name_fragments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments.append(item)
        return self

    def clear_short_name_fragments(self) -> "AclPermissionBuilder":
        """Clear all items from short_name_fragments list.

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = []
        return self

    def add_annotation(self, item: Annotation) -> "AclPermissionBuilder":
        """Add a single item to annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.annotations.append(item)
        return self

    def clear_annotations(self) -> "AclPermissionBuilder":
        """Clear all items from annotations list.

        Returns:
            self for method chaining
        """
        self._obj.annotations = []
        return self

    def add_acl_context(self, item: NameToken) -> "AclPermissionBuilder":
        """Add a single item to acl_contexts list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.acl_contexts.append(item)
        return self

    def clear_acl_contexts(self) -> "AclPermissionBuilder":
        """Clear all items from acl_contexts list.

        Returns:
            self for method chaining
        """
        self._obj.acl_contexts = []
        return self

    def add_acl_object_set(self, item: AclObjectSet) -> "AclPermissionBuilder":
        """Add a single item to acl_object_sets list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.acl_object_sets.append(item)
        return self

    def clear_acl_object_sets(self) -> "AclPermissionBuilder":
        """Clear all items from acl_object_sets list.

        Returns:
            self for method chaining
        """
        self._obj.acl_object_sets = []
        return self

    def add_acl_operation(self, item: AclOperation) -> "AclPermissionBuilder":
        """Add a single item to acl_operations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.acl_operations.append(item)
        return self

    def clear_acl_operations(self) -> "AclPermissionBuilder":
        """Clear all items from acl_operations list.

        Returns:
            self for method chaining
        """
        self._obj.acl_operations = []
        return self

    def add_acl_role(self, item: AclRole) -> "AclPermissionBuilder":
        """Add a single item to acl_roles list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.acl_roles.append(item)
        return self

    def clear_acl_roles(self) -> "AclPermissionBuilder":
        """Clear all items from acl_roles list.

        Returns:
            self for method chaining
        """
        self._obj.acl_roles = []
        return self


    @staticmethod
    def _coerce_to_int(value: Any) -> int:
        """Coerce value to int.

        Args:
            value: Value to coerce

        Returns:
            Integer value

        Raises:
            ValueError: If value cannot be coerced to int
        """
        if isinstance(value, int):
            return value
        if isinstance(value, str) and value.isdigit():
            return int(value)
        if isinstance(value, float):
            return int(value)
        if isinstance(value, bool):
            return int(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to int: {value}")

    @staticmethod
    def _coerce_to_float(value: Any) -> float:
        """Coerce value to float.

        Args:
            value: Value to coerce

        Returns:
            Float value

        Raises:
            ValueError: If value cannot be coerced to float
        """
        if isinstance(value, float):
            return value
        if isinstance(value, int):
            return float(value)
        if isinstance(value, str):
            try:
                return float(value)
            except ValueError:
                pass
        raise ValueError(f"Cannot coerce {type(value).__name__} to float: {value}")

    @staticmethod
    def _coerce_to_bool(value: Any) -> bool:
        """Coerce value to bool.

        Args:
            value: Value to coerce

        Returns:
            Boolean value

        Raises:
            ValueError: If value cannot be coerced to bool
        """
        if isinstance(value, bool):
            return value
        if isinstance(value, int):
            return bool(value)
        if isinstance(value, str):
            if value.lower() in ("true", "1", "yes"):
                return True
            if value.lower() in ("false", "0", "no"):
                return False
        raise ValueError(f"Cannot coerce {type(value).__name__} to bool: {value}")

    @staticmethod
    def _coerce_to_str(value: Any) -> str:
        """Coerce value to str.

        Args:
            value: Value to coerce

        Returns:
            String value
        """
        return str(value)


    @staticmethod
    def _coerce_to_list(value: Any, item_type: str) -> list:
        """Coerce value to list.

        Args:
            value: Value to coerce
            item_type: Expected item type (for error messages)

        Returns:
            List value

        Raises:
            ValueError: If value cannot be coerced to list
        """
        if isinstance(value, list):
            return value
        if isinstance(value, tuple):
            return list(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to list[{item_type}]: {value}")


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Get type hints for the class
        try:
            type_hints_dict = get_type_hints(type(self._obj))
        except Exception:
            # Cannot resolve type hints (e.g., forward references), skip validation
            return

        for attr_name, attr_type in type_hints_dict.items():
            if attr_name.startswith("_"):
                continue

            value = getattr(self._obj, attr_name)

            # Check required fields (not Optional)
            if value is None and not self._is_optional_type(attr_type):
                if mode == BuilderValidationMode.STRICT:
                    raise ValueError(
                        f"Required attribute '{attr_name}' is None"
                    )
                elif mode == BuilderValidationMode.LENIENT:
                    import warnings
                    warnings.warn(
                        f"Required attribute '{attr_name}' is None",
                        UserWarning
                    )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type is Optional, False otherwise
        """
        origin = getattr(type_hint, "__origin__", None)
        return origin is Union

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract expected type from type hint.

        Args:
            type_hint: Type hint to extract from

        Returns:
            Expected type
        """
        if isinstance(type_hint, str):
            return object
        origin = getattr(type_hint, "__origin__", None)
        if origin is Union:
            args = getattr(type_hint, "__args__", [])
            for arg in args:
                if arg is not type(None):
                    return arg
        elif origin is list:
            args = getattr(type_hint, "__args__", [object])
            return args[0] if args else object
        return type_hint if isinstance(type_hint, type) else object


    def build(self) -> AclPermission:
        """Build and return the AclPermission instance with validation."""
        self._validate_instance()
        pass
        return self._obj