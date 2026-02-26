"""CryptoKeySlot AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 57)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_AdaptivePlatform_PlatformModuleDeployment_CryptoDeployment.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    String,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


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



class CryptoKeySlotBuilder(IdentifiableBuilder):
    """Builder for CryptoKeySlot with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CryptoKeySlot = CryptoKeySlot()


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



    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

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