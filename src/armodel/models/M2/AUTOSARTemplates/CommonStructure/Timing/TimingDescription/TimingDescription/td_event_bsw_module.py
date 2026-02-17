"""TDEventBswModule AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 75)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_bsw import (
    TDEventBsw,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_entry import (
    BswModuleEntry,
)


class TDEventBswModule(TDEventBsw):
    """AUTOSAR TDEventBswModule."""

    bsw_module_entry_entry: Optional[BswModuleEntry]
    td_event_bsw: Optional[TDEventBswModule]
    def __init__(self) -> None:
        """Initialize TDEventBswModule."""
        super().__init__()
        self.bsw_module_entry_entry: Optional[BswModuleEntry] = None
        self.td_event_bsw: Optional[TDEventBswModule] = None


class TDEventBswModuleBuilder:
    """Builder for TDEventBswModule."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventBswModule = TDEventBswModule()

    def build(self) -> TDEventBswModule:
        """Build and return TDEventBswModule object.

        Returns:
            TDEventBswModule instance
        """
        # TODO: Add validation
        return self._obj
