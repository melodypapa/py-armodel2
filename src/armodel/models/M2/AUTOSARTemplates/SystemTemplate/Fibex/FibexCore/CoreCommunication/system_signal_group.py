"""SystemSignalGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 324)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.system_signal import (
    SystemSignal,
)


class SystemSignalGroup(ARElement):
    """AUTOSAR SystemSignalGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    system_signals: list[SystemSignal]
    transforming: Optional[SystemSignal]
    def __init__(self) -> None:
        """Initialize SystemSignalGroup."""
        super().__init__()
        self.system_signals: list[SystemSignal] = []
        self.transforming: Optional[SystemSignal] = None


class SystemSignalGroupBuilder:
    """Builder for SystemSignalGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SystemSignalGroup = SystemSignalGroup()

    def build(self) -> SystemSignalGroup:
        """Build and return SystemSignalGroup object.

        Returns:
            SystemSignalGroup instance
        """
        # TODO: Add validation
        return self._obj
