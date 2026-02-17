"""DoIpLogicTargetAddressProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 556)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DoIP.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DoIP.abstract_do_ip_logic_address_props import (
    AbstractDoIpLogicAddressProps,
)


class DoIpLogicTargetAddressProps(AbstractDoIpLogicAddressProps):
    """AUTOSAR DoIpLogicTargetAddressProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize DoIpLogicTargetAddressProps."""
        super().__init__()


class DoIpLogicTargetAddressPropsBuilder:
    """Builder for DoIpLogicTargetAddressProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DoIpLogicTargetAddressProps = DoIpLogicTargetAddressProps()

    def build(self) -> DoIpLogicTargetAddressProps:
        """Build and return DoIpLogicTargetAddressProps object.

        Returns:
            DoIpLogicTargetAddressProps instance
        """
        # TODO: Add validation
        return self._obj
