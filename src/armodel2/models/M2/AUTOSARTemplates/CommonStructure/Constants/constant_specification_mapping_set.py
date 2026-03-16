"""ConstantSpecificationMappingSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 445)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Constants.constant_specification_mapping import (
    ConstantSpecificationMapping,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ConstantSpecificationMappingSet(ARElement):
    """AUTOSAR ConstantSpecificationMappingSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CONSTANT-SPECIFICATION-MAPPING-SET"


    mappings: list[ConstantSpecificationMapping]
    _DESERIALIZE_DISPATCH = {
        "MAPPINGS": lambda obj, elem: obj.mappings.append(SerializationHelper.deserialize_by_tag(elem, "ConstantSpecificationMapping")),
    }


    def __init__(self) -> None:
        """Initialize ConstantSpecificationMappingSet."""
        super().__init__()
        self.mappings: list[ConstantSpecificationMapping] = []

    def serialize(self) -> ET.Element:
        """Serialize ConstantSpecificationMappingSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ConstantSpecificationMappingSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize mappings (list to container "MAPPINGS")
        if self.mappings:
            wrapper = ET.Element("MAPPINGS")
            for item in self.mappings:
                serialized = SerializationHelper.serialize_item(item, "ConstantSpecificationMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ConstantSpecificationMappingSet":
        """Deserialize XML element to ConstantSpecificationMappingSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ConstantSpecificationMappingSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ConstantSpecificationMappingSet, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "MAPPINGS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.mappings.append(SerializationHelper.deserialize_by_tag(item_elem, "ConstantSpecificationMapping"))

        return obj



class ConstantSpecificationMappingSetBuilder(ARElementBuilder):
    """Builder for ConstantSpecificationMappingSet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ConstantSpecificationMappingSet = ConstantSpecificationMappingSet()


    def with_mappings(self, items: list[ConstantSpecificationMapping]) -> "ConstantSpecificationMappingSetBuilder":
        """Set mappings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.mappings = list(items) if items else []
        return self


    def add_mapping(self, item: ConstantSpecificationMapping) -> "ConstantSpecificationMappingSetBuilder":
        """Add a single item to mappings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.mappings.append(item)
        return self

    def clear_mappings(self) -> "ConstantSpecificationMappingSetBuilder":
        """Clear all items from mappings list.

        Returns:
            self for method chaining
        """
        self._obj.mappings = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "mapping",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ConstantSpecificationMappingSet:
        """Build and return the ConstantSpecificationMappingSet instance with validation."""
        self._validate_instance()
        return self._obj