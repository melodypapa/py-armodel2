"""UdpNmEcu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 688)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.busspecific_nm_ecu import (
    BusspecificNmEcu,
)


class UdpNmEcu(BusspecificNmEcu):
    """AUTOSAR UdpNmEcu."""

    def __init__(self) -> None:
        """Initialize UdpNmEcu."""
        super().__init__()


class UdpNmEcuBuilder:
    """Builder for UdpNmEcu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UdpNmEcu = UdpNmEcu()

    def build(self) -> UdpNmEcu:
        """Build and return UdpNmEcu object.

        Returns:
            UdpNmEcu instance
        """
        # TODO: Add validation
        return self._obj
