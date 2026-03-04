"""BlueprintMappingSet AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 48)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 34)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_BlueprintMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure.atp_blueprint_mapping import (
    AtpBlueprintMapping,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class BlueprintMappingSet(ARElement):
    """AUTOSAR BlueprintMappingSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "BLUEPRINT-MAPPING-SET"


    blueprint_map_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "BLUEPRINT-MAP-REFS": ("_POLYMORPHIC_LIST", "blueprint_map_refs", ["BlueprintMapping"]),
    }


    def __init__(self) -> None:
        """Initialize BlueprintMappingSet."""
        super().__init__()
        self.blueprint_map_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize BlueprintMappingSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BlueprintMappingSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize blueprint_map_refs (list to container "BLUEPRINT-MAP-REFS")
        if self.blueprint_map_refs:
            wrapper = ET.Element("BLUEPRINT-MAP-REFS")
            for item in self.blueprint_map_refs:
                serialized = SerializationHelper.serialize_item(item, "AtpBlueprintMapping")
                if serialized is not None:
                    child_elem = ET.Element("BLUEPRINT-MAP-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BlueprintMappingSet":
        """Deserialize XML element to BlueprintMappingSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BlueprintMappingSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BlueprintMappingSet, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "BLUEPRINT-MAP-REFS":
                for item_elem in child:
                    obj.blueprint_map_refs.append(ARRef.deserialize(item_elem))

        return obj



class BlueprintMappingSetBuilder(ARElementBuilder):
    """Builder for BlueprintMappingSet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: BlueprintMappingSet = BlueprintMappingSet()


    def with_blueprint_maps(self, items: list[AtpBlueprintMapping]) -> "BlueprintMappingSetBuilder":
        """Set blueprint_maps list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.blueprint_maps = list(items) if items else []
        return self


    def add_blueprint_map(self, item: AtpBlueprintMapping) -> "BlueprintMappingSetBuilder":
        """Add a single item to blueprint_maps list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.blueprint_maps.append(item)
        return self

    def clear_blueprint_maps(self) -> "BlueprintMappingSetBuilder":
        """Clear all items from blueprint_maps list.

        Returns:
            self for method chaining
        """
        self._obj.blueprint_maps = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "blueprintMap",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> BlueprintMappingSet:
        """Build and return the BlueprintMappingSet instance with validation."""
        self._validate_instance()
        return self._obj