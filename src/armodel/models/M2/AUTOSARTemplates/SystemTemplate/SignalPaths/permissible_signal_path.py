"""PermissibleSignalPath AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 256)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SignalPaths.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths.signal_path_constraint import (
    SignalPathConstraint,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths.swc_to_swc_signal import (
    SwcToSwcSignal,
)


class PermissibleSignalPath(SignalPathConstraint):
    """AUTOSAR PermissibleSignalPath."""

    operations: list[Any]
    physical_channels: list[PhysicalChannel]
    signals: list[SwcToSwcSignal]
    def __init__(self) -> None:
        """Initialize PermissibleSignalPath."""
        super().__init__()
        self.operations: list[Any] = []
        self.physical_channels: list[PhysicalChannel] = []
        self.signals: list[SwcToSwcSignal] = []


class PermissibleSignalPathBuilder:
    """Builder for PermissibleSignalPath."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PermissibleSignalPath = PermissibleSignalPath()

    def build(self) -> PermissibleSignalPath:
        """Build and return PermissibleSignalPath object.

        Returns:
            PermissibleSignalPath instance
        """
        # TODO: Add validation
        return self._obj
