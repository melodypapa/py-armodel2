"""DtcStatusChangeNotificationNeeds AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)


class DtcStatusChangeNotificationNeeds(DiagnosticCapabilityElement):
    """AUTOSAR DtcStatusChangeNotificationNeeds."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("notification_time", None, False, False, any (DiagnosticClearDtc)),  # notificationTime
    ]

    def __init__(self) -> None:
        """Initialize DtcStatusChangeNotificationNeeds."""
        super().__init__()
        self.notification_time: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DtcStatusChangeNotificationNeeds to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DtcStatusChangeNotificationNeeds":
        """Create DtcStatusChangeNotificationNeeds from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DtcStatusChangeNotificationNeeds instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DtcStatusChangeNotificationNeeds since parent returns ARObject
        return cast("DtcStatusChangeNotificationNeeds", obj)


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
