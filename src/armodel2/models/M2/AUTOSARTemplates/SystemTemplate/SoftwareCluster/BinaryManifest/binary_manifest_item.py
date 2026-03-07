"""BinaryManifestItem AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 919)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster_BinaryManifest.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest.binary_manifest_addressable_object import (
    BinaryManifestAddressableObject,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest.binary_manifest_addressable_object import BinaryManifestAddressableObjectBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class BinaryManifestItem(BinaryManifestAddressableObject):
    """AUTOSAR BinaryManifestItem."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "BINARY-MANIFEST-ITEM"


    auxiliary_fields: list[BinaryManifestItem]
    default_value: Optional[BinaryManifestItem]
    is_unused: Optional[Boolean]
    value: Optional[BinaryManifestItem]
    _DESERIALIZE_DISPATCH = {
        "AUXILIARY-FIELDS": lambda obj, elem: obj.auxiliary_fields.append(SerializationHelper.deserialize_by_tag(elem, "BinaryManifestItem")),
        "DEFAULT-VALUE": lambda obj, elem: setattr(obj, "default_value", SerializationHelper.deserialize_by_tag(elem, "BinaryManifestItem")),
        "IS-UNUSED": lambda obj, elem: setattr(obj, "is_unused", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "VALUE": lambda obj, elem: setattr(obj, "value", SerializationHelper.deserialize_by_tag(elem, "BinaryManifestItem")),
    }


    def __init__(self) -> None:
        """Initialize BinaryManifestItem."""
        super().__init__()
        self.auxiliary_fields: list[BinaryManifestItem] = []
        self.default_value: Optional[BinaryManifestItem] = None
        self.is_unused: Optional[Boolean] = None
        self.value: Optional[BinaryManifestItem] = None

    def serialize(self) -> ET.Element:
        """Serialize BinaryManifestItem to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BinaryManifestItem, self).serialize()

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

        # Serialize default_value
        if self.default_value is not None:
            serialized = SerializationHelper.serialize_item(self.default_value, "BinaryManifestItem")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEFAULT-VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize is_unused
        if self.is_unused is not None:
            serialized = SerializationHelper.serialize_item(self.is_unused, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IS-UNUSED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize value
        if self.value is not None:
            serialized = SerializationHelper.serialize_item(self.value, "BinaryManifestItem")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BinaryManifestItem":
        """Deserialize XML element to BinaryManifestItem object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BinaryManifestItem object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BinaryManifestItem, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "AUXILIARY-FIELDS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.auxiliary_fields.append(SerializationHelper.deserialize_by_tag(item_elem, "BinaryManifestItem"))
            elif tag == "DEFAULT-VALUE":
                setattr(obj, "default_value", SerializationHelper.deserialize_by_tag(child, "BinaryManifestItem"))
            elif tag == "IS-UNUSED":
                setattr(obj, "is_unused", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "VALUE":
                setattr(obj, "value", SerializationHelper.deserialize_by_tag(child, "BinaryManifestItem"))

        return obj



class BinaryManifestItemBuilder(BinaryManifestAddressableObjectBuilder):
    """Builder for BinaryManifestItem with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: BinaryManifestItem = BinaryManifestItem()


    def with_auxiliary_fields(self, items: list[BinaryManifestItem]) -> "BinaryManifestItemBuilder":
        """Set auxiliary_fields list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.auxiliary_fields = list(items) if items else []
        return self

    def with_default_value(self, value: Optional[BinaryManifestItem]) -> "BinaryManifestItemBuilder":
        """Set default_value attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'default_value' is required and cannot be None")
        self._obj.default_value = value
        return self

    def with_is_unused(self, value: Optional[Boolean]) -> "BinaryManifestItemBuilder":
        """Set is_unused attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'is_unused' is required and cannot be None")
        self._obj.is_unused = value
        return self

    def with_value(self, value: Optional[BinaryManifestItem]) -> "BinaryManifestItemBuilder":
        """Set value attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'value' is required and cannot be None")
        self._obj.value = value
        return self


    def add_auxiliary_field(self, item: BinaryManifestItem) -> "BinaryManifestItemBuilder":
        """Add a single item to auxiliary_fields list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.auxiliary_fields.append(item)
        return self

    def clear_auxiliary_fields(self) -> "BinaryManifestItemBuilder":
        """Clear all items from auxiliary_fields list.

        Returns:
            self for method chaining
        """
        self._obj.auxiliary_fields = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "auxiliaryField",
        "defaultValue",
        "isUnused",
        "value",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> BinaryManifestItem:
        """Build and return the BinaryManifestItem instance with validation."""
        self._validate_instance()
        return self._obj