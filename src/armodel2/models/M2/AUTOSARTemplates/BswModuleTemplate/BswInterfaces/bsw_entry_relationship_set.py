"""BswEntryRelationshipSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 51)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 51)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswInterfaces.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_entry_relationship import (
    BswEntryRelationship,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class BswEntryRelationshipSet(ARElement):
    """AUTOSAR BswEntryRelationshipSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "BSW-ENTRY-RELATIONSHIP-SET"


    bsw_entry_relationships: list[BswEntryRelationship]
    _DESERIALIZE_DISPATCH = {
        "BSW-ENTRY-RELATIONSHIPS": lambda obj, elem: obj.bsw_entry_relationships.append(SerializationHelper.deserialize_by_tag(elem, "BswEntryRelationship")),
    }


    def __init__(self) -> None:
        """Initialize BswEntryRelationshipSet."""
        super().__init__()
        self.bsw_entry_relationships: list[BswEntryRelationship] = []

    def serialize(self) -> ET.Element:
        """Serialize BswEntryRelationshipSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BswEntryRelationshipSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize bsw_entry_relationships (list to container "BSW-ENTRY-RELATIONSHIPS")
        if self.bsw_entry_relationships:
            wrapper = ET.Element("BSW-ENTRY-RELATIONSHIPS")
            for item in self.bsw_entry_relationships:
                serialized = SerializationHelper.serialize_item(item, "BswEntryRelationship")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswEntryRelationshipSet":
        """Deserialize XML element to BswEntryRelationshipSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswEntryRelationshipSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswEntryRelationshipSet, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "BSW-ENTRY-RELATIONSHIPS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.bsw_entry_relationships.append(SerializationHelper.deserialize_by_tag(item_elem, "BswEntryRelationship"))

        return obj



class BswEntryRelationshipSetBuilder(ARElementBuilder):
    """Builder for BswEntryRelationshipSet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: BswEntryRelationshipSet = BswEntryRelationshipSet()


    def with_bsw_entry_relationships(self, items: list[BswEntryRelationship]) -> "BswEntryRelationshipSetBuilder":
        """Set bsw_entry_relationships list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.bsw_entry_relationships = list(items) if items else []
        return self


    def add_bsw_entry_relationship(self, item: BswEntryRelationship) -> "BswEntryRelationshipSetBuilder":
        """Add a single item to bsw_entry_relationships list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.bsw_entry_relationships.append(item)
        return self

    def clear_bsw_entry_relationships(self) -> "BswEntryRelationshipSetBuilder":
        """Clear all items from bsw_entry_relationships list.

        Returns:
            self for method chaining
        """
        self._obj.bsw_entry_relationships = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "bswEntryRelationship",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> BswEntryRelationshipSet:
        """Build and return the BswEntryRelationshipSet instance with validation."""
        self._validate_instance()
        return self._obj