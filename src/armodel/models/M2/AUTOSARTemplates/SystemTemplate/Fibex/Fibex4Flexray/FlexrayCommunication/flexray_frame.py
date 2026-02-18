"""FlexrayFrame AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 422)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Flexray_FlexrayCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.frame import (
    Frame,
)


class FlexrayFrame(Frame):
    """AUTOSAR FlexrayFrame."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize FlexrayFrame."""
        super().__init__()


class FlexrayFrameBuilder:
    """Builder for FlexrayFrame."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayFrame = FlexrayFrame()

    def build(self) -> FlexrayFrame:
        """Build and return FlexrayFrame object.

        Returns:
            FlexrayFrame instance
        """
        # TODO: Add validation
        return self._obj
