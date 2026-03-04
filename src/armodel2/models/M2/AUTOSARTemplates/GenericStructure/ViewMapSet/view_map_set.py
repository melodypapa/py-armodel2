"""ViewMapSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2079)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 401)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_ViewMapSet.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.ViewMapSet.view_map import (
    ViewMap,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ViewMapSet(ARElement):
    """AUTOSAR ViewMapSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "VIEW-MAP-SET"


    view_maps: list[ViewMap]
    _DESERIALIZE_DISPATCH = {
        "VIEW-MAPS": lambda obj, elem: obj.view_maps.append(SerializationHelper.deserialize_by_tag(elem, "ViewMap")),
    }


    def __init__(self) -> None:
        """Initialize ViewMapSet."""
        super().__init__()
        self.view_maps: list[ViewMap] = []

    def serialize(self) -> ET.Element:
        """Serialize ViewMapSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ViewMapSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize view_maps (list to container "VIEW-MAPS")
        if self.view_maps:
            wrapper = ET.Element("VIEW-MAPS")
            for item in self.view_maps:
                serialized = SerializationHelper.serialize_item(item, "ViewMap")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ViewMapSet":
        """Deserialize XML element to ViewMapSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ViewMapSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ViewMapSet, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "VIEW-MAPS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.view_maps.append(SerializationHelper.deserialize_by_tag(item_elem, "ViewMap"))

        return obj



class ViewMapSetBuilder(ARElementBuilder):
    """Builder for ViewMapSet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ViewMapSet = ViewMapSet()


    def with_view_maps(self, items: list[ViewMap]) -> "ViewMapSetBuilder":
        """Set view_maps list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.view_maps = list(items) if items else []
        return self


    def add_view_map(self, item: ViewMap) -> "ViewMapSetBuilder":
        """Add a single item to view_maps list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.view_maps.append(item)
        return self

    def clear_view_maps(self) -> "ViewMapSetBuilder":
        """Clear all items from view_maps list.

        Returns:
            self for method chaining
        """
        self._obj.view_maps = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "viewMap",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ViewMapSet:
        """Build and return the ViewMapSet instance with validation."""
        self._validate_instance()
        return self._obj