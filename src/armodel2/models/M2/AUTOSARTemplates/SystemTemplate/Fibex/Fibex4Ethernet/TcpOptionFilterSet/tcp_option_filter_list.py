"""TcpOptionFilterList AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 457)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_TcpOptionFilterSet.classes.json"""

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


class TcpOptionFilterList(Identifiable):
    """AUTOSAR TcpOptionFilterList."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "TCP-OPTION-FILTER-LIST"


    allowed_tcp_options: list[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "ALLOWED-TCP-OPTIONS": lambda obj, elem: obj.allowed_tcp_options.append(SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize TcpOptionFilterList."""
        super().__init__()
        self.allowed_tcp_options: list[PositiveInteger] = []

    def serialize(self) -> ET.Element:
        """Serialize TcpOptionFilterList to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TcpOptionFilterList, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize allowed_tcp_options (list to container "ALLOWED-TCP-OPTIONS")
        if self.allowed_tcp_options:
            wrapper = ET.Element("ALLOWED-TCP-OPTIONS")
            for item in self.allowed_tcp_options:
                serialized = SerializationHelper.serialize_item(item, "PositiveInteger")
                if serialized is not None:
                    child_elem = ET.Element("ALLOWED-TCP-OPTION")
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
    def deserialize(cls, element: ET.Element) -> "TcpOptionFilterList":
        """Deserialize XML element to TcpOptionFilterList object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TcpOptionFilterList object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TcpOptionFilterList, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ALLOWED-TCP-OPTIONS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.allowed_tcp_options.append(SerializationHelper.deserialize_by_tag(item_elem, "PositiveInteger"))

        return obj



class TcpOptionFilterListBuilder(IdentifiableBuilder):
    """Builder for TcpOptionFilterList with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TcpOptionFilterList = TcpOptionFilterList()


    def with_allowed_tcp_options(self, items: list[PositiveInteger]) -> "TcpOptionFilterListBuilder":
        """Set allowed_tcp_options list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.allowed_tcp_options = list(items) if items else []
        return self


    def add_allowed_tcp_option(self, item: PositiveInteger) -> "TcpOptionFilterListBuilder":
        """Add a single item to allowed_tcp_options list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.allowed_tcp_options.append(item)
        return self

    def clear_allowed_tcp_options(self) -> "TcpOptionFilterListBuilder":
        """Clear all items from allowed_tcp_options list.

        Returns:
            self for method chaining
        """
        self._obj.allowed_tcp_options = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "allowedTcpOption",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> TcpOptionFilterList:
        """Build and return the TcpOptionFilterList instance with validation."""
        self._validate_instance()
        return self._obj