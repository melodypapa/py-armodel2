"""TpPort AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 461)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class TpPort(ARObject):
    """AUTOSAR TpPort."""

    dynamically: Optional[Boolean]
    port_number: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize TpPort."""
        super().__init__()
        self.dynamically: Optional[Boolean] = None
        self.port_number: Optional[PositiveInteger] = None


class TpPortBuilder:
    """Builder for TpPort."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TpPort = TpPort()

    def build(self) -> TpPort:
        """Build and return TpPort object.

        Returns:
            TpPort instance
        """
        # TODO: Add validation
        return self._obj
