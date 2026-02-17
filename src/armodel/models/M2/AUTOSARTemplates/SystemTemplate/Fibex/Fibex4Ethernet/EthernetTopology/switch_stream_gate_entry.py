"""SwitchStreamGateEntry AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 142)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class SwitchStreamGateEntry(Identifiable):
    """AUTOSAR SwitchStreamGateEntry."""

    internal_priority: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize SwitchStreamGateEntry."""
        super().__init__()
        self.internal_priority: Optional[PositiveInteger] = None


class SwitchStreamGateEntryBuilder:
    """Builder for SwitchStreamGateEntry."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwitchStreamGateEntry = SwitchStreamGateEntry()

    def build(self) -> SwitchStreamGateEntry:
        """Build and return SwitchStreamGateEntry object.

        Returns:
            SwitchStreamGateEntry instance
        """
        # TODO: Add validation
        return self._obj
