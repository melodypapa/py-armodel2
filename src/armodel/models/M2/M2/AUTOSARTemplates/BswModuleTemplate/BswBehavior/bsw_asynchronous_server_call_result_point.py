"""BswAsynchronousServerCallResultPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 80)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_module_call_point import (
    BswModuleCallPoint,
)


class BswAsynchronousServerCallResultPoint(BswModuleCallPoint):
    """AUTOSAR BswAsynchronousServerCallResultPoint."""

    def __init__(self) -> None:
        """Initialize BswAsynchronousServerCallResultPoint."""
        super().__init__()
        self.asynchronous: Optional[Any] = None


class BswAsynchronousServerCallResultPointBuilder:
    """Builder for BswAsynchronousServerCallResultPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswAsynchronousServerCallResultPoint = BswAsynchronousServerCallResultPoint()

    def build(self) -> BswAsynchronousServerCallResultPoint:
        """Build and return BswAsynchronousServerCallResultPoint object.

        Returns:
            BswAsynchronousServerCallResultPoint instance
        """
        # TODO: Add validation
        return self._obj
