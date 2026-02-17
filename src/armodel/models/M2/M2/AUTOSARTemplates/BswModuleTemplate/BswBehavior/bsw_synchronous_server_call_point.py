"""BswSynchronousServerCallPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 79)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_module_call_point import (
    BswModuleCallPoint,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_client_server_entry import (
    BswModuleClientServerEntry,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.exclusive_area_nesting_order import (
    ExclusiveAreaNestingOrder,
)


class BswSynchronousServerCallPoint(BswModuleCallPoint):
    """AUTOSAR BswSynchronousServerCallPoint."""

    def __init__(self) -> None:
        """Initialize BswSynchronousServerCallPoint."""
        super().__init__()
        self.called_entry_entry: Optional[BswModuleClientServerEntry] = None
        self.called_from: Optional[ExclusiveAreaNestingOrder] = None


class BswSynchronousServerCallPointBuilder:
    """Builder for BswSynchronousServerCallPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswSynchronousServerCallPoint = BswSynchronousServerCallPoint()

    def build(self) -> BswSynchronousServerCallPoint:
        """Build and return BswSynchronousServerCallPoint object.

        Returns:
            BswSynchronousServerCallPoint instance
        """
        # TODO: Add validation
        return self._obj
