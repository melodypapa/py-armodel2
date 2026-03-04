"""MetaDataItemSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 99)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2037)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.meta_data_item import (
    MetaDataItem,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class MetaDataItemSet(ARObject):
    """AUTOSAR MetaDataItemSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "META-DATA-ITEM-SET"


    data_element_refs: list[ARRef]
    meta_data_items: list[MetaDataItem]
    _DESERIALIZE_DISPATCH = {
        "DATA-ELEMENT-REFS": lambda obj, elem: [obj.data_element_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "META-DATA-ITEMS": lambda obj, elem: obj.meta_data_items.append(SerializationHelper.deserialize_by_tag(elem, "MetaDataItem")),
    }


    def __init__(self) -> None:
        """Initialize MetaDataItemSet."""
        super().__init__()
        self.data_element_refs: list[ARRef] = []
        self.meta_data_items: list[MetaDataItem] = []

    def serialize(self) -> ET.Element:
        """Serialize MetaDataItemSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MetaDataItemSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_element_refs (list to container "DATA-ELEMENT-REFS")
        if self.data_element_refs:
            wrapper = ET.Element("DATA-ELEMENT-REFS")
            for item in self.data_element_refs:
                serialized = SerializationHelper.serialize_item(item, "VariableDataPrototype")
                if serialized is not None:
                    child_elem = ET.Element("DATA-ELEMENT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize meta_data_items (list to container "META-DATA-ITEMS")
        if self.meta_data_items:
            wrapper = ET.Element("META-DATA-ITEMS")
            for item in self.meta_data_items:
                serialized = SerializationHelper.serialize_item(item, "MetaDataItem")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MetaDataItemSet":
        """Deserialize XML element to MetaDataItemSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MetaDataItemSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MetaDataItemSet, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DATA-ELEMENT-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.data_element_refs.append(ARRef.deserialize(item_elem))
            elif tag == "META-DATA-ITEMS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.meta_data_items.append(SerializationHelper.deserialize_by_tag(item_elem, "MetaDataItem"))

        return obj



class MetaDataItemSetBuilder(BuilderBase):
    """Builder for MetaDataItemSet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: MetaDataItemSet = MetaDataItemSet()


    def with_data_elements(self, items: list[VariableDataPrototype]) -> "MetaDataItemSetBuilder":
        """Set data_elements list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.data_elements = list(items) if items else []
        return self

    def with_meta_data_items(self, items: list[MetaDataItem]) -> "MetaDataItemSetBuilder":
        """Set meta_data_items list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.meta_data_items = list(items) if items else []
        return self


    def add_data_element(self, item: VariableDataPrototype) -> "MetaDataItemSetBuilder":
        """Add a single item to data_elements list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.data_elements.append(item)
        return self

    def clear_data_elements(self) -> "MetaDataItemSetBuilder":
        """Clear all items from data_elements list.

        Returns:
            self for method chaining
        """
        self._obj.data_elements = []
        return self

    def add_meta_data_item(self, item: MetaDataItem) -> "MetaDataItemSetBuilder":
        """Add a single item to meta_data_items list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.meta_data_items.append(item)
        return self

    def clear_meta_data_items(self) -> "MetaDataItemSetBuilder":
        """Clear all items from meta_data_items list.

        Returns:
            self for method chaining
        """
        self._obj.meta_data_items = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "dataElement",
        "metaDataItem",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> MetaDataItemSet:
        """Build and return the MetaDataItemSet instance with validation."""
        self._validate_instance()
        return self._obj