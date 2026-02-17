"""AsynchronousServerCallPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 581)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_ServerCall.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServerCall.server_call_point import (
    ServerCallPoint,
)


class AsynchronousServerCallPoint(ServerCallPoint):
    """AUTOSAR AsynchronousServerCallPoint."""

    def __init__(self) -> None:
        """Initialize AsynchronousServerCallPoint."""
        super().__init__()


class AsynchronousServerCallPointBuilder:
    """Builder for AsynchronousServerCallPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AsynchronousServerCallPoint = AsynchronousServerCallPoint()

    def build(self) -> AsynchronousServerCallPoint:
        """Build and return AsynchronousServerCallPoint object.

        Returns:
            AsynchronousServerCallPoint instance
        """
        # TODO: Add validation
        return self._obj
