"""NvBlockDataMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 688)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_NvBlockComponent.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.autosar_variable_ref import (
    AutosarVariableRef,
)


class NvBlockDataMapping(ARObject):
    """AUTOSAR NvBlockDataMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bitfield_text_table: Optional[PositiveInteger]
    nv_ram_block_ref: Optional[ARRef]
    read_nv_data_ref: Optional[ARRef]
    written_nv_data_ref: Optional[ARRef]
    written_read_nv_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize NvBlockDataMapping."""
        super().__init__()
        self.bitfield_text_table: Optional[PositiveInteger] = None
        self.nv_ram_block_ref: Optional[ARRef] = None
        self.read_nv_data_ref: Optional[ARRef] = None
        self.written_nv_data_ref: Optional[ARRef] = None
        self.written_read_nv_ref: Optional[ARRef] = None


class NvBlockDataMappingBuilder:
    """Builder for NvBlockDataMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NvBlockDataMapping = NvBlockDataMapping()

    def build(self) -> NvBlockDataMapping:
        """Build and return NvBlockDataMapping object.

        Returns:
            NvBlockDataMapping instance
        """
        # TODO: Add validation
        return self._obj
