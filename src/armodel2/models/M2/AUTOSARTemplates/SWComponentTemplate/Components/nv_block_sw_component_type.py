"""NvBlockSwComponentType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 663)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2040)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.atomic_sw_component_type import (
    AtomicSwComponentType,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.atomic_sw_component_type import AtomicSwComponentTypeBuilder
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent.bulk_nv_data_descriptor import (
    BulkNvDataDescriptor,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent.nv_block_descriptor import (
    NvBlockDescriptor,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class NvBlockSwComponentType(AtomicSwComponentType):
    """AUTOSAR NvBlockSwComponentType."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "NV-BLOCK-SW-COMPONENT-TYPE"


    bulk_nv_data_descriptors: list[BulkNvDataDescriptor]
    nv_block_descriptors: list[NvBlockDescriptor]
    _DESERIALIZE_DISPATCH = {
        "BULK-NV-DATA-DESCRIPTORS": lambda obj, elem: obj.bulk_nv_data_descriptors.append(SerializationHelper.deserialize_by_tag(elem, "BulkNvDataDescriptor")),
        "NV-BLOCK-DESCRIPTORS": lambda obj, elem: obj.nv_block_descriptors.append(SerializationHelper.deserialize_by_tag(elem, "NvBlockDescriptor")),
    }


    def __init__(self) -> None:
        """Initialize NvBlockSwComponentType."""
        super().__init__()
        self.bulk_nv_data_descriptors: list[BulkNvDataDescriptor] = []
        self.nv_block_descriptors: list[NvBlockDescriptor] = []

    def serialize(self) -> ET.Element:
        """Serialize NvBlockSwComponentType to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(NvBlockSwComponentType, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize bulk_nv_data_descriptors (list to container "BULK-NV-DATA-DESCRIPTORS")
        if self.bulk_nv_data_descriptors:
            wrapper = ET.Element("BULK-NV-DATA-DESCRIPTORS")
            for item in self.bulk_nv_data_descriptors:
                serialized = SerializationHelper.serialize_item(item, "BulkNvDataDescriptor")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize nv_block_descriptors (list to container "NV-BLOCK-DESCRIPTORS")
        if self.nv_block_descriptors:
            wrapper = ET.Element("NV-BLOCK-DESCRIPTORS")
            for item in self.nv_block_descriptors:
                serialized = SerializationHelper.serialize_item(item, "NvBlockDescriptor")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "NvBlockSwComponentType":
        """Deserialize XML element to NvBlockSwComponentType object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized NvBlockSwComponentType object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(NvBlockSwComponentType, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "BULK-NV-DATA-DESCRIPTORS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.bulk_nv_data_descriptors.append(SerializationHelper.deserialize_by_tag(item_elem, "BulkNvDataDescriptor"))
            elif tag == "NV-BLOCK-DESCRIPTORS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.nv_block_descriptors.append(SerializationHelper.deserialize_by_tag(item_elem, "NvBlockDescriptor"))

        return obj



class NvBlockSwComponentTypeBuilder(AtomicSwComponentTypeBuilder):
    """Builder for NvBlockSwComponentType with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: NvBlockSwComponentType = NvBlockSwComponentType()


    def with_bulk_nv_data_descriptors(self, items: list[BulkNvDataDescriptor]) -> "NvBlockSwComponentTypeBuilder":
        """Set bulk_nv_data_descriptors list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.bulk_nv_data_descriptors = list(items) if items else []
        return self

    def with_nv_block_descriptors(self, items: list[NvBlockDescriptor]) -> "NvBlockSwComponentTypeBuilder":
        """Set nv_block_descriptors list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.nv_block_descriptors = list(items) if items else []
        return self


    def add_bulk_nv_data_descriptor(self, item: BulkNvDataDescriptor) -> "NvBlockSwComponentTypeBuilder":
        """Add a single item to bulk_nv_data_descriptors list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.bulk_nv_data_descriptors.append(item)
        return self

    def clear_bulk_nv_data_descriptors(self) -> "NvBlockSwComponentTypeBuilder":
        """Clear all items from bulk_nv_data_descriptors list.

        Returns:
            self for method chaining
        """
        self._obj.bulk_nv_data_descriptors = []
        return self

    def add_nv_block_descriptor(self, item: NvBlockDescriptor) -> "NvBlockSwComponentTypeBuilder":
        """Add a single item to nv_block_descriptors list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.nv_block_descriptors.append(item)
        return self

    def clear_nv_block_descriptors(self) -> "NvBlockSwComponentTypeBuilder":
        """Clear all items from nv_block_descriptors list.

        Returns:
            self for method chaining
        """
        self._obj.nv_block_descriptors = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "bulkNvDataDescriptor",
        "nvBlockDescriptor",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> NvBlockSwComponentType:
        """Build and return the NvBlockSwComponentType instance with validation."""
        self._validate_instance()
        return self._obj