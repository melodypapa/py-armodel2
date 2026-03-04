"""BinaryManifestResourceDefinition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 917)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster_BinaryManifest.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest.binary_manifest_item import (
    BinaryManifestItem,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class BinaryManifestResourceDefinition(Identifiable):
    """AUTOSAR BinaryManifestResourceDefinition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "BINARY-MANIFEST-RESOURCE-DEFINITION"


    item_definitions: list[BinaryManifestItem]
    _DESERIALIZE_DISPATCH = {
        "ITEM-DEFINITIONS": lambda obj, elem: obj.item_definitions.append(SerializationHelper.deserialize_by_tag(elem, "BinaryManifestItem")),
    }


    def __init__(self) -> None:
        """Initialize BinaryManifestResourceDefinition."""
        super().__init__()
        self.item_definitions: list[BinaryManifestItem] = []

    def serialize(self) -> ET.Element:
        """Serialize BinaryManifestResourceDefinition to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BinaryManifestResourceDefinition, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize item_definitions (list to container "ITEM-DEFINITIONS")
        if self.item_definitions:
            wrapper = ET.Element("ITEM-DEFINITIONS")
            for item in self.item_definitions:
                serialized = SerializationHelper.serialize_item(item, "BinaryManifestItem")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BinaryManifestResourceDefinition":
        """Deserialize XML element to BinaryManifestResourceDefinition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BinaryManifestResourceDefinition object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BinaryManifestResourceDefinition, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ITEM-DEFINITIONS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.item_definitions.append(SerializationHelper.deserialize_by_tag(item_elem, "BinaryManifestItem"))

        return obj



class BinaryManifestResourceDefinitionBuilder(IdentifiableBuilder):
    """Builder for BinaryManifestResourceDefinition with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: BinaryManifestResourceDefinition = BinaryManifestResourceDefinition()


    def with_item_definitions(self, items: list[BinaryManifestItem]) -> "BinaryManifestResourceDefinitionBuilder":
        """Set item_definitions list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.item_definitions = list(items) if items else []
        return self


    def add_item_definition(self, item: BinaryManifestItem) -> "BinaryManifestResourceDefinitionBuilder":
        """Add a single item to item_definitions list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.item_definitions.append(item)
        return self

    def clear_item_definitions(self) -> "BinaryManifestResourceDefinitionBuilder":
        """Clear all items from item_definitions list.

        Returns:
            self for method chaining
        """
        self._obj.item_definitions = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "itemDefinition",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> BinaryManifestResourceDefinition:
        """Build and return the BinaryManifestResourceDefinition instance with validation."""
        self._validate_instance()
        return self._obj