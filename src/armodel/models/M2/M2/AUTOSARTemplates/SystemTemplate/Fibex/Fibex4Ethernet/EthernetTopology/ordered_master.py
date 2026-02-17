"""OrderedMaster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 470)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.time_sync_server_configuration import (
    TimeSyncServerConfiguration,
)


class OrderedMaster(ARObject):
    """AUTOSAR OrderedMaster."""

    def __init__(self) -> None:
        """Initialize OrderedMaster."""
        super().__init__()
        self.index: Optional[PositiveInteger] = None
        self.time_sync_server_configuration: Optional[TimeSyncServerConfiguration] = None


class OrderedMasterBuilder:
    """Builder for OrderedMaster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: OrderedMaster = OrderedMaster()

    def build(self) -> OrderedMaster:
        """Build and return OrderedMaster object.

        Returns:
            OrderedMaster instance
        """
        # TODO: Add validation
        return self._obj
