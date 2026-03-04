"""BulkNvDataDescriptor AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 692)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_NvBlockComponent.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent.nv_block_data_mapping import (
    NvBlockDataMapping,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class BulkNvDataDescriptor(Identifiable):
    """AUTOSAR BulkNvDataDescriptor."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "BULK-NV-DATA-DESCRIPTOR"


    bulk_nv_block_ref: Optional[ARRef]
    nv_block_data_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "BULK-NV-BLOCK-REF": lambda obj, elem: setattr(obj, "bulk_nv_block_ref", ARRef.deserialize(elem)),
        "NV-BLOCK-DATA-REFS": lambda obj, elem: [obj.nv_block_data_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
    }


    def __init__(self) -> None:
        """Initialize BulkNvDataDescriptor."""
        super().__init__()
        self.bulk_nv_block_ref: Optional[ARRef] = None
        self.nv_block_data_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize BulkNvDataDescriptor to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BulkNvDataDescriptor, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize bulk_nv_block_ref
        if self.bulk_nv_block_ref is not None:
            serialized = SerializationHelper.serialize_item(self.bulk_nv_block_ref, "VariableDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BULK-NV-BLOCK-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nv_block_data_refs (list to container "NV-BLOCK-DATA-REFS")
        if self.nv_block_data_refs:
            wrapper = ET.Element("NV-BLOCK-DATA-REFS")
            for item in self.nv_block_data_refs:
                serialized = SerializationHelper.serialize_item(item, "NvBlockDataMapping")
                if serialized is not None:
                    child_elem = ET.Element("NV-BLOCK-DATA-REF")
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
    def deserialize(cls, element: ET.Element) -> "BulkNvDataDescriptor":
        """Deserialize XML element to BulkNvDataDescriptor object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BulkNvDataDescriptor object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BulkNvDataDescriptor, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "BULK-NV-BLOCK-REF":
                setattr(obj, "bulk_nv_block_ref", ARRef.deserialize(child))
            elif tag == "NV-BLOCK-DATA-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.nv_block_data_refs.append(ARRef.deserialize(item_elem))

        return obj



class BulkNvDataDescriptorBuilder(IdentifiableBuilder):
    """Builder for BulkNvDataDescriptor with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: BulkNvDataDescriptor = BulkNvDataDescriptor()


    def with_bulk_nv_block(self, value: Optional[VariableDataPrototype]) -> "BulkNvDataDescriptorBuilder":
        """Set bulk_nv_block attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.bulk_nv_block = value
        return self

    def with_nv_block_datas(self, items: list[NvBlockDataMapping]) -> "BulkNvDataDescriptorBuilder":
        """Set nv_block_datas list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.nv_block_datas = list(items) if items else []
        return self


    def add_nv_block_data(self, item: NvBlockDataMapping) -> "BulkNvDataDescriptorBuilder":
        """Add a single item to nv_block_datas list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.nv_block_datas.append(item)
        return self

    def clear_nv_block_datas(self) -> "BulkNvDataDescriptorBuilder":
        """Clear all items from nv_block_datas list.

        Returns:
            self for method chaining
        """
        self._obj.nv_block_datas = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "bulkNvBlock",
        "nvBlockData",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> BulkNvDataDescriptor:
        """Build and return the BulkNvDataDescriptor instance with validation."""
        self._validate_instance()
        return self._obj