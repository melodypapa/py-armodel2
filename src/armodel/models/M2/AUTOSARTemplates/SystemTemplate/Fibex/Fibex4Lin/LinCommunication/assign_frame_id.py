"""AssignFrameId AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_configuration_entry import (
    LinConfigurationEntry,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_frame_triggering import (
    LinFrameTriggering,
)


class AssignFrameId(LinConfigurationEntry):
    """AUTOSAR AssignFrameId."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("assigned_frame", None, False, False, LinFrameTriggering),  # assignedFrame
    ]

    def __init__(self) -> None:
        """Initialize AssignFrameId."""
        super().__init__()
        self.assigned_frame: Optional[LinFrameTriggering] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert AssignFrameId to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AssignFrameId":
        """Create AssignFrameId from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            AssignFrameId instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to AssignFrameId since parent returns ARObject
        return cast("AssignFrameId", obj)


class AssignFrameIdBuilder:
    """Builder for AssignFrameId."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AssignFrameId = AssignFrameId()

    def build(self) -> AssignFrameId:
        """Build and return AssignFrameId object.

        Returns:
            AssignFrameId instance
        """
        # TODO: Add validation
        return self._obj
