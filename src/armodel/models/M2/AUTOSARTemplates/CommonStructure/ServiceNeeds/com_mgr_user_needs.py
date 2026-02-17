"""ComMgrUserNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 235)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 711)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    MaxCommModeEnum,
)


class ComMgrUserNeeds(ServiceNeeds):
    """AUTOSAR ComMgrUserNeeds."""

    max_comm_mode_enum: Optional[MaxCommModeEnum]
    def __init__(self) -> None:
        """Initialize ComMgrUserNeeds."""
        super().__init__()
        self.max_comm_mode_enum: Optional[MaxCommModeEnum] = None


class ComMgrUserNeedsBuilder:
    """Builder for ComMgrUserNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ComMgrUserNeeds = ComMgrUserNeeds()

    def build(self) -> ComMgrUserNeeds:
        """Build and return ComMgrUserNeeds object.

        Returns:
            ComMgrUserNeeds instance
        """
        # TODO: Add validation
        return self._obj
