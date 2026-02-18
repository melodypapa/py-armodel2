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

    bulk_nv_block: Optional[VariableDataPrototype]
    nv_block_datas: list[NvBlockDataMapping]
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
