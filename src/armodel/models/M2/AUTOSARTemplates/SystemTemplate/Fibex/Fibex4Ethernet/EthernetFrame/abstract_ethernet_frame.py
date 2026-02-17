"""AbstractEthernetFrame AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 578)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetFrame.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.frame import (
    Frame,
)


class AbstractEthernetFrame(Frame):
    """AUTOSAR AbstractEthernetFrame."""
    """Abstract base class - do not instantiate directly."""

    def __init__(self) -> None:
        """Initialize AbstractEthernetFrame."""
        super().__init__()


class AbstractEthernetFrameBuilder:
    """Builder for AbstractEthernetFrame."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractEthernetFrame = AbstractEthernetFrame()

    def build(self) -> AbstractEthernetFrame:
        """Build and return AbstractEthernetFrame object.

        Returns:
            AbstractEthernetFrame instance
        """
        # TODO: Add validation
        return self._obj
