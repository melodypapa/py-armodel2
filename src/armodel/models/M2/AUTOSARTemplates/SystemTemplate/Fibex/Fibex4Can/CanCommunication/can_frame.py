"""CanFrame AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 442)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.frame import (
    Frame,
)


class CanFrame(Frame):
    """AUTOSAR CanFrame."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize CanFrame."""
        super().__init__()


class CanFrameBuilder:
    """Builder for CanFrame."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanFrame = CanFrame()

    def build(self) -> CanFrame:
        """Build and return CanFrame object.

        Returns:
            CanFrame instance
        """
        # TODO: Add validation
        return self._obj
