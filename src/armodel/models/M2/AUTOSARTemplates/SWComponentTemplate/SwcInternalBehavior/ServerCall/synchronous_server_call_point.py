"""SynchronousServerCallPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 580)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2074)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_ServerCall.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServerCall.server_call_point import (
    ServerCallPoint,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.exclusive_area_nesting_order import (
    ExclusiveAreaNestingOrder,
)


class SynchronousServerCallPoint(ServerCallPoint):
    """AUTOSAR SynchronousServerCallPoint."""

    called_from: Optional[ExclusiveAreaNestingOrder]
    def __init__(self) -> None:
        """Initialize SynchronousServerCallPoint."""
        super().__init__()
        self.called_from: Optional[ExclusiveAreaNestingOrder] = None


class SynchronousServerCallPointBuilder:
    """Builder for SynchronousServerCallPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SynchronousServerCallPoint = SynchronousServerCallPoint()

    def build(self) -> SynchronousServerCallPoint:
        """Build and return SynchronousServerCallPoint object.

        Returns:
            SynchronousServerCallPoint instance
        """
        # TODO: Add validation
        return self._obj
