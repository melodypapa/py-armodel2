"""Ipv4Props AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 146)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ipv4_arp_props import (
    Ipv4ArpProps,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ipv4_auto_ip_props import (
    Ipv4AutoIpProps,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ipv4_fragmentation_props import (
    Ipv4FragmentationProps,
)


class Ipv4Props(ARObject):
    """AUTOSAR Ipv4Props."""

    def __init__(self) -> None:
        """Initialize Ipv4Props."""
        super().__init__()
        self.arp_props: Optional[Ipv4ArpProps] = None
        self.auto_ip_props: Optional[Ipv4AutoIpProps] = None
        self.fragmentation: Optional[Ipv4FragmentationProps] = None


class Ipv4PropsBuilder:
    """Builder for Ipv4Props."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Ipv4Props = Ipv4Props()

    def build(self) -> Ipv4Props:
        """Build and return Ipv4Props object.

        Returns:
            Ipv4Props instance
        """
        # TODO: Add validation
        return self._obj
