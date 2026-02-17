"""SwitchStreamFilterEntry AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 141)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port import (
    CouplingPort,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.switch_flow_metering_entry import (
    SwitchFlowMeteringEntry,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.switch_stream_gate_entry import (
    SwitchStreamGateEntry,
)


class SwitchStreamFilterEntry(Identifiable):
    """AUTOSAR SwitchStreamFilterEntry."""

    def __init__(self) -> None:
        """Initialize SwitchStreamFilterEntry."""
        super().__init__()
        self.asynchronous: Optional[CouplingPort] = None
        self.filter_priority: Optional[PositiveInteger] = None
        self.flow_metering: Optional[SwitchFlowMeteringEntry] = None
        self.max_sdu_size: Optional[PositiveInteger] = None
        self.stream_gate: Optional[SwitchStreamGateEntry] = None
        self.stream: Optional[Boolean] = None


class SwitchStreamFilterEntryBuilder:
    """Builder for SwitchStreamFilterEntry."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwitchStreamFilterEntry = SwitchStreamFilterEntry()

    def build(self) -> SwitchStreamFilterEntry:
        """Build and return SwitchStreamFilterEntry object.

        Returns:
            SwitchStreamFilterEntry instance
        """
        # TODO: Add validation
        return self._obj
