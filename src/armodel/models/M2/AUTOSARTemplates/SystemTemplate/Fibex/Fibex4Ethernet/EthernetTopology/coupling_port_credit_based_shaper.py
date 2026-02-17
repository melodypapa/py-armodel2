"""CouplingPortCreditBasedShaper AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2013)

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


class CouplingPortCreditBasedShaper(Identifiable):
    """AUTOSAR CouplingPortCreditBasedShaper."""

    idle_slope: Optional[PositiveInteger]
    lower_boundary: Optional[PositiveInteger]
    upper_boundary: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize CouplingPortCreditBasedShaper."""
        super().__init__()
        self.idle_slope: Optional[PositiveInteger] = None
        self.lower_boundary: Optional[PositiveInteger] = None
        self.upper_boundary: Optional[PositiveInteger] = None


class CouplingPortCreditBasedShaperBuilder:
    """Builder for CouplingPortCreditBasedShaper."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CouplingPortCreditBasedShaper = CouplingPortCreditBasedShaper()

    def build(self) -> CouplingPortCreditBasedShaper:
        """Build and return CouplingPortCreditBasedShaper object.

        Returns:
            CouplingPortCreditBasedShaper instance
        """
        # TODO: Add validation
        return self._obj
