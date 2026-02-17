"""GenericEthernetFrame AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 578)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetFrame.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetFrame.abstract_ethernet_frame import (
    AbstractEthernetFrame,
)


class GenericEthernetFrame(AbstractEthernetFrame):
    """AUTOSAR GenericEthernetFrame."""

    def __init__(self) -> None:
        """Initialize GenericEthernetFrame."""
        super().__init__()


class GenericEthernetFrameBuilder:
    """Builder for GenericEthernetFrame."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GenericEthernetFrame = GenericEthernetFrame()

    def build(self) -> GenericEthernetFrame:
        """Build and return GenericEthernetFrame object.

        Returns:
            GenericEthernetFrame instance
        """
        # TODO: Add validation
        return self._obj
