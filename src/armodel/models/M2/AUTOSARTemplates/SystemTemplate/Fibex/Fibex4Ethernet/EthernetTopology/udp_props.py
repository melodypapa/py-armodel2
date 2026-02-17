"""UdpProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 154)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class UdpProps(ARObject):
    """AUTOSAR UdpProps."""

    udp_ttl: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize UdpProps."""
        super().__init__()
        self.udp_ttl: Optional[PositiveInteger] = None


class UdpPropsBuilder:
    """Builder for UdpProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UdpProps = UdpProps()

    def build(self) -> UdpProps:
        """Build and return UdpProps object.

        Returns:
            UdpProps instance
        """
        # TODO: Add validation
        return self._obj
