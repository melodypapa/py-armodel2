"""DtcStatusChangeNotificationNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 776)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)


class DtcStatusChangeNotificationNeeds(DiagnosticCapabilityElement):
    """AUTOSAR DtcStatusChangeNotificationNeeds."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "notification_time": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Any,
        ),  # notificationTime
    }

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
