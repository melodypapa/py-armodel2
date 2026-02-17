"""NvBlockNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 231)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 679)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    NvBlockNeedsWritingPriorityEnum,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import (
    RamBlockStatusControlEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    TimeValue,
)


class NvBlockNeeds(ServiceNeeds):
    """AUTOSAR NvBlockNeeds."""

    def __init__(self) -> None:
        """Initialize NvBlockNeeds."""
        super().__init__()
        self.calc_ram_block: Optional[Boolean] = None
        self.check_static_block_id: Optional[Boolean] = None
        self.cyclic_writing: Optional[TimeValue] = None
        self.n_data_sets: Optional[PositiveInteger] = None
        self.n_rom_blocks: Optional[PositiveInteger] = None
        self.ram_block_status_control: Optional[RamBlockStatusControlEnum] = None
        self.readonly: Optional[Boolean] = None
        self.reliability_reliability_enum: Optional[NvBlockNeeds] = None
        self.resistant_to: Optional[Boolean] = None
        self.restore_at_start: Optional[Boolean] = None
        self.select_block_for: Optional[Boolean] = None
        self.store_at: Optional[Boolean] = None
        self.store_cyclic: Optional[Boolean] = None
        self.store: Optional[Boolean] = None
        self.store_immediate: Optional[Boolean] = None
        self.store_on_change: Optional[Boolean] = None
        self.use_auto: Optional[Boolean] = None
        self.use_crc_comp: Optional[Boolean] = None
        self.write_only_once: Optional[Boolean] = None
        self.write_verification: Optional[Boolean] = None
        self.writing: Optional[PositiveInteger] = None
        self.writing_priority: Optional[NvBlockNeedsWritingPriorityEnum] = None


class NvBlockNeedsBuilder:
    """Builder for NvBlockNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NvBlockNeeds = NvBlockNeeds()

    def build(self) -> NvBlockNeeds:
        """Build and return NvBlockNeeds object.

        Returns:
            NvBlockNeeds instance
        """
        # TODO: Add validation
        return self._obj
