"""GlobalTimeEthSlave AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 867)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime_ETH.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_slave import (
    GlobalTimeSlave,
)


class GlobalTimeEthSlave(GlobalTimeSlave):
    """AUTOSAR GlobalTimeEthSlave."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "crc_validated": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (GlobalTimeCrc),
        ),  # crcValidated
    }

    def __init__(self) -> None:
        """Initialize GlobalTimeEthSlave."""
        super().__init__()
        self.crc_validated: Optional[Any] = None


class GlobalTimeEthSlaveBuilder:
    """Builder for GlobalTimeEthSlave."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GlobalTimeEthSlave = GlobalTimeEthSlave()

    def build(self) -> GlobalTimeEthSlave:
        """Build and return GlobalTimeEthSlave object.

        Returns:
            GlobalTimeEthSlave instance
        """
        # TODO: Add validation
        return self._obj
