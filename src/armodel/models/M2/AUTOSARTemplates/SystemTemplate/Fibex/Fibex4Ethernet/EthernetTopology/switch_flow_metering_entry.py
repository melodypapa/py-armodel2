"""SwitchFlowMeteringEntry AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 143)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    FlowMeteringColorModeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class SwitchFlowMeteringEntry(Identifiable):
    """AUTOSAR SwitchFlowMeteringEntry."""

    def __init__(self) -> None:
        """Initialize SwitchFlowMeteringEntry."""
        super().__init__()
        self.color_mode: Optional[FlowMeteringColorModeEnum] = None
        self.committed_burst: Optional[PositiveInteger] = None
        self.committed: Optional[PositiveInteger] = None
        self.coupling_flag: Optional[Boolean] = None
        self.excess_burst: Optional[PositiveInteger] = None
        self.excess: Optional[PositiveInteger] = None


class SwitchFlowMeteringEntryBuilder:
    """Builder for SwitchFlowMeteringEntry."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwitchFlowMeteringEntry = SwitchFlowMeteringEntry()

    def build(self) -> SwitchFlowMeteringEntry:
        """Build and return SwitchFlowMeteringEntry object.

        Returns:
            SwitchFlowMeteringEntry instance
        """
        # TODO: Add validation
        return self._obj
