"""UserDefinedEthernetFrame AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 579)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetFrame.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetFrame.abstract_ethernet_frame import (
    AbstractEthernetFrame,
)


class UserDefinedEthernetFrame(AbstractEthernetFrame):
    """AUTOSAR UserDefinedEthernetFrame."""

    def __init__(self) -> None:
        """Initialize UserDefinedEthernetFrame."""
        super().__init__()


class UserDefinedEthernetFrameBuilder:
    """Builder for UserDefinedEthernetFrame."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UserDefinedEthernetFrame = UserDefinedEthernetFrame()

    def build(self) -> UserDefinedEthernetFrame:
        """Build and return UserDefinedEthernetFrame object.

        Returns:
            UserDefinedEthernetFrame instance
        """
        # TODO: Add validation
        return self._obj
