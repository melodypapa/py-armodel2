"""AclObjectSet AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 383)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 158)

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
    ReferrableSubtypesEnum,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure.atp_blueprint import (
    AtpBlueprint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject.autosar_engineering_object import (
    AutosarEngineeringObject,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ElementCollection.collection import (
    Collection,
)


class AclObjectSet(ARElement):
    """AUTOSAR AclObjectSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    acl_object_classe_refs: list[ReferrableSubtypesEnum]
    acl_scope: AclScopeEnum
    collection_ref: Optional[ARRef]
    derived_from_refs: list[ARRef]
    engineerings: list[AutosarEngineeringObject]
    def __init__(self) -> None:
        """Initialize AclObjectSet."""
        super().__init__()
        self.acl_object_classe_refs: list[ReferrableSubtypesEnum] = []
        self.acl_scope: AclScopeEnum = None
        self.collection_ref: Optional[ARRef] = None
        self.derived_from_refs: list[ARRef] = []
        self.engineerings: list[AutosarEngineeringObject] = []

    def serialize(self) -> ET.Element:
        """Serialize AclObjectSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AclObjectSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize acl_object_classe_refs (list to container "ACL-OBJECT-CLASSE-REFS")
        if self.acl_object_classe_refs:
            wrapper = ET.Element("ACL-OBJECT-CLASSE-REFS")
            for item in self.acl_object_classe_refs:
                serialized = SerializationHelper.serialize_item(item, "ReferrableSubtypesEnum")
                if serialized is not None:
                    child_elem = ET.Element("ACL-OBJECT-CLASSE-REF")
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

        # Serialize collection_ref
        if self.collection_ref is not None:
            serialized = SerializationHelper.serialize_item(self.collection_ref, "Collection")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COLLECTION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize derived_from_refs (list to container "DERIVED-FROM-REFS")
        if self.derived_from_refs:
            wrapper = ET.Element("DERIVED-FROM-REFS")
            for item in self.derived_from_refs:
                serialized = SerializationHelper.serialize_item(item, "AtpBlueprint")
                if serialized is not None:
                    child_elem = ET.Element("DERIVED-FROM-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize engineerings (list to container "ENGINEERINGS")
        if self.engineerings:
            wrapper = ET.Element("ENGINEERINGS")
            for item in self.engineerings:
                serialized = SerializationHelper.serialize_item(item, "AutosarEngineeringObject")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AclObjectSet":
        """Deserialize XML element to AclObjectSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AclObjectSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AclObjectSet, cls).deserialize(element)

        # Parse acl_object_classe_refs (list from container "ACL-OBJECT-CLASSE-REFS")
        obj.acl_object_classe_refs = []
        container = SerializationHelper.find_child_element(element, "ACL-OBJECT-CLASSE-REFS")
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
                    obj.acl_object_classe_refs.append(child_value)

        # Parse acl_scope
        child = SerializationHelper.find_child_element(element, "ACL-SCOPE")
        if child is not None:
            acl_scope_value = AclScopeEnum.deserialize(child)
            obj.acl_scope = acl_scope_value

        # Parse collection_ref
        child = SerializationHelper.find_child_element(element, "COLLECTION-REF")
        if child is not None:
            collection_ref_value = ARRef.deserialize(child)
            obj.collection_ref = collection_ref_value

        # Parse derived_from_refs (list from container "DERIVED-FROM-REFS")
        obj.derived_from_refs = []
        container = SerializationHelper.find_child_element(element, "DERIVED-FROM-REFS")
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
                    obj.derived_from_refs.append(child_value)

        # Parse engineerings (list from container "ENGINEERINGS")
        obj.engineerings = []
        container = SerializationHelper.find_child_element(element, "ENGINEERINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.engineerings.append(child_value)

        return obj



class AclObjectSetBuilder:
    """Builder for AclObjectSet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: AclObjectSet = AclObjectSet()


    def with_short_name(self, value: Identifier) -> "AclObjectSetBuilder":
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

    def with_short_name_fragments(self, items: list[ShortNameFragment]) -> "AclObjectSetBuilder":
        """Set short_name_fragments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = list(items) if items else []
        return self

    def with_long_name(self, value: Optional[MultilanguageLongName]) -> "AclObjectSetBuilder":
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

    def with_admin_data(self, value: Optional[AdminData]) -> "AclObjectSetBuilder":
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

    def with_annotations(self, items: list[Annotation]) -> "AclObjectSetBuilder":
        """Set annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.annotations = list(items) if items else []
        return self

    def with_desc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "AclObjectSetBuilder":
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

    def with_category(self, value: Optional[CategoryString]) -> "AclObjectSetBuilder":
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

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "AclObjectSetBuilder":
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

    def with_uuid(self, value: Optional[String]) -> "AclObjectSetBuilder":
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

    def with_acl_object_classes(self, items: list[ReferrableSubtypesEnum]) -> "AclObjectSetBuilder":
        """Set acl_object_classes list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.acl_object_classes = list(items) if items else []
        return self

    def with_acl_scope(self, value: AclScopeEnum) -> "AclObjectSetBuilder":
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

    def with_collection(self, value: Optional[Collection]) -> "AclObjectSetBuilder":
        """Set collection attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.collection = value
        return self

    def with_derived_froms(self, items: list[AtpBlueprint]) -> "AclObjectSetBuilder":
        """Set derived_froms list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.derived_froms = list(items) if items else []
        return self

    def with_engineerings(self, items: list[AutosarEngineeringObject]) -> "AclObjectSetBuilder":
        """Set engineerings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.engineerings = list(items) if items else []
        return self


    def add_short_name_fragment(self, item: ShortNameFragment) -> "AclObjectSetBuilder":
        """Add a single item to short_name_fragments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments.append(item)
        return self

    def clear_short_name_fragments(self) -> "AclObjectSetBuilder":
        """Clear all items from short_name_fragments list.

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = []
        return self

    def add_annotation(self, item: Annotation) -> "AclObjectSetBuilder":
        """Add a single item to annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.annotations.append(item)
        return self

    def clear_annotations(self) -> "AclObjectSetBuilder":
        """Clear all items from annotations list.

        Returns:
            self for method chaining
        """
        self._obj.annotations = []
        return self

    def add_acl_object_classe(self, item: ReferrableSubtypesEnum) -> "AclObjectSetBuilder":
        """Add a single item to acl_object_classes list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.acl_object_classes.append(item)
        return self

    def clear_acl_object_classes(self) -> "AclObjectSetBuilder":
        """Clear all items from acl_object_classes list.

        Returns:
            self for method chaining
        """
        self._obj.acl_object_classes = []
        return self

    def add_derived_from(self, item: AtpBlueprint) -> "AclObjectSetBuilder":
        """Add a single item to derived_froms list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.derived_froms.append(item)
        return self

    def clear_derived_froms(self) -> "AclObjectSetBuilder":
        """Clear all items from derived_froms list.

        Returns:
            self for method chaining
        """
        self._obj.derived_froms = []
        return self

    def add_engineering(self, item: AutosarEngineeringObject) -> "AclObjectSetBuilder":
        """Add a single item to engineerings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.engineerings.append(item)
        return self

    def clear_engineerings(self) -> "AclObjectSetBuilder":
        """Clear all items from engineerings list.

        Returns:
            self for method chaining
        """
        self._obj.engineerings = []
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


    def build(self) -> AclObjectSet:
        """Build and return the AclObjectSet instance with validation."""
        self._validate_instance()
        pass
        return self._obj