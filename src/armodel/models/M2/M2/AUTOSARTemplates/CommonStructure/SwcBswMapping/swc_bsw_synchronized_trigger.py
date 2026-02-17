"""SwcBswSynchronizedTrigger AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 111)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_SwcBswMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)


class SwcBswSynchronizedTrigger(ARObject):
    """AUTOSAR SwcBswSynchronizedTrigger."""

    def __init__(self) -> None:
        """Initialize SwcBswSynchronizedTrigger."""
        super().__init__()
        self.bsw_trigger: Optional[Trigger] = None
        self.swc_trigger: Optional[Trigger] = None


class SwcBswSynchronizedTriggerBuilder:
    """Builder for SwcBswSynchronizedTrigger."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcBswSynchronizedTrigger = SwcBswSynchronizedTrigger()

    def build(self) -> SwcBswSynchronizedTrigger:
        """Build and return SwcBswSynchronizedTrigger object.

        Returns:
            SwcBswSynchronizedTrigger instance
        """
        # TODO: Add validation
        return self._obj
