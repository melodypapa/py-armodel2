"""IncludedModeDeclarationGroupSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 601)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_ModeDeclarationGroup.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class IncludedModeDeclarationGroupSet(ARObject):
    """AUTOSAR IncludedModeDeclarationGroupSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "INCLUDED-MODE-DECLARATION-GROUP-SET"


    mode_declaration_group_refs: list[ARRef]
    prefix: Optional[Identifier]
    _DESERIALIZE_DISPATCH = {
        "MODE-DECLARATION-GROUP-REFS": lambda obj, elem: [obj.mode_declaration_group_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "PREFIX": lambda obj, elem: setattr(obj, "prefix", SerializationHelper.deserialize_by_tag(elem, "Identifier")),
    }


    def __init__(self) -> None:
        """Initialize IncludedModeDeclarationGroupSet."""
        super().__init__()
        self.mode_declaration_group_refs: list[ARRef] = []
        self.prefix: Optional[Identifier] = None

    def serialize(self) -> ET.Element:
        """Serialize IncludedModeDeclarationGroupSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IncludedModeDeclarationGroupSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize mode_declaration_group_refs (list to container "MODE-DECLARATION-GROUP-REFS")
        if self.mode_declaration_group_refs:
            wrapper = ET.Element("MODE-DECLARATION-GROUP-REFS")
            for item in self.mode_declaration_group_refs:
                serialized = SerializationHelper.serialize_item(item, "ModeDeclarationGroup")
                if serialized is not None:
                    child_elem = ET.Element("MODE-DECLARATION-GROUP-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize prefix
        if self.prefix is not None:
            serialized = SerializationHelper.serialize_item(self.prefix, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PREFIX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IncludedModeDeclarationGroupSet":
        """Deserialize XML element to IncludedModeDeclarationGroupSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IncludedModeDeclarationGroupSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IncludedModeDeclarationGroupSet, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "MODE-DECLARATION-GROUP-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.mode_declaration_group_refs.append(ARRef.deserialize(item_elem))
            elif tag == "PREFIX":
                setattr(obj, "prefix", SerializationHelper.deserialize_by_tag(child, "Identifier"))

        return obj



class IncludedModeDeclarationGroupSetBuilder(BuilderBase):
    """Builder for IncludedModeDeclarationGroupSet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: IncludedModeDeclarationGroupSet = IncludedModeDeclarationGroupSet()


    def with_mode_declaration_groups(self, items: list[ModeDeclarationGroup]) -> "IncludedModeDeclarationGroupSetBuilder":
        """Set mode_declaration_groups list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.mode_declaration_groups = list(items) if items else []
        return self

    def with_prefix(self, value: Optional[Identifier]) -> "IncludedModeDeclarationGroupSetBuilder":
        """Set prefix attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'prefix' is required and cannot be None")
        self._obj.prefix = value
        return self


    def add_mode_declaration_group(self, item: ModeDeclarationGroup) -> "IncludedModeDeclarationGroupSetBuilder":
        """Add a single item to mode_declaration_groups list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.mode_declaration_groups.append(item)
        return self

    def clear_mode_declaration_groups(self) -> "IncludedModeDeclarationGroupSetBuilder":
        """Clear all items from mode_declaration_groups list.

        Returns:
            self for method chaining
        """
        self._obj.mode_declaration_groups = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "modeDeclarationGroup",
        "prefix",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> IncludedModeDeclarationGroupSet:
        """Build and return the IncludedModeDeclarationGroupSet instance with validation."""
        self._validate_instance()
        return self._obj