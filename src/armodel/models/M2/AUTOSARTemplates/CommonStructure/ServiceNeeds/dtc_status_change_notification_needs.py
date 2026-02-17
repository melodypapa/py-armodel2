"""DtcStatusChangeNotificationNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 776)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)


class DtcStatusChangeNotificationNeeds(DiagnosticCapabilityElement):
    """AUTOSAR DtcStatusChangeNotificationNeeds."""

    notification_time: Optional[Any]
    def __init__(self) -> None:
        """Initialize DtcStatusChangeNotificationNeeds."""
        super().__init__()
        self.notification_time: Optional[Any] = None


class DtcStatusChangeNotificationNeedsBuilder:
    """Builder for DtcStatusChangeNotificationNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DtcStatusChangeNotificationNeeds = DtcStatusChangeNotificationNeeds()

    def build(self) -> DtcStatusChangeNotificationNeeds:
        """Build and return DtcStatusChangeNotificationNeeds object.

        Returns:
            DtcStatusChangeNotificationNeeds instance
        """
        # TODO: Add validation
        return self._obj
