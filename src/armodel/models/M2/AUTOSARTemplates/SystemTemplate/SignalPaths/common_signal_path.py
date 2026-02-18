"""CommonSignalPath AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 253)

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


class CommonSignalPath(SignalPathConstraint):
    """AUTOSAR CommonSignalPath."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    operations: list[Any]
    signals: list[SwcToSwcSignal]
    def __init__(self) -> None:
        """Initialize CommonSignalPath."""
        super().__init__()
        self.operations: list[Any] = []
        self.signals: list[SwcToSwcSignal] = []


class CommonSignalPathBuilder:
    """Builder for CommonSignalPath."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CommonSignalPath = CommonSignalPath()

    def build(self) -> CommonSignalPath:
        """Build and return CommonSignalPath object.

        Returns:
            CommonSignalPath instance
        """
        # TODO: Add validation
        return self._obj
