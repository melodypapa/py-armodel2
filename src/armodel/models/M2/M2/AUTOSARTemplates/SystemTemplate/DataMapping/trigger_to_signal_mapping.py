"""TriggerToSignalMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 249)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DataMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.data_mapping import (
    DataMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.system_signal import (
    SystemSignal,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)


class TriggerToSignalMapping(DataMapping):
    """AUTOSAR TriggerToSignalMapping."""

    def __init__(self) -> None:
        """Initialize TriggerToSignalMapping."""
        super().__init__()
        self.system_signal: Optional[SystemSignal] = None
        self.trigger: Optional[Trigger] = None


class TriggerToSignalMappingBuilder:
    """Builder for TriggerToSignalMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TriggerToSignalMapping = TriggerToSignalMapping()

    def build(self) -> TriggerToSignalMapping:
        """Build and return TriggerToSignalMapping object.

        Returns:
            TriggerToSignalMapping instance
        """
        # TODO: Add validation
        return self._obj
