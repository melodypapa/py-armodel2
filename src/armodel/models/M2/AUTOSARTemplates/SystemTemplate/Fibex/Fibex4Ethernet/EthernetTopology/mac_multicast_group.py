"""MacMulticastGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 103)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    MacAddressString,
)


class MacMulticastGroup(Identifiable):
    """AUTOSAR MacMulticastGroup."""

    mac_multicast: Optional[MacAddressString]
    def __init__(self) -> None:
        """Initialize MacMulticastGroup."""
        super().__init__()
        self.mac_multicast: Optional[MacAddressString] = None


class MacMulticastGroupBuilder:
    """Builder for MacMulticastGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MacMulticastGroup = MacMulticastGroup()

    def build(self) -> MacMulticastGroup:
        """Build and return MacMulticastGroup object.

        Returns:
            MacMulticastGroup instance
        """
        # TODO: Add validation
        return self._obj
