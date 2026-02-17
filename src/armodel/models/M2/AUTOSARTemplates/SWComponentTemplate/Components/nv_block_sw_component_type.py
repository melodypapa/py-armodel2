"""NvBlockSwComponentType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 663)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2040)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "bulk_nv_datas": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=BulkNvDataDescriptor,
        ),  # bulkNvDatas
        "nv_blocks": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=NvBlockDescriptor,
        ),  # nvBlocks
    }

    def __init__(self) -> None:
        """Initialize NvBlockSwComponentType."""
        super().__init__()
        self.bulk_nv_datas: list[BulkNvDataDescriptor] = []
        self.nv_blocks: list[NvBlockDescriptor] = []


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
