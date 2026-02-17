"""IEEE1722TpAcfBus AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 657)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols_IEEE1722Tp_IEEE1722TpAcf.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf.ieee1722_tp_acf_bus_part import (
    IEEE1722TpAcfBusPart,
)


class IEEE1722TpAcfBus(Identifiable):
    """AUTOSAR IEEE1722TpAcfBus."""
    """Abstract base class - do not instantiate directly."""

    acf_parts: list[IEEE1722TpAcfBusPart]
    bus_id: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize IEEE1722TpAcfBus."""
        super().__init__()
        self.acf_parts: list[IEEE1722TpAcfBusPart] = []
        self.bus_id: Optional[PositiveInteger] = None


class IEEE1722TpAcfBusBuilder:
    """Builder for IEEE1722TpAcfBus."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IEEE1722TpAcfBus = IEEE1722TpAcfBus()

    def build(self) -> IEEE1722TpAcfBus:
        """Build and return IEEE1722TpAcfBus object.

        Returns:
            IEEE1722TpAcfBus instance
        """
        # TODO: Add validation
        return self._obj
