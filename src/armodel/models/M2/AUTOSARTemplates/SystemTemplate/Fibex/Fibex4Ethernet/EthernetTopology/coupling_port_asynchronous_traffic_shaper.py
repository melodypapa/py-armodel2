"""CouplingPortAsynchronousTrafficShaper AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2012)

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
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.switch_asynchronous_traffic_shaper_group_entry import (
    SwitchAsynchronousTrafficShaperGroupEntry,
)


class CouplingPortAsynchronousTrafficShaper(Identifiable):
    """AUTOSAR CouplingPortAsynchronousTrafficShaper."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    committed_burst: Optional[PositiveInteger]
    committed: Optional[PositiveInteger]
    traffic_shaper: Optional[SwitchAsynchronousTrafficShaperGroupEntry]
    def __init__(self) -> None:
        """Initialize CouplingPortAsynchronousTrafficShaper."""
        super().__init__()
        self.committed_burst: Optional[PositiveInteger] = None
        self.committed: Optional[PositiveInteger] = None
        self.traffic_shaper: Optional[SwitchAsynchronousTrafficShaperGroupEntry] = None


class CouplingPortAsynchronousTrafficShaperBuilder:
    """Builder for CouplingPortAsynchronousTrafficShaper."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CouplingPortAsynchronousTrafficShaper = CouplingPortAsynchronousTrafficShaper()

    def build(self) -> CouplingPortAsynchronousTrafficShaper:
        """Build and return CouplingPortAsynchronousTrafficShaper object.

        Returns:
            CouplingPortAsynchronousTrafficShaper instance
        """
        # TODO: Add validation
        return self._obj
