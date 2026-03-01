"""BinaryManifestItemDefinition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 920)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster_BinaryManifest.classes.json"""

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
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest.binary_manifest_item import (
    BinaryManifestItem,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class BinaryManifestItemDefinition(Identifiable):
    """AUTOSAR BinaryManifestItemDefinition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "BINARY-MANIFEST-ITEM-DEFINITION"


    auxiliary_fields: list[BinaryManifestItem]
    is_optional: Optional[Boolean]
    size: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "AUXILIARY-FIELDS": lambda obj, elem: obj.auxiliary_fields.append(SerializationHelper.deserialize_by_tag(elem, "BinaryManifestItem")),
        "IS-OPTIONAL": lambda obj, elem: setattr(obj, "is_optional", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "SIZE": lambda obj, elem: setattr(obj, "size", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize BinaryManifestItemDefinition."""
        super().__init__()
        self.auxiliary_fields: list[BinaryManifestItem] = []
        self.is_optional: Optional[Boolean] = None
        self.size: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize BinaryManifestItemDefinition to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BinaryManifestItemDefinition, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize auxiliary_fields (list to container "AUXILIARY-FIELDS")
        if self.auxiliary_fields:
            wrapper = ET.Element("AUXILIARY-FIELDS")
            for item in self.auxiliary_fields:
                serialized = SerializationHelper.serialize_item(item, "BinaryManifestItem")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize is_optional
        if self.is_optional is not None:
            serialized = SerializationHelper.serialize_item(self.is_optional, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IS-OPTIONAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize size
        if self.size is not None:
            serialized = SerializationHelper.serialize_item(self.size, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SIZE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BinaryManifestItemDefinition":
        """Deserialize XML element to BinaryManifestItemDefinition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BinaryManifestItemDefinition object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BinaryManifestItemDefinition, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "AUXILIARY-FIELDS":
                obj.auxiliary_fields.append(SerializationHelper.deserialize_by_tag(child, "BinaryManifestItem"))
            elif tag == "IS-OPTIONAL":
                setattr(obj, "is_optional", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "SIZE":
                setattr(obj, "size", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class BinaryManifestItemDefinitionBuilder(IdentifiableBuilder):
    """Builder for BinaryManifestItemDefinition with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: BinaryManifestItemDefinition = BinaryManifestItemDefinition()


    def with_auxiliary_fields(self, items: list[BinaryManifestItem]) -> "BinaryManifestItemDefinitionBuilder":
        """Set auxiliary_fields list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.auxiliary_fields = list(items) if items else []
        return self

    def with_is_optional(self, value: Optional[Boolean]) -> "BinaryManifestItemDefinitionBuilder":
        """Set is_optional attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.is_optional = value
        return self

    def with_size(self, value: Optional[PositiveInteger]) -> "BinaryManifestItemDefinitionBuilder":
        """Set size attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.size = value
        return self


    def add_auxiliary_field(self, item: BinaryManifestItem) -> "BinaryManifestItemDefinitionBuilder":
        """Add a single item to auxiliary_fields list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.auxiliary_fields.append(item)
        return self

    def clear_auxiliary_fields(self) -> "BinaryManifestItemDefinitionBuilder":
        """Clear all items from auxiliary_fields list.

        Returns:
            self for method chaining
        """
        self._obj.auxiliary_fields = []
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


    def build(self) -> BinaryManifestItemDefinition:
        """Build and return the BinaryManifestItemDefinition instance with validation."""
        self._validate_instance()
        pass
        return self._obj