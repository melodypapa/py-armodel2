"""NvBlockSwComponentType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 663)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2040)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.atomic_sw_component_type import (
    AtomicSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent.bulk_nv_data_descriptor import (
    BulkNvDataDescriptor,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent.nv_block_descriptor import (
    NvBlockDescriptor,
)


class NvBlockSwComponentType(AtomicSwComponentType):
    """AUTOSAR NvBlockSwComponentType."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bulk_nv_datas: list[BulkNvDataDescriptor]
    nv_blocks: list[NvBlockDescriptor]
    def __init__(self) -> None:
        """Initialize NvBlockSwComponentType."""
        super().__init__()
        self.bulk_nv_datas: list[BulkNvDataDescriptor] = []
        self.nv_blocks: list[NvBlockDescriptor] = []

    def serialize(self) -> ET.Element:
        """Serialize NvBlockSwComponentType to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

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

        # Serialize bulk_nv_datas (list to container "BULK-NV-DATAS")
        if self.bulk_nv_datas:
            wrapper = ET.Element("BULK-NV-DATAS")
            for item in self.bulk_nv_datas:
                serialized = ARObject._serialize_item(item, "BulkNvDataDescriptor")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize nv_blocks (list to container "NV-BLOCKS")
        if self.nv_blocks:
            wrapper = ET.Element("NV-BLOCKS")
            for item in self.nv_blocks:
                serialized = ARObject._serialize_item(item, "NvBlockDescriptor")
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

        # Parse bulk_nv_datas (list from container "BULK-NV-DATAS")
        obj.bulk_nv_datas = []
        container = ARObject._find_child_element(element, "BULK-NV-DATAS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.bulk_nv_datas.append(child_value)

        # Parse nv_blocks (list from container "NV-BLOCKS")
        obj.nv_blocks = []
        container = ARObject._find_child_element(element, "NV-BLOCKS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.nv_blocks.append(child_value)

        return obj



class NvBlockSwComponentTypeBuilder:
    """Builder for NvBlockSwComponentType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NvBlockSwComponentType = NvBlockSwComponentType()

    def build(self) -> NvBlockSwComponentType:
        """Build and return NvBlockSwComponentType object.

        Returns:
            NvBlockSwComponentType instance
        """
        # TODO: Add validation
        return self._obj
