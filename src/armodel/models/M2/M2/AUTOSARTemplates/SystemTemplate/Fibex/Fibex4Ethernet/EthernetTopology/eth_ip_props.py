"""EthIpProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 146)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ipv4_props import (
    Ipv4Props,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ipv6_props import (
    Ipv6Props,
)


class EthIpProps(ARElement):
    """AUTOSAR EthIpProps."""

    def __init__(self) -> None:
        """Initialize EthIpProps."""
        super().__init__()
        self.ipv4_props: Optional[Ipv4Props] = None
        self.ipv6_props: Optional[Ipv6Props] = None


class EthIpPropsBuilder:
    """Builder for EthIpProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EthIpProps = EthIpProps()

    def build(self) -> EthIpProps:
        """Build and return EthIpProps object.

        Returns:
            EthIpProps instance
        """
        # TODO: Add validation
        return self._obj
