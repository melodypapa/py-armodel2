"""DoIpLogicTesterAddressProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 556)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DoIP.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DoIP.abstract_do_ip_logic_address_props import (
    AbstractDoIpLogicAddressProps,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DoIP.do_ip_routing_activation import (
    DoIpRoutingActivation,
)


class DoIpLogicTesterAddressProps(AbstractDoIpLogicAddressProps):
    """AUTOSAR DoIpLogicTesterAddressProps."""

    def __init__(self) -> None:
        """Initialize DoIpLogicTesterAddressProps."""
        super().__init__()
        self.do_ip_testers: list[DoIpRoutingActivation] = []


class DoIpLogicTesterAddressPropsBuilder:
    """Builder for DoIpLogicTesterAddressProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DoIpLogicTesterAddressProps = DoIpLogicTesterAddressProps()

    def build(self) -> DoIpLogicTesterAddressProps:
        """Build and return DoIpLogicTesterAddressProps object.

        Returns:
            DoIpLogicTesterAddressProps instance
        """
        # TODO: Add validation
        return self._obj
