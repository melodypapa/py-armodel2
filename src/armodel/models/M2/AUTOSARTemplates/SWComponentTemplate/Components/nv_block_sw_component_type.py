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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "NvBlockSwComponentType":
        """Deserialize XML element to NvBlockSwComponentType object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized NvBlockSwComponentType object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse bulk_nv_datas (list)
        obj.bulk_nv_datas = []
        for child in ARObject._find_all_child_elements(element, "BULK-NV-DATAS"):
            bulk_nv_datas_value = ARObject._deserialize_by_tag(child, "BulkNvDataDescriptor")
            obj.bulk_nv_datas.append(bulk_nv_datas_value)

        # Parse nv_blocks (list)
        obj.nv_blocks = []
        for child in ARObject._find_all_child_elements(element, "NV-BLOCKS"):
            nv_blocks_value = ARObject._deserialize_by_tag(child, "NvBlockDescriptor")
            obj.nv_blocks.append(nv_blocks_value)

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
