"""IPv6ExtHeaderFilterSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 455)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_IPv6HeaderFilterList.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.IPv6HeaderFilterList.i_pv6_ext_header_filter_list import (
    IPv6ExtHeaderFilterList,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class IPv6ExtHeaderFilterSet(ARElement):
    """AUTOSAR IPv6ExtHeaderFilterSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "I-PV6-EXT-HEADER-FILTER-SET"


    ext_header_filter_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "EXT-HEADER-FILTER-REFS": lambda obj, elem: [obj.ext_header_filter_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
    }


    def __init__(self) -> None:
        """Initialize IPv6ExtHeaderFilterSet."""
        super().__init__()
        self.ext_header_filter_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize IPv6ExtHeaderFilterSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IPv6ExtHeaderFilterSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ext_header_filter_refs (list to container "EXT-HEADER-FILTER-REFS")
        if self.ext_header_filter_refs:
            wrapper = ET.Element("EXT-HEADER-FILTER-REFS")
            for item in self.ext_header_filter_refs:
                serialized = SerializationHelper.serialize_item(item, "IPv6ExtHeaderFilterList")
                if serialized is not None:
                    child_elem = ET.Element("EXT-HEADER-FILTER-REF")
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
    def deserialize(cls, element: ET.Element) -> "IPv6ExtHeaderFilterSet":
        """Deserialize XML element to IPv6ExtHeaderFilterSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IPv6ExtHeaderFilterSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IPv6ExtHeaderFilterSet, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "EXT-HEADER-FILTER-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.ext_header_filter_refs.append(ARRef.deserialize(item_elem))

        return obj



class IPv6ExtHeaderFilterSetBuilder(ARElementBuilder):
    """Builder for IPv6ExtHeaderFilterSet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: IPv6ExtHeaderFilterSet = IPv6ExtHeaderFilterSet()


    def with_ext_header_filters(self, items: list[IPv6ExtHeaderFilterList]) -> "IPv6ExtHeaderFilterSetBuilder":
        """Set ext_header_filters list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.ext_header_filters = list(items) if items else []
        return self


    def add_ext_header_filter(self, item: IPv6ExtHeaderFilterList) -> "IPv6ExtHeaderFilterSetBuilder":
        """Add a single item to ext_header_filters list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.ext_header_filters.append(item)
        return self

    def clear_ext_header_filters(self) -> "IPv6ExtHeaderFilterSetBuilder":
        """Clear all items from ext_header_filters list.

        Returns:
            self for method chaining
        """
        self._obj.ext_header_filters = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "extHeaderFilter",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> IPv6ExtHeaderFilterSet:
        """Build and return the IPv6ExtHeaderFilterSet instance with validation."""
        self._validate_instance()
        return self._obj