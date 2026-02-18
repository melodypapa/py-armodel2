"""LinUnconditionalFrame AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 429)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_frame import (
    LinFrame,
)


class LinUnconditionalFrame(LinFrame):
    """AUTOSAR LinUnconditionalFrame."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize LinUnconditionalFrame."""
        super().__init__()


class LinUnconditionalFrameBuilder:
    """Builder for LinUnconditionalFrame."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinUnconditionalFrame = LinUnconditionalFrame()

    def build(self) -> LinUnconditionalFrame:
        """Build and return LinUnconditionalFrame object.

        Returns:
            LinUnconditionalFrame instance
        """
        # TODO: Add validation
        return self._obj
