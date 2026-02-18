"""BackgroundEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 544)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_RTEEvents.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)


class BackgroundEvent(RTEEvent):
    """AUTOSAR BackgroundEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize BackgroundEvent."""
        super().__init__()


class BackgroundEventBuilder:
    """Builder for BackgroundEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BackgroundEvent = BackgroundEvent()

    def build(self) -> BackgroundEvent:
        """Build and return BackgroundEvent object.

        Returns:
            BackgroundEvent instance
        """
        # TODO: Add validation
        return self._obj
