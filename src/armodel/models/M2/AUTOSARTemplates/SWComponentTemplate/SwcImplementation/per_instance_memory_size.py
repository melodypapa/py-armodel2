"""PerInstanceMemorySize AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 623)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcImplementation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PerInstanceMemory.per_instance_memory import (
    PerInstanceMemory,
)


class PerInstanceMemorySize(ARObject):
    """AUTOSAR PerInstanceMemorySize."""

    def __init__(self) -> None:
        """Initialize PerInstanceMemorySize."""
        super().__init__()
        self.alignment: Optional[PositiveInteger] = None
        self.per_instance_memory_memory: Optional[PerInstanceMemory] = None
        self.size: Optional[PositiveInteger] = None


class PerInstanceMemorySizeBuilder:
    """Builder for PerInstanceMemorySize."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PerInstanceMemorySize = PerInstanceMemorySize()

    def build(self) -> PerInstanceMemorySize:
        """Build and return PerInstanceMemorySize object.

        Returns:
            PerInstanceMemorySize instance
        """
        # TODO: Add validation
        return self._obj
