"""NvBlockSwComponentType AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.atomic_sw_component_type import (
    AtomicSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent.bulk_nv_data_descriptor import (
    BulkNvDataDescriptor,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent.nv_block_descriptor import (
    NvBlockDescriptor,
)


class NvBlockSwComponentType(AtomicSwComponentType):
    """AUTOSAR NvBlockSwComponentType."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("bulk_nv_datas", None, False, True, BulkNvDataDescriptor),  # bulkNvDatas
        ("nv_blocks", None, False, True, NvBlockDescriptor),  # nvBlocks
    ]

    def __init__(self) -> None:
        """Initialize NvBlockSwComponentType."""
        super().__init__()
        self.bulk_nv_datas: list[BulkNvDataDescriptor] = []
        self.nv_blocks: list[NvBlockDescriptor] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert NvBlockSwComponentType to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "NvBlockSwComponentType":
        """Create NvBlockSwComponentType from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            NvBlockSwComponentType instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to NvBlockSwComponentType since parent returns ARObject
        return cast("NvBlockSwComponentType", obj)


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
