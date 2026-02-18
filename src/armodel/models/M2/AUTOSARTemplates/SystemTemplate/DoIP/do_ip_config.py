"""DoIpConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 551)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DoIP.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DoIP.do_ip_interface import (
    DoIpInterface,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.do_ip_logic_address import (
    DoIpLogicAddress,
)


class DoIpConfig(ARObject):
    """AUTOSAR DoIpConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    doip_interfaces: list[DoIpInterface]
    logic_address: Optional[DoIpLogicAddress]
    def __init__(self) -> None:
        """Initialize DoIpConfig."""
        super().__init__()
        self.doip_interfaces: list[DoIpInterface] = []
        self.logic_address: Optional[DoIpLogicAddress] = None


class DoIpConfigBuilder:
    """Builder for DoIpConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DoIpConfig = DoIpConfig()

    def build(self) -> DoIpConfig:
        """Build and return DoIpConfig object.

        Returns:
            DoIpConfig instance
        """
        # TODO: Add validation
        return self._obj
