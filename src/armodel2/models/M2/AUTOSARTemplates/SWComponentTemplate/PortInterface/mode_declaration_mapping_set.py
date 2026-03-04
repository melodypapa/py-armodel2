"""ModeDeclarationMappingSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 132)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ModeDeclarationMappingSet(ARElement):
    """AUTOSAR ModeDeclarationMappingSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "MODE-DECLARATION-MAPPING-SET"


    modes: list[ModeDeclaration]
    _DESERIALIZE_DISPATCH = {
        "MODES": lambda obj, elem: obj.modes.append(SerializationHelper.deserialize_by_tag(elem, "ModeDeclaration")),
    }


    def __init__(self) -> None:
        """Initialize ModeDeclarationMappingSet."""
        super().__init__()
        self.modes: list[ModeDeclaration] = []

    def serialize(self) -> ET.Element:
        """Serialize ModeDeclarationMappingSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ModeDeclarationMappingSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize modes (list to container "MODES")
        if self.modes:
            wrapper = ET.Element("MODES")
            for item in self.modes:
                serialized = SerializationHelper.serialize_item(item, "ModeDeclaration")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeDeclarationMappingSet":
        """Deserialize XML element to ModeDeclarationMappingSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ModeDeclarationMappingSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ModeDeclarationMappingSet, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "MODES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.modes.append(SerializationHelper.deserialize_by_tag(item_elem, "ModeDeclaration"))

        return obj



class ModeDeclarationMappingSetBuilder(ARElementBuilder):
    """Builder for ModeDeclarationMappingSet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ModeDeclarationMappingSet = ModeDeclarationMappingSet()


    def with_modes(self, items: list[ModeDeclaration]) -> "ModeDeclarationMappingSetBuilder":
        """Set modes list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.modes = list(items) if items else []
        return self


    def add_mode(self, item: ModeDeclaration) -> "ModeDeclarationMappingSetBuilder":
        """Add a single item to modes list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.modes.append(item)
        return self

    def clear_modes(self) -> "ModeDeclarationMappingSetBuilder":
        """Clear all items from modes list.

        Returns:
            self for method chaining
        """
        self._obj.modes = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "mode",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ModeDeclarationMappingSet:
        """Build and return the ModeDeclarationMappingSet instance with validation."""
        self._validate_instance()
        return self._obj