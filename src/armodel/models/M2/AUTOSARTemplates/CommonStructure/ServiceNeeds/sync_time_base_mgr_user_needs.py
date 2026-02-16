"""SyncTimeBaseMgrUserNeeds AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)


class SyncTimeBaseMgrUserNeeds(ServiceNeeds):
    """AUTOSAR SyncTimeBaseMgrUserNeeds."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize SyncTimeBaseMgrUserNeeds."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SyncTimeBaseMgrUserNeeds to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SyncTimeBaseMgrUserNeeds":
        """Create SyncTimeBaseMgrUserNeeds from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SyncTimeBaseMgrUserNeeds instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SyncTimeBaseMgrUserNeeds since parent returns ARObject
        return cast("SyncTimeBaseMgrUserNeeds", obj)


class SyncTimeBaseMgrUserNeedsBuilder:
    """Builder for SyncTimeBaseMgrUserNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SyncTimeBaseMgrUserNeeds = SyncTimeBaseMgrUserNeeds()

    def build(self) -> SyncTimeBaseMgrUserNeeds:
        """Build and return SyncTimeBaseMgrUserNeeds object.

        Returns:
            SyncTimeBaseMgrUserNeeds instance
        """
        # TODO: Add validation
        return self._obj
