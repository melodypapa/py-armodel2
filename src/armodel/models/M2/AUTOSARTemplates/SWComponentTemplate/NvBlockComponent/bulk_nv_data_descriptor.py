"""BulkNvDataDescriptor AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 692)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_NvBlockComponent.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent.nv_block_data_mapping import (
    NvBlockDataMapping,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class BulkNvDataDescriptor(Identifiable):
    """AUTOSAR BulkNvDataDescriptor."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bulk_nv_block_ref: Optional[ARRef]
    nv_block_data_refs: list[ARRef]
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
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BulkNvDataDescriptor, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize bulk_nv_block_ref
        if self.bulk_nv_block_ref is not None:
            serialized = ARObject._serialize_item(self.bulk_nv_block_ref, "VariableDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BULK-NV-BLOCK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nv_block_data_refs (list to container "NV-BLOCK-DATAS")
        if self.nv_block_data_refs:
            wrapper = ET.Element("NV-BLOCK-DATAS")
            for item in self.nv_block_data_refs:
                serialized = ARObject._serialize_item(item, "NvBlockDataMapping")
                if serialized is not None:
                    wrapper.append(serialized)
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

        # Parse bulk_nv_block_ref
        child = ARObject._find_child_element(element, "BULK-NV-BLOCK")
        if child is not None:
            bulk_nv_block_ref_value = ARObject._deserialize_by_tag(child, "VariableDataPrototype")
            obj.bulk_nv_block_ref = bulk_nv_block_ref_value

        # Parse nv_block_data_refs (list from container "NV-BLOCK-DATAS")
        obj.nv_block_data_refs = []
        container = ARObject._find_child_element(element, "NV-BLOCK-DATAS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.nv_block_data_refs.append(child_value)

        return obj



class BulkNvDataDescriptorBuilder:
    """Builder for BulkNvDataDescriptor."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BulkNvDataDescriptor = BulkNvDataDescriptor()

    def build(self) -> BulkNvDataDescriptor:
        """Build and return BulkNvDataDescriptor object.

        Returns:
            BulkNvDataDescriptor instance
        """
        # TODO: Add validation
        return self._obj
