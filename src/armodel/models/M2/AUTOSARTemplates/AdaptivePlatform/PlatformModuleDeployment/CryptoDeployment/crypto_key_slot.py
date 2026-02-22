"""CryptoKeySlot AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 57)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_AdaptivePlatform_PlatformModuleDeployment_CryptoDeployment.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    String,
)


class CryptoKeySlot(Identifiable):
    """AUTOSAR CryptoKeySlot."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    allocate_shadow_copy: Optional[Boolean]
    crypto_alg_id: Optional[String]
    crypto_object_type: Optional[CryptoObjectTypeEnum]
    key_slot_allowed_modification: Optional[CryptoKeySlotAllowedModification]
    key_slot_content_allowed_usages: list[CryptoKeySlotContentAllowedUsage]
    slot_capacity: Optional[PositiveInteger]
    slot_type: Optional[CryptoKeySlotTypeEnum]
    def __init__(self) -> None:
        """Initialize CryptoKeySlot."""
        super().__init__()
        self.allocate_shadow_copy: Optional[Boolean] = None
        self.crypto_alg_id: Optional[String] = None
        self.crypto_object_type: Optional[CryptoObjectTypeEnum] = None
        self.key_slot_allowed_modification: Optional[CryptoKeySlotAllowedModification] = None
        self.key_slot_content_allowed_usages: list[CryptoKeySlotContentAllowedUsage] = []
        self.slot_capacity: Optional[PositiveInteger] = None
        self.slot_type: Optional[CryptoKeySlotTypeEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize CryptoKeySlot to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CryptoKeySlot, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize allocate_shadow_copy
        if self.allocate_shadow_copy is not None:
            serialized = SerializationHelper.serialize_item(self.allocate_shadow_copy, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ALLOCATE-SHADOW-COPY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize crypto_alg_id
        if self.crypto_alg_id is not None:
            serialized = SerializationHelper.serialize_item(self.crypto_alg_id, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CRYPTO-ALG-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize crypto_object_type
        if self.crypto_object_type is not None:
            serialized = SerializationHelper.serialize_item(self.crypto_object_type, "CryptoObjectTypeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CRYPTO-OBJECT-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize key_slot_allowed_modification
        if self.key_slot_allowed_modification is not None:
            serialized = SerializationHelper.serialize_item(self.key_slot_allowed_modification, "CryptoKeySlotAllowedModification")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("KEY-SLOT-ALLOWED-MODIFICATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize key_slot_content_allowed_usages (list to container "KEY-SLOT-CONTENT-ALLOWED-USAGES")
        if self.key_slot_content_allowed_usages:
            wrapper = ET.Element("KEY-SLOT-CONTENT-ALLOWED-USAGES")
            for item in self.key_slot_content_allowed_usages:
                serialized = SerializationHelper.serialize_item(item, "CryptoKeySlotContentAllowedUsage")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize slot_capacity
        if self.slot_capacity is not None:
            serialized = SerializationHelper.serialize_item(self.slot_capacity, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SLOT-CAPACITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize slot_type
        if self.slot_type is not None:
            serialized = SerializationHelper.serialize_item(self.slot_type, "CryptoKeySlotTypeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SLOT-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CryptoKeySlot":
        """Deserialize XML element to CryptoKeySlot object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CryptoKeySlot object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CryptoKeySlot, cls).deserialize(element)

        # Parse allocate_shadow_copy
        child = SerializationHelper.find_child_element(element, "ALLOCATE-SHADOW-COPY")
        if child is not None:
            allocate_shadow_copy_value = child.text
            obj.allocate_shadow_copy = allocate_shadow_copy_value

        # Parse crypto_alg_id
        child = SerializationHelper.find_child_element(element, "CRYPTO-ALG-ID")
        if child is not None:
            crypto_alg_id_value = child.text
            obj.crypto_alg_id = crypto_alg_id_value

        # Parse crypto_object_type
        child = SerializationHelper.find_child_element(element, "CRYPTO-OBJECT-TYPE")
        if child is not None:
            crypto_object_type_value = SerializationHelper.deserialize_by_tag(child, "CryptoObjectTypeEnum")
            obj.crypto_object_type = crypto_object_type_value

        # Parse key_slot_allowed_modification
        child = SerializationHelper.find_child_element(element, "KEY-SLOT-ALLOWED-MODIFICATION")
        if child is not None:
            key_slot_allowed_modification_value = SerializationHelper.deserialize_by_tag(child, "CryptoKeySlotAllowedModification")
            obj.key_slot_allowed_modification = key_slot_allowed_modification_value

        # Parse key_slot_content_allowed_usages (list from container "KEY-SLOT-CONTENT-ALLOWED-USAGES")
        obj.key_slot_content_allowed_usages = []
        container = SerializationHelper.find_child_element(element, "KEY-SLOT-CONTENT-ALLOWED-USAGES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.key_slot_content_allowed_usages.append(child_value)

        # Parse slot_capacity
        child = SerializationHelper.find_child_element(element, "SLOT-CAPACITY")
        if child is not None:
            slot_capacity_value = child.text
            obj.slot_capacity = slot_capacity_value

        # Parse slot_type
        child = SerializationHelper.find_child_element(element, "SLOT-TYPE")
        if child is not None:
            slot_type_value = SerializationHelper.deserialize_by_tag(child, "CryptoKeySlotTypeEnum")
            obj.slot_type = slot_type_value

        return obj



class CryptoKeySlotBuilder:
    """Builder for CryptoKeySlot with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: CryptoKeySlot = CryptoKeySlot()


    def with_short_name(self, value: Identifier) -> "CryptoKeySlotBuilder":
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

    def with_short_name_fragments(self, items: list[ShortNameFragment]) -> "CryptoKeySlotBuilder":
        """Set short_name_fragments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = list(items) if items else []
        return self

    def with_long_name(self, value: Optional[MultilanguageLongName]) -> "CryptoKeySlotBuilder":
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

    def with_admin_data(self, value: Optional[AdminData]) -> "CryptoKeySlotBuilder":
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

    def with_annotations(self, items: list[Annotation]) -> "CryptoKeySlotBuilder":
        """Set annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.annotations = list(items) if items else []
        return self

    def with_desc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "CryptoKeySlotBuilder":
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

    def with_category(self, value: Optional[CategoryString]) -> "CryptoKeySlotBuilder":
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

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "CryptoKeySlotBuilder":
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

    def with_uuid(self, value: Optional[String]) -> "CryptoKeySlotBuilder":
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

    def with_allocate_shadow_copy(self, value: Optional[Boolean]) -> "CryptoKeySlotBuilder":
        """Set allocate_shadow_copy attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.allocate_shadow_copy = value
        return self

    def with_crypto_alg_id(self, value: Optional[String]) -> "CryptoKeySlotBuilder":
        """Set crypto_alg_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.crypto_alg_id = value
        return self

    def with_crypto_object_type(self, value: Optional[CryptoObjectTypeEnum]) -> "CryptoKeySlotBuilder":
        """Set crypto_object_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.crypto_object_type = value
        return self

    def with_key_slot_allowed_modification(self, value: Optional[CryptoKeySlotAllowedModification]) -> "CryptoKeySlotBuilder":
        """Set key_slot_allowed_modification attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.key_slot_allowed_modification = value
        return self

    def with_key_slot_content_allowed_usages(self, items: list[CryptoKeySlotContentAllowedUsage]) -> "CryptoKeySlotBuilder":
        """Set key_slot_content_allowed_usages list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.key_slot_content_allowed_usages = list(items) if items else []
        return self

    def with_slot_capacity(self, value: Optional[PositiveInteger]) -> "CryptoKeySlotBuilder":
        """Set slot_capacity attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.slot_capacity = value
        return self

    def with_slot_type(self, value: Optional[CryptoKeySlotTypeEnum]) -> "CryptoKeySlotBuilder":
        """Set slot_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.slot_type = value
        return self


    def add_short_name_fragment(self, item: ShortNameFragment) -> "CryptoKeySlotBuilder":
        """Add a single item to short_name_fragments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments.append(item)
        return self

    def clear_short_name_fragments(self) -> "CryptoKeySlotBuilder":
        """Clear all items from short_name_fragments list.

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = []
        return self

    def add_annotation(self, item: Annotation) -> "CryptoKeySlotBuilder":
        """Add a single item to annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.annotations.append(item)
        return self

    def clear_annotations(self) -> "CryptoKeySlotBuilder":
        """Clear all items from annotations list.

        Returns:
            self for method chaining
        """
        self._obj.annotations = []
        return self

    def add_key_slot_content_allowed_usage(self, item: CryptoKeySlotContentAllowedUsage) -> "CryptoKeySlotBuilder":
        """Add a single item to key_slot_content_allowed_usages list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.key_slot_content_allowed_usages.append(item)
        return self

    def clear_key_slot_content_allowed_usages(self) -> "CryptoKeySlotBuilder":
        """Clear all items from key_slot_content_allowed_usages list.

        Returns:
            self for method chaining
        """
        self._obj.key_slot_content_allowed_usages = []
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


    def build(self) -> CryptoKeySlot:
        """Build and return the CryptoKeySlot instance with validation."""
        self._validate_instance()
        pass
        return self._obj