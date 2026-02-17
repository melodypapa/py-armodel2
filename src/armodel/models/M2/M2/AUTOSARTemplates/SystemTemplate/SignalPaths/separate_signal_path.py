"""SeparateSignalPath AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 257)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SignalPaths.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths.signal_path_constraint import (
    SignalPathConstraint,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths.swc_to_swc_signal import (
    SwcToSwcSignal,
)


class SeparateSignalPath(SignalPathConstraint):
    """AUTOSAR SeparateSignalPath."""

    def __init__(self) -> None:
        """Initialize SeparateSignalPath."""
        super().__init__()
        self.operations: list[Any] = []
        self.signals: list[SwcToSwcSignal] = []


class SeparateSignalPathBuilder:
    """Builder for SeparateSignalPath."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SeparateSignalPath = SeparateSignalPath()

    def build(self) -> SeparateSignalPath:
        """Build and return SeparateSignalPath object.

        Returns:
            SeparateSignalPath instance
        """
        # TODO: Add validation
        return self._obj
