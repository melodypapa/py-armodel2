"""BulkNvDataDescriptor AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent.nv_block_data_mapping import (
    NvBlockDataMapping,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class BulkNvDataDescriptor(Identifiable):
    """AUTOSAR BulkNvDataDescriptor."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "bulk_nv_block": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=VariableDataPrototype,
        ),  # bulkNvBlock
        "nv_block_datas": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=NvBlockDataMapping,
        ),  # nvBlockDatas
    }

    def __init__(self) -> None:
        """Initialize BulkNvDataDescriptor."""
        super().__init__()
        self.bulk_nv_block: Optional[VariableDataPrototype] = None
        self.nv_block_datas: list[NvBlockDataMapping] = []


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
