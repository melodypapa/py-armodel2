"""UnassignFrameId AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_configuration_entry import (
    LinConfigurationEntry,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_frame_triggering import (
    LinFrameTriggering,
)


class UnassignFrameId(LinConfigurationEntry):
    """AUTOSAR UnassignFrameId."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("unassigned", None, False, False, LinFrameTriggering),  # unassigned
    ]

    def __init__(self) -> None:
        """Initialize UnassignFrameId."""
        super().__init__()
        self.unassigned: Optional[LinFrameTriggering] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert UnassignFrameId to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "UnassignFrameId":
        """Create UnassignFrameId from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            UnassignFrameId instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to UnassignFrameId since parent returns ARObject
        return cast("UnassignFrameId", obj)


class UnassignFrameIdBuilder:
    """Builder for UnassignFrameId."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UnassignFrameId = UnassignFrameId()

    def build(self) -> UnassignFrameId:
        """Build and return UnassignFrameId object.

        Returns:
            UnassignFrameId instance
        """
        # TODO: Add validation
        return self._obj
