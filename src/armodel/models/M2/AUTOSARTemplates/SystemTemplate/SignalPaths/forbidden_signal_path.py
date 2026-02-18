"""ForbiddenSignalPath AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 255)

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


class ForbiddenSignalPath(SignalPathConstraint):
    """AUTOSAR ForbiddenSignalPath."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    operations: list[Any]
    physical_channels: list[PhysicalChannel]
    signals: list[SwcToSwcSignal]
    def __init__(self) -> None:
        """Initialize ForbiddenSignalPath."""
        super().__init__()
        self.operations: list[Any] = []
        self.physical_channels: list[PhysicalChannel] = []
        self.signals: list[SwcToSwcSignal] = []


class ForbiddenSignalPathBuilder:
    """Builder for ForbiddenSignalPath."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ForbiddenSignalPath = ForbiddenSignalPath()

    def build(self) -> ForbiddenSignalPath:
        """Build and return ForbiddenSignalPath object.

        Returns:
            ForbiddenSignalPath instance
        """
        # TODO: Add validation
        return self._obj
