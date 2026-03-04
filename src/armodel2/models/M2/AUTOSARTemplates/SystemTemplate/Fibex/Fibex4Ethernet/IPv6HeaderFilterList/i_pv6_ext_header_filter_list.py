"""IPv6ExtHeaderFilterList AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 455)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_IPv6HeaderFilterList.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class IPv6ExtHeaderFilterList(Identifiable):
    """AUTOSAR IPv6ExtHeaderFilterList."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "I-PV6-EXT-HEADER-FILTER-LIST"


    allowed_i_pv6_exts: list[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "ALLOWED-I-PV6-EXTS": lambda obj, elem: obj.allowed_i_pv6_exts.append(SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize IPv6ExtHeaderFilterList."""
        super().__init__()
        self.allowed_i_pv6_exts: list[PositiveInteger] = []

    def serialize(self) -> ET.Element:
        """Serialize IPv6ExtHeaderFilterList to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IPv6ExtHeaderFilterList, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize allowed_i_pv6_exts (list to container "ALLOWED-I-PV6-EXTS")
        if self.allowed_i_pv6_exts:
            wrapper = ET.Element("ALLOWED-I-PV6-EXTS")
            for item in self.allowed_i_pv6_exts:
                serialized = SerializationHelper.serialize_item(item, "PositiveInteger")
                if serialized is not None:
                    child_elem = ET.Element("ALLOWED-I-PV6-EXT")
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
    def deserialize(cls, element: ET.Element) -> "IPv6ExtHeaderFilterList":
        """Deserialize XML element to IPv6ExtHeaderFilterList object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IPv6ExtHeaderFilterList object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IPv6ExtHeaderFilterList, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ALLOWED-I-PV6-EXTS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.allowed_i_pv6_exts.append(SerializationHelper.deserialize_by_tag(item_elem, "PositiveInteger"))

        return obj



class IPv6ExtHeaderFilterListBuilder(IdentifiableBuilder):
    """Builder for IPv6ExtHeaderFilterList with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: IPv6ExtHeaderFilterList = IPv6ExtHeaderFilterList()


    def with_allowed_i_pv6_exts(self, items: list[PositiveInteger]) -> "IPv6ExtHeaderFilterListBuilder":
        """Set allowed_i_pv6_exts list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.allowed_i_pv6_exts = list(items) if items else []
        return self


    def add_allowed_i_pv6_ext(self, item: PositiveInteger) -> "IPv6ExtHeaderFilterListBuilder":
        """Add a single item to allowed_i_pv6_exts list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.allowed_i_pv6_exts.append(item)
        return self

    def clear_allowed_i_pv6_exts(self) -> "IPv6ExtHeaderFilterListBuilder":
        """Clear all items from allowed_i_pv6_exts list.

        Returns:
            self for method chaining
        """
        self._obj.allowed_i_pv6_exts = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "allowedIPv6Ext",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> IPv6ExtHeaderFilterList:
        """Build and return the IPv6ExtHeaderFilterList instance with validation."""
        self._validate_instance()
        return self._obj