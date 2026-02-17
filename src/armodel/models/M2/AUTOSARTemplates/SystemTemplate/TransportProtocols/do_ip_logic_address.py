"""DoIpLogicAddress AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 555)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DoIP.abstract_do_ip_logic_address_props import (
    AbstractDoIpLogicAddressProps,
)


class DoIpLogicAddress(Identifiable):
    """AUTOSAR DoIpLogicAddress."""

    address: Optional[Integer]
    do_ip_logic: Optional[AbstractDoIpLogicAddressProps]
    def __init__(self) -> None:
        """Initialize DoIpLogicAddress."""
        super().__init__()
        self.address: Optional[Integer] = None
        self.do_ip_logic: Optional[AbstractDoIpLogicAddressProps] = None


class DoIpLogicAddressBuilder:
    """Builder for DoIpLogicAddress."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DoIpLogicAddress = DoIpLogicAddress()

    def build(self) -> DoIpLogicAddress:
        """Build and return DoIpLogicAddress object.

        Returns:
            DoIpLogicAddress instance
        """
        # TODO: Add validation
        return self._obj
